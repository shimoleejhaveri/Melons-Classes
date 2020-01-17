"""Classes for melon orders."""
from random import randint

class AbstractMelonOrder():
    """Abstract Melon Order Class"""

    def __init__(self, species, qty, country_code='USA'):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
        self.base_price = None

    def get_base_price(self):
        return randint(5, 10)

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


