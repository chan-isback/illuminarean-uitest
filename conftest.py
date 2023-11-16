import os
from time import sleep
from typing import Any

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver(base_url: str) -> Any:
    """Install Chrome driver and open test url"""

    chrome_options = Options()
    chrome_options.add_experimental_option(
        "prefs", {"download.default_directory": os.getcwd()}
    )

    # Executable_path has been deprecated 로 service를 통해 driver 를 호출함
    service = Service(ChromeDriverManager().install())

    print(service.path)
    try:
        # Executable_path has been deprecated 로 service를 통해 driver 를 호출함
        web_driver = webdriver.Chrome(service=service)
        web_driver.set_window_size(1500, 800)
        web_driver.get(base_url)

        sleep(5)
        yield web_driver
        web_driver.quit()
    except ConnectionResetError as error_msg:
        print("Failed to start webdriver: ", error_msg)
