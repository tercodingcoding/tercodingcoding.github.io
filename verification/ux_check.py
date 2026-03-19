import asyncio
import os
from playwright.async_api import async_playwright

async def verify_ux():
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 720})
        page = await context.new_page()

        # Determine the base path for local files
        base_url = f"file://{os.getcwd()}/index.html"
        print(f"Opening {base_url}")

        await page.goto(base_url)

        # 1. Verify search placeholder hint
        search_input = page.locator('input[type="search"]').first
        placeholder = await search_input.get_attribute('placeholder')
        print(f"Search placeholder: {placeholder}")
        assert "[/]" in placeholder, "Search placeholder missing [/] hint"

        # 2. Verify aria-current="page" on active nav link
        active_link = page.locator('.nav-link.active')
        aria_current = await active_link.get_attribute('aria-current')
        print(f"Active link aria-current: {aria_current}")
        assert aria_current == "page", "Active link missing aria-current='page'"

        # 3. Verify sidebar toggler a11y attributes
        toggler = page.locator('.sidebar-toggler')
        label = await toggler.get_attribute('aria-label')
        title = await toggler.get_attribute('title')
        print(f"Sidebar toggler label: {label}, title: {title}")
        assert label is not None and "Sidebar" in label, "Sidebar toggler missing aria-label"
        assert title == label, "Title does not match aria-label"

        # 4. Verify keyboard shortcut [/]
        # Focus something else first
        await page.evaluate("document.body.focus()")
        await page.keyboard.press("/")

        # Check if search input is focused
        is_focused = await page.evaluate("document.activeElement.type === 'search'")
        print(f"Is search input focused after [/]? {is_focused}")
        assert is_focused, "Search input not focused after pressing [/]"

        # 5. Check English page (e.g., table.html)
        table_url = f"file://{os.getcwd()}/table.html"
        print(f"Opening {table_url}")
        await page.goto(table_url)

        toggler_en = page.locator('.sidebar-toggler')
        label_en = await toggler_en.get_attribute('aria-label')
        print(f"English Sidebar toggler label: {label_en}")
        assert label_en == "Show/Hide Sidebar", f"Unexpected English label: {label_en}"

        placeholder_en = await page.locator('input[type="search"]').first.get_attribute('placeholder')
        print(f"English search placeholder: {placeholder_en}")
        assert "[/]" in placeholder_en, "English search placeholder missing [/] hint"

        print("Verification successful!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_ux())
