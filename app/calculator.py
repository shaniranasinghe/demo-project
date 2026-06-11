def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract_numbers(a, b):
    """Return the difference between two numbers."""
    return a - b


def calculate_total(price, quantity):
    """Calculate total amount using price and quantity."""
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be positive")

    total_amount = price * quantity
    return total_amount


def apply_discount(total_amount, discount_percentage):
    """Apply discount to a total amount."""
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100")

    discount_amount = total_amount * (discount_percentage / 100)
    return total_amount - discount_amount
