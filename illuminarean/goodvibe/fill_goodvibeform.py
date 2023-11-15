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
            elem = self.find_element_with_wait(self.mainpath_close_modal)
            elem.click()
        elem = self.find_element_with_wait(self.mainpath_gnb_work)
        elem.click()

        elem = self.find_element_with_wait(self.mainpath_goodvibe_btn)
        elem.click()
        # 창이 열린뒤 페이지가 Load 될 때 까지 대기
        self.driver.implicitly_wait(10)
        # assert check_comment in check_element.text

    def fill_the_form(self) -> None:
        """fill the form"""
        # 창 전환후 elem 을 가져와야 됨
        # https://stackoverflow.com/questions/10629815/how-to-switch-to-new-window-in-selenium-for-python

        new_window_count = len(self.driver.window_handles)
        # 새창으로 띄워졌을 경우 2개 이상의 창이 존재함
        if new_window_count >= 2:
            # 마지막 창으로 이동한다.
            last_window = self.driver.window_handles[new_window_count - 1]
            self.driver.switch_to.window(last_window)
        elem = self.find_element_with_wait(self.gvpath_gnb_trial_btn)
        elem.click()

        elem_company_name = self.find_element_with_wait(self.gvpath_form_company_name)
        elem_company_name.send_keys("주식회사 일이삼")
        elem_ceo = self.find_element_with_wait(self.gvpath_form_ceo_name)
        elem_ceo.send_keys("김사장")
        elem_name = self.find_element_with_wait(self.gvpath_form_name)
        elem_name.send_keys("이사원")
        elem_email = self.find_element_with_wait(self.gvpath_form_email)
        elem_email.send_keys("123@company.com")
        elem_mobile = self.find_element_with_wait(self.gvpath_form_mobile)
        elem_mobile.send_keys("01011112222")
        elem_check_term = self.find_element_with_wait(self.gvpath_form_checkbox_term)
        elem_check_term.click()
        elem_check_privacy = self.find_element_with_wait(
            self.gvpath_form_checkbox_privacy
        )
        elem_check_privacy.click()

        business_type = "개인"
        elem_business_type = self.find_element_with_wait(self.gvpath_form_business_type)
        elem_business_type.click()
        # 클릭한 이후에 개인, 법인 옵션을 찾는다.
        elem_business_type_co = elem_business_type.find_element(
            *self.gvpath_form_business_type_co
        )
        elem_business_type_ind = elem_business_type.find_element(
            *self.gvpath_form_business_type_ind
        )
        if business_type == "개인":
            elem_business_type_ind.click()
            print("개인클릭")
        else:
            elem_business_type_co.click()
            print("법인클릭")
        # 두번 클릭 하여 선택을 완료함
        [elem_business_type.click() for i in range(2)]

        scale_number = "6-20"
        # scale_number 가 유효한 숫자인지 확인한다.
        assert scale_number in self.scale_preset
        elem_scale = self.find_element_with_wait(self.gvpath_form_scale)
        elem_scale.click()
        gvpath_form_scale_item = self.gvpath_form_scale_items_pre.copy()
        gvpath_form_scale_item[1] = gvpath_form_scale_item[1].replace(
            "!scale_preset!", scale_number
        )
        print("gvpath_form_scale_item", gvpath_form_scale_item)
        elem_scale_item = self.find_element_with_wait(gvpath_form_scale_item)
        elem_scale_item.click()
        [elem_scale.click() for i in range(2)]

        sleep(30)
