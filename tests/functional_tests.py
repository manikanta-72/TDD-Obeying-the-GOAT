import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        # He is invited to enter a to-do item straight away
        input_box = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(input_box.get_attribute("placeholder"), "Enter a to-do item")

        # He types "Complete 'TDD - Obey the Testing GOAT' in 30 days."
        # into text box (Mani is determined to attain TDD GOAT status)
        test_entry = "Complete 'TDD - Obey the Testing GOAT' in 30 days."
        input_box.send_keys(test_entry)

        # when he hits enter, the page updates, and now the page lists
        # "1: Complete 'TDD - Obey the Testing GOAT' in 30 days." as an item in a to-do list
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(
            "1: Complete 'TDD - Obey the Testing GOAT' in 30 days.",
            [row.text for row in rows],
        )

        # There is still a text box inviting him to add another item. He
        # enters  "Use the principles of TDD to build a RAG application" (Mani is hungry)
        input_box = self.browser.find_element(By.ID, "id_new_item")
        input_box.send_keys("Use the principles of TDD to build a RAG application.")
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on his list

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(
            "1: Complete 'TDD - Obey the Testing GOAT' in 30 days.",
            [row.text for row in rows],
        )
        self.assertIn(
            "2: Use the principles of TDD to build a RAG application.",
            [row.text for row in rows],
        )

        self.fail("Finish the test!")

        # Mani wonders whether the site will remember his list. Then he sees
        # that the site has generated a unique URL for him -- there is some
        # exploratory text to that effect.

        # He visits that URL - her to-do list is still there.

        # Satisfied, He starts the real work.


if __name__ == "__main__":
    unittest.main(warnings="ignore")
