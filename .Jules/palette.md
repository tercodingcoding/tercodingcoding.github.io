## 2025-05-15 - [Accessibility Gaps in Bootstrap Templates]
**Learning:** Bootstrap templates like DASHMIN often lack proper ARIA labels for icon-only buttons (sidebar toggler, back-to-top) and correct `lang` attributes when repurposed for other languages.
**Action:** Always check the `html` tag's `lang` attribute against the content language and ensure all icon-only links/buttons have descriptive `aria-label`s.

## 2024-05-22 - [Keyboard Shortcuts and Visual Affordance]
**Learning:** Adding keyboard shortcuts (like '/' for search) significantly improves UX for power users, but they need visual hints (like ' [/]' in placeholders) and ARIA attributes (`aria-keyshortcuts`) for discoverability and accessibility.
**Action:** When implementing keyboard shortcuts, always provide a visual hint in the UI and use the `aria-keyshortcuts` attribute.
