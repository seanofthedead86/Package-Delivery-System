# O(1)
class DeliveryTruck:
    def __init__(self, packages, priority_packages,location, end_time, total_miles):
        self.packages = packages
        self.priority_packages = priority_packages
        self.location = location
        self.end_time = end_time
        self.total_miles = total_miles

    # O(1)
    def __str__(self):
        return "%s, %s, %s, %s" % (
            self.packages, self.priority_packages, self.location, self.end_time, self.total_miles)
