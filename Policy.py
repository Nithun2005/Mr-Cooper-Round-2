from datetime import timedelta

class Policy:
    def __init__(self, policy_number, holder_id, policy_type, coverage_amount, premium, start_date, end_date):
        self.__policy_number = policy_number
        self.__holder_id = holder_id
        self.__type = policy_type
        self.__coverage_amount = coverage_amount
        self.__premium = premium
        self.__start_date = start_date
        self.__end_date = end_date
        self.__status = "Pending"

        # Getters
    def get_policy_number(self):
        return self.__policy_number

    def get_coverage_amount(self):
        return self.__coverage_amount

    def get_premium(self):
        return self.__premium

    def get_status(self):
        return self.__status

    def get_end_date(self):
        return self.__end_date

    # Setters
    def set_coverage_amount(self, value):
        self.__coverage_amount = value

    def set_premium(self, value):
        self.__premium = value

    def set_status(self, value):
        self.__status = value

    def set_end_date(self, value):
        self.__end_date = value

    # Methods
    def activate(self):
        self.set_status("Active")
        print(f"[SYSTEM] Policy {self.get_policy_number()} ACTIVATED.")

    def lapse(self):
        self.set_status("Lapsed")
        print(f"[SYSTEM] Policy {self.get_policy_number()} LAPSED.")

    def renew(self, duration_days=365):
        new_end_date = self.get_end_date() + timedelta(days=duration_days)
        self.set_end_date(new_end_date)
        self.set_status("Active")
        print(f"[SYSTEM] Policy {self.get_policy_number()} RENEWED until {self.get_end_date().strftime('%Y-%m-%d')}.")

    def surrender(self):
        self.set_status("Surrendered")
        surrender_value = self.get_premium() * 0.40
        print(f"[SYSTEM] Policy {self.get_policy_number()} SURRENDERED. Surrender value processed: Rs.{surrender_value}")
        return surrender_value

    def modify_coverage(self, new_coverage, new_premium):
        self.set_coverage_amount(new_coverage)
        self.set_premium(new_premium)
        print(f"[SYSTEM] Endorsement Added: Coverage updated to Rs.{self.get_coverage_amount()}, Pro-rata Premium adjusted to Rs.{self.get_premium()}")