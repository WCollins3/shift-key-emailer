SHIFT_CODE_LENGTH = 29
SHIFT_CODE_SECTIONS = 5
FIRST_DASH_INDEX = 5
LAST_DASH_INDEX = 23
CHARACTERS_BETWEEN_DASHES = 6
SECTION_DIVIDER = "-"
EMPTY_STRING = ""
TIMEZONES_LIST = list()
TIMEZONES_FILE = "data/timezones.txt"
TIME_REFERENCING_WORDS = ["days", "hours", "minutes", "seconds"]

def get_shift_codes(text: str) -> list:
    """
    Gets possible Shift codes from a string.
    :param text: String that may or may not include Shift codes.
    :return: List of strings representing Shift codes from the text parameter.
    """
    codes = []
    words = get_words_from_text(text)
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

def get_expiration(text: str) -> str:
    """
    Gets the first possible expiration time of a Shift code.
    :param text: String that may or may not contain an expiration time
    :return: Possible expiration time. Returns an empty string if no expiration time is found.
    """
    words = get_words_from_text(text)
    for i in range(1, len(words)):
        word = words[i]
        if is_timezone_abbreviation(word) or is_time_referencing_word(word):
            time_string = words[i-1]
            return time_string + " " + word
    return EMPTY_STRING

def is_time_referencing_word(text: str) -> bool:
    """
    Determines if a string is a time-referencing word. Not case-sensitive.
    Time referencing words are: days, hours, minutes, seconds.
    :param text: String that may or may not be a time-referencing word.
    :return: Boolean value representing whether or not the text parameter is a time-referencing word.
    """
    if text.lower() in TIME_REFERENCING_WORDS:
        return True
    return False

def is_timezone_abbreviation(text: str) -> bool:
    """
    Determines if a string is a timezone abbreviation. Not case-sensitive.
    :param text: String that may or may not be a timezone abbreviation.
    :return: Boolean value representing whether or not the text parameter is a timezone abbreviation.
    """
    if TIMEZONES_LIST is None or len(TIMEZONES_LIST) == 0:
        populate_timezones_list()
    if text.upper() in TIMEZONES_LIST:
        return True
    else:
        return False

def populate_timezones_list():
    """
    Populates TIMEZONES_LIST
    :return: void
    """
    with open(TIMEZONES_FILE) as f:
        text = f.read()
        timezones = text.split("\n")
        for timezone in timezones:
            TIMEZONES_LIST.append(timezone)

def get_words_from_text(text: str) -> list:
    """
    Cleans text and retrieves a list of words.
    :param text: Text string.
    :return: List of words from the text parameter.
    """
    if len(text) == 0:
        return list()
    text_clean = text.replace("\n", " ").replace("=", " ")
    words = text_clean.split(" ")
    return words
