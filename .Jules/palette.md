## 2025-05-15 - [Accessibility Gaps in Bootstrap Templates]
**Learning:** Bootstrap templates like DASHMIN often lack proper ARIA labels for icon-only buttons (sidebar toggler, back-to-top) and correct `lang` attributes when repurposed for other languages.
**Action:** Always check the `html` tag's `lang` attribute against the content language and ensure all icon-only links/buttons have descriptive `aria-label`s.

## 2024-05-16 - [Slash to Search Keyboard Shortcut]
**Learning:** Adding a keyboard shortcut like '/' to focus the search input significantly improves the efficiency of navigation in dashboards. Combining this with dynamic placeholder updates (` [/]`) and `aria-keyshortcuts` ensures both discoverability and accessibility.
**Action:** Implement dynamic keyboard shortcut hints and listeners in a central JS file (`js/main.js`) to apply them across all pages of a template-based site.
