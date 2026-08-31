# Axon Compass — Build & Deploy Instructions

## 1. Where to put this folder

Unzip this entire folder as-is. Everything (`_config.yml`, `_toc.yml`, `intro.md`, `process.md`, `fields/`, `robots.txt`, `requirements.txt`) must sit **directly inside one project folder** — for example:

```
C:\Users\YOU\axon-compass\
    _config.yml
    _toc.yml
    intro.md
    process.md
    robots.txt
    requirements.txt
    fields\
        education\
            index.md
            01-the-forgetting-curve-classroom.md
            ...
        economics\
            ...
```

Do not put it inside another folder that already has its own `_config.yml` — Jupyter Book only looks at the top level of the folder you point it at.

## 2. Build it locally

Open a terminal **inside** the `axon-compass` folder and run:

```
pip install -r requirements.txt
jupyter-book build .
```

The finished site appears at `_build/html/index.html`. Open that file directly in a browser to check it before publishing.

## 3. Before you publish — edit three placeholders

Two files have `YOUR-GITHUB-USERNAME` placeholders that must be replaced with your real GitHub username (or organization name) before publishing:

- `_config.yml` — the `repository.url`, `html.baseurl`, and `sphinx.config.html_baseurl` lines.
- `robots.txt` — the `Sitemap:` line.

These control the links search engines and the "open in GitHub" button use — if left as placeholders, search engines will index broken URLs.

## 4. Publish it — free, public, no login wall (GitHub Pages)

This is what makes it genuinely open access: no password, no paywall, indexable by Google.

```
git init
git add .
git commit -m "Axon Compass v1"
git branch -M main
git remote add origin https://github.com/YOUR-GITHUB-USERNAME/axon-compass.git
git push -u origin main

ghp-import -n -p -f _build/html
```

`ghp-import` pushes the built site to a `gh-pages` branch and turns on GitHub Pages automatically. Within a few minutes the book is live at:

```
https://YOUR-GITHUB-USERNAME.github.io/axon-compass/
```

Anyone can open that link — no account, no login, nothing to install. That link IS the "open access" version.

## 5. Making it the first result when people search for it

No one can guarantee the #1 spot on Google, but these are the concrete, real steps that actually move the needle, in order of impact:

1. **Use an exact-match, uncommon title.** "Axon Compass" is already a good choice precisely because almost nothing else online uses that exact phrase — a search for "Axon Compass" will have very little competition. Keep the page title consistent everywhere (browser tab, `_config.yml` `title:`, and the `<h1>` on `intro.md` all already say the same thing).
2. **Submit the site to Google Search Console** (search.google.com/search-console, free). Add the property, verify ownership (GitHub Pages supports the HTML-file verification method), and submit the URL `https://YOUR-GITHUB-USERNAME.github.io/axon-compass/`. This is what actually gets a brand-new site crawled quickly instead of waiting weeks.
3. **Link to it from somewhere Google already trusts** — your nonprofit's main website, your Instagram/LinkedIn bio, any partner organization's site. A single link from an established domain does more for ranking than almost anything else on this list.
4. **Keep `robots.txt` allowing everything** (already set to `Allow: /` in this package) — this is what tells search engines they're allowed to index every page, which is required for full open access to actually show up in search results.
5. **Once live, ask Google to index the specific new URL directly** inside Search Console's "URL Inspection" tool — this can get a specific page indexed within hours instead of days.

None of this requires touching the book's content again — it's entirely about the publishing and promotion steps above, which only need to be done once.
