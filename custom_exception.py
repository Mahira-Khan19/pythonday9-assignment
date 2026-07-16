class InsufficientFundsError(Exception):
    """Raised when withdrawal exceeds balance."""
    pass


class UnauthorizedAccessError(Exception):
    """Raised when admin PIN is incorrect."""
    pass