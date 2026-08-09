# Find Me On The Internet

Hover an icon — it grows, goes rainbow, and shows the link in the middle so you can copy it. This is the same widget on the [home page](/).

<div>
<find-me-dock background="/assets/BusinessCard2022Backpsd.png"></find-me-dock>
</div>

---

## Embed on your site

One script tag, one element. Styles stay inside a Shadow DOM so your site's CSS won't fight it.

### Basic

```html
<script src="https://docs.jumperless.org/embed/find-me-dock.js" defer></script>
<find-me-dock></find-me-dock>
```

Uses the default links and background image from this site.

### Custom background or height

```html
<find-me-dock
  background="https://yoursite.com/your-image.png"
  min-height="220px"
></find-me-dock>
```

### Custom title

```html
<find-me-dock title="Say Hi"></find-me-dock>
```

### Custom links

Icon names come from [Simple Icons](https://simpleicons.org/) (`discord`, `github`, `bluesky`, `youtube`, …).

```html
<find-me-dock links='[
  {"href":"https://discord.gg/your-server","icon":"discord"},
  {"href":"https://github.com/you","icon":"github","label":"GitHub"}
]'></find-me-dock>
```

### iframe (no JavaScript on your page)

Minimal chrome-free version for CMSes that only allow embeds:

```html
<iframe
  src="https://docs.jumperless.org/embed/demo.html"
  width="100%"
  height="280"
  style="border:0;border-radius:12px;"
  loading="lazy"
  title="Find me on the internet"
></iframe>
```

### Self-host

Copy [`find-me-dock.js`](/embed/find-me-dock.js) to your server and point the script tag at your copy. Host your own background image or pass a full URL in `background=`.

Full API comments are at the top of that file in the repo.
