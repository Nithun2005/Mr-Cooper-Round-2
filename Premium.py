from datetime import timedelta

class Premium:
    def __init__(self, premium_id, policy_number, due_date, amount):
        self.__premium_id = premium_id
        self.__policy_number = policy_number
        self.__due_date = due_date
        self.__amount = amount
        self.__paid_date = None
        self.__status = "Pending"

    # Getters
    def get_premium_id(self):
        return self.__premium_id

    def get_policy_number(self):
        return self.__policy_number

    def get_due_date(self):
        return self.__due_date

    def get_amount(self):
        return self.__amount

    def get_status(self):
        return self.__status

    # Setters
    def set_due_date(self, value):
        self.__due_date = value

    def set_status(self, value):
        self.__status = value

    # Methods
    def pay(self, date_paid):
        self.__paid_date = date_paid
        self.set_status("Paid")
        print(f"[SYSTEM] Premium {self.get_premium_id()} of Rs.{self.get_amount()} PAID on {date_paid.strftime('%Y-%m-%d')}")

    def mark_overdue(self):
        self.set_status("Overdue")

    def apply_grace_period(self):
        new_due_date = self.get_due_date() + timedelta(days=30)
        self.set_due_date(new_due_date)
        self.set_status("Grace Period")
        print(f"[SYSTEM] Grace Period applied for {self.get_premium_id()}. New due date is {self.get_due_date().strftime('%Y-%m-%d')}")