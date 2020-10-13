from models.employee import Employee

EMPLOYEES = [
    Employee(1, "Butt McButtenstein", False, True, 12, "756 Slaughter Ct")
]


def get_all_employees():
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found animal, if it exists
    requested_employee = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee.id == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    # Get the id value of the last animal in the list
    last_employee = EMPLOYEES[-1]

    # Add 1 to whatever that number is
    new_id = last_employee.id + 1

    # Add an `id` property to the animal dictionary
    employee["id"] = new_id

    # Add the animal dictionary to the list
    new_employee = Employee(employee['id'], employee['name'], employee['manager'], employee['full_time'], employee['hourly_rate'], employee['location'])
    EMPLOYEES.append(new_employee)

    # Return the dictionary with `id` property added
    return employee

def delete_employee(id):
    # Initial -1 value for animal index, in case one isn't found
    employee_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee.id == id:
            # Found the animal. Store the current index.
            employee_index = index

    # If the animal was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, updated_employee):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee.id == id:
            # Found the animal. Update the value.
            EMPLOYEES[index] = Employee(updated_employee['id'], updated_employee['name'], updated_employee['manager'], updated_employee['full_time'], updated_employee['hourly_rate'], updated_employee['location'])
            break
