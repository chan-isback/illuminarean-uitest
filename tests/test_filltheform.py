from typing import Any

import pytest

from illuminarean.goodvibe.fill_goodvibeform import FillTheForm

def test_fill_the_form(driver: Any) -> None:
    """"""
    ftf = FillTheForm(driver)
    ftf.access_website_to_good_vibe()
    ftf.fill_the_form()