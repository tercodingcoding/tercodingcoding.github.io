## 2025-05-15 - [Accessibility Gaps in Bootstrap Templates]
**Learning:** Bootstrap templates like DASHMIN often lack proper ARIA labels for icon-only buttons (sidebar toggler, back-to-top) and correct `lang` attributes when repurposed for other languages.
**Action:** Always check the `html` tag's `lang` attribute against the content language and ensure all icon-only links/buttons have descriptive `aria-label`s.

## 2024-05-24 - [Keyboard Shortcuts for Search]
**Learning:** Adding a '/' keyboard shortcut to focus the search bar significantly improves navigation speed for power users. Providing a visual hint like `[/]` in the placeholder is crucial for discoverability.
**Action:** Implement search shortcuts using global keydown listeners, ensuring they don't interfere with existing text inputs, and always provide an affordance in the UI to notify the user.
