## 2025-05-15 - [Accessibility Gaps in Bootstrap Templates]
**Learning:** Bootstrap templates like DASHMIN often lack proper ARIA labels for icon-only buttons (sidebar toggler, back-to-top) and correct `lang` attributes when repurposed for other languages.
**Action:** Always check the `html` tag's `lang` attribute against the content language and ensure all icon-only links/buttons have descriptive `aria-label`s.

## 2026-04-11 - [Dynamic Keyboard Shortcut Hinting]
**Learning:** Adding a keyboard shortcut (like '/') significantly improves navigation efficiency, but it must be paired with visible hints (like ' [/]') in placeholders and proper `aria-keyshortcuts` attributes to be discoverable and accessible.
**Action:** When implementing global keyboard shortcuts for inputs, dynamically inject hints into placeholders and apply `aria-keyshortcuts` to all relevant elements via a global script to ensure consistency across templated pages.
