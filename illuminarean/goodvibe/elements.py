from selenium.webdriver.common.by import By

from typing import Any
from illuminarean.common import TestTools


class Elements(TestTools):
    """Elements for find_elements"""

    def __init__(self, driver: Any) -> None:
        """init params"""

        super().__init__(driver)

        # main site
        self.mainpath_close_modal = [
            By.CSS_SELECTOR,
            '[aria-label="company:close_modal"',
        ]
        self.mainpath_gnb_work = [By.CSS_SELECTOR, '[aria-label="a11y:Work"']
        self.mainpath_goodvibe_btn = [
            By.XPATH,
            '//a[contains(text(),"GOODVIBE WORKS")]',
        ]

        # GOODVIBE site
        self.gvpath_gnb_trial_btn = [By.XPATH, '//button[text()="무료 체험 신청"]']
        self.gvpath_form_company_name = [By.XPATH, '//input[@name="companyName"]']
        self.gvpath_form_ceo_name = [By.XPATH, '//input[@name="ceoName"]']
        self.gvpath_form_name = [By.XPATH, '//input[@name="name"]']
        self.gvpath_form_email = [By.XPATH, '//input[@name="email"]']
        self.gvpath_form_mobile = [By.XPATH, '//input[@name="mobile"]']

        self.gvpath_form_business_type = [By.ID, "businessType"]
        self.business_type_preset = ["법인", "개인"]
        self.business_type_preset_substitution = "!business_type_preset!"
        self.gvpath_form_business_type_items_pre = [
            By.XPATH,
            '//div[text()="{0}"]'.format(self.business_type_preset_substitution),
        ]

        self.gvpath_form_scale = [By.ID, "scale"]
        self.scale_preset = ["1-5", "6-20", "21-50", "51-100", "101-200", "201-500"]
        self.scale_preset_substitution = "!scale_preset!"
        self.gvpath_form_scale_items_pre = [
            By.XPATH,
            '//div[contains(text(), "{0}")]'.format(self.scale_preset_substitution),
        ]

        self.gvpath_form_duties_root = [By.CLASS_NAME, "duties"]
        self.gvpath_form_duties_root_input = [By.XPATH, "//dd/div/div/button"]
        self.gvpath_form_duties_root_options = [
            By.XPATH,
            "//dd/div/div/div/div[1]/button",
        ]
        self.gvpath_form_duties_root_submit = [
            By.XPATH,
            '//button[text()="등록"]',
        ]

        self.gvpath_Form_duties_search = [
            By.XPATH,
            "//input[contains(@placeholder, '업무명 검색')]",
        ]

        self.gvpath_form_checkbox_term = [By.ID, "agreeTermsOfUse"]
        self.gvpath_form_checkbox_privacy = [By.ID, "agreePrivacyStatement"]

        self.gvpath_form_close = [By.XPATH, "//span[text()='신청 취소']"]
        self.gvpath_form_close_confirm = [By.XPATH, "//button[text()='확인']"]
