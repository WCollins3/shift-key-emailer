SHIFT_CODE_LENGTH = 29
SHIFT_CODE_SECTIONS = 5
FIRST_DASH_INDEX = 5
LAST_DASH_INDEX = 23
CHARACTERS_BETWEEN_DASHES = 6
SECTION_DIVIDER = "-"

def get_shift_codes(text: str) -> list:
    """
    Gets possible Shift codes from a string.
    :param text: String that may or may not include Shift codes.
    :return: List of strings representing Shift codes from the text parameter.
    """
    codes = []
    text_clean = text.replace("\n", " ")
    words = text_clean.split(" ")
    for word in words:
        if is_shift_code(word):
            codes.append(word)
    return codes

def is_shift_code(text: str) -> bool:
    """
    Determines if a string looks like it could be a Shift code.
    Qualifications for a proper Shift code:
    * Contains 29 characters
    * Every 6th character is '-'
    * Does not contain spaces
    :param text: String that may or may not be a Shift code.
    :return: Boolean value representing whether or not the text parameter looks like a Shift code.
    """
    if len(text) == SHIFT_CODE_LENGTH and " " not in text:
        sections = text.split(SECTION_DIVIDER)
        if len(sections) == SHIFT_CODE_SECTIONS:
            for i in range(FIRST_DASH_INDEX, LAST_DASH_INDEX, CHARACTERS_BETWEEN_DASHES):
                if text[i] != SECTION_DIVIDER:
                    return False
            return True
    return False
