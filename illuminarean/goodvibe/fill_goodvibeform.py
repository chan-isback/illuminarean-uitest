from datetime import datetime
from time import sleep
from typing import Any, Dict
from illuminarean.common import TestTools
from illuminarean.goodvibe.elements import Elements


class CustomException(Exception):
    """Custom Exception Declare"""

    pass


class SelectBox:
    def __init__(self, item_located, preset, substitution, items):
        self.item_located = item_located
        self.preset = preset
        self.substitution = substitution
        self.items = items


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

    def choose_select_box(self, selected_item: str, value_type: str) -> None:
        if value_type == "business":
            sb = SelectBox(
                item_located=self.gvpath_form_business_type,
                preset=self.business_type_preset,
                substitution=self.business_type_preset_substitution,
                items=self.gvpath_form_business_type_items_pre,
            )

        elif value_type == "scale":
            sb = SelectBox(
                item_located=self.gvpath_form_scale,
                preset=self.scale_preset,
                substitution=self.scale_preset_substitution,
                items=self.gvpath_form_scale_items_pre,
            )
        else:
            raise CustomException("value_type is invalid")

        # selected_item 가 유효한 옵션인지 확인한다.
        assert selected_item in sb.preset

        elem_item = self.find_element_with_wait(sb.item_located)
        elem_item.click()
        item_located = sb.items.copy()
        item_located[1] = item_located[1].replace(sb.substitution, selected_item)
        elem_item_selected = self.find_element_with_wait(item_located)
        elem_item_selected.click()
        [elem_item.click() for i in range(2)]

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

        # business, scale
        self.choose_select_box(selected_item="개인", value_type="business")
        self.choose_select_box(selected_item="6-20", value_type="scale")

        elem_duty_root = self.find_element_with_wait(self.gvpath_form_duties_root)
        elem_duty_input = elem_duty_root.find_element(
            *self.gvpath_form_duties_root_input
        )
        elem_duty_input.click()

        elem_duty_options = elem_duty_root.find_elements(
            *self.gvpath_form_duties_root_options
        )
        duty_select_options = ["공연기획", "음반제작"]
        duty_select_options_elem = []
        duty_options = []
        for elem_duty_option in elem_duty_options:
            duty_option_name = elem_duty_option.text
            duty_options.append(duty_option_name)
            for duty_select_option in duty_select_options:
                if duty_option_name == duty_select_option:
                    duty_select_options_elem.append(elem_duty_option)

        # 선택한 옵션이 없을 경우 assert False 판단함
        for duty_select_option in duty_select_options:
            assert duty_select_option in duty_options

        # 옵션 일괄 선택
        for duty_select_option_elem in duty_select_options_elem:
            duty_select_option_elem.click()

        elem_duty_submit = elem_duty_root.find_element(
            *self.gvpath_form_duties_root_submit
        )
        elem_duty_submit.click()
        sleep(5)

        elem_close = self.find_element_with_wait(self.gvpath_form_close)
        elem_close.click()
        sleep(5)
        elem_close_confirm = self.find_element_with_wait(self.gvpath_form_close_confirm)
        elem_close_confirm.click()
        sleep(5)
