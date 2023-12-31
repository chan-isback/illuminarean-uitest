# pylint: disable=W0107, R0903, W0106

from time import sleep
import ast
from typing import Any, List
import pandas as pd
from illuminarean.goodvibe.elements import Elements

# pytest 로 실행할 예정이므로 tests 상위 폴더 기준으로 csv 파일을 불러온다.
df = pd.read_csv("../illuminarean/goodvibe/sample.csv")


class CustomException(Exception):
    """Custom Exception Declare"""

    pass


class SelectBox:
    """Bind essential selectbox values"""

    def __init__(
        self,
        item_located: List[Any],
        preset: List[Any],
        substitution: str,
        items: List[Any],
    ) -> None:
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

    def send_key_to_elem(self, target_path: Any, words: str) -> None:
        """send_keys with elements"""
        elem = self.find_element_with_wait(target_path)
        elem.send_keys(words)

    def choose_select_box(self, selected_item: str, value_type: str) -> None:
        """choose selectbox menu"""
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

    def duty_search_a(self, elem_duty_root: Any) -> None:
        """Requirement 1: Select a duty from list"""
        elem_duty_options = elem_duty_root.find_elements(
            *self.gvpath_form_duties_root_options
        )
        # 추후 다중 선택이 가능할 수도 있으므로 리스트 형태로 가져오는 형태로 구현
        # Pandas 에서 불러오기 시 list 가 아닌 str 로 불러오므로, list 로 변환하여 가져온다.
        duty_select_options = ast.literal_eval(df["duty"][0])
        duty_select_options_elem = []  # duty_select_options 의 element 값을 담을 리스트 변수
        duty_options = []  # 전체 옵션을 담을 리스트 변수
        for elem_duty_option in elem_duty_options:
            duty_option_name = elem_duty_option.text
            duty_options.append(duty_option_name)
            for duty_select_option in duty_select_options:
                if duty_option_name == duty_select_option:
                    duty_select_options_elem.append(elem_duty_option)

        # 선택한 옵션이 없을 경우 assert False 판단함
        for duty_select_option in duty_select_options:
            assert duty_select_option in duty_options

        # 옵션 선택
        for duty_select_option_elem in duty_select_options_elem:
            duty_select_option_elem.click()

    def duty_search_b(self, elem_duty_root: Any, duty_select_option_b: str) -> None:
        """Requirement 2: Select a duty with the search form"""
        elem_duty_search = self.find_element_with_wait(self.gvpath_form_duties_search)
        elem_duty_search.send_keys(duty_select_option_b)
        # 검색한 뒤 UI 에 반영되는데 약간의 시간이 소요되어서 Sleep 삽입
        sleep(1)
        # element 정보를 다시 가져옴 (StaleElementReferenceException 방지)
        elem_duty_options = elem_duty_root.find_elements(
            *self.gvpath_form_duties_root_options
        )
        for elem_duty_option in elem_duty_options:
            display_property = elem_duty_option.value_of_css_property("display")
            if display_property == "inline-block":
                elem_duty_option.click()
        # element 정보를 다시 가져옴 (StaleElementReferenceException 방지)
        elem_duty_submit = elem_duty_root.find_element(
            *self.gvpath_form_duties_root_submit
        )
        elem_duty_submit.click()

    def duty_search(self, duty_select_option_b: str) -> None:
        """search duties from the form"""
        elem_duty_root = self.find_element_with_wait(self.gvpath_form_duties_root)
        elem_duty_input = elem_duty_root.find_element(
            *self.gvpath_form_duties_root_input
        )
        elem_duty_input.click()

        self.duty_search_a(elem_duty_root)

        elem_duty_submit = elem_duty_root.find_element(
            *self.gvpath_form_duties_root_submit
        )
        elem_duty_submit.click()

        elem_duty_input = elem_duty_root.find_element(
            *self.gvpath_form_duties_root_input
        )
        elem_duty_input.click()

        self.duty_search_b(elem_duty_root, duty_select_option_b)

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

        self.send_key_to_elem(self.gvpath_form_company_name, df["company_name"][0])
        self.send_key_to_elem(self.gvpath_form_ceo_name, df["ceo_name"][0])
        self.send_key_to_elem(self.gvpath_form_name, df["name"][0])
        self.send_key_to_elem(self.gvpath_form_email, df["email"][0])
        # Mobile 의 경우 문자로 받아와야 되므로 csv 에는 문자 형태로 따옴표''로 묶어서 저장하였음
        self.send_key_to_elem(self.gvpath_form_mobile, df["mobile"][0])

        # business, scale
        self.choose_select_box(selected_item=df["business"][0], value_type="business")
        self.choose_select_box(selected_item=df["scale"][0], value_type="scale")

        self.duty_search(duty_select_option_b="스타일리스트")

        # 이용 약관 및 개인정보 활용 동의 체크
        elem_check_term = self.find_element_with_wait(self.gvpath_form_checkbox_term)
        elem_check_term.click()
        elem_check_privacy = self.find_element_with_wait(
            self.gvpath_form_checkbox_privacy
        )
        elem_check_privacy.click()
        sleep(5)

        elem_close = self.find_element_with_wait(self.gvpath_form_close)
        elem_close.click()
        sleep(3)
        elem_close_confirm = self.find_element_with_wait(self.gvpath_form_close_confirm)
        elem_close_confirm.click()
        sleep(5)
