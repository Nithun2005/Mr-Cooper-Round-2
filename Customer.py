class Customer:
    def __init__(self, customer_id, name, age, kyc_status, pre_existing_conditions=0, ncb_years=0):
        self.__customer_id = customer_id
        self.__name = name
        self.__age = age
        self.__kyc_status = kyc_status
        self.__policies = []
        self.__pre_existing_conditions = pre_existing_conditions
        self.__ncb_years = ncb_years

    # Getters
    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_kyc_status(self):
        return self.__kyc_status

    def get_pre_existing_conditions(self):
        return self.__pre_existing_conditions

    def get_ncb_years(self):
        return self.__ncb_years

    def get_policies(self):
        return self.__policies

    # Setters
    def set_name(self, value):
        self.__name = value

    def set_age(self, value):
        if value >= 0:
            self.__age = value

    def set_kyc_status(self, value):
        self.__kyc_status = value

    def set_ncb_years(self, value):
        self.__ncb_years = value

    # Methods
    def add_policy(self, policy):
        self.__policies.append(policy)