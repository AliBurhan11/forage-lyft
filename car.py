from abc import ABC, abstractmethod
from datetime import date


class Car(ABC):
    def __init__(self, last_service_date: date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Engine(Serviceable):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Battery(Serviceable):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class CapuletEngine(Engine):
    def needs_service(self) -> bool:
        # Implementation specific to CapuletEngine
        pass


class WilloughbyEngine(Engine):
    def needs_service(self) -> bool:
        # Implementation specific to WilloughbyEngine
        pass


class SternmanEngine(Engine):
    def needs_service(self) -> bool:
        # Implementation specific to SternmanEngine
        pass


class SpindlerBattery(Battery):
    def needs_service(self) -> bool:
        # Implementation specific to SpindlerBattery
        pass


class NubbinBattery(Battery):
    def needs_service(self) -> bool:
        # Implementation specific to NubbinBattery
        pass


class Calliope(Car):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        super().__init__(last_service_date)
        self.current_date = current_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < self.current_date or self.engine_should_be_serviced():
            return True
        else:
            return False

    def engine_should_be_serviced(self) -> bool:
        engine = CapuletEngine()  # Replace with appropriate engine instance
        return engine.needs_service()


class Glissade(Car):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        super().__init__(last_service_date)
        self.current_date = current_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < self.current_date or self.engine_should_be_serviced():
            return True
        else:
            return False

    def engine_should_be_serviced(self) -> bool:
        engine = WilloughbyEngine()  # Replace with appropriate engine instance
        return engine.needs_service()


class Thovex(Car):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        super().__init__(last_service_date)
        self.current_date = current_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < self.current_date or self.engine_should_be_serviced():
            return True
        else:
            return False

    def engine_should_be_serviced(self) -> bool:
        engine = CapuletEngine()  # Replace with appropriate engine instance
        return engine.needs_service()


class Palindrome(Car):
    def __init__(self, current_date: date, last_service_date: date, warning_light_on: bool):
        super().__init__(last_service_date)
        self.current_date = current_date
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        if self.warning_light_on:
            return True
        else:
            return False


class Rorschach(Car):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        super().__init__(last_service_date)
        self.current_date = current_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < self.current_date or self.engine_should_be_serviced():
            return True
        else:
            return False

    def engine_should_be_serviced(self) -> bool:
        engine = SternmanEngine()  # Replace with appropriate engine instance
        return engine.needs_service()


class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Calliope(current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Glissade(current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        return Palindrome(current_date, last_service_date, warning_light_on)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Rorschach(current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Thovex(current_date, last_service_date, current_mileage, last_service_mileage)

