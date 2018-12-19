import pytest

from pangram import is_pangram

def test_sentence_empty():
    assert not is_pangram('')

def test_recognizes_a_perfect_lower_case_pangram():
    assert is_pangram('abcdefghijklmnopqrstuvwxyz')

def test_pangram_with_only_lower_case():
    assert is_pangram('the quick brown fox jumps over the lazy dog')

def test_missing_character_x():
    assert not is_pangram('a quick movement of the enemy will '
                    'jeopardize five gunboats')

def test_another_missing_character():
    assert not is_pangram('five boxing wizards jump quickly at it')

def test_pangram_with_underscores():
    assert  is_pangram('the_quick_brown_fox_jumps_over_the_lazy_dog')

def test_pangram_with_numbers():
    assert is_pangram('the 1 quick brown fox jumps over the 2 lazy dogs')

def test_missing_letters_replaced_by_numbers():
    assert not is_pangram('7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog')

def test_pangram_with_mixedcase_and_punctuation():
    assert is_pangram('"Five quacking Zephyrs jolt my wax bed."')

def test_upper_and_lower_case_versions_of_the_same_character():
    assert not is_pangram('the quick brown fox jumped over the lazy FX')
