"""Classes for melon orders."""


class AbstractMelonOrder():
    """Abstract Melon Order Class"""

    def __init__(self, species, qty, country_code='USA'):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""

        if self.species == "Christmas melon":
            base_price = 7.5

        else:
            base_price = 5

        total = (1 + self.tax) * self.qty * base_price

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

        if self.qty < 10:
            total += 3

        return total
