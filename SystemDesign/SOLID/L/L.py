from abc import ABC, abstractmethod


class PaymentResult:
    def __init__(self, success, message):
        self.success = success
        self.message = message


class Payment(ABC):
    @abstractmethod
    def pay(self) -> PaymentResult:
        """
        Contract:
        - Must always return a PaymentResult object.
        """
        pass


class CreditCard(Payment):
    def pay(self):
        print("Processing Credit Card Payment...")
        return PaymentResult(True, "Credit Card Payment Successful")


class UPI(Payment):
    def pay(self):
        print("Processing UPI Payment...")
        return PaymentResult(True, "UPI Payment Successful")


class NetBanking(Payment):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def pay(self):
        print("Processing Net Banking Payment...")

        if self.password != "correct123":
            return PaymentResult(False, "Invalid Username or Password")

        return PaymentResult(True, "Net Banking Payment Successful")


# ❌ LSP Violation
class CryptoPayment(Payment):
    def pay(self):
        print("Processing Crypto Payment...")
        raise Exception("Crypto network is down")


def checkout(payment: Payment):
    result = payment.pay()

    if result.success:
        print("✅", result.message)
    else:
        print("❌", result.message)


# -----------------------
# LSP Followed
# -----------------------

checkout(CreditCard())

print()

checkout(UPI())

print()

checkout(NetBanking("sameer", "wrong"))

print()

checkout(NetBanking("sameer", "correct123"))

print()

# -----------------------
# LSP Violated
# -----------------------

checkout(CryptoPayment())


"""
Why is CryptoPayment violating LSP?

The parent contract says:

pay() -> PaymentResult

So checkout() is written assuming:

result = payment.pay()

if result.success:
    ...

This works for:

CreditCard ✅
UPI ✅
NetBanking ✅

But when CryptoPayment is substituted:

checkout(CryptoPayment())

pay() throws an exception instead of returning a PaymentResult.

Therefore, checkout() crashes before it can access:

result.success

So CryptoPayment is not a valid substitute for Payment, which is exactly what LSP warns against.



"""