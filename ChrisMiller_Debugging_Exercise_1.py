"""
Discount Calculator Program
Program calculates the discount amount and final price for products, prints the results.
"""
def calculate_discount(price, discount_rate):
    """
         Description
            Calculates discount amount by multiplying price by discount rate.
            Includes error handling if inputs are not numbers.

         Parameters
            - price:  original price of product (should be number)
            - discount_rate: discount percentage as decimal

         Variables
            - discount_amount: result of price * discount_rate

         Steps
            - multiply price by discount_rate
            - If TypeError happens (e.g. price is a string),
              print an error message and return 0 instead
            - If other error happens, print a general message and return 0
            - Otherwise return discount amount

         Return
            Discount amount as number, or 0 if error
        """
    # Error handling
    try:
        discount_amount = price * discount_rate
    except TypeError:
        print("Error: Price or discount rate is not a number! Skipping this product.")
        return 0
    except:
        print("Error: Something went wrong with the calculation.")
        return 0

    return discount_amount


def apply_discount(price, discount_amount):
    # Apply discount amount to original price and return new price.
    """
         Description
            Subtract discount amount from original price to get final price.
            Include basic error handling to avoid crashing if input is not a number.

         Parameters
            - price: original price of product (number)
            - discount_amount: amount to subtract (number)

         Variable
            - new_price: result after subtracting discount_amount

         Steps
            - Try to subtract discount_amount from price
            - If TypeError happens (example: not a number),
              print error message
            - Otherwise return discounted price

         Return
            Final price after discount, or original price if error
        """
    try:
        new_price = price - discount_amount
    except TypeError:
        print("Error: Price or discount amount is not a number!")
        return price  # original price if error

    return new_price


def main():
    """
         Description
            Main function that runs discount calculator.
            Has list of products, loops, calculates discounts,
             prints results. Catches errors.

         Parameters
            None

         Variables
            - products: list of dictionaries containing product name, price, discount_rate
            - product: current product dictionary in the loop
            - price: price value from product dictionary
            - discount_rate: discount rate value from product dictionary
            - discount_amount: result from calculate_discount function
            - final_price: result from apply_discount function

         Steps
            - Create list of products
            - Loop through each
            - Get price and discount_rate
            - Call calculate_discount to get discount amount
            - Call apply_discount to get final price
            - Print product name and all three prices
            - If Error (missing price or discount_rate), print error message
            - If other error, print unexpected error

         Return
            None
        """
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": "500", "discount_rate": 0.2},
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    for product in products:
        try:
            price = product["price"]
            discount_rate = product["discount_rate"]

            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount_amount)

            print(f"Product: {product['name']}")
            print(f"Original Price: ${price}")
            print(f"Discount Amount: ${discount_amount}")
            print(f"Final Price: ${final_price}")
            print()

        except KeyError:
            print(f"Error: Missing price or discount rate for {product.get('name', 'a product')}")
            print()
        except Exception as e:
            print(f"Unexpected error with {product.get('name', 'a product')}: {e}")
            print()


if __name__ == "__main__":
    main()