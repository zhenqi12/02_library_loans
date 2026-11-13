def can_borrow(active_loans, overdue_books):
    """Determine whether a reader is allowed to borrow one more book."""
    if type(active_loans) is not int or type(overdue_books) is not int:
        raise TypeError("invalid argument type")

    if active_loans < 0 or overdue_books < 0:
        raise ValueError("argument outside permitted range")
        
    return active_loans <= 5 and overdue_books == 0
