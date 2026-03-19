import asyncio
import os
from playwright.async_api import async_playwright

async def verify_ux_visual():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport={'width': 1280, 'height': 720},
            record_video_dir="/home/jules/verification/video"
        )
        page = await context.new_page()

        # Disable CSS transitions/animations for stable screenshots
        await page.add_init_script("""
            const style = document.createElement('style');
            style.innerHTML = `
                *, *::before, *::after {
                    transition: none !important;
                    animation: none !important;
                }
            `;
            document.head.appendChild(style);
        """)

        base_url = f"file://{os.getcwd()}/index.html"
        await page.goto(base_url)
        await page.wait_for_timeout(500)

        # Demonstrate keyboard shortcut [/]
        await page.keyboard.press("/")
        await page.wait_for_timeout(500)

        # Take screenshot of focused search with hint
        await page.screenshot(path="/home/jules/verification/verification.png")
        await page.wait_for_timeout(1000)

        # Navigate to English page to show localization
        table_url = f"file://{os.getcwd()}/table.html"
        await page.goto(table_url)
        await page.wait_for_timeout(500)

        # Trigger sidebar toggler tooltip
        await page.hover('.sidebar-toggler')
        await page.wait_for_timeout(500)
        await page.screenshot(path="/home/jules/verification/verification_en.png")
        await page.wait_for_timeout(1000)

        await context.close()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_ux_visual())
