/**
 * stl-viewer — embeddable 3D model viewer with variant switcher + downloads
 *
 * <script src="https://docs.jumperless.org/embed/stl-viewer.js" defer></script>
 * <stl-viewer></stl-viewer>
 *
 * With no attributes it fetches /assets/3Dstands/index.json (generated at build
 * time by docs/generate_3d_models_index.py) and lists every model in that
 * folder. Files sharing a base name are grouped into one entry with multiple
 * download formats (e.g. .stl + .step + .3mf). Preview renders .stl (in the
 * variant's accent color) or .3mf (with its own baked colors); .step and other
 * non-previewable formats still get a download button.
 *
 * --- Custom / explicit models (skips the manifest) ---
 *
 * <stl-viewer models='[
 *   {"label":"My Part","files":{"stl":"/assets/mypart.stl","step":"/assets/mypart.step"}}
 * ]' color="#7AB7F0"></stl-viewer>
 *   (legacy {"src":..., "step":...} form is also accepted)
 *
 * Point at a different manifest with manifest="/assets/other/index.json".
 *
 * Self-contained (Shadow DOM); host CSS won't leak in/out. three.js is loaded
 * lazily from esm.sh the first time a viewer scrolls into view.
 *
 * ponytail: three.js is pulled from a CDN at runtime (no bundler). If the CDN
 * is unreachable the viewer shows an error + download links still work.
 */
