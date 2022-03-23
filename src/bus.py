from dataclasses import asdict


class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []
    
    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, passenger):
        self.passengers.append(passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)

    def empty(self):
        self.passengers = []

    def pick_up_from_stop(self, bus_stop):
        for passenger in bus_stop.queue:
            self.pick_up(passenger)
        # This picks up everybody at the stop, so it can't be selective,
        # but that's all that the task is asking for.
        # It's implied by context that I should also be removing the passengers
        # from the bus stop, though this isn't actually tested for. Still, let's do it:
        bus_stop.clear()
        # If I were to make it more selective, it would require quite a few changes,
        # and I have to start work in my day job in a moment, so I'll leave it for now.