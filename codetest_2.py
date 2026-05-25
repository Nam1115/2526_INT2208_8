def process_loan_application(age, income, credit_score, employment):
    # 1. Validation Logic
    if not isinstance(age, int) or age < 18 or age > 65:
        return "Invalid Input"
    if not isinstance(income, (int, float)) or income < 5.0 or income > 500.0:
        return "Invalid Input"
    if not isinstance(credit_score, int) or credit_score < 300 or credit_score > 850:
        return "Invalid Input"
    if employment not in ["C", "F"]:
        return "Invalid Input"

    # 2. Determine Risk Level
    if 300 <= credit_score <= 500:
        risk = "High"
    elif 501 <= credit_score <= 700:
        risk = "Medium"
    else:  # 701 <= credit_score <= 850
        risk = "Low"

    # 3. Business Logic (Decision Rules)
    if risk == "High":
        return "REJECT"
    
    if income < 15.0:
        if risk == "Medium":
            return "REJECT"
        elif risk == "Low" and employment == "F":
            return "REJECT"
        elif risk == "Low" and employment == "C":
            return "MANUAL REVIEW"
            
    else: # income >= 15.0
        # Covers both Low and Medium Risk
        if employment == "C":
            return "APPROVE"
        elif employment == "F":
            return "MANUAL REVIEW"

# ==========================================
# TEST RUNNER
# ==========================================
test_cases = [
    # TC_ID, inputs: (age, income, credit_score, employment), Expected Output
    # Validation (Negative)
    ("TC_INV_01", (17, 20.0, 600, "C"), "Invalid Input"),
    ("TC_INV_02", (66, 20.0, 600, "C"), "Invalid Input"),
    ("TC_INV_03", (25, 4.9, 600, "C"), "Invalid Input"),
    ("TC_INV_04", (25, 500.1, 600, "C"), "Invalid Input"),
    ("TC_INV_05", (25, 20.0, 299, "C"), "Invalid Input"),
    ("TC_INV_06", (25, 20.0, 851, "C"), "Invalid Input"),
    ("TC_INV_07", (25, 20.0, 600, "X"), "Invalid Input"),
    
    # Business Logic (Positive)
    ("TC_R1_01", (18, 50.0, 300, "C"), "REJECT"),
    ("TC_R1_02", (65, 50.0, 500, "F"), "REJECT"),
    ("TC_R2_01", (25, 14.9, 501, "C"), "REJECT"),
    ("TC_R3_01", (30, 5.0, 701, "F"), "REJECT"),
    ("TC_R4_01", (30, 10.0, 850, "C"), "MANUAL REVIEW"),
    ("TC_R5_01", (40, 15.0, 700, "C"), "APPROVE"),
    ("TC_R6_01", (50, 500.0, 701, "F"), "MANUAL REVIEW")
]

if __name__ == "__main__":
    passed_all = True
    print("Running Tests...\n")
    for tc_id, inputs, expected in test_cases:
        result = process_loan_application(*inputs)
        if result == expected:
            print(f"[{tc_id}] PASSED")
        else:
            print(f"[{tc_id}] FAILED: Expected '{expected}', got '{result}'")
            passed_all = False
            
    print("\nOVERALL STATUS: ", "SUCCESS" if passed_all else "FAIL")