## 2025-05-15 - [Accessibility Gaps in Bootstrap Templates]
**Learning:** Bootstrap templates like DASHMIN often lack proper ARIA labels for icon-only buttons (sidebar toggler, back-to-top) and correct `lang` attributes when repurposed for other languages.
**Action:** Always check the `html` tag's `lang` attribute against the content language and ensure all icon-only links/buttons have descriptive `aria-label`s.

## 2026-03-19 - [Global Accessibility & UX Patching via JS]
**Learning:** In projects with many legacy or static HTML files, a global JS script can efficiently apply accessibility attributes (aria-current, aria-label) and UX hints (keyboard shortcuts) across the entire site without manual per-file edits.
**Action:** Use a global script like `js/main.js` to dynamically inject a11y attributes and shortcuts, using the `<html>` lang attribute for localization.
