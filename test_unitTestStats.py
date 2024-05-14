import statistics

def calculate_statistics(investment_values, initial_investment, monthly_investment, num_years):
    # Calculating the statistics of the investment values
    median_investment = statistics.median(sorted(investment_values, key=abs))
    average_investment = sum(investment_values) / len(investment_values)
    min_investment = min(investment_values)
    max_investment = max(investment_values)
    #calculating the standard deviation of the investment values
    std_dev_investment = statistics.stdev(investment_values)
    total_investment = monthly_investment * 12 * num_years
    #returning the calculated statistics
    return median_investment, average_investment, min_investment, max_investment, std_dev_investment, total_investment

# Unit tests
def test_calculate_statistics():
    # Test case 1
    investment_values = [2000, 2500, 3200, 4000, 5000]
    initial_investment = 2000
    monthly_investment = 100
    num_years = 1
    expected_result1 = 3200
    expected_result2 = 3340
    expected_result3 = 2000
    expected_result4 = 5000
    expected_result5 = 1194.9895397031726
    expected_result6 = 3200

    result = calculate_statistics(investment_values, initial_investment, monthly_investment, num_years)
    if result[0] == expected_result1:
        print("Unit test 1 passed")
    else:
        print("Unit test 1 failed")
    if result[1] == expected_result2:
        print("Unit test 2 passed")
    else:
        print("Unit test 2 failed")
    if result[2] == expected_result3:
        print("Unit test 3 passed")
    else:
        print("Unit test 3 failed")
    if result[3] == expected_result4:
        print("Unit test 4 passed")
    else:
        print("Unit test 4 failed")
    if result[4] == expected_result5:
        print("Unit test 5 passed")
    else:
        print("Unit test 5 failed")
    if result[5] == expected_result6:
        print("Unit test 6 passed")
    else:
        print("Unit test 6 failed")
# Run the unit tests
test_calculate_statistics()