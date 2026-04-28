import datetime
from datetime import timedelta
from Customer import Customer
from Policy import Policy
from Premium import Premium
from Claim import Claim
from Underwriter import Underwriter

class InsuranceSystem:
    def __init__(self):
        self.customers = {}
        self.policies = {}
        self.claims = {}
        self.premiums = {}
        self.underwriter = Underwriter("UW001", "Raja")
        self._id_counter = 1000

    def generate_id(self, prefix):
        self._id_counter += 1
        return f"{prefix}{self._id_counter}"

    def register_customer(self, name, age, kyc_status, pre_existing, ncb):
        cust_id = self.generate_id("CUST")
        customer = Customer(cust_id, name, age, kyc_status, pre_existing, ncb)
        self.customers[cust_id] = customer
        print(f"Customer {name} registered successfully with ID: {cust_id}")
        return customer

    def apply_for_policy(self, customer_id, policy_type, coverage_amount):
        customer = self.customers.get(customer_id)
        if not customer:
            print("Customer not found.")
            return

        print(f"\n--- Application Initiated for {customer.get_name()} ---")
        try:
            premium_amount = self.underwriter.process_application(customer, coverage_amount)

            policy_num = self.generate_id("POL")
            start_date = datetime.date.today()
            end_date = start_date + timedelta(days=365)

            new_policy = Policy(policy_num, customer.get_customer_id(), policy_type, coverage_amount, premium_amount, start_date, end_date)
            self.policies[policy_num] = new_policy
            customer.add_policy(new_policy)

            prem_id = self.generate_id("PRM")
            new_premium = Premium(prem_id, policy_num, start_date, premium_amount)
            self.premiums[prem_id] = new_premium

            print(f"Application Approved! Policy {policy_num} created. Calculated Premium: Rs.{premium_amount}")
            print(f"Pending Premium ID generated: {prem_id}")
            return new_policy, new_premium

        except Exception as e:
            print(f"Application Failed: {e}")
            return None, None

    def process_premium_payment(self, premium_id):
        premium = self.premiums.get(premium_id)
        if not premium:
            print("Premium ID not found.")
            return

        if premium.get_status() != "Paid":
            premium.pay(datetime.date.today())
            policy = self.policies[premium.get_policy_number()]
            if policy.get_status() in ["Pending", "Grace Period"]:
                policy.activate()
        else:
            print("Premium is already paid.")

    def raise_claim(self, policy_number, amount):
        policy = self.policies.get(policy_number)
        if not policy:
            print("Policy not found.")
            return

        incident_date = datetime.date.today().strftime('%Y-%m-%d')
        print(f"\n--- Processing Claim for Policy {policy_number} ---")

        if policy.get_status() == "Lapsed":
            print("E2 Exception: Policy is lapsed. Please renew first.")
            return

        for existing_claim in self.claims.values():
            if existing_claim.get_policy_number() == policy_number and existing_claim.get_incident_date() == incident_date:
                print(f"E3 Exception: Claim already registered for this incident on {incident_date}.")
                return existing_claim

        claim_id = self.generate_id("CLM")
        new_claim = Claim(claim_id, policy_number, incident_date, amount)
        self.claims[claim_id] = new_claim
        print(f"Claim {claim_id} submitted for Rs.{amount}.")

        settlement_amount = new_claim.calculate_settlement(policy.get_coverage_amount())
        if settlement_amount < amount:
            new_claim.approve(settlement_amount, "A4: Approved up to coverage limit. Customer informed of shortfall.")
        else:
            new_claim.approve(settlement_amount, "Claim looks good. Fully approved.")

def main_menu():
    sys = InsuranceSystem()

    # Pre-seed a customer for easy testing
    sys.register_customer("Murali", 42, True, 2, 3)

    while True:
        print("\n" + "="*40)
        print(" INSURANCE POLICY MANAGEMENT CONSOLE ")
        print("="*40)
        print("1. Register New Customer")
        print("2. Apply for Policy")
        print("3. Pay Premium")
        print("4. Raise a Claim")
        print("5. View System Database (Counts)")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            kyc = input("KYC Verified? (y/n): ").lower() == 'y'
            pre_ex = int(input("Number of Pre-existing conditions: "))
            ncb = int(input("Years of No-Claim Bonus: "))
            sys.register_customer(name, age, kyc, pre_ex, ncb)

        elif choice == '2':
            cust_id = input("Enter Customer ID (e.g., CUST1001): ")
            cov_amt = float(input("Enter Desired Coverage Amount (Rs): "))
            sys.apply_for_policy(cust_id, "Health", cov_amt)

        elif choice == '3':
            prem_id = input("Enter Premium ID to pay (e.g., PRM1003): ")
            sys.process_premium_payment(prem_id)

        elif choice == '4':
            pol_id = input("Enter Policy Number to claim against: ")
            amt = float(input("Enter Claim Amount (Rs): "))
            sys.raise_claim(pol_id, amt)

        elif choice == '5':
            print(f"\n--- System Status ---")
            print(f"Registered Customers: {len(sys.customers)}")
            print(f"Active/Pending Policies: {len(sys.policies)}")
            print(f"Generated Premiums: {len(sys.premiums)}")
            print(f"Processed Claims: {len(sys.claims)}")

        elif choice == '6':
            print("Exiting Insurance System. Goodbye!")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main_menu()