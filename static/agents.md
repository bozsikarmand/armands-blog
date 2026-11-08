# AGENTS.md – armands.blog

Conventions for AI agents visiting this site.

- Bilingual static blog (Hugo). English content under /en/, Hungarian under /hu/.
- Every HTML page declares `lang`, links to its translation via `hreflang`, and has a
  skip link, a single `<main id="main-content">` landmark and a valid heading outline.
- Markdown is not content-negotiated; use the HTML pages or the JSON search indexes:
  /en/index.json, /hu/index.json (Fuse.js-compatible: title, description, content, uri).
- Dates in front matter are authoritative; the sitemap carries lastmod.
- No tracking, no ads, no cookies. Embedded YouTube videos use the nocookie player.
- Contact: hello@armands.site · Accessibility: /en/accessibility/, /hu/accessibility/
- There is no API, MCP server or agent endpoint; content discovery happens via the
  sitemap (/sitemap.xml), the tag pages and the search indexes above.
