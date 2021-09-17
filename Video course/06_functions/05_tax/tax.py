def calc_tax(amount,tax_rate,age):


    if not isinstance(amount, (int, float)):
        raise TypeError("Must be int/float")
    if not amount >= 0:
        raise ValueError("Amount must be positive")

    if not isinstance(tax_rate, float):
        raise TypeError("Must be float")
    if not 0 < tax_rate < 1:
        raise ValueError("Must be between 0 and 1")

    if not isinstance(age, int):
        raise TypeError("The age must be int.")
    if not age > 0:
        raise ValueError("Must be positive.")

    if age <= 18:
        return int(min(amount * tax_rate,5000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount*tax_rate, 8000))