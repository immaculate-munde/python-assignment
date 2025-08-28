# Function to calculate discount
def calculate_discount(price, discount_percent):
    """
    Calculate final price after applying discount.
    If discount is less than 20%, no discount is applied.
    """
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price


# Prompt user for input
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Final price after {discount_percent}% discount: {final_price}")
    else:
        print(f"No discount applied. Final price: {final_price}")

except ValueError:
    print("Please enter valid numeric values.")
