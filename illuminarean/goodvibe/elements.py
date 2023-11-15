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
        self.gvpath_form_business_type_co = [By.XPATH, '//div[text()="법인"]']
        self.gvpath_form_business_type_ind = [By.XPATH, '//div[text()="개인"]']

        self.gvpath_form_checkbox_term = [By.ID, "agreeTermsOfUse"]
        self.gvpath_form_checkbox_privacy = [By.ID, "agreePrivacyStatement"]

        # 사업자 유형
        # //*[@id="businessType"]/div/div[1]
        # 직원수
        # //*[@id="scale"]/div/div[1]
        # 담당업무
        # /html/body/div[5]/div/div/div/div/div/div/div/div[2]/dl[8]/dd/div/div[2]/button/p/div
        # /html/body/div[5]/div/div/div/div/div/div/div/div[2]/div/div[1]/label

        # GOODVIBE WORKS 바로가기
        # //*[@id="__next"]/div/main/div/div[2]/div/div[3]/div/a
