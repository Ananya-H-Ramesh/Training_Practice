import logging

logging.basicConfig(level=logging.INFO,
                    format = "%(levelname)s %(message)s"
                    )


class Car:
    """
    A class representing a vehicle.

    Attributes:
        brand (str): The brand of the vehicle.
        model (str): The model of the vehicle.
        color (str): The color of the vehicle.
        speed (float): The current speed of the vehicle.

    Methods:
        accelerate(acceleration: float): Increases the speed of the vehicle by the given acceleration value.
        brake(deceleration: float): Decreases the speed of the vehicle by the given deceleration value.
    """

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self, acceleration):
        self.speed += acceleration

    def brake(self, deceleration):
        if self.speed - deceleration < 0:
            self.speed = 0
        else:
            self.speed -= deceleration

    def display_info(self):
        logging.info(f"Brand: {self.brand}")
        logging.info(f"Model: {self.model}")
        logging.info(f"Color: {self.color}")
        logging.info(f"Current Speed: {self.speed} mph")


#creating Object car1 and car2
car1 = Car("Toyota", "Camry", "Silver")
car2 = Car("Honda", "Civic", "Red")


car1.accelerate(30)
car1.display_info()

car2.accelerate(20)
car2.brake(10)
car2.display_info()