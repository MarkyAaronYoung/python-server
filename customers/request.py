CUSTOMERS = [
  {
        "id": 1,
        "name": "Hannah Hall",
        "business": "NSS",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Brain Neal",
        "business": "NSS Day",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Mitchell Blom",
        "business": "NSS Evening",
        "locationId": 2,
        "customerId": 1
    }
]

def get_all_customers():
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
