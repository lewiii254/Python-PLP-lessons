def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage.
    
    Returns:
    float: The final price after applying the discount, or the original price if
           the discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percent)

    # Output the result
    if discount_percent >= 20:
        print(f"Discount applied. The final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")




    """
    Calculate the final price after applying a discount of 20% or more.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage.
    
    Returns:
    float: The final price or the original price if the discount is less than 20%.
    """