from banking_engine import (
    BankAccount,
    AdminAccount,
)
from custom_exception import (
    InsufficientFundsError,
    UnauthorizedAccessError,
)

print("BANK ACCOUNT SYSTEM")
print("-" * 40)

user = BankAccount(
    "Mahira",
    1000
)

admin = AdminAccount(
    "Manager",
    5000
)

print()
print("User Account")
print(user)

print()

try:

    user.deposit(500)

    user.withdraw(300)

    print()

    print(
        "Current Balance:",
        user.balance
    )

except ValueError as e:

    print(e)

except InsufficientFundsError as e:

    print(e)

print()

print("Testing Insufficient Funds")

try:

    user.withdraw(5000)

except InsufficientFundsError as e:

    print(e)

print()

print("Testing Invalid Deposit")

try:

    user.deposit(-200)

except ValueError as e:

    print(e)

print()

print("Testing Invalid Admin PIN")

try:

    admin.force_override_withdrawal(
        500,
        "9999"
    )

except UnauthorizedAccessError as e:

    print(e)

print()

print("Testing Valid Admin PIN")

try:

    admin.force_override_withdrawal(
        500,
        "1234"
    )

except UnauthorizedAccessError as e:

    print(e)

print()

print("Final User Account")
print(user)

print()

print("Final Admin Account")
print(admin)

print()

print("Program Finished.")