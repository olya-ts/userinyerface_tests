import os


class TestData(object):
    MIN_PSSWD_LENGTH = 10
    MAX_PSSWD_LENGTH = 20

    MIN_EMAIL_LENGTH = 3
    MAX_EMAIL_LENGTH = 10

    MIN_DOMAIN_LENGTH = 2
    MAX_DOMAIN_LENGTH = 5

    COMMON_LETTER = "u"

    ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..'))
    IMAGE_PATH = os.path.join(ROOT_DIR, 'tests', 'images', "cutie.jpg")

    TIMER_VALUE = "00:00:00"

    CHECKBOXES_LIST_TO_EXCLUDE = ["interest_selectall", "interest_unselectall"]
