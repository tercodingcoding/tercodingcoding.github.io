## 2025-05-15 - [Accessibility Gaps in Bootstrap Templates]
**Learning:** Bootstrap templates like DASHMIN often lack proper ARIA labels for icon-only buttons (sidebar toggler, back-to-top) and correct `lang` attributes when repurposed for other languages.
**Action:** Always check the `html` tag's `lang` attribute against the content language and ensure all icon-only links/buttons have descriptive `aria-label`s.

## 2025-05-24 - [Search Shortcut UX]
**Learning:** Adding a '/' keyboard shortcut to focus the search bar is a highly appreciated micro-UX improvement. It should be accompanied by a visual hint in the placeholder (e.g., " [/]") for discoverability.
**Action:** Implement a global keydown listener for '/' and dynamically append a hint to search placeholders in the site's main JS.
