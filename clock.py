# CLOCK WAS AN OLDER IDEA TO KEEP TRACK OF TIME. STILL KEPT THE CLASS BUT IT IS NOT VITAL TO THE
# RUNNING OF THE PROGRAM
class clock:
    def __init__(self, current_time):
        self.current_time = current_time


    def __str__(self):
        return "%s" % (
            self.current_time)