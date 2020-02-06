"""Classes for melon orders."""
from random import randint

class AbstractMelonOrder():

    def __init__(self, species, qty, order_type):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type

    def get_base_price(self):
        """Get random int for base price"""

        return randint(5, 9)

    def get_total(self):
        """Calculate price, including tax."""

        self.base_price = self.get_base_price()

        if self.species == "christmas melon":
            self.base_price = self.base_price*1.5

        total = (1 + self.tax) * self.qty * self.base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "domestic")
        self.tax = 0.08
   

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty, "international")
        self.country_code = country_code
        self.tax = 0.17

    def get_total(self):
        total = super().get_total()
        if self.qty < 10:
            total = total + 3

        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty, "government")
        self.tax = 0
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Track whether order has passed inspection."""

        self.passed_inspection = passed

        # if passed == True:
        #     self.passed_inspection = True
