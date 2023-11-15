
from datetime import datetime
from time import sleep
from typing import Any, Dict
from illuminarean.common import TestTools
from illuminarean.goodvibe.elements import Elements

class FillTheForm(Elements):
    """Create Data source Class"""

    def access_website_to_good_vibe(self) -> None:
        """fill the form"""
        if self.does_element_exist(self.mainpath_close_modal):
            elem = self.find_element(self.mainpath_close_modal)
            elem.click()
        elem = self.find_element(self.mainpath_gnb_work)
        elem.click()

        elem = self.find_element(self.mainpath_goodvibe_btn)
        elem.click()

        sleep(3)
        # assert check_comment in check_element.text

    def fill_the_form(self) -> None:
        """fill the form"""
        # 창 전환후 elem 을 가져와야 됨
        # https://stackoverflow.com/questions/10629815/how-to-switch-to-new-window-in-selenium-for-python

        # 새창으로 띄워졌을 경우 마지막 창으로 이동한다.
        new_window_count = len(self.driver.window_handles)
        if new_window_count > 2:
            last_window = self.driver.window_handles[new_window_count - 1]
            self.driver.switch_to.window(last_window)
        elem = self.find_element(self.gvpath_gnb_trial_btn)
        elem.click()

        elem = self.find_element(self.gvpath_form_ceo_name)
        elem.send_keys("회사회사")
        sleep(10)