(() => {
  const DEFAULT_MODELS = [
    { label: "With Probe Holder", src: "/assets/3Dstands/JumperlessStandProbeHolder.stl" },
    { label: "No Probe Holder", src: "/assets/3Dstands/JumperlessStandNoProbeHolder.stl" },
    { label: "FPC", src: "/assets/3Dstands/JumperlessStandFPC.stl" },
  ];

  // Same rainbow the docs use elsewhere (nav + find-me-dock): pink, purple,
  // blue, green, yellow, coral. Each variant gets its own hue; the model and
  // download button recolor to match the selected variant.
  const RAINBOW = ["#FF81BA", "#bf96ff", "#7AB7F0", "#BFF08E", "#FFE07A", "#FF7E72"];
  const rainbow = (i) => RAINBOW[((i % RAINBOW.length) + RAINBOW.length) % RAINBOW.length];

  // ─────────────────────────────────────────────────────────────────────────
  // All the look-and-feel knobs live here. Tweak these and nothing else.
  // ─────────────────────────────────────────────────────────────────────────
  const CONFIG = {
    height: "440px",           // viewer height (overridable via height="" attr)
    exposure: 1.0,             // ACES filmic tone-mapping exposure
    autoRotateSpeed: 1.1,      // spins until the user grabs it

    // Subtle dark gradient behind the model (radial, brighter at top-center).
    background: { top: "#232833", bottom: "#14161c" },

    lights: {
      hemi: { sky: 0xbcd2ff, ground: 0x080a0f, intensity: 0.45 },
      key:  { color: 0xffffff, intensity: 1.16, pos: [1.3, 1.9, 1.1] },
      rim:  { intensity: 1.3, pos: [-1.5, 0.5, -1.1] }, // color = variant accent
      fill: { color: 0x88aaff, intensity: 0.45, pos: [-0.7, -0.5, 0.9] },
      // Grid of dim point lights above the model → many soft glint spots.
      catchGrid: { count: 4, spread: 3, height: 1.2, illuminance: 0.25 },
    },

    material: { metalness: 0.2, roughness: 0.4, emissiveIntensity: 0.14 },

    // UnrealBloomPass: gentle glow that only clips the brighter grid glints.
    bloom: { strength: 0.3, radius: 0.45, threshold: 0.80 },
  };

  // Radial dark gradient as a scene-background texture. Needed because the
  // bloom EffectComposer clears the canvas opaque, hiding any CSS background.
  const makeGradientTexture = (THREE, top, bottom) => {
    const c = document.createElement("canvas");
    c.width = 256;
    c.height = 256;
    const ctx = c.getContext("2d");
    const g = ctx.createRadialGradient(128, 0, 0, 128, 0, 300);
    g.addColorStop(0, top);
    g.addColorStop(0.7, bottom);
    g.addColorStop(1, bottom);
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, c.width, c.height);
    const tex = new THREE.CanvasTexture(c);
    tex.colorSpace = THREE.SRGBColorSpace;
    return tex;
  };

  const CDN = "https://esm.sh/three@0.160.0";
  const THREE_URL = CDN;
  const STL_URL = `${CDN}/examples/jsm/loaders/STLLoader.js`;
  const ORBIT_URL = `${CDN}/examples/jsm/controls/OrbitControls.js`;
  const PP = `${CDN}/examples/jsm/postprocessing`;

  let threePromise = null;
  const loadThree = () => {
    if (!threePromise) {
      threePromise = Promise.all([
        import(THREE_URL),
        import(STL_URL),
        import(ORBIT_URL),
      ]).then(([THREE, stl, orbit]) => ({
        THREE,
        STLLoader: stl.STLLoader,
        OrbitControls: orbit.OrbitControls,
      }));
    }
    return threePromise;
  };

  // 3MF loader is loaded on demand (only when a .3mf model is previewed).
  let tmfPromise = null;
  const loadThreeMF = () =>
    (tmfPromise ||= import(`${CDN}/examples/jsm/loaders/3MFLoader.js`).then(
      (m) => m.ThreeMFLoader
    ));

  // Formats we can render a preview for, in preference order (first wins).
  const LOADABLE_EXTS = ["stl", "3mf"];
  // Every format we'll offer as a download button, in display order. STL first
  // so it's the primary (filled) action; the rest render as secondary outlines.
  const DOWNLOAD_ORDER = ["stl", "3mf", "step", "stp", "obj", "ply", "gltf", "glb"];
  const DOWNLOAD_TITLES = {
    stl: "Ready to print",
    "3mf": "Print project (colors + settings)",
    step: "Editable CAD source",
    stp: "Editable CAD source",
  };

  const extOf = (url) => (url.split(".").pop() || "").toLowerCase();

  // Normalize a model entry to the { label, files: { ext: url } } shape, so the
  // old { src, step } attribute form and the folder manifest both work.
  const normalizeModel = (m) => {
    if (m.files) return m;
    const files = {};
    if (m.src) files[extOf(m.src)] = m.src;
    if (m.step) files.step = m.step;
    return { label: m.label, color: m.color, files };
  };

  // Bloom post-processing is loaded separately so a failure here still leaves
  // a working (un-bloomed) viewer. ponytail: no WebGL2 feature-detect beyond
  // the try/catch — if any addon import throws, we fall back to plain render.
  let bloomPromise = null;
  const loadBloom = () => {
    if (!bloomPromise) {
      bloomPromise = Promise.all([
        import(`${PP}/EffectComposer.js`),
        import(`${PP}/RenderPass.js`),
        import(`${PP}/UnrealBloomPass.js`),
        import(`${PP}/OutputPass.js`),
      ]).then(([c, r, b, o]) => ({
        EffectComposer: c.EffectComposer,
        RenderPass: r.RenderPass,
        UnrealBloomPass: b.UnrealBloomPass,
        OutputPass: o.OutputPass,
      }));
    }
    return bloomPromise;
  };

  const stlCache = new Map();
  const fetchSTL = (src) => {
    if (!stlCache.has(src)) {
      stlCache.set(
        src,
        fetch(src).then((r) => {
          if (!r.ok) throw new Error(`${r.status} ${r.statusText}`);
          return r.arrayBuffer();
        })
      );
    }
    return stlCache.get(src);
  };

  const STYLES = `
    :host {
      display: block;
      margin: 1.25rem 0;
      font-family: Lato, proxima-nova, "Helvetica Neue", Arial, sans-serif;
    }
    .wrap {
      border-radius: 12px;
      overflow: hidden;
      background: #14161c;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .stage {
      position: relative;
      width: 100%;
      height: var(--stl-height, 440px);
      background:
        radial-gradient(120% 120% at 50% 0%, ${CONFIG.background.top} 0%, ${CONFIG.background.bottom} 70%);
      touch-action: none;
    }
    canvas { display: block; width: 100%; height: 100%; }
    .status {
      position: absolute;
      inset: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      color: rgba(255, 255, 255, 0.7);
      font-size: 0.95rem;
      text-align: center;
      padding: 1rem;
      pointer-events: none;
    }
    .status.error { color: #FF7E72; }
    .hint {
      position: absolute;
      left: 12px;
      bottom: 10px;
      font-size: 0.72rem;
      letter-spacing: 0.02em;
      color: rgba(255, 255, 255, 0.45);
      pointer-events: none;
      user-select: none;
    }
    .bar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 0.5rem;
      padding: 0.75rem;
      background: #1b1e26;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
    }
    .variants { display: flex; flex-wrap: wrap; gap: 0.4rem; }
    button {
      --c: #BFF08E;
      font: inherit;
      font-size: 0.9rem;
      color: var(--c);
      background: color-mix(in srgb, var(--c) 12%, transparent);
      border: 1px solid color-mix(in srgb, var(--c) 45%, transparent);
      border-radius: 8px;
      padding: 0.4rem 0.8rem;
      cursor: pointer;
      transition: background 0.12s ease, border-color 0.12s ease, color 0.12s ease;
    }
    button:hover { background: color-mix(in srgb, var(--c) 22%, transparent); }
    button.active {
      color: #14161c;
      background: var(--c);
      border-color: var(--c);
      font-weight: 700;
    }
    .spacer { flex: 1; }
    .downloads { display: flex; flex-wrap: wrap; gap: 0.4rem; }
    a.download {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.9rem;
      font-weight: 700;
      text-decoration: none;
      color: #14161c;
      background: var(--stl-accent, #BFF08E);
      border: 1px solid var(--stl-accent, #BFF08E);
      border-radius: 8px;
      padding: 0.4rem 0.85rem;
      transition: filter 0.12s ease, background 0.15s ease, border-color 0.15s ease, color 0.15s ease;
    }
    a.download:hover { filter: brightness(1.08); }
    a.download svg { width: 15px; height: 15px; }
    /* Non-primary formats (STEP, 3MF, …) render as outlined secondary actions */
    a.download.secondary {
      color: var(--stl-accent, #BFF08E);
      background: color-mix(in srgb, var(--stl-accent, #BFF08E) 12%, transparent);
    }
    a.download.secondary:hover {
      filter: none;
      background: color-mix(in srgb, var(--stl-accent, #BFF08E) 22%, transparent);
    }
  `;

  const DL_ICON =
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12"/><path d="M7 11l5 5 5-5"/><path d="M5 21h14"/></svg>';

  class STLViewer extends HTMLElement {
    connectedCallback() {
      if (this.shadowRoot) return;

      // Optional single-color override; otherwise each variant gets a rainbow hue.
      this.mono = this.getAttribute("color");
      const height = this.getAttribute("height") || CONFIG.height;

      const shadow = this.attachShadow({ mode: "open" });
      shadow.innerHTML = `
        <style>${STYLES}</style>
        <div class="wrap">
          <div class="stage">
            <div class="status">Loading models…</div>
            <div class="hint">drag to rotate · scroll to zoom</div>
          </div>
          <div class="bar">
            <div class="variants"></div>
            <span class="spacer"></span>
            <div class="downloads"></div>
          </div>
        </div>
      `;

      this.stage = shadow.querySelector(".stage");
      this.statusEl = shadow.querySelector(".status");
      this.downloadsEl = shadow.querySelector(".downloads");
      this.variantsEl = shadow.querySelector(".variants");
      this.wrap = shadow.querySelector(".wrap");
      this.stage.style.setProperty("--stl-height", height);

      this.models = [];
      this.current = -1;
      this.selectPending = 0;

      // Resolve the model list (attribute or folder manifest), then wire up.
      this.resolveModels().then((models) => {
        this.models = models;
        this.wrap.style.setProperty("--stl-accent", this.variantColor(0));
        this.buttons = this.models.map((m, i) => {
          const b = document.createElement("button");
          b.textContent = m.label;
          b.style.setProperty("--c", this.variantColor(i));
          b.addEventListener("click", () => this.select(i));
          this.variantsEl.appendChild(b);
          return b;
        });
        this.statusEl.textContent = "Scroll to load 3D preview…";

        // Lazy-init three.js only when the viewer is near the viewport.
        const io = new IntersectionObserver((entries, obs) => {
          if (entries.some((e) => e.isIntersecting)) {
            obs.disconnect();
            this.init();
          }
        }, { rootMargin: "200px" });
        io.observe(this);
      });
    }

    variantColor(i) {
      return (this.models[i] && this.models[i].color) || this.mono || rainbow(i);
    }

    // Attribute `models='[...]'` wins; otherwise pull the folder manifest
    // (generated at build time), falling back to the bundled default list.
    async resolveModels() {
      const attr = this.getAttribute("models");
      if (attr) {
        try {
          const parsed = JSON.parse(attr);
          if (Array.isArray(parsed) && parsed.length) return parsed.map(normalizeModel);
        } catch {
          /* fall through to manifest */
        }
      }
      const manifest = this.getAttribute("manifest") || "/assets/3Dstands/index.json";
      try {
        const r = await fetch(manifest);
        if (r.ok) {
          const data = await r.json();
          if (Array.isArray(data.models) && data.models.length) {
            return data.models.map(normalizeModel);
          }
        }
      } catch {
        /* fall through to defaults */
      }
      return DEFAULT_MODELS.map(normalizeModel);
    }

    previewFile(entry) {
      for (const ext of LOADABLE_EXTS) {
        if (entry.files[ext]) return [ext, entry.files[ext]];
      }
      return null;
    }

    async init() {
      this.statusEl.textContent = "Loading 3D viewer…";
      let lib;
      try {
        lib = await loadThree();
      } catch (e) {
        this.fail("Couldn't load the 3D viewer. Downloads still work.");
        return;
      }
      const { THREE, STLLoader, OrbitControls } = lib;
      this.THREE = THREE;
      this.stlLoader = new STLLoader();

      const L = CONFIG.lights;
      const scene = new THREE.Scene();
      scene.background = makeGradientTexture(
        THREE,
        CONFIG.background.top,
        CONFIG.background.bottom
      );
      const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 5000);
      const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      // Filmic tone mapping gives the highlights something for bloom to grab.
      renderer.toneMapping = THREE.ACESFilmicToneMapping;
      renderer.toneMappingExposure = CONFIG.exposure;
      this.stage.appendChild(renderer.domElement);

      // Dramatic key/rim setup: dim ambient for deep shadows, one bright key,
      // and a punchy accent-colored rim that recolors per variant.
      scene.add(new THREE.HemisphereLight(L.hemi.sky, L.hemi.ground, L.hemi.intensity));
      const key = new THREE.DirectionalLight(L.key.color, L.key.intensity);
      key.position.set(...L.key.pos);
      scene.add(key);
      const rim = new THREE.DirectionalLight(0xffffff, L.rim.intensity);
      rim.position.set(...L.rim.pos);
      rim.color.set(this.variantColor(0));
      scene.add(rim);
      const fill = new THREE.DirectionalLight(L.fill.color, L.fill.intensity);
      fill.position.set(...L.fill.pos);
      scene.add(fill);
      this.rim = rim;

      // A grid of dim point lights hovering above the model. Each one throws a
      // soft specular glint, so as the model turns there are many little spots
      // where the bloom catches. Positioned/scaled to the model in frameModel().
      this.catch = [];
      const N = L.catchGrid.count;
      for (let ix = 0; ix < N; ix++) {
        for (let iz = 0; iz < N; iz++) {
          const l = new THREE.PointLight(0xffffff, 1, 0, 2);
          l.userData.gx = (ix / (N - 1)) * 2 - 1; // -1..1 across the grid
          l.userData.gz = (iz / (N - 1)) * 2 - 1;
          scene.add(l);
          this.catch.push(l);
        }
      }

      const controls = new OrbitControls(camera, renderer.domElement);
      controls.enableDamping = true;
      controls.enablePan = false;
      controls.autoRotate = true;
      controls.autoRotateSpeed = CONFIG.autoRotateSpeed;
      controls.addEventListener("start", () => { controls.autoRotate = false; });

      this.scene = scene;
      this.camera = camera;
      this.renderer = renderer;
      this.controls = controls;

      // Optional bloom composer — falls back to direct rendering on any failure.
      try {
        const pp = await loadBloom();
        const composer = new pp.EffectComposer(renderer);
        composer.setPixelRatio(renderer.getPixelRatio());
        composer.addPass(new pp.RenderPass(scene, camera));
        // strength, radius, threshold — gentle glow, only clipping the brighter
        // grid glints (high threshold keeps the emissive body from washing out).
        const B = CONFIG.bloom;
        const bloom = new pp.UnrealBloomPass(new THREE.Vector2(1, 1), B.strength, B.radius, B.threshold);
        composer.addPass(bloom);
        composer.addPass(new pp.OutputPass());
        this.composer = composer;
      } catch (e) {
        this.composer = null;
      }

      const resize = () => {
        const w = this.stage.clientWidth || 1;
        const h = this.stage.clientHeight || 1;
        renderer.setSize(w, h, false);
        if (this.composer) this.composer.setSize(w, h);
        camera.aspect = w / h;
        camera.updateProjectionMatrix();
      };
      resize();
      new ResizeObserver(resize).observe(this.stage);

      const animate = () => {
        this.raf = requestAnimationFrame(animate);
        controls.update();
        if (this.composer) this.composer.render();
        else renderer.render(scene, camera);
      };
      animate();

      this.select(0);
    }

    async select(index) {
      this.buttons.forEach((b, i) => b.classList.toggle("active", i === index));
      const entry = this.models[index];
      this.current = index;
      const accentHex = this.variantColor(index);
      this.wrap.style.setProperty("--stl-accent", accentHex);
      this.renderDownloads(entry);

      if (!this.THREE) return; // three.js not ready yet; select(0) re-runs after init

      const token = ++this.selectPending;
      const preview = this.previewFile(entry);
      if (!preview) {
        // Only non-previewable formats (e.g. STEP-only) — show a note, keep DLs.
        if (this.mesh) { this.scene.remove(this.mesh); this.disposeObject(this.mesh); this.mesh = null; }
        this.statusEl.textContent = "No 3D preview for this format — download to view.";
        this.statusEl.classList.remove("error");
        this.statusEl.style.display = "";
        return;
      }

      this.statusEl.textContent = "Loading model…";
      this.statusEl.classList.remove("error");
      this.statusEl.style.display = "";

      let built;
      try {
        built = await this.buildObject(preview, accentHex, token);
      } catch (e) {
        if (token === this.selectPending) this.fail("Model failed to load.");
        return;
      }
      if (!built || token !== this.selectPending) return; // superseded

      if (this.rim) this.rim.color.set(accentHex);
      if (this.mesh) { this.scene.remove(this.mesh); this.disposeObject(this.mesh); }
      this.scene.add(built.object);
      this.mesh = built.object;

      this.frameModel(built.radius);
      this.statusEl.style.display = "none";
    }

    // Build a centered, camera-tipped Object3D from a [ext, url] preview file.
    // STL gets our accent material; 3MF keeps its own baked colors.
    async buildObject([ext, url], accentHex, token) {
      const THREE = this.THREE;
      const buffer = await fetchSTL(url);
      if (token !== this.selectPending) return null;

      let object;
      if (ext === "stl") {
        const geometry = this.stlLoader.parse(buffer);
        geometry.computeVertexNormals();
        object = new THREE.Mesh(geometry, this.makeMaterial(new THREE.Color(accentHex)));
      } else if (ext === "3mf") {
        const ThreeMFLoader = await loadThreeMF();
        if (token !== this.selectPending) return null;
        object = new ThreeMFLoader().parse(buffer);
      } else {
        return null;
      }

      // Wrap so we can tip Z-up sources into the Y-up view, then recenter.
      const pivot = new THREE.Group();
      pivot.add(object);
      pivot.rotation.x = -Math.PI / 2;
      const box = new THREE.Box3().setFromObject(pivot);
      const center = box.getCenter(new THREE.Vector3());
      pivot.position.sub(center);
      const radius = box.getSize(new THREE.Vector3()).length() / 2 || 1;
      return { object: pivot, radius };
    }

    makeMaterial(accent) {
      return new this.THREE.MeshStandardMaterial({
        color: accent,
        metalness: CONFIG.material.metalness,
        // Rougher so the form reads clearly and the grid glints stay soft.
        roughness: CONFIG.material.roughness,
        // A bit emissive so you can always make out the shape in shadow.
        emissive: accent,
        emissiveIntensity: CONFIG.material.emissiveIntensity,
        flatShading: false,
      });
    }

    disposeObject(obj) {
      obj.traverse((o) => {
        if (o.geometry) o.geometry.dispose();
        if (o.material) {
          (Array.isArray(o.material) ? o.material : [o.material]).forEach((m) => m.dispose());
        }
      });
    }

    // Rebuild the download buttons from whatever formats this model has.
    renderDownloads(entry) {
      this.downloadsEl.innerHTML = "";
      const exts = DOWNLOAD_ORDER.filter((ext) => entry.files[ext]);
      exts.forEach((ext, i) => {
        const url = entry.files[ext];
        const a = document.createElement("a");
        a.className = "download" + (i === 0 ? "" : " secondary");
        a.href = url;
        a.setAttribute("download", url.split("/").pop());
        if (DOWNLOAD_TITLES[ext]) a.title = DOWNLOAD_TITLES[ext];
        a.innerHTML = `${DL_ICON}<span>${ext.toUpperCase()}</span>`;
        this.downloadsEl.appendChild(a);
      });
    }

    frameModel(r) {
      const dist = r / Math.sin((this.camera.fov * Math.PI) / 180 / 2);
      this.camera.position.set(dist * 0.7, dist * 0.55, dist * 0.9);
      this.camera.near = r / 100;
      this.camera.far = dist * 10;
      this.camera.updateProjectionMatrix();
      this.controls.target.set(0, 0, 0);
      this.controls.minDistance = r * 1.1;
      this.controls.maxDistance = dist * 3;
      this.controls.update();

      // Scale the overhead catch-light grid to the model and boost intensity by
      // distance^2 to counter inverse-square falloff, so glints stay consistent
      // regardless of model size.
      if (this.catch && this.catch.length) {
        const g = CONFIG.lights.catchGrid;
        const spread = r * g.spread; // half-width of the overhead grid
        const height = r * g.height; // how far above the model it floats
        const d = Math.hypot(spread, height);
        const I = g.illuminance * d * d;
        this.catch.forEach((l) => {
          l.position.set(l.userData.gx * spread, height, l.userData.gz * spread);
          l.intensity = I;
        });
      }
    }

    fail(msg) {
      this.statusEl.textContent = msg;
      this.statusEl.classList.add("error");
      this.statusEl.style.display = "";
    }

    disconnectedCallback() {
      if (this.raf) cancelAnimationFrame(this.raf);
      if (this.composer) this.composer.dispose();
      if (this.renderer) this.renderer.dispose();
    }
  }

  if (!customElements.get("stl-viewer")) {
    customElements.define("stl-viewer", STLViewer);
  }
})();
