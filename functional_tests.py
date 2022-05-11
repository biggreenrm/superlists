from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text: str = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is immediately prompted to enter a list item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types in the text box "Buy peacock feathers"
        # (her hobby is knitting fishing flies)
        inputbox.send_keys('Buy peacock feathers')

        # When she presses enter, the page refreshes and now
        # the page contains "1: Buy Peacock Feathers" as a list item
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # The text field still invites her to add another element.
        # She introduces "Make a fly out of peacock feathers"
        # (Amber is very methodical)
        self.fail('End test!')


        # The page is updated again, and now shows both elements of its list


        # Edith wonders if the site will remember her list. Next, she
        # sees that the site has generated a unique URL for her – about this
        # a small text with explanations is displayed.


        # She visits this URL - her list is still there.


        # Satisfied, she goes back to bed

if __name__ == "__main__":
    unittest.main(warnings="ignore")