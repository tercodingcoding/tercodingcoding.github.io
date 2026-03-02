## 2025-05-15 - [Accessibility Gaps in Bootstrap Templates]
**Learning:** Bootstrap templates like DASHMIN often lack proper ARIA labels for icon-only buttons (sidebar toggler, back-to-top) and correct `lang` attributes when repurposed for other languages.
**Action:** Always check the `html` tag's `lang` attribute against the content language and ensure all icon-only links/buttons have descriptive `aria-label`s.

## 2026-03-02 - [Skip to Content Link Implementation]
**Learning:** For accessibility in templates with sticky navbars, a "Skip to Content" link should have a high z-index (e.g., 10001) to ensure it's visible when focused and not hidden behind the navigation.
**Action:** Implement the "Skip to Content" link as the first focusable element in the `<body>` and target the main content area with `id="main-content"` and `tabindex="-1"`.
