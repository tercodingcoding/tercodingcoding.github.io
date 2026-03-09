## 2025-05-15 - [Accessibility Gaps in Bootstrap Templates]
**Learning:** Bootstrap templates like DASHMIN often lack proper ARIA labels for icon-only buttons (sidebar toggler, back-to-top) and correct `lang` attributes when repurposed for other languages.
**Action:** Always check the `html` tag's `lang` attribute against the content language and ensure all icon-only links/buttons have descriptive `aria-label`s.

## 2026-03-09 - [Legacy Bootstrap Accessibility & Visual Stability]
**Learning:** Older DASHMIN templates frequently use legacy Bootstrap 4 classes like `.sr-only` which should be updated to `.visually-hidden` for modern framework compliance. Additionally, pulse/infinite animations on small UI elements (like status dots) can cause instability in automated visual verification tools like Playwright.
**Action:** Replace `.sr-only` with `.visually-hidden` for accessibility and disable animations via script during Playwright visual testing to ensure screenshot consistency.
