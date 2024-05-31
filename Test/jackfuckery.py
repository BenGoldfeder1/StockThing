import yfinance as yf
import pandas as pd
import numpy as np

def get_financial_data(ticker):
    stock = yf.Ticker(ticker)
    financials = stock.financials
    cashflow = stock.cashflow
    return financials, cashflow

def dcf_model(ticker, growth_rate, terminal_value, discount_rate=0.10):
    financials, cashflow = get_financial_data(ticker)
    
    # Extracting relevant financial data
    revenue = financials.loc['Total Revenue']
    free_cash_flow = cashflow.loc['Free Cash Flow']
    
    # Assuming the latest free cash flow as the base
    latest_fcf = free_cash_flow.iloc[0]
    
    # Projecting future free cash flows
    projected_fcfs = []
    for i in range(1, 6):
        projected_fcfs.append(latest_fcf * ((1 + growth_rate) ** i))
    
    # Calculating the present value of projected free cash flows
    discounted_fcfs = [fcf / ((1 + discount_rate) ** i) for i, fcf in enumerate(projected_fcfs, start=1)]
    
    # Calculating the present value of terminal value
    terminal_value_pv = terminal_value / ((1 + discount_rate) ** 5)
    
    # Total DCF value
    total_value = sum(discounted_fcfs) + terminal_value_pv
    
    return total_value

def main():
    ticker = input("Enter the stock ticker: ")
    growth_rate = float(input("Enter the annual growth rate (as a decimal): "))
    terminal_value = float(input("Enter the terminal value: "))
    
    dcf_value = dcf_model(ticker, growth_rate, terminal_value)
    print(f"The projected DCF value for {ticker} is: ${dcf_value:.2f}")

if __name__ == "__main__":
    main()
