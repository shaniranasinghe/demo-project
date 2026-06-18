import pytest

from app.user_service import create_user, deactivate_user, get_user_display_name


def test_create_user(sample_user):
    user = create_user(1, "Charith", "charith@example.com")

    assert user["id"] == 1
    assert user["name"] == "Charith"
    assert user["email"] == "charith@example.com"
    assert user["active"] is True


def test_create_user_rejects_missing_name():
    with pytest.raises(ValueError):
        create_user(1, "", "charith@example.com")


def test_create_user_rejects_invalid_email():
    with pytest.raises(ValueError):
        create_user(1, "Charith", "invalid-email")


def test_deactivate_user():
    user = create_user(1, "Charith", "charith@example.com")
    updated_user = deactivate_user(user)

    assert updated_user["active"] is False


def test_get_user_display_name():
    user = create_user(1, "Charith", "charith@example.com")

    assert get_user_display_name(user) == "Charith <charith@example.com>"
