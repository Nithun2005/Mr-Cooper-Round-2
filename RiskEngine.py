class RiskEngine:
    def calculate_premium(self, customer, coverage_amount):
        base_premium = coverage_amount * 0.005

        age_loading = 0
        customer_age = customer.get_age()

        if 18 <= customer_age <= 35:
            age_loading = 0
        elif 36 <= customer_age <= 50:
            age_loading = base_premium * 0.
        elif 51 <= customer_age <= 60:
            age_loading = base_premium * 1.0
        elif customer_age >= 61:
            age_loading = base_premium * 2.0

        condition_loading = customer.get_pre_existing_conditions() * 500
        subtotal = base_premium + age_loading + condition_loading

        ncb_discount_percent = min(customer.get_ncb_years() * 0.05, 0.50)
        ncb_discount = subtotal * ncb_discount_percent

        final_premium = subtotal - ncb_discount
        return round(final_premium / 10) * 10

    def score_risk(self, customer):
        if customer.get_age() > 70 and customer.get_pre_existing_conditions() >= 3:
            return "High"
        return "Normal"