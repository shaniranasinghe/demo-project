from app.calculator import calculate_total, apply_discount
from app.user_service import create_user


def run_demo():
    """Small demo function."""
    total = calculate_total(price=100, quantity=2)
    final_total = apply_discount(total, discount_percentage=10)

    user = create_user(
        user_id=1,
        name="Demo User",
        email="demo@example.com"
    )

    return {
        "user": user,
        "total": total,
        "final_total": final_total
    }


if __name__ == "__main__":
    print(run_demo())
