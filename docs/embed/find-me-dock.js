/**
 * find-me-dock — embeddable social dock with rainbow hover + URL preview
 *
 * --- Basic embed (any site) ---
 *
 * <script src="https://docs.jumperless.org/embed/find-me-dock.js" defer></script>
 * <find-me-dock></find-me-dock>
 *
 * Uses built-in links + background. Self-contained (Shadow DOM); host CSS won't leak in/out.
 *
 * --- Custom background / height ---
 *
 * <find-me-dock
 *   background="https://yoursite.com/path/to/image.png"
 *   min-height="220px"
 * ></find-me-dock>
 *
 * --- Custom title ---
 *
 * <find-me-dock title="Say Hi"></find-me-dock>
 *
 * --- Custom links (icon names from https://simpleicons.org/) ---
 *
 * <find-me-dock links='[
 *   {"href":"https://discord.gg/your-server","icon":"discord"},
 *   {"href":"https://github.com/you","icon":"github","label":"GitHub"}
 * ]'></find-me-dock>
 *
 * --- iframe embed (no JS on host page) ---
 *
 * <iframe
 *   src="https://docs.jumperless.org/embed/demo.html"
 *   width="100%"
 *   height="280"
 *   style="border:0;border-radius:12px;"
 *   loading="lazy"
 *   title="Find me on the internet"
 * ></iframe>
 *
 * --- Self-host ---
 *
 * Copy find-me-dock.js (+ optional demo.html) and point the script src at your copy.
 * If you use a custom background image, host that too or pass a full URL in background=.
 *
 * --- Local preview ---
 *
 * https://docs.jumperless.org/embed/demo.html
 */
