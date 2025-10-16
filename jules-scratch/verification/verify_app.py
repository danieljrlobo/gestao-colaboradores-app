import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Navigate to the local HTML file
        await page.goto("file:///app/gestao_colaboradores.html")

        # Wait for the main app container to be visible
        app_container = page.locator("#app")
        await expect(app_container).to_be_visible(timeout=15000)

        # Wait for the loading overlay to be hidden
        loading_overlay = page.locator("#loading-overlay")
        await expect(loading_overlay).to_be_hidden(timeout=15000)

        # --- Screenshot 1: Main Dashboard ("Visão da Liderança") ---
        print("Capturing dashboard screenshot...")
        await page.screenshot(path="jules-scratch/verification/01_dashboard_view.png")

        # --- Screenshot 2: "Equipe" Tab ---
        print("Navigating to 'Equipe' tab and capturing screenshot...")
        await page.get_by_role("button", name="Equipe").click()
        # Wait for the main content to update
        await page.wait_for_timeout(500)
        await page.screenshot(path="jules-scratch/verification/02_team_view.png")

        # --- Screenshot 3: "Estratégias" Tab ---
        print("Navigating to 'Estratégias' tab and capturing screenshot...")
        await page.get_by_role("button", name="Estratégias").click()
        await page.wait_for_timeout(500)
        await page.screenshot(path="jules-scratch/verification/03_strategies_view.png")

        # --- Screenshot 4: "Feedbacks" Tab ---
        print("Navigating to 'Feedbacks' tab and capturing screenshot...")
        await page.get_by_role("button", name="Feedbacks").click()
        await page.wait_for_timeout(500)
        await page.screenshot(path="jules-scratch/verification/04_feedbacks_view.png")

        # --- Screenshot 5: "Análises" Tab ---
        print("Navigating to 'Análises' tab and capturing screenshot...")
        await page.get_by_role("button", name="Análises").click()
        # Wait for charts to render
        await page.wait_for_timeout(1500)
        await page.screenshot(path="jules-scratch/verification/05_analysis_view.png")

        await browser.close()
    print("Verification script finished successfully.")

if __name__ == "__main__":
    asyncio.run(main())