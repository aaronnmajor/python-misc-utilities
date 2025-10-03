#!/usr/bin/env python3
"""
Example script demonstrating string manipulation utilities.

This script shows how to use the string_helpers module for:
- Case conversions
- String validation
- Text processing
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.string_helpers import (
    to_snake_case,
    to_camel_case,
    to_pascal_case,
    is_valid_email,
    count_words,
    truncate_string,
)


def main():
    """Demonstrate string operations."""
    print("String Operations Example")
    print("=" * 50)

    # Example 1: Case conversions
    test_string = "HelloWorldExample"
    print(f"\nOriginal: {test_string}")
    print(f"Snake case: {to_snake_case(test_string)}")
    print(f"Camel case: {to_camel_case('hello_world_example')}")
    print(f"Pascal case: {to_pascal_case('hello_world_example')}")

    # Example 2: Email validation
    emails = ["test@example.com", "invalid-email", "user@domain.co.uk"]
    print("\nEmail validation:")
    for email in emails:
        valid = is_valid_email(email)
        print(f"  {email}: {'✓ Valid' if valid else '✗ Invalid'}")

    # Example 3: Text processing
    long_text = "This is a very long text that needs to be truncated for display"
    print(f"\nOriginal text: {long_text}")
    print(f"Truncated: {truncate_string(long_text, 30)}")
    print(f"Word count: {count_words(long_text)}")


if __name__ == "__main__":
    main()
