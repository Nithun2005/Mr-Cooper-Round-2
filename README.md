Insurance Policy Management
A.Use Case Details

Actors:PolicyHolder(Customer),Insurance agent,Underwriter,ClaimsAdjuster,System
PreConditions:Insurance products defined with coverage types,premium tables, and terms. Customer KYC documents are verified.
Trigger:Customer applies for new Insurance policy
Main Flow:
1.Customer submits application with personal details and desired coverage
2.Underwriter reviews application and risk profiles.
3.System calculates premium based on age,coverage, and risk score.
4.Underwriter approves or rejects applications.
5.On Approval, policy created with unique policy Number and validity dates
6.Customer pays first premium
7.policy activated
8.customer can raise claims during policy period
9.Adjuster reviews and approve/reject claims
10.On policy expiry, system sends renewal reminder

Alternate Flow:
A1:Customer wants to modify coverage mid term -> Endrosement added;premium adjusted pro-rata.
A2:Customer misses premium payment -> Grace preiod of 30 days;lapse after grace period.
A3:Customer wants to surrender policy before maturity -> calculate surrender value and process
A4:Claim exceeds coverage limit -> Approve only up to coverage limit;inform customer of shortfall

Exception Flow:
E1: Application rejected by underwriter -> 'Application Rejected Profile High Risk' with reason.
E2:Claim raised on lapsed policy -> 'Policy is lapsed.Please renew first.'
E3:Duplicate claim for same Incident -> "claim already registered for this incident"
E4:Claim amount exceeds sum amount -> auto cap at sum assured;flag for review
E5:KYC documents missing -> 'Application on hold:KYC pending'

Postconditions:Policy record created.Premium Schedule generated.Policy activated.Claim record created(if raised).Renewal notification scheduled
Non Functional:Premium Calculation in < 2 seconds.Claims decision with in 5 bussiness days(Work flow SLA).Policy Document generated as PDF within 10 Seconds.All financial transaction Auditable

B.Class Design

1.Policy
Class: Policy
Attributes: policyNumber, holderId, type, coverageAmount, premium. startDate, endDate, status
Key Methods: activate(), lapse(), renew(), surrender()

2.Claim
Class: Claim
Attributes: claimId, policyNumber, incidentDate, amount, status, adjusterNotes
Key Methods: submit(), approve(), reject(), calculateSettlement()

3.Premium
Class: Premium
Attributes: premiumId, policyNumber, dueDate, amount, paidDate, status
Key Methods: pay(), markOverdue(), applyGracePeriod()

4.Underwriter
class: Underwriter
Attributes: underwriterId, name
Key Methods: assessRisk(application), approve(), reject()

5.Customer
class: Customer
Attributes: customerId, name, age, kycStatus, polices[]
Key Methods: applyPolicy(), raiseClaim(), renewPolicy()

6.RiskEngine
Class: RiskEngine
Attributes: ageFactor, coverageFactor, historyFactor
Key Methods: CalculatePremium(customer,coverage),scoreRisk()

C.Premium Calculation Model(Health Insurance Example)

1.Base Premium:
Factor: Base Premium
Weights/Formula: CoverageAmount*BaseRate(0.5%)
example: Rs.500000*0.005= Rs.2500 yearly

2.Age Loading
Factors: Age Loading
Weights/Formula: 18-35: 0x, 36-50: 0.5x, 51-60: 1x, 61+: 2x
eg: age 42 -> Rs.1250

3.pre-existing conditions:
Factor: Pre_existing conditions
Weights/Formula: + Rs.500 yearly per conditions
example:2 condition +Rs.1000

4.No-Claim Bonus
Factor: No-Claim Bonus
Weights/Formula:-5% for each claim-free year(max50%)
eg: 3 NCB years -> -15%

5.Final Premium
factor: Final Premium
Weights/Formula:Sum of factors above rounded to nearest Rs.10
eg : =Rs.3900 per Year
