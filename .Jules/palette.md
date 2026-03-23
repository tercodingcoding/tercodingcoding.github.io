## 2025-05-15 - [Accessibility Gaps in Bootstrap Templates]
**Learning:** Bootstrap templates like DASHMIN often lack proper ARIA labels for icon-only buttons (sidebar toggler, back-to-top) and correct `lang` attributes when repurposed for other languages.
**Action:** Always check the `html` tag's `lang` attribute against the content language and ensure all icon-only links/buttons have descriptive `aria-label`s.

## 2025-05-20 - [Resilient JS Pattern for Multi-page Templates]
**Learning:** In projects where a single `main.js` is shared across many different template pages, failing to check for the existence of an element before initializing a third-party plugin (like Chart.js or OwlCarousel) can cause script termination, breaking unrelated UI features like tooltips or navigation.
**Action:** Always implement defensive checks (e.g., `if ($('#element').length > 0)`) before initializing plugins to ensure JS execution continues for all features on all pages.
