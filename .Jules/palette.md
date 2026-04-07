## 2025-05-15 - [Accessibility Gaps in Bootstrap Templates]
**Learning:** Bootstrap templates like DASHMIN often lack proper ARIA labels for icon-only buttons (sidebar toggler, back-to-top) and correct `lang` attributes when repurposed for other languages.
**Action:** Always check the `html` tag's `lang` attribute against the content language and ensure all icon-only links/buttons have descriptive `aria-label`s.

## 2025-06-23 - [Resilient Global UX Logic in Template Environments]
**Learning:** In projects using DASHMIN or similar Bootstrap templates, dashboard-specific scripts (like Chart.js) often lack defensive checks and can throw errors if elements are missing, halting script execution. Global UX features (like keyboard shortcuts) should be placed at the beginning of the main script or within a `$(document).ready()` block that is independent of specific DOM element existence.
**Action:** Place global interaction logic (shortcuts, accessibility fixes) before specialized dashboard initializations and use `$(document).ready()` to ensure elements like search bars are available for manipulation.
