def calculate_fine(days_overdue):
    """Calculate an overdue fine from the number of overdue days."""
    if type(days_overdue) is not int:
        raise TypeError("invalid argument type")

    if days_overdue < 0:
        raise ValueError("argument outside permitted range")
        
    return min(days_overdue, 10) * 50
