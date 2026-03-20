## 2025-05-15 - [Accessibility Gaps in Bootstrap Templates]
**Learning:** Bootstrap templates like DASHMIN often lack proper ARIA labels for icon-only buttons (sidebar toggler, back-to-top) and correct `lang` attributes when repurposed for other languages.
**Action:** Always check the `html` tag's `lang` attribute against the content language and ensure all icon-only links/buttons have descriptive `aria-label`s.

## 2025-06-23 - [Keyboard Shortcut Conflict Mitigation]
**Learning:** Implementing global keyboard shortcuts (like '/' for search) can interfere with browser native features or other interactive elements (selects, contenteditable).
**Action:** Always wrap `e.preventDefault()` within existence checks for the target element and exclude common interactive tags (`input`, `textarea`, `select`, `[contenteditable]`) from triggering the shortcut.
