from RiskEngine import RiskEngine

class Underwriter:
    def __init__(self, underwriter_id, name):
        self.__underwriter_id = underwriter_id
        self.__name = name
        self.__risk_engine = RiskEngine()
    # Getters
    def get_underwriter_id(self):
        return self.__underwriter_id

    def get_name(self):
        return self.__name

    # Methods
    def assess_risk(self, customer):
        return self.__risk_engine.score_risk(customer)

    def process_application(self, customer, coverage_amount):
        if not customer.get_kyc_status():
            raise Exception(f"E5 Exception: Application on hold: KYC pending for {customer.get_name()}")

        risk = self.assess_risk(customer)

        if risk == "High":
            raise Exception("E1 Exception: Application Rejected Profile High Risk - Excessive age and pre-existing conditions.")

        return self.__risk_engine.calculate_premium(customer, coverage_amount)