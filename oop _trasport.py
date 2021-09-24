from abc import ABC, abstractmethod


class Transport(ABC):

    list_objects = []               # list of all objects of class transport

    def __init__(self, model, speed, passengers):
        self.model = model
        self.speed = speed
        self.passengers = passengers
        Transport.list_objects.append(self)

    def __repr__(self):
        return f"{self.model} speed {self.speed}"

    def __gt__(self, other):
        return self.speed > other.speed

    def __lt__(self, other):
        return self.speed < other.speed

    @classmethod
    def total_objects(cls):
        """returns all objects of class transport"""
        return cls.list_objects

    @staticmethod
    def race(array, top):
        """ returns top of the fastest transport"""
        return sorted(array, reverse=True)[:top]


class Engine(ABC):

    def __init__(self, type_of_engine, power, fuel_consumption):

        fuel = {"electric": 0, "petrol": 34, "diesel": 28, "aviation fuel": 20}

        self.type_of_engine = type_of_engine
        self.power = power
        self.fuel_consumption = fuel_consumption
        self.cost_of_fuel = fuel[self.type_of_engine]

    @abstractmethod
    def trip_price(self, distance):
        """returns fare for a given distance"""
        pass


class Car(Transport, Engine):

    list_objects = []                           # list of all objects of class Car

    def __init__(self, model, speed, passengers,
                 type_of_engine, power, fuel_consumption):
        Transport.__init__(self, model, speed, passengers)
        Engine.__init__(self, type_of_engine, power, fuel_consumption)
        Car.list_objects.append(self)

    @abstractmethod
    def trip_price(self, distance):
        """returns fare for a given distance"""
        return f"{distance * self.fuel_consumption / 100 * self.cost_of_fuel / self.passengers} grn"


class Plane(Transport, Engine):

    k = 5           # factory profit factor

    list_objects = []                   # list of all objects of class Plane
    _flight_seats = {"economy": 0, "business_class": 0, "first_class": 0}

    def __init__(self, model, speed, passengers, fuel_consumption,
                 type_of_engine, power):
        Transport.__init__(self, model, speed, passengers)
        Engine.__init__(self, type_of_engine, power, fuel_consumption)
        Plane.list_objects.append(self)

    def __setitem__(self, flight_class, number):
        self._flight_seats[flight_class] = number

    def __getitem__(self, flight_class):
        return self._flight_seats[flight_class]

    def trip_price(self, distance):
        """returns fare for a given distance"""
        return f"{distance * self.fuel_consumption / 100 * self.cost_of_fuel / self.passengers * self.k} grn"


class Train(Transport, Engine):

    list_objects = []
    train_price = {"platskart": 200, "kupe": 900,
                   "intercity": 400, "luks": 2500}

    def __init__(self, model, speed, passengers, fuel_consumption,
                 type_of_engine, power, train_klass):
        Transport.__init__(self, model, speed, passengers)
        Engine.__init__(self, type_of_engine, power, fuel_consumption)
        self.train_klass = train_klass
        Train.list_objects.append(self)

    def trip_price(self, distance):
        """returns fare for a given distance"""
        return f"{self.train_price[self.train_klass]} grn"


class Bus(Transport, Engine):
    k = 5                               # factory profit factor
    list_objects = []

    def __init__(self, model, speed, passengers, fuel_consumption,
                 type_of_engine, power):
        Transport.__init__(self, model, speed, passengers)
        Engine.__init__(self, type_of_engine, power, fuel_consumption)
        Bus.list_objects.append(self)

    def trip_price(self, distance):
        """returns fare for a given distance"""
        return f"{distance * self.fuel_consumption / 100 * self.cost_of_fuel / self.passengers * self.k} grn"


a = Bus("intersity", 100, 50, 40, "diesel", 1000)
print(a.trip_price(200))
print(a)

