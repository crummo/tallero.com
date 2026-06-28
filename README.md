# Tallero — marketing site

The public website for **Tallero**, the score-keeper for game night. Plain
static HTML/CSS/JS — no build step. Lives at **https://gettallero.com**
(currently deployed to https://tallero.netlify.app).

## Structure

```
index.html      Landing page (hero, app mockups, dark-mode showcase, games, beta signup)
support.html    Support / FAQ
privacy.html    Privacy policy
tally.css       All styles
assets/         Brand mark variants, og-image, and the game/UI glyphs
                (game icons mirror the app's own icons)
netlify.toml    Static publish config (publish = ".")
```

## Two launch switches (in index.html)

Both default to a safe "coming soon / not wired" state. Flip them at launch:

- **App Store badge** — `APPSTORE` config near the bottom of `index.html`.
  Set `live: true`, add your App Store `url`, and drop Apple's official
  badge over `assets/appstore-badge.svg`. All "Coming soon" pills become the
  real linked badge.
- **Beta "Notify me" signup** — `NOTIFY` config below it. Add an email-capture
  `endpoint` (Formspree/Buttondown/Mailchimp) and/or a public `testflight`
  link. Until then the form shows an honest "not switched on yet" message.

## Deploy

Static site, deploys to Netlify (site id stored locally in `.netlify/state.json`,
which is gitignored). With git-based continuous deployment connected in the
Netlify dashboard, every push to this repo deploys automatically.

## Brand

Wordmark: **Bricolage Grotesque 800**. Brand blue `#0F5FA5`, gold slash
`#D9A934`. The four mark bars are fixed (purple, pink, green, teal); the slash
recolors per background. See the app's design handoff for full tokens.
