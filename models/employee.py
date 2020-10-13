class Employee():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, manager, full_time, hourly_rate, location):
        self.id = id
        self.name = name
        self.manager = manager
        self.full_time = full_time
        self.hourly_rate = hourly_rate
        self.location = location
