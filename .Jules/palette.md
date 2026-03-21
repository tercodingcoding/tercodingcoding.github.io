## 2025-05-15 - [Accessibility Gaps in Bootstrap Templates]
**Learning:** Bootstrap templates like DASHMIN often lack proper ARIA labels for icon-only buttons (sidebar toggler, back-to-top) and correct `lang` attributes when repurposed for other languages.
**Action:** Always check the `html` tag's `lang` attribute against the content language and ensure all icon-only links/buttons have descriptive `aria-label`s.

## 2025-06-23 - [Resilient JS Pattern for Template Components]
**Learning:** DASHMIN and similar Bootstrap templates often initialize all plugins (Charts, Calendars, etc.) in a single global script. If an element is missing from a specific page, these initializations can fail and halt subsequent JS execution (like tooltips or custom UX logic).
**Action:** Use defensive checks (e.g., `if ($el.length > 0)`) before initializing plugins and place custom UX enhancements at the top of the script to ensure they run regardless of downstream errors.
