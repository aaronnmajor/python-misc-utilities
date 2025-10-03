"""
String manipulation utilities for common text processing tasks.
"""

import re
from typing import List


def to_snake_case(text: str) -> str:
    """
    Convert a string to snake_case.

    Args:
        text: Input string

    Returns:
        String in snake_case format
    """
    # Insert underscore before uppercase letters
    text = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", text)
    text = re.sub("([a-z0-9])([A-Z])", r"\1_\2", text)
    return text.lower()


def to_camel_case(text: str) -> str:
    """
    Convert a string to camelCase.

    Args:
        text: Input string

    Returns:
        String in camelCase format
    """
    words = re.split(r"[_\s-]+", text)
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])


def to_pascal_case(text: str) -> str:
    """
    Convert a string to PascalCase.

    Args:
        text: Input string

    Returns:
        String in PascalCase format
    """
    words = re.split(r"[_\s-]+", text)
    return "".join(word.capitalize() for word in words)


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate a string to a maximum length with an optional suffix.

    Args:
        text: Input string
        max_length: Maximum length of output string
        suffix: Suffix to append if truncated

    Returns:
        Truncated string
    """
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def remove_extra_whitespace(text: str) -> str:
    """
    Remove extra whitespace from a string, replacing multiple spaces with single space.

    Args:
        text: Input string

    Returns:
        String with normalized whitespace
    """
    return " ".join(text.split())


def extract_numbers(text: str) -> List[int]:
    """
    Extract all numbers from a string.

    Args:
        text: Input string

    Returns:
        List of integers found in the string
    """
    return [int(num) for num in re.findall(r"\d+", text)]


def count_words(text: str) -> int:
    """
    Count the number of words in a string.

    Args:
        text: Input string

    Returns:
        Number of words
    """
    return len(text.split())


def is_valid_email(email: str) -> bool:
    """
    Check if a string is a valid email address.

    Args:
        email: Email string to validate

    Returns:
        True if valid email format, False otherwise
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def reverse_words(text: str) -> str:
    """
    Reverse the order of words in a string.

    Args:
        text: Input string

    Returns:
        String with words in reversed order
    """
    return " ".join(text.split()[::-1])


def remove_punctuation(text: str) -> str:
    """
    Remove all punctuation from a string.

    Args:
        text: Input string

    Returns:
        String without punctuation
    """
    return re.sub(r"[^\w\s]", "", text)
