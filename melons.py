"""Classes for melon orders."""
from random import randint
import datetime as dt

class AbstractMelonOrder():
    """Abstract Melon Order Class"""

    def __init__(self, species, qty, country_code='USA'):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
        self.base_price = None

    def get_base_price(self):
        base_price = randint(5, 10)

        current_datetime = dt.datetime.now()
        #current_date = current_datetime.date()
        current_time = current_datetime.time()
        
        day_of_week = current_datetime.weekday()
        
        morning_8am = dt.time(hour=8)
        morning_11am = dt.time(hour=11)

        if morning_8am <= current_time < morning_11am and 0 <= day_of_week <= 4:
            base_price += 4

        return base_price


    def get_total(self):
        """Calculate price, including tax."""

        if not self.base_price:
            self.base_price = self.get_base_price()

        if self.species == "Christmas melon":
            self.base_price *= 1.5

        total = (1 + self.tax) * self.qty * self.base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def get_total(self):
        
        total = super().get_total()

        return total+3 if self.qty < 10 else total


class GovernmentMelonOrder(AbstractMelonOrder):
    """For Government orders"""

    tax = 0

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed


