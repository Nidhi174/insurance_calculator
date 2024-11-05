import streamlit as st

def calculate_life_insurance_cover(planned_expenses, outstanding_loan, investments, annual_expenses, other_family_income):
    """
    Calculate the required life insurance coverage in Rupees using the specified formula.

    Parameters:
    planned_expenses (float): The planned future expenses in Rupees.
    outstanding_loan (float): The outstanding loan amount in Rupees.
    investments (float): The current investments of the individual in Rupees.
    annual_expenses (float): Annual expenses for the family in Rupees.
    other_family_income (float): Other family members' annual income in Rupees.

    Returns:
    float: Required life insurance cover in Rupees.
    """
    # Calculate required insurance cover using the provided formula
    insurance_cover = (planned_expenses + outstanding_loan - investments +
                       (10 * annual_expenses) - (10 * other_family_income))
    return max(insurance_cover, 0)  # Ensure cover is not negative

st.title("Life Insurance Cover Calculator")

# Input fields
investments = st.number_input("How much have you saved/invested to date? (in Rupees)", min_value=0.0, step=1000.0)
outstanding_loan = st.number_input("How much loan amount is still unpaid? (in Rupees)", min_value=0.0, step=1000.0)
planned_expenses = st.number_input("Enter planned future expenses (in Rupees)", min_value=0.0, step=1000.0)

# Ask about dependents
has_dependents = st.radio("Do you have any family members dependent on you?", ("Yes", "No"))
if has_dependents == "Yes":
    annual_expenses = st.number_input("Annual expenses to take care of family's basic financial needs (in Rupees)", min_value=0.0, step=1000.0)
else:
    annual_expenses = 0

# Ask about sole earner status
is_sole_earner = st.radio("Are you the sole earning member in your family?", ("Yes", "No"))
if is_sole_earner == "No":
    other_family_income = st.number_input("Steady Annual Income earned by other family members (after tax, in Rupees)", min_value=0.0, step=1000.0)
else:
    other_family_income = 0

# Buttons for submission and reset
if st.button("Submit"):
    # Calculate insurance cover
    insurance_cover = calculate_life_insurance_cover(planned_expenses, outstanding_loan, investments, annual_expenses, other_family_income)
    st.write(f"### Suggested Insurance Cover: ₹{insurance_cover:,.2f}")

if st.button("Reset"):
    st.experimental_rerun()  # Rerun the app to clear inputs
