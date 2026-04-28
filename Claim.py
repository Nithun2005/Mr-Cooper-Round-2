class Claim:
    def __init__(self, claim_id, policy_number, incident_date, amount):
        self.__claim_id = claim_id
        self.__policy_number = policy_number
        self.__incident_date = incident_date
        self.__amount = amount
        self.__status = "Submitted"
        self.__adjuster_notes = ""
        self.__settlement_amount = 0

    # Getters
    def get_claim_id(self):
        return self.__claim_id

    def get_policy_number(self):
        return self.__policy_number

    def get_incident_date(self):
        return self.__incident_date

    def get_amount(self):
        return self.__amount

    def get_status(self):
        return self.__status

    def get_settlement_amount(self):
        return self.__settlement_amount

    def get_adjuster_notes(self):
        return self.__adjuster_notes

    # Setters
    def set_status(self, value):
        self.__status = value

    def set_settlement_amount(self, value):
        self.__settlement_amount = value

    def set_adjuster_notes(self, value):
        self.__adjuster_notes = value

    # Methods
    def approve(self, amount, notes=""):
        self.set_status("Approved")
        self.set_settlement_amount(amount)
        self.set_adjuster_notes(notes)
        print(f"[SYSTEM] Claim {self.get_claim_id()} APPROVED for Rs.{self.get_settlement_amount()}. Notes: {notes}")

    def reject(self, notes=""):
        self.set_status("Rejected")
        self.set_settlement_amount(0)
        self.set_adjuster_notes(notes)
        print(f"[SYSTEM] Claim {self.get_claim_id()} REJECTED. Notes: {notes}")

    def calculate_settlement(self, coverage_limit):
        if self.get_amount() > coverage_limit:
            print(f"[WARNING] Review Flag: Claim Rs.{self.get_amount()} exceeds Sum Assured Rs.{coverage_limit}. Auto-capping.")
            return coverage_limit
        return self.get_amount()