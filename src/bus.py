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
        # There is an implication that I'm supposed to call bus_stop.clear() here,
        # but what if only some passengers got on the bus?
        # Better to modify pick_up(), in my opinion. However, this would require
        # rewriting the test file to feed pick_up another argument for the stop.
        # So I'll do what I'm probably supposed to do instead:
        bus_stop.clear()
        # This isn't even tested for anyway, but otherwise, we're cloning passengers.
        # I'm wondering if it would also work if I had a separate method to remove
        # passengers from the queue, but for some reason I can't seem to get this to work.
        # I would've thought that the method (in bus_stop.py) would be:
        # def remove_from_queue(self, passenger):
        #     self.passenger = passenger
        #     self.queue.remove(passenger)
        # And then I'd run it like this:
        # for passenger in bus_stop.queue:
        #     self.pick_up(passenger)
        #     bus_stop.remove_from_queue(passenger)
        # But doing that only adds the first passenger to the bus and it seems to be
        # removing the second from the queue before they're added to the bus, which I
        # don't quite get. I'll have a think.