def calculate_tax(amount, age, tax=17.0):
    """The function returns the amount of income tax."""

    tax_rate = tax / 100.0

    if age <= 18:
        return int(min(amount * tax_rate, 6000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 9000))

def income_tax(income, first_thresh=17.0, second_thresh=32.0):
    first_rate = first_thresh / 100.0
    second_rate = second_thresh / 100.0
    threshold = 85528
    if income < threshold:
        return income * first_rate
    else:
        return threshold * first_rate + (income - threshold) * second_rate


class SimpleTaxCalculator:

    def income_tax(self, income, first_thresh=17.0, second_thresh=32.0):
        first_rate = first_thresh / 100.0
        second_rate = second_thresh / 100.0
        threshold = 85528
        if income < threshold:
            return income * first_rate
        else:
            return threshold * first_rate + (income - threshold) * second_rate

    def vat_tax(self, net_price, tax=23.0):
        tax_rate = tax / 100.0
        return net_price * tax_rate

    def capital_gains_tax(self, profit, tax=19.0):
        tax_rate = tax / 100.0
        if profit > 0:
            return profit * tax_rate
        return 0

def calc_tax(amount, tax_rate, age):
    """The function returns the amount of income tax."""

    if not isinstance(amount, (int, float)):
        raise TypeError('The amount value must be int or float type.')
    if not amount >= 0:
        raise ValueError('The amount value must be positive.')

    if not isinstance(tax_rate, float):
        raise TypeError('The tax_rate must be float.')
    if not 0 < tax_rate < 1:
        raise ValueError('The tax_rate must be between 0 and 1 (exclusive).')

    if not isinstance(age, int):
        raise TypeError('The age value must be int.')
    if not age > 0:
        raise ValueError('The age value must be positive.')

    if age <= 18:
        return int(min(amount * tax_rate, 5000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 8000))