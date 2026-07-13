def create_user(user_id, name, email):
    """Create a user dictionary."""
    if not user_id:
        raise ValueError("User ID is required")

    if not name:
        raise ValueError("Name is required")

    if "@" not in email:
        raise ValueError("Invalid email address")

    return {
        "id": user_id,
        "name": name,
        "email": email,
        "active": True
    }


def deactivate_user(user):
    """Deactivate a user."""
    if "active" not in user:
        raise KeyError("User does not contain active status")

    user["active"] = False
    return user


def get_user_display_name(user):
    """Return formatted user display name."""
    return f"{user['name']} <{user['email']}>"
