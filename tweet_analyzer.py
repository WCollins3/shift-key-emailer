SHIFT_CODE_LENGTH = 29
SHIFT_CODE_SECTIONS = 5
FIRST_DASH_INDEX = 5
LAST_DASH_INDEX = 23
CHARACTERS_BETWEEN_DASHES = 6
SECTION_DIVIDER = "-"

def get_shift_codes(text: str) -> list:
    """Return a list of strings representing Shift codes from the text parameter.
    
    Keyword arguments:
    text -- text that may or may not include Shift codes.
    """

    codes = []
    text_clean = text.replace("\n", " ")
    words = text_clean.split(" ")
    for word in words:
        if is_shift_code(word):
            codes.append(word)
    return codes

def is_shift_code(text: str) -> bool:
    """Returns a boolean representing whether or not the text parameter looks like a Shift code.
    Qualifications for a proper Shift code:
    * Contains 29 characters
    * Every 6th character is '-'
    * Does not contain spaces 
    
    Keyword arguments:
    text -- text that may or may not be a Shift code.
    """

    if len(text) == SHIFT_CODE_LENGTH and " " not in text:
        sections = text.split(SECTION_DIVIDER)
        if len(sections) == SHIFT_CODE_SECTIONS:
            for i in range(FIRST_DASH_INDEX, LAST_DASH_INDEX, CHARACTERS_BETWEEN_DASHES):
                if text[i] != SECTION_DIVIDER:
                    return False
            return True
    return False
