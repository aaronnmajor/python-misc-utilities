"""Tests for date_time_utils module."""

from datetime import datetime, timedelta
from utils.date_time_utils import (
    format_datetime,
    parse_datetime,
    get_date_n_days_ago,
    get_date_n_days_ahead,
    days_between_dates,
    is_weekend,
    get_day_name,
    get_month_name,
    get_quarter,
)


def test_format_datetime():
    """Test datetime formatting."""
    dt = datetime(2024, 1, 15, 10, 30, 45)
    assert format_datetime(dt) == "2024-01-15 10:30:45"
    assert format_datetime(dt, "%Y-%m-%d") == "2024-01-15"


def test_parse_datetime():
    """Test datetime parsing."""
    dt = parse_datetime("2024-01-15 10:30:45")
    assert dt.year == 2024
    assert dt.month == 1
    assert dt.day == 15


def test_get_date_n_days_ago():
    """Test getting date n days ago."""
    result = get_date_n_days_ago(7)
    expected = datetime.now() - timedelta(days=7)
    assert abs((result - expected).total_seconds()) < 1


def test_get_date_n_days_ahead():
    """Test getting date n days ahead."""
    result = get_date_n_days_ahead(7)
    expected = datetime.now() + timedelta(days=7)
    assert abs((result - expected).total_seconds()) < 1


def test_days_between_dates():
    """Test calculating days between dates."""
    dt1 = datetime(2024, 1, 1)
    dt2 = datetime(2024, 1, 8)
    assert days_between_dates(dt1, dt2) == 7
    assert days_between_dates(dt2, dt1) == 7  # Test absolute value


def test_is_weekend():
    """Test weekend detection."""
    # Saturday
    saturday = datetime(2024, 1, 6)  # Known Saturday
    assert is_weekend(saturday) is True

    # Monday
    monday = datetime(2024, 1, 1)  # Known Monday
    assert is_weekend(monday) is False


def test_get_day_name():
    """Test getting day name."""
    monday = datetime(2024, 1, 1)  # Known Monday
    assert get_day_name(monday) == "Monday"


def test_get_month_name():
    """Test getting month name."""
    january = datetime(2024, 1, 15)
    assert get_month_name(january) == "January"


def test_get_quarter():
    """Test getting quarter."""
    assert get_quarter(datetime(2024, 1, 1)) == 1
    assert get_quarter(datetime(2024, 4, 1)) == 2
    assert get_quarter(datetime(2024, 7, 1)) == 3
    assert get_quarter(datetime(2024, 10, 1)) == 4
