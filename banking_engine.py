from custom_exception import (
    InsufficientFundsError,
    UnauthorizedAccessError,
)


class BankAccount:

    def __init__(
        self,
        owner: str,
        initial_balance: float
    ):

        self.owner = owner

        self._balance = initial_balance

        self._account_number = "ACC1001"

    @property
    def balance(self):

        return self._balance

    @property
    def account_number(self):

        return self._account_number

    def deposit(
        self,
        amount: float
    ):

        if amount <= 0:

            raise ValueError(
                "Deposit amount must be positive."
            )

        self._balance += amount

        print(
            f"Deposited: ${amount}"
        )

    def withdraw(
        self,
        amount: float
    ):

        if amount <= 0:

            raise ValueError(
                "Amount must be positive."
            )

        if amount > self._balance:

            raise InsufficientFundsError(
                "Insufficient funds."
            )

        self._balance -= amount

        print(
            f"Withdrawn: ${amount}"
        )

    def __str__(self):

        return (
            f"Owner: {self.owner}\n"
            f"Account Number: "
            f"{self.account_number}\n"
            f"Balance: ${self.balance}"
        )


class AdminAccount(BankAccount):

    ADMIN_PIN = "1234"

    def __init__(
        self,
        owner: str,
        initial_balance: float
    ):

        super().__init__(
            owner,
            initial_balance
        )

    def force_override_withdrawal(
        self,
        amount: float,
        admin_pin: str
    ):

        if admin_pin != self.ADMIN_PIN:

            raise UnauthorizedAccessError(
                "Invalid Admin PIN."
            )

        self._balance -= amount

        print(
            f"Admin withdrew "
            f"${amount}"
        )