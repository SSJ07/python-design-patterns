from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount: int):
        pass


class UPIPayment(Payment):

    def __init__(self, upi_number: str) -> None:
        self.upi_number = upi_number

    def pay(self, amount: int) -> None:
        print(f"Paying {amount} to {self.upi_number}")


class CreditCardPayment(Payment):
    def __init__(self, card_number: int) -> None:
        self.card_number = card_number

    def pay(self, amount: int) -> None:
        print(f"Paying {amount} to {self.card_number}")


class PaymentFactory:

    @staticmethod
    def create_payment(payment_type: str) -> Payment:
        if payment_type == "UPIPayment":
            return UPIPayment("k23423jf")
        elif payment_type == "CreditCardPayment":
            return CreditCardPayment(2142134)
        else:
            print(f"Payment mode {payment_type} is not available")


def main():
    upi_pay = PaymentFactory().create_payment("UPIPayment")
    credit_pay = PaymentFactory().create_payment("CreditCardPayment")

    upi_pay.pay(1400)
    credit_pay.pay(2000)


if __name__ == '__main__':
    main()