(() => {
  const DEFAULT_LINKS = [
    { href: "https://discord.gg/bvacV7r3FP", icon: "discord" },
    { href: "https://github.com/Architeuthis-Flux", icon: "github" },
    { href: "https://bsky.app/profile/jumperless.org", icon: "bluesky" },
    { href: "https://x.com/arabidsquid", icon: "twitter" },
    { href: "https://leds.social/@ArchiteuthisFlux", icon: "mastodon" },
    { href: "https://www.youtube.com/@arabidsquid", icon: "youtube" },
  ];

  const ICON_CDN =
    "https://cdn.jsdelivr.net/npm/simple-icons@v10/icons";

  // Same rainbow as docs heading classes (.red, .orange, .yellow, …)
  const RAINBOW = [

   
    
    "#FF8EC1",
    "#bf96ff",
    "#7AB7F0",
    "#BFF08E",
    "#FFE07A",
    "#FF7E72",
   
   
   
    
    
  ];

  const RAINBOW_HOVER = Array.from({ length: 6 }, (_, i) => {
    const color = RAINBOW[i % RAINBOW.length];
    const n = i + 1;
    return `.dock a:nth-child(${n}):hover .icon, .dock a:nth-child(${n}):focus-visible .icon { background: ${color}; }`;
  }).join("\n");

  const STYLES = `
    :host {
      display: block;
      margin: 1rem 0;
      font-family: Lato, proxima-nova, "Helvetica Neue", Arial, sans-serif;
    }
    .section {
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      min-height: var(--fmd-min-height, 180px);
      padding: 2.25rem 1.25rem 1.5rem;
      border-radius: 12px;
      overflow: visible;
      text-align: center;
      color: #FFFFFF;
    }
    .backdrop {
      position: absolute;
      inset: 0;
      border-radius: inherit;
      overflow: hidden;
      pointer-events: none;
      z-index: 0;
      background-image: var(--fmd-bg);
      background-position: center;
      background-size: cover;
      background-repeat: no-repeat;
    }
    .backdrop::after {
      content: "";
      position: absolute;
      inset: 0;
      background: rgba(0, 0, 0, 0.28);
    }
    .title, .url, .dock {
      position: relative;
      z-index: 1;
    }
    .title {
      margin: 0;
      font-family: "Roboto Slab", ff-tisa-web-pro, Georgia, Arial, sans-serif;
      font-size: 2.65rem;
      font-weight: 700;
      color: #FFFFFFE4;
      line-height: 1.2;
      transition: color 0.15s ease;
    }
    .url {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0;
      min-height: 2rem;
      font-size: 1rem;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      color: rgba(255, 255, 255, 0.9);
      text-shadow: 0 1px 10px rgba(0, 0, 0, 0.85);
      opacity: 0;
      transform: translateY(6px);
      transition: opacity 0.15s ease, transform 0.15s ease, color 0.15s ease;
      pointer-events: none;
    }
    .url.visible {
      opacity: 1;
      transform: translateY(-0.25rem);
      pointer-events: auto;
      user-select: all;
      cursor: text;
    }
    .dock {
      display: flex;
      align-items: flex-end;
      justify-content: center;
      flex-wrap: wrap;
      gap: 2.45rem;
      margin: 0;
      padding-bottom: 0.25rem;
    }
    .dock a {
      display: flex;
      align-items: flex-end;
      line-height: 0;
      transition: transform 0.13s cubic-bezier(0.34, 1.56, 0.64, 1);
      transform-origin: bottom center;
      --icon-url: none;
    }
    .dock a:hover {
      transform: scale(1.95);
      z-index: 5;
    }
    .dock a:hover + a,
    .dock a:has(+ a:hover) {
      transform: scale(1.12);
      z-index: 4;
    }
    .dock a:hover + a + a,
    .dock a:has(+ a + a:hover) {
      transform: scale(1);
      z-index: 3;
    }
    .dock .icon {
      display: block;
      width: 48px;
      height: 48px;
      border-radius: 12px;
      background: rgba(255 255 255 / 0.89);
      transition: background 0.12s ease, opacity 0.12s ease;
      -webkit-mask: var(--icon-url) center / contain no-repeat;
      mask: var(--icon-url) center / contain no-repeat;
    }
    .dock a:hover .icon {
      opacity: 1;
    }
    ${RAINBOW_HOVER}
  `;

  function parseLinks(raw) {
    if (!raw) return DEFAULT_LINKS;
    try {
      const parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed : DEFAULT_LINKS;
    } catch {
      return DEFAULT_LINKS;
    }
  }

  function rainbowColor(index) {
    const n = RAINBOW.length;
    return RAINBOW[((index % n) + n) % n];
  }

  function wireDock(section, label, dock, titleEl) {
    const isInHoverZone = (node) =>
      !!node && (dock.contains(node) || label.contains(node));

    const dockLinks = () => [...dock.querySelectorAll("a")];

    const show = (link) => {
      label.textContent = link.href.replace(/^https?:\/\//, "");
      const i = dockLinks().indexOf(link);
      const urlColor = i >= 0 ? rainbowColor(i - 1) : "rgba(255, 255, 255, 0.9)";
      const titleColor = i >= 0 ? rainbowColor(i - 2) : "#FFFFFF";
      label.style.color = urlColor;
      titleEl.style.color = titleColor;
      label.classList.add("visible");
    };

    const clear = () => {
      label.textContent = "";
      label.style.color = "";
      titleEl.style.color = "";
      label.classList.remove("visible");
    };

    dock.querySelectorAll("a").forEach((link) => {
      link.addEventListener("mouseenter", () => show(link));
      link.addEventListener("focus", () => show(link));
    });

    const maybeClear = (event) => {
      if (!isInHoverZone(event.relatedTarget)) clear();
    };

    dock.addEventListener("mouseleave", maybeClear);
    label.addEventListener("mouseleave", maybeClear);
    section.addEventListener("focusout", maybeClear);
  }

  function ensureFonts() {
    if (document.querySelector("link[data-find-me-dock-fonts]")) return;
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href =
      "https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@700&family=Lato:wght@400;700&display=swap";
    link.dataset.findMeDockFonts = "";
    document.head.appendChild(link);
  }

  class FindMeDock extends HTMLElement {
    connectedCallback() {
      if (this.shadowRoot) return;

      ensureFonts();

      const title = this.getAttribute("title") || "Find Me On The Internet";
      const background =
        this.getAttribute("background") ||
        "https://docs.jumperless.org/assets/BusinessCard2022Backpsd.png";
      const minHeight = this.getAttribute("min-height") || "245px";
      const links = parseLinks(this.getAttribute("links"));

      const shadow = this.attachShadow({ mode: "open" });
      shadow.innerHTML = `
        <style>${STYLES}</style>
        <div class="section" part="section">
          <div class="backdrop" part="backdrop"></div>
          <h2 class="title" part="title">${title}</h2>
          <p class="url" part="url" aria-live="polite"></p>
          <div class="dock" part="dock">
            ${links
              .map(
                ({ href, icon, label }) =>
                  `<a href="${href}" data-icon="${icon}" target="_blank" rel="noopener noreferrer" aria-label="${label || icon}" style="--icon-url: url('${ICON_CDN}/${icon}.svg')">
                    <span class="icon"></span>
                  </a>`
              )
              .join("")}
          </div>
        </div>
      `;

      const section = shadow.querySelector(".section");
      section.style.setProperty("--fmd-bg", `url("${background}")`);
      section.style.setProperty("--fmd-min-height", minHeight);

      wireDock(
        section,
        shadow.querySelector(".url"),
        shadow.querySelector(".dock"),
        shadow.querySelector(".title")
      );
    }
  }

  if (!customElements.get("find-me-dock")) {
    customElements.define("find-me-dock", FindMeDock);
  }
})();
