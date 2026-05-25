"""
Chương trình mô phỏng xử lý hồ sơ vay cá nhân của ngân hàng CS2045.

Code gồm 2 phần chính:
1. Hàm xử lý nghiệp vụ: kiểm tra đầu vào, phân loại rủi ro và trả kết quả.
2. Bộ test case: chứng minh chương trình chạy đúng với các ca kiểm thử đã thiết kế.
"""


# Các kết quả đầu ra theo đúng yêu cầu đề bài.
INVALID_INPUT = "Invalid Input"
APPROVE = "APPROVE"
MANUAL_REVIEW = "MANUAL REVIEW"
REJECT = "REJECT"

# Mã loại hình việc làm hợp lệ.
CONTRACT = "C" 
FREELANCE = "F"

# Các mức rủi ro tín dụng được phân loại từ credit_score.
HIGH_RISK = "High"
MEDIUM_RISK = "Medium"
LOW_RISK = "Low"

# Các giá trị biên của miền dữ liệu đầu vào.
MIN_AGE = 18
MAX_AGE = 65
MIN_INCOME = 5.0
MAX_INCOME = 500.0
INCOME_THRESHOLD = 15.0
MIN_CREDIT_SCORE = 300
MAX_CREDIT_SCORE = 850


def is_valid_input(age, income, credit_score, employment):
    """Kiểm tra toàn bộ ràng buộc dữ liệu trước khi xử lý nghiệp vụ."""
    if type(age) is not int or not MIN_AGE <= age <= MAX_AGE:
        return False

    if type(income) not in (int, float) or not MIN_INCOME <= income <= MAX_INCOME:
        return False

    if type(credit_score) is not int or not MIN_CREDIT_SCORE <= credit_score <= MAX_CREDIT_SCORE:
        return False

    return employment in (CONTRACT, FREELANCE)


def get_risk_level(credit_score):
    """Phân loại rủi ro dựa trên credit_score."""
    if credit_score <= 500:
        return HIGH_RISK

    if credit_score <= 700:
        return MEDIUM_RISK

    return LOW_RISK


def process_loan_application(age, income, credit_score, employment):
    """Trả về quyết định phê duyệt khoản vay theo bảng quyết định."""
    if not is_valid_input(age, income, credit_score, employment):
        return INVALID_INPUT

    risk = get_risk_level(credit_score)

    if risk == HIGH_RISK:
        return REJECT

    # Với income dưới 15 triệu: Medium Risk hoặc Freelance đều bị từ chối.
    # Trường hợp còn lại chỉ có Low Risk + Contract nên chuyển thẩm định tay.
    if income < INCOME_THRESHOLD:
        if risk == MEDIUM_RISK or employment == FREELANCE:
            return REJECT

        return MANUAL_REVIEW

    # Với income từ 15 triệu trở lên: Contract được duyệt, Freelance thẩm định tay.
    if employment == CONTRACT:
        return APPROVE

    return MANUAL_REVIEW


# Danh sách test case gồm:
# - TC_INV: kiểm thử ràng buộc đầu vào không hợp lệ.
# - TC_R: kiểm thử 6 luật nghiệp vụ đã rút gọn từ bảng quyết định.
TEST_CASES = [
    ("TC_INV_01", (17, 20.0, 600, CONTRACT), INVALID_INPUT),
    ("TC_INV_02", (66, 20.0, 600, CONTRACT), INVALID_INPUT),
    ("TC_INV_03", (25, 4.9, 600, CONTRACT), INVALID_INPUT),
    ("TC_INV_04", (25, 500.1, 600, CONTRACT), INVALID_INPUT),
    ("TC_INV_05", (25, 20.0, 299, CONTRACT), INVALID_INPUT),
    ("TC_INV_06", (25, 20.0, 851, CONTRACT), INVALID_INPUT),
    ("TC_INV_07", (25, 20.0, 600, "X"), INVALID_INPUT),
    ("TC_R1_01", (18, 50.0, 300, CONTRACT), REJECT),
    ("TC_R1_02", (65, 50.0, 500, FREELANCE), REJECT),
    ("TC_R2_01", (25, 14.9, 501, CONTRACT), REJECT),
    ("TC_R3_01", (30, 5.0, 701, FREELANCE), REJECT),
    ("TC_R4_01", (30, 10.0, 850, CONTRACT), MANUAL_REVIEW),
    ("TC_R5_01", (40, 15.0, 700, CONTRACT), APPROVE),
    ("TC_R6_01", (50, 500.0, 701, FREELANCE), MANUAL_REVIEW),
]


def run_tests():
    """Chạy toàn bộ test case và in kết quả pass/fail."""
    passed_all = True

    print("Running Tests...\n")
    for test_id, inputs, expected in TEST_CASES:
        actual = process_loan_application(*inputs)

        if actual == expected:
            print(f"[{test_id}] PASSED")
        else:
            print(f"[{test_id}] FAILED: Expected '{expected}', got '{actual}'")
            passed_all = False

    print("\nOVERALL STATUS:", "SUCCESS" if passed_all else "FAIL")
    return passed_all


if __name__ == "__main__":
    run_tests()
