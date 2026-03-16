## 2025-05-15 - [Accessibility Gaps in Bootstrap Templates]
**Learning:** Bootstrap templates like DASHMIN often lack proper ARIA labels for icon-only buttons (sidebar toggler, back-to-top) and correct `lang` attributes when repurposed for other languages.
**Action:** Always check the `html` tag's `lang` attribute against the content language and ensure all icon-only links/buttons have descriptive `aria-label`s.

## 2025-06-23 - [Keyboard Shortcut Discoverability]
**Learning:** Power-user shortcuts like `/` for search focus are highly appreciated but need discovery hints (like `[/]` in placeholder) to be effective for all users.
**Action:** When adding keyboard shortcuts, always include a visual hint or tooltip to make the feature discoverable.
