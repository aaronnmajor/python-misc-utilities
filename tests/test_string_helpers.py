"""Tests for string_helpers module."""

from utils.string_helpers import (
    to_snake_case,
    to_camel_case,
    to_pascal_case,
    truncate_string,
    remove_extra_whitespace,
    extract_numbers,
    count_words,
    is_valid_email,
    reverse_words,
    remove_punctuation,
)


def test_to_snake_case():
    """Test snake_case conversion."""
    assert to_snake_case("HelloWorld") == "hello_world"
    assert to_snake_case("helloWorld") == "hello_world"
    assert to_snake_case("hello_world") == "hello_world"
    assert to_snake_case("HTTPSConnection") == "https_connection"


def test_to_camel_case():
    """Test camelCase conversion."""
    assert to_camel_case("hello_world") == "helloWorld"
    assert to_camel_case("hello-world") == "helloWorld"
    assert to_camel_case("hello world") == "helloWorld"


def test_to_pascal_case():
    """Test PascalCase conversion."""
    assert to_pascal_case("hello_world") == "HelloWorld"
    assert to_pascal_case("hello-world") == "HelloWorld"
    assert to_pascal_case("hello world") == "HelloWorld"


def test_truncate_string():
    """Test string truncation."""
    assert truncate_string("Hello World", 20) == "Hello World"
    assert truncate_string("Hello World", 8) == "Hello..."
    assert truncate_string("Hello World", 8, "..") == "Hello .."


def test_remove_extra_whitespace():
    """Test whitespace normalization."""
    assert remove_extra_whitespace("Hello   World") == "Hello World"
    assert remove_extra_whitespace("  Hello  World  ") == "Hello World"


def test_extract_numbers():
    """Test number extraction."""
    assert extract_numbers("abc123def456") == [123, 456]
    assert extract_numbers("no numbers here") == []
    assert extract_numbers("2024-01-15") == [2024, 1, 15]


def test_count_words():
    """Test word counting."""
    assert count_words("Hello World") == 2
    assert count_words("") == 0
    assert count_words("One") == 1


def test_is_valid_email():
    """Test email validation."""
    assert is_valid_email("test@example.com") is True
    assert is_valid_email("invalid-email") is False
    assert is_valid_email("user@domain.co.uk") is True
    assert is_valid_email("@example.com") is False


def test_reverse_words():
    """Test word reversal."""
    assert reverse_words("Hello World") == "World Hello"
    assert reverse_words("One Two Three") == "Three Two One"


def test_remove_punctuation():
    """Test punctuation removal."""
    assert remove_punctuation("Hello, World!") == "Hello World"
    assert remove_punctuation("Test: 123...") == "Test 123"
