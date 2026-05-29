INVALID_INPUT = "Invalid Input"
NOT_A_TRIANGLE = "Not a Triangle"
EQUILATERAL = "Equilateral"
ISOSCELES = "Isosceles"
SCALENE = "Scalene"


def classify_triangle(a, b, c):
    """Classify a triangle using the EP/BVA and decision-table rules."""
    if not (1 <= a <= 100 and 1 <= b <= 100 and 1 <= c <= 100):
        return INVALID_INPUT

    if a + b <= c or a + c <= b or b + c <= a:
        return NOT_A_TRIANGLE

    if a == b == c:
        return EQUILATERAL

    if a == b or b == c or a == c:
        return ISOSCELES

    return SCALENE


TEST_CASES = [
    # Invalid inputs - boundary value analysis.
    ("TC_01", 0, 50, 50, INVALID_INPUT),
    ("TC_02", 101, 50, 50, INVALID_INPUT),
    ("TC_03", 50, 0, 50, INVALID_INPUT),
    ("TC_04", 50, 50, 101, INVALID_INPUT),
    ("TC_14", 50, 101, 50, INVALID_INPUT),
    ("TC_15", 50, 50, 0, INVALID_INPUT),

    # Business rules - optimized decision table.
    ("TC_05", 10, 20, 50, NOT_A_TRIANGLE),
    ("TC_06", 1, 2, 3, NOT_A_TRIANGLE),
    ("TC_07", 50, 50, 50, EQUILATERAL),
    ("TC_08", 100, 100, 100, EQUILATERAL),
    ("TC_09", 50, 50, 40, ISOSCELES),
    ("TC_10", 40, 50, 50, ISOSCELES),
    ("TC_11", 50, 40, 50, ISOSCELES),
    ("TC_12", 3, 4, 5, SCALENE),
    ("TC_13", 98, 99, 100, SCALENE),
]


def run_tests():
    passed_count = 0
    total_count = len(TEST_CASES)

    print(
        f"{'TC ID':<8} | {'a':<5} | {'b':<5} | {'c':<5} | "
        f"{'Expected Output':<16} | {'Actual Output':<16} | Status"
    )
    print("-" * 80)

    for test_id, a, b, c, expected in TEST_CASES:
        actual = classify_triangle(a, b, c)
        status = "PASSED" if actual == expected else "FAILED"

        if status == "PASSED":
            passed_count += 1

        print(
            f"{test_id:<8} | {a:<5} | {b:<5} | {c:<5} | "
            f"{expected:<16} | {actual:<16} | {status}"
        )

    failed_count = total_count - passed_count
    print("-" * 80)
    print(f"Total: {total_count} | Passed: {passed_count} | Failed: {failed_count}")

    if failed_count == 0:
        print("Conclusion: source code PASSED all test cases.")
        return True

    print("Conclusion: source code FAILED at least one test case.")
    return False


if __name__ == "__main__":
    raise SystemExit(0 if run_tests() else 1)
