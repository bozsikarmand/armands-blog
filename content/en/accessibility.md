---
title: Accessibility statement
date: 2026-11-08
slug: accessibility
_build:
  list: never
  render: always
---

Armand Viktor Bozsik is committed to ensuring digital accessibility for people
with disabilities. I continually improve the user experience for everyone and
apply the relevant accessibility standards.

## Conformance status

This website aims to conform to the **Web Content Accessibility Guidelines
(WCAG) 2.2 at Level AAA**. The guidelines explain how to make web content
more accessible to people with a wide range of disabilities.

## Measures taken

- **Contrast**: all text meets enhanced contrast ratios (7:1 for normal
  text, 4.5:1 for large text) in both the dark and the light theme,
  verified by automated tooling (`tools/contrast-audit.py`).
- **Keyboard**: every interactive element (navigation, search, language and
  theme switchers, menus) is fully operable by keyboard alone.
- **Focus**: a clearly visible focus indicator follows the WCAG 2.2 AAA
  focus-appearance requirements and is never obscured by the fixed header.
- **Screen readers**: semantic landmarks, headings, skip link, labels and
  status messages support assistive technology; automated audits run with
  axe-core (`tools/axe-scan.sh`).
- **Adaptability**: content reflows at 320&nbsp;px, survives 200% text
  resizing, and honors the user's text-spacing and reduced-motion settings.
- **Images**: alternative text is provided for informative images; purely
  decorative images are marked as such.
- **Language**: page language is declared; a language switcher is available
  in the header and the footer.
- **Motion**: animations are disabled when the user prefers reduced motion.

## Not applicable / third-party content

- **Embedded videos** are hosted on YouTube; captions/subtitles are
  provided by the video player. Sign-language interpretation of third-party
  videos is outside the publisher's control.
- **No timed content, authentication or multi-step forms** exist on this site.
- Older posts may link to external, third-party resources whose
  accessibility is outside my control.

## Feedback

If you encounter an accessibility barrier, please let me know and I will
try to fix it promptly:

- Email: [hello@armands.site](mailto:hello@armands.site)
- This statement was last updated on **2026-11-08**.
