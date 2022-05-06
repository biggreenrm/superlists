from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    """Test of new visitor."""

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
    
    def tearDown(self) -> None:
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        """User can start new list and retrive later again."""
        # Amber heard about new cool app with to-do lists
        # and she decided to check its main page
        self.browser.get('http://localhost:8000')

        # She see that title tells her it is To-Do list
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish test")

        # She is immediately prompted to enter a list item


        # She types in the text box "Buy peacock feathers"
        # (her hobby is knitting fishing flies)


        # When she presses enter, the page refreshes and now
        # the page contains "1: Buy Peacock Feathers" as a list item

        # the text field still invites her to add another element.
        # She introduces "Make a fly out of peacock feathers"
        # (Amber is very methodical)


        # The page is updated again, and now shows both elements of its list


        # Edith wonders if the site will remember her list. Next, she
        # sees that the site has generated a unique URL for her – about this
        # a small text with explanations is displayed.


        # She visits this URL - her list is still there.


        # Satisfied, she goes back to bed

if __name__ == "__main__":
    unittest.main(warnings="ignore")