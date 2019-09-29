import unittest
import tweet_analyzer

GOOD_SHIFT_CODE = "5SWTJ-BBW93-SWJ55-B3BJ3-5BH99"
GOOD_SHIFT_CODE_2 = "5SWTJ-BBW93-SWJ55-B3BJ3-5BH98"
BAD_SHIFT_CODE = "This is a bad shift code"
SHIFT_CODE_INCLUDES_SPACE = "5SWTJ-BBW93-SW 55-B3BJ3-5BH99"
SHIFT_CODE_MISSING_CHARACTER_AT_END = "5SWTJ-BBW93-SWJ55-B3BJ3-5BH9"
SHIFT_CODE_EXTRA_CHARACTER_AT_END = "5SWTJ-BBW93-SWJ55-B3BJ3-5BH999"
SHIFT_CODE_MISSING_CHARACTER_AT_BEGINNING = "SWTJ-BBW93-SWJ55-B3BJ3-5BH99"
SHIFT_CODE_EXTRA_CHARACTER_AT_BEGINNING = "55SWTJ-BBW93-SWJ55-B3BJ3-5BH99"
SHIFT_CODE_CORRECT_LENGTH_7_SECTIONS = "5SWTJ-BB-93-SWJ55-B3BJ3-5BH99"
SHIFT_CODE_CORRECT_LENGTH_5_SECTIONS = "5SWTJ-BBW93ASWJ55-B3BJ3-5BH99"
SHIFT_CODE_CORRECT_LENGTH_CORRECT_SECTION_COUNT_INCORRECT_SECTION_PLACEMENT = "5SWT-JBBW93S-WJ55-B3BJ3-5BH99"
GOOD_SHIFT_CODE_TWEET_FILE = "tests/data/text_with_good_shift_code.txt"
TWEET_FILE_WITHOUT_SHIFT_CODE = "tests/data/text_without_shift_code.txt"
BAD_SHIFT_CODE_TWEET_FILE = "tests/data/text_with_bad_shift_code.txt"
GOOD_2_SHIFT_CODES_TWEET_FILE = "tests/data/text_with_2_good_shift_codes.txt"
GOOD_2_SHIFT_CODES_IN_DIFFERENT_PLACES_TWEET_FILE = "tests/data/text_with_2_good_shift_codes_in_different_places.txt"
GOOD_1_SHIFT_CODE_2_BAD_SHIFT_CODES_TWEET_FILE = "tests/data/text_with_1_good_shift_code_2_bad_shift_codes.txt"
GOOD_2_SHIFT_CODE_2_BAD_SHIFT_CODES_TWEET_FILE = "tests/data/text_with_2_good_shift_codes_2_bad_shift_codes.txt"

class Test_is_shift_code_function(unittest.TestCase):

    def test_check_is_shift_code_returns_true_for_good_shift_code(self):
        actual = tweet_analyzer.is_shift_code(GOOD_SHIFT_CODE)
        self.assertTrue(actual)

    def test_check_is_shift_code_returns_false_for_bad_shift_code(self):
        actual = tweet_analyzer.is_shift_code(BAD_SHIFT_CODE)
        self.assertFalse(actual)

    def test_check_is_shift_code_returns_false_for_shift_code_that_includes_space(self):
        actual = tweet_analyzer.is_shift_code(SHIFT_CODE_INCLUDES_SPACE)
        self.assertFalse(actual)

    def test_check_is_shift_code_returns_false_for_missing_character_at_end(self):
        actual = tweet_analyzer.is_shift_code(SHIFT_CODE_MISSING_CHARACTER_AT_END)
        self.assertFalse(actual)

    def test_check_is_shift_code_returns_false_for_extra_character_at_end(self):
        actual = tweet_analyzer.is_shift_code(SHIFT_CODE_EXTRA_CHARACTER_AT_END)
        self.assertFalse(actual)

    def test_check_is_shift_code_returns_false_for_missing_character_at_beginning(self):
        actual = tweet_analyzer.is_shift_code(SHIFT_CODE_MISSING_CHARACTER_AT_BEGINNING)
        self.assertFalse(actual)

    def test_check_is_shift_code_returns_false_for_extra_character_at_beginning(self):
        actual = tweet_analyzer.is_shift_code(SHIFT_CODE_EXTRA_CHARACTER_AT_BEGINNING)
        self.assertFalse(actual)

    def test_check_is_shift_code_returns_false_for_correct_character_length_and_7_sections(self):
        actual = tweet_analyzer.is_shift_code(SHIFT_CODE_CORRECT_LENGTH_7_SECTIONS)
        self.assertFalse(actual)

    def test_check_is_shift_code_returns_false_for_correct_character_length_and_5_sections(self):
        actual = tweet_analyzer.is_shift_code(SHIFT_CODE_CORRECT_LENGTH_5_SECTIONS)
        self.assertFalse(actual)

    def test_check_is_shift_code_returns_false_for_correct_character_correct_section_count_incorrect_section_placement(self):
        actual = tweet_analyzer.is_shift_code(SHIFT_CODE_CORRECT_LENGTH_CORRECT_SECTION_COUNT_INCORRECT_SECTION_PLACEMENT)
        self.assertFalse(actual)

