// pymdownx.superfences renders ```mermaid blocks as
// `<pre class="mermaid"><code>...&gt;...</code></pre>`. mermaid v10 reads
// the inner HTML and treats the literal `&gt;` entities as part of the
// diagram source, which produces a generic "Syntax error in text"
// because `--&gt;` is not the transition operator (it's `-->`).
//
// We disable mermaid's startOnLoad, unwrap the <code> child ourselves,
// and then explicitly call mermaid.run() so the unwrap is guaranteed to
// happen before mermaid scans for diagrams.
(function () {
  function unwrapMermaidCode() {
    document.querySelectorAll('pre.mermaid > code').forEach(function (code) {
      var pre = code.parentElement;
      pre.textContent = code.textContent;
    });
  }
  function init() {
    if (typeof mermaid === 'undefined') return;
    mermaid.initialize({
      startOnLoad: false,
      theme: 'dark',
      securityLevel: 'loose',
      flowchart: { useMaxWidth: true, htmlLabels: true },
    });
    unwrapMermaidCode();
    if (typeof mermaid.run === 'function') {
      mermaid.run({ querySelector: 'pre.mermaid' });
    } else if (typeof mermaid.init === 'function') {
      mermaid.init(undefined, document.querySelectorAll('pre.mermaid'));
    }
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
