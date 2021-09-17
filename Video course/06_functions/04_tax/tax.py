def calc_tax(amount,tax_rate):

    if not isinstance(amount,(int,float)):
        raise TypeError("Must be int/float")
    if not amount >= 0:
        raise ValueError("Amount must be positive")

    if not isinstance(tax_rate,float):
        raise TypeError("Must be float")
    if not 0<tax_rate<1:
        raise ValueError("Must be between 0 and 1")

    return amount * tax_rate