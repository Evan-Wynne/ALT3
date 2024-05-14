

import random
from tqdm import tqdm
import statistics
import numpy as np
import matplotlib.pyplot as plt

#simulation function that takes in the following parameters:
def simulation(initial_investment, monthly_investment, annual_return_mean, annual_return_stddev, num_years, num_simulations):
    #emptying list to store the investment values for each simulation
    investment_values = []

    # Running the simulation for the specified number of simulations
    for _ in tqdm(range(num_simulations), desc="Simulating"):
        # Setting the initial investment value for each simulation
        investment = initial_investment
        # Iterating over each year in the simulation
        for _ in range(num_years):
            # Generating a random annual return value based on the mean and standard deviation
            annual_return = random.gauss(annual_return_mean, annual_return_stddev)
            # Calculating the monthly return based on the annual return
            monthly_return = (1 + annual_return)**(1/12) - 1
            # Iterating over each month in the year
            for _ in range(12):
                # Adding the monthly investment amount to the investment value
                investment += monthly_investment
                # Calculating the new investment value based on the monthly return
                investment *= 1 + monthly_return
        # Appending the final investment value to the list of investment values
        investment_values.append(investment)
    # Return the list of investment values
    return investment_values

def calculate_statistics(investment_values, initial_investment, monthly_investment, num_years):
    # Calculating the statistics of the investment values
    median_investment = statistics.median(sorted(investment_values, key=abs))
    average_investment = sum(investment_values) / len(investment_values)
    min_investment = min(investment_values)
    max_investment = max(investment_values)
    #calculating the standard deviation of the investment values
    std_dev_investment = statistics.stdev(investment_values)
    total_investment = initial_investment + monthly_investment * 12 * num_years
    #returning the calculated statistics
    return median_investment, average_investment, min_investment, max_investment, std_dev_investment, total_investment


# USER INPUTS section - NICE UI
print('-----------------------------------------------------')
print("Welcome to the best index fund investment simulator out there!" )
print("This simulator will run 100,000 simulations to predict the value of your investment after a certain number of years.")
print('This model assumes you will invest an initial amount and a fixed amount monthly for a certain number of years.')
print("Please enter the following information to get started: ")
print('-----------------------------------------------------')
#number of years being invested for
num_years = input("Enter the number of years you plan to invest monthly for: ")
#catching errors in user input

try:
    num_years = int(num_years)
    if num_years < 0:
        print("Number of years cannot be negative - please try again with a positive value")
        exit()
except ValueError:
    print("Number of years must be an integer - please try again with a whole number")
    exit()

initial_investment = float(input("Your initial investment($)\n- *Remember: You will be investing monthly after this\nEnter: "))
#catching errors in user input - this repeats for all inputs!!!!!!!
if initial_investment < 0:
    print("Initial investment cannot be negative  -  please try again with a positive value")
    exit()
monthly_investment = float(input("Enter the recurring monthly investment amount($): "))
if monthly_investment < 0:
    print("Monthly investment cannot be negative  -  please try again with a positive value")
    exit()
annual_return_mean = float(input("Enter your expected mean annual return(%)\n- This is the average percentage change in the value of your investments in a year\nEnter: "))
if annual_return_mean < 0:
    print("Mean annual return cannot be negative  -  please try again with a positive value")
    exit()
annual_return_mean /= 100

annual_return_stddev = float(input("Enter the standard deviation of annual return\n(this represents the expected variability around the mean return you entered earlier, encompassing about 68.2% of the possible outcomes): "))
if annual_return_stddev < 0:
    print("Standard deviation of annual return cannot be negative  -  please try again with a positive value")
    exit()
annual_return_stddev /= 100
           # Number of years for simulation
num_simulations = 100000      # Number of simulations

investment_values = simulation(initial_investment, monthly_investment, annual_return_mean, annual_return_stddev, num_years, num_simulations)

# Calculate statistics
median_investment, average_investment, min_investment, max_investment, std_dev_investment, total_investment = calculate_statistics(investment_values, initial_investment, monthly_investment, num_years)

# Print the results
#your inputs
print(f"\nSimulation Inputs: ")
print(f"Number of Years: {num_years}")
print(f"Initial Investment: ${initial_investment:,.2f}")
print(f"Monthly Investment: ${monthly_investment:,.2f}")
print(f"Total Investment: ${total_investment:,.2f}")
print("-----------------------------------------------------")
print(f"Average Value of you investment: ${average_investment:,.2f}")
print(f"Median Value of you investment: ${median_investment:,.2f}")
print("*Note the median value is usually lower than the average value due to the presence of outliers")
print("-----------------------------------------------------")
print(f"Minimum Value of you investment (Worst Case): ${min_investment:,.2f}")
print(f"Maximum Value of you investment (Best Case): ${max_investment:,.2f}")
print("-----------------------------------------------------")
print(f"Standard Deviation of Investment Values(34% on either side of mean - labelled on graph with green dotted lines): ${std_dev_investment:,.2f}")
print(f"Probability of Losing Money: {sum(1 for investment in investment_values if investment < total_investment) / num_simulations * 100:.2f}%")

#total return - percent and dollar amount
print(f"Mean ROI(Return on Investment): {((average_investment - total_investment) / total_investment) * 100:.2f}%")
print(f"Mean Profit: ${average_investment - total_investment:,.2f}")

# Create a graph of the standard deviation of final returns
plt.hist(investment_values, bins=30, edgecolor='black')
plt.xlabel('Final Investment Value ($)')
plt.ylabel('Frequency')
plt.title('Distribution of Final Investment Values')

# Add a trend line for standard deviation
std_dev = np.std(investment_values)
mean = np.mean(investment_values)
plt.axvline(mean, color='r', linestyle='--', label='Mean')
plt.axvline(mean + std_dev, color='g', linestyle='--', label='Mean + Std Dev')
table = []  # Define the table variable

plt.axvline(mean - std_dev, color='g', linestyle='--', label='Mean - Std Dev')
plt.legend()
plt.show()


