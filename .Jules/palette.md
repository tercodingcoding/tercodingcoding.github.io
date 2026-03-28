## 2025-05-15 - [Accessibility Gaps in Bootstrap Templates]
**Learning:** Bootstrap templates like DASHMIN often lack proper ARIA labels for icon-only buttons (sidebar toggler, back-to-top) and correct `lang` attributes when repurposed for other languages.
**Action:** Always check the `html` tag's `lang` attribute against the content language and ensure all icon-only links/buttons have descriptive `aria-label`s.

## 2025-06-24 - [Search Discovery via Keyboard Shortcuts]
**Learning:** Adding a '/' shortcut to focus search is highly expected by power users, but it must be discoverable through localized placeholder hints and tooltips, while being accessible via `aria-keyshortcuts`.
**Action:** Implement search shortcuts using a global listener that avoids form fields, and dynamically enhance visible search inputs with ` [/]` placeholders and `aria-keyshortcuts="/"`.
