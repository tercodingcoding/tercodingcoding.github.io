## 2025-05-15 - [Accessibility Gaps in Bootstrap Templates]
**Learning:** Bootstrap templates like DASHMIN often lack proper ARIA labels for icon-only buttons (sidebar toggler, back-to-top) and correct `lang` attributes when repurposed for other languages.
**Action:** Always check the `html` tag's `lang` attribute against the content language and ensure all icon-only links/buttons have descriptive `aria-label`s.

## 2025-05-22 - [Centralized UX & Accessibility Injection]
**Learning:** For template-heavy projects with many static HTML files, injecting accessibility attributes (ARIA labels, tooltips) and UX enhancements (keyboard shortcuts) via a global JavaScript file is more maintainable than manual per-file edits. It also allows for easier localization by checking the `html` tag's `lang` attribute once.
**Action:** Use centralized logic in `js/main.js` to scan and enhance common template components (e.g., sidebar togglers, search inputs) to ensure a consistent experience across the entire application.
