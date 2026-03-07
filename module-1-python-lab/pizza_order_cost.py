
# Given Constants
SIZE_TO_PRICE = {"small": 8, "large": 12}
PRICE_PER_TOPPING = 1
PRICE_PER_XTR_MILE = 1
PRICE_FOR_BASE_MILE = 2
BASE_MILES = 5

# Helpers for readability and testing
def requestSize():
    return input("What size pizza would you like? (Small $8, Large $12):")

def requestToppings():
    return input("How many toppings would you like?:")

def requestMiles():
    return input("How many miles away do you live?:")

def start():

    # 1. Prompt for Pizza Size
    input_size = None
    while input_size not in SIZE_TO_PRICE:
        input_size = requestSize().lower()
    # 2. Calculate the base cost of the pizza using conditional statements. (small - $8, large - $12)
    size_price = SIZE_TO_PRICE[input_size]

    # 3. Prompt for # of toppings
    input_toppings = None
    while input_toppings is None:
        try:
            input_toppings = int(requestToppings())
            if input_toppings < 0:
                input_toppings = None
        except ValueError:
            pass
    # 4. Calculate the cost of toppings. ($1 per topping)
    toppings_price = PRICE_PER_TOPPING * input_toppings

    # 5. Prompt for mileage
    input_miles = None
    while input_miles is None:
        try:
            input_miles = float(requestMiles())
            if input_miles < 0:
                input_miles = None
        except ValueError:
            pass

    # 6. Calculate the delivery fee. ($2 for the first 5 miles, $1 for each add. mile)
    miles_price = None
    if input_miles <= BASE_MILES:
        miles_price = PRICE_FOR_BASE_MILE
    else:
        miles_price = PRICE_FOR_BASE_MILE + (input_miles - BASE_MILES) * PRICE_PER_XTR_MILE

    # 7. Sum up the total cost.
    total = size_price + toppings_price + miles_price
    # 8. Display the result using an f-string.
    print(f"Pizza ({input_size}): ${size_price}")
    print(f"Toppings ({input_toppings}): ${toppings_price}")
    print(f"Delivery ({input_miles} miles): ${miles_price}")
    print(f"Total: ${total}")

start()
