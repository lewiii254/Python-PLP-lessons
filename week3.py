def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    price (float): Original price of the item.
    discount_percent (float): Discount percentage to apply.

    Returns:
    float: Final price after discount if discount_percent is 20 or more,
           otherwise the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Prompt the user for inputs
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price using the function
    final_price = calculate_discount(original_price, discount_percentage)

    # Display the result
    if discount_percentage >= 20:
        print(f"Discount applied! The final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${original_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount percentage.")
