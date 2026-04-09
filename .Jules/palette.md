## 2025-05-15 - [Accessibility Gaps in Bootstrap Templates]
**Learning:** Bootstrap templates like DASHMIN often lack proper ARIA labels for icon-only buttons (sidebar toggler, back-to-top) and correct `lang` attributes when repurposed for other languages.
**Action:** Always check the `html` tag's `lang` attribute against the content language and ensure all icon-only links/buttons have descriptive `aria-label`s.

## 2025-06-23 - [Global Keyboard Shortcuts for Semantic Inputs]
**Learning:** Implementing keyboard shortcuts like '/' for search can be done globally via `js/main.js` using `aria-keyshortcuts` and dynamic placeholder updates. This ensures consistency across multiple static template files without manual edits.
**Action:** Use `$(document).on('keydown', ...)` with exclusions for other input types to prevent focus hijacking, and use semantic selectors like `input[type="search"]` to target elements across the entire dashboard.
