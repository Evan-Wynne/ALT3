print('------------------------------------------------------')
print('Welcome to the Stock intrinsic value calculation model')
print('------------------------------------------------------')
print('Please find all of the information about yourt chosen stock from the following sources: \nYahoo Finance, MarketWatch, Morningstar, etc.')
company = input('Enter the name of the company: ')


def calculate_intrinsic_value(eps, bvps, dy, fcf, discount_rate):
    # Forecast period
    forecast_period = 5
    
    # Terminal growth rate (perpetual growth rate)
    terminal_growth_rate = 0.03
    
    # Discounted Cash Flow calculation
    present_value_cf = sum([fcf / ((1 + discount_rate) ** year) for year in range(1, forecast_period + 1)])
    
    # Terminal value
    terminal_value = (fcf * (1 + terminal_growth_rate)) / (discount_rate - terminal_growth_rate)
    present_value_tv = terminal_value / ((1 + discount_rate) ** forecast_period)
    
    # Total present value
    total_present_value = present_value_cf + present_value_tv
    
    # Intrinsic value calculation
    intrinsic_value = (eps + bvps + dy + total_present_value) / 4
    
    return intrinsic_value

# Example usage
current_price = float(input(f'Current price of {company} stock: '))  
eps = float(input(f'Earnings per share(EPS) of {company} today: ')) # Example earnings per share
#Book value per share calculation
total_equity = float(input(f'Total equity of {company} today: '))  # Example total equity
shares_outstanding = float(input(f'Shares outstanding of {company} today: '))  # Example shares outstanding
bvps = total_equity / shares_outstanding  # Example book value per share
#dividend yield
dividend_yield = float(input(f'Dividend yield of {company} today(%): '))  # Example dividend yield
if dividend_yield not in range(0, 101):
    print('Please enter a valid dividend yield')
    dividend_yield = float(input(f'Dividend yield of {company} today(%): '))
dy = dividend_yield / 100
#calculating free cash flow rate
#operating cash flow
operating_cash_flow = float(input(f'Operating cash flow of {company} today: $'))  # Example operating cash flow
#capital expenditure
capital_expenditure = float(input(f'Capital expenditure of {company} today: $'))  # Example capital expenditure
fcf = operating_cash_flow - capital_expenditure  # Example free cash flow

#Calculating the dicount rate
print("Please navigate to your company's balance sheet, found on Yahoo Finace, Mornigstar, Finvizz etc, to find the following information")
#step 1: cost of equity - CAPM model
risk_free_rate = float(input(f'Risk-free rate of 10-year treasury - in country of the stock exchange where {company} is listed(%): '))  # Example risk-free rate
market_return = 0.10  # Example market return
beta = float(input(f'Beta of {company} today: '))  # Example beta
cost_of_equity = risk_free_rate + beta * (market_return - risk_free_rate)
#step 2: cost of debt
interest_expense = float(input(f'Interest expense of {company} today(The interest rate they pay on their debt): $'))  # Example interest expense
total_debt = float(input(f'Total debt of {company} today: $'))  # Example total debt
cost_of_debt = interest_expense / total_debt
#step 3: cost of capital
tax_rate = float(input(f'Please enter the Corporate Tax rate that {company} pay(%): '))  # Example tax rate
debt_equity_ratio = total_debt / total_equity  # Example debt-equity ratio
cost_of_capital = (cost_of_equity * (1 - tax_rate) * (1 - debt_equity_ratio)) + (cost_of_debt * debt_equity_ratio)
discount_rate = cost_of_capital
# Print the discount rate
print(f"Discount Rate: {discount_rate}")
# Print the intrinsic value of the stock
print(f"Intrinsic Value of the Stock: ${calculate_intrinsic_value(eps, bvps, dy, fcf, discount_rate)}")
# Print the difference between intrinsic value and current price
print(f"Difference between intrinsic value and current price: ${calculate_intrinsic_value(eps, bvps, dy, fcf, discount_rate) - current_price}")
# Print the potential return
print(f"Potential return: {((calculate_intrinsic_value(eps, bvps, dy, fcf, discount_rate) - current_price) / current_price) * 100}%")
# Print the decision to buy or sell
if calculate_intrinsic_value(eps, bvps, dy, fcf, discount_rate) > current_price:
    print(f"Buy {company} stock")
else:
    print(f"Sell {company} stock")

