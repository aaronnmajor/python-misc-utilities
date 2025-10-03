#!/usr/bin/env python3
"""
Basic usage examples for the utility functions.

This file demonstrates simple, common use cases for each utility module.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.string_helpers import to_snake_case, is_valid_email, truncate_string
from utils.date_time_utils import get_current_timestamp, is_weekend, get_quarter
from datetime import datetime


def string_examples():
    """Examples of string utility functions."""
    print("=" * 60)
    print("STRING UTILITIES EXAMPLES")
    print("=" * 60)

    # Case conversion
    print("\n1. Case Conversion:")
    print(f"   'MyVariableName' -> {to_snake_case('MyVariableName')}")

    # Email validation
    print("\n2. Email Validation:")
    test_emails = ["user@example.com", "invalid.email", "admin@company.org"]
    for email in test_emails:
        status = "✓" if is_valid_email(email) else "✗"
        print(f"   {status} {email}")

    # String truncation
    print("\n3. String Truncation:")
    long_text = "This is a very long piece of text that needs truncation"
    print(f"   Original: {long_text}")
    print(f"   Truncated: {truncate_string(long_text, 30)}")


def datetime_examples():
    """Examples of date/time utility functions."""
    print("\n" + "=" * 60)
    print("DATE/TIME UTILITIES EXAMPLES")
    print("=" * 60)

    # Current timestamp
    print("\n1. Current Timestamp:")
    print(f"   {get_current_timestamp()}")

    # Weekend check
    print("\n2. Weekend Check:")
    today = datetime.now()
    print(f"   Is today a weekend? {'Yes' if is_weekend(today) else 'No'}")

    # Quarter information
    print("\n3. Current Quarter:")
    print(f"   We are in Q{get_quarter(today)} of {today.year}")


def practical_example():
    """A practical example combining multiple utilities."""
    print("\n" + "=" * 60)
    print("PRACTICAL EXAMPLE: Processing User Data")
    print("=" * 60)

    # Simulated user data
    users = [
        {"name": "JohnDoe", "email": "john@example.com", "joined": "2024-01-15"},
        {"name": "JaneSmith", "email": "invalid-email", "joined": "2024-02-20"},
        {"name": "BobJohnson", "email": "bob@test.com", "joined": "2024-03-10"},
    ]

    print("\nProcessing user data:")
    for user in users:
        # Convert name to snake_case
        username = to_snake_case(user["name"])

        # Validate email
        email_valid = is_valid_email(user["email"])

        # Display results
        status = "✓" if email_valid else "✗"
        print(f"\n   User: {username}")
        print(f"   Email: {user['email']} {status}")
        print(f"   Joined: {user['joined']}")


def main():
    """Run all examples."""
    string_examples()
    datetime_examples()
    practical_example()

    print("\n" + "=" * 60)
    print("Examples complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
