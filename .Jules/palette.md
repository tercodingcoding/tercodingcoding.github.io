## 2025-05-15 - [Accessibility Gaps in Bootstrap Templates]
**Learning:** Bootstrap templates like DASHMIN often lack proper ARIA labels for icon-only buttons (sidebar toggler, back-to-top) and correct `lang` attributes when repurposed for other languages.
**Action:** Always check the `html` tag's `lang` attribute against the content language and ensure all icon-only links/buttons have descriptive `aria-label`s.

## 2025-05-16 - [Keyboard Shortcut Hints]
**Learning:** Adding dynamic keyboard shortcut hints (like " [/]") to input placeholders and localized tooltips significantly improves feature discoverability for power users while maintaining accessibility for screen readers via `aria-keyshortcuts`.
**Action:** When implementing keyboard shortcuts for global actions (like search), update the UI to show the shortcut hint and ensure it is localized based on the page's `lang` attribute.
