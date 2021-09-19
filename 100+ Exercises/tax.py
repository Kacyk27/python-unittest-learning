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