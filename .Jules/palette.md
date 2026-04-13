## 2025-05-15 - [Accessibility Gaps in Bootstrap Templates]
**Learning:** Bootstrap templates like DASHMIN often lack proper ARIA labels for icon-only buttons (sidebar toggler, back-to-top) and correct `lang` attributes when repurposed for other languages.
**Action:** Always check the `html` tag's `lang` attribute against the content language and ensure all icon-only links/buttons have descriptive `aria-label`s.

## 2025-05-16 - [Dynamic Template Corrections]
**Learning:** DASHMIN templates contain hardcoded typos like "Notificatin" and inconsistent localization in navbar labels. These can be fixed globally via script without modifying every HTML file.
**Action:** Use regex-based dynamic text replacement in `main.js` to correct template typos and enforce consistent localization based on the document's `lang` attribute.

## 2025-05-16 - [ARIA Property vs. Attribute]
**Learning:** Modern IDL properties like `el.ariaLabel` are not supported in older browsers, whereas `el.setAttribute('aria-label', ...)` or `$(el).attr('aria-label', ...)` has universal support.
**Action:** Always prefer `setAttribute` or jQuery `.attr()` for ARIA attributes to ensure accessibility works across all browser versions.
