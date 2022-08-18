class Package:
    def __init__(self, ID, address, city, state, zipcode, deadline, mass, notes, status, delivery_time):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.status = status
        self.delivery_time = delivery_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.ID, self.address, self.city, self.state, self.zipcode, self.deadline, self.mass, self.notes,
            self.status, self.delivery_time)

    # O(1)
    def get_id(self):
        return self.ID

    # O(1)
    def set_address(self, address):
        self.address = address

    # O(1)
    def get_address(self):
        return self.address

    # O(1)
    def get_city(self):
        return self.city

    # O(1)
    def get_zip(self):
        return self.zipcode

    # O(1)
    def set_zip(self, zip):
        self.zipcode = zip

    # O(1)
    def get_deadline(self):
        return self.deadline

    # O(1)
    def get_notes(self):
        return self.notes

    # O(1)
    def get_mass(self):
        return self.mass

    # O(1)
    def get_status(self):
        return self.delivery_status

    # O(1)
    def set_status(self, new_status):
        self.delivery_status = new_status

    # O(1)
    def get_delivery_time(self):
        return self.delivery_time

    # O(1)
    def set_delivery_time(self, time):
        self.delivery_time = time


