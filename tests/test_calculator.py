import pytest

from app.calculator import (
    add_numbers,
    subtract_numbers,
    calculate_total,
    apply_discount,
)


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_subtract_numbers():
    assert subtract_numbers(10, 4) == 6


def test_calculate_total():
    assert calculate_total(100, 3) == 300


def test_calculate_total_rejects_negative_values():
    with pytest.raises(ValueError):
        calculate_total(-100, 3)


def test_apply_discount():
    assert apply_discount(200, 10) == 180


def test_apply_discount_rejects_invalid_discount():
    with pytest.raises(ValueError):
        apply_discount(200, 120)
