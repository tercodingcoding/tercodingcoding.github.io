## 2025-05-15 - [Accessibility Gaps in Bootstrap Templates]
**Learning:** Bootstrap templates like DASHMIN often lack proper ARIA labels for icon-only buttons (sidebar toggler, back-to-top) and correct `lang` attributes when repurposed for other languages.
**Action:** Always check the `html` tag's `lang` attribute against the content language and ensure all icon-only links/buttons have descriptive `aria-label`s.

## 2025-06-24 - [Discoverable Keyboard Shortcuts]
**Learning:** Keyboard shortcuts like `/` for focusing search are high-impact micro-UX wins, but they must be discoverable. Adding a simple `[/]` hint in the placeholder and `aria-keyshortcuts` attribute ensures both power users and screen reader users can benefit.
**Action:** When adding shortcuts, always include visual hints in the UI and appropriate ARIA attributes for accessibility.
