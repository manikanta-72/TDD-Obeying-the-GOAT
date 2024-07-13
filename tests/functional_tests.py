import unittest

from selenium import webdriver
from typing_extensions import Self


class NewVisitorTest(unittest.TestCase):

    def setUp(self: Self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self: Self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self: Self):
        # Mani has heard about a cool new online to-do app.
        # He goes to checkout its homepage
        self.browser.get("http://localhost:8000")

        # He notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")

        # He is invited to enter a to-do item straight away
        # He types "Complete 'TDD - Obey the Testing GOAT' in 30 days."
        # into text box (Mani is determined to attain TDD GOAT status)

        # when he hits enter, the page updates, and now the page lists
        # 1. "Complete 'TDD - Obey the Testing GOAT' in 30 days." as an item in a to-do list

        # There is still a text box inviting him to add another item. He
        # enters  "Use the principles of TDD to build a RAG application" (Mani is hungry)

        # The page updates again, and now shows both items on his list

        # Mani wonders whether the site will remember his list. Then he sees
        # that the site has generated a unique URL for him -- there is some
        # exploratory text to that effect.

        # He visits that URL - her to-do list is still there.

        # Satisfied, He starts the real work.


if __name__ == "__main__":
    unittest.main(warnings="ignore")