class Test_get_shift_codes_function(unittest.TestCase):

    def test_check_get_shift_codes_returns_shift_code_from_tweet(self):
        with open(GOOD_SHIFT_CODE_TWEET_FILE) as f:
            tweet = f.read()
        actual = tweet_analyzer.get_shift_codes(tweet)
        self.assertEqual(1, len(actual))
        self.assertEqual(GOOD_SHIFT_CODE, actual[0])

    def test_check_get_shift_codes_returns_empty_list_when_tweet_does_not_contain_shift_code(self):
        with open(TWEET_FILE_WITHOUT_SHIFT_CODE) as f:
            tweet = f.read()
        actual = tweet_analyzer.get_shift_codes(tweet)
        self.assertEqual(0, len(actual))

    def test_check_get_shift_codes_returns_empty_list_when_tweet_contains_bad_shift_code(self):
        with open(BAD_SHIFT_CODE_TWEET_FILE) as f:
            tweet = f.read()
        actual = tweet_analyzer.get_shift_codes(tweet)
        self.assertEqual(0, len(actual))

    def test_check_get_shift_codes_returns_2_shift_codes_from_tweet_with_2_shift_codes(self):
        with open(GOOD_2_SHIFT_CODES_TWEET_FILE) as f:
            tweet = f.read()
        actual = tweet_analyzer.get_shift_codes(tweet)
        self.assertEqual(2, len(actual))
        self.assertEqual(GOOD_SHIFT_CODE, actual[0])
        self.assertEqual(GOOD_SHIFT_CODE_2, actual[1])

    def test_check_get_shift_codes_returns_2_shift_codes_from_tweet_with_2_shift_codes_in_different_places(self):
        with open(GOOD_2_SHIFT_CODES_IN_DIFFERENT_PLACES_TWEET_FILE) as f:
            tweet = f.read()
        actual = tweet_analyzer.get_shift_codes(tweet)
        self.assertEqual(2, len(actual))
        self.assertEqual(GOOD_SHIFT_CODE, actual[0])
        self.assertEqual(GOOD_SHIFT_CODE_2, actual[1])

    def test_check_get_shift_codes_returns_only_good_shift_code_from_text_with_1_good_shift_code_and_2_bad_shift_codes(self):
        with open(GOOD_1_SHIFT_CODE_2_BAD_SHIFT_CODES_TWEET_FILE) as f:
            tweet = f.read()
        actual = tweet_analyzer.get_shift_codes(tweet)
        self.assertEqual(1, len(actual))
        self.assertEqual(GOOD_SHIFT_CODE, actual[0])

    def test_check_get_shift_codes_returns_only_good_shift_code_from_text_with_2_good_shift_code_and_2_bad_shift_codes(self):
        with open(GOOD_2_SHIFT_CODE_2_BAD_SHIFT_CODES_TWEET_FILE) as f:
            tweet = f.read()
        actual = tweet_analyzer.get_shift_codes(tweet)
        self.assertEqual(2, len(actual))
        self.assertEqual(GOOD_SHIFT_CODE, actual[0])
        self.assertEqual(GOOD_SHIFT_CODE_2, actual[1])
