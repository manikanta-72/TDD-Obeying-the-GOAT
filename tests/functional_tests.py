from selenium import webdriver

browser = webdriver.Firefox()

# Mani has heard about a cool new online to-do app.
# He goes to checkout its homepage
browser.get('http://localhost:8000')

# He notices the page title and header mention to-do lists
assert 'To-Do' in browser.title

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

browser.quit()
