import re
from playwright.sync_api import Page, expect


def test_titre(page: Page):
    page.goto("https://thorigne-tt.net/tournoi/")
    expect(page).to_have_title(re.compile("Playwright"))
