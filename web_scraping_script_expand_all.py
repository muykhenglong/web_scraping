#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 17:26:23 2024

Getting financial data from yahoo finance using Selenium

@author: Muykheng Long
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


income_statement_dir = {}
balance_sheet_dir = {}
cash_flow_st_dir = {}

tickers = {"AAPL",'META','CSCO','INFY.NS','3988.HK'} 

# Extract Income Statement
for ticker in tickers:
    url = f"https://finance.yahoo.com/quote/{ticker}/financials"
    
    driver = webdriver.Safari()
    driver.get(url)
    driver.implicitly_wait(2)
    
    buttons = driver.find_elements(By.XPATH,"//article[@class='svelte-k66eqn']//button")
        
    for button in buttons:
        if button.accessible_name in ['']:
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable(button)).click()
        else:
            pass
    
    # Convert HTML data
    table = driver.find_element(By.XPATH,"//div[@class='table svelte-1pgoo1f']").text
    table_text = table.strip().split('   ')
    
    heading = {} # Heading of the financial statement
    income_statement = {} # To store values of the financial statement
    
    no_period = len(table_text[0].split(' '))
        
    heading[' '.join(table_text[0].split(' ')[:-(no_period-1)])] = table_text[0].split(' ')[-(no_period-1):]
    for row in table_text[1:]:
        income_statement[' '.join(row.split(' ')[:-(no_period-1)])] = row.split(' ')[-(no_period-1):]
    
    temp = pd.DataFrame(income_statement).transpose() # Temporary dataframe to store financial statement
    temp.columns = heading['Breakdown']
    
    income_statement_dir[ticker] = temp
    driver.quit()

# Extract Balance Sheet
for ticker in tickers:
    url = f"https://finance.yahoo.com/quote/{ticker}/balance-sheet"
    
    driver = webdriver.Safari()
    driver.get(url)
    driver.implicitly_wait(2)
    
    buttons = driver.find_elements(By.XPATH,"//article[@class='svelte-k66eqn']//button")
        
    for button in buttons:
        if button.accessible_name in ['']:
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable(button)).click()
        else:
            pass

    # Convert HTML data
    table = driver.find_element(By.XPATH,"//div[@class='table svelte-1pgoo1f']").text
    table_text = table.strip().split('   ')
    
    heading = {} # Heading of the financial statement
    balance_sheet = {} # To store values of the financial statement
    
    no_period = len(table_text[0].split(' '))
        
    heading[' '.join(table_text[0].split(' ')[:-(no_period-1)])] = table_text[0].split(' ')[-(no_period-1):]
    for row in table_text[1:]:
        balance_sheet[' '.join(row.split(' ')[:-(no_period-1)])] = row.split(' ')[-(no_period-1):]
    
    temp = pd.DataFrame(balance_sheet).transpose() # Temporary dataframe to store financial statement
    temp.columns = heading['Breakdown']
    
    balance_sheet_dir[ticker] = temp
    driver.quit()


# Extract Cash Flow Statement
for ticker in tickers:
    url = f"https://finance.yahoo.com/quote/{ticker}/cash-flow"
    
    driver = webdriver.Safari()
    driver.get(url)
    driver.implicitly_wait(2)
    
    buttons = driver.find_elements(By.XPATH,"//article[@class='svelte-k66eqn']//button")
        
    for button in buttons:
        if button.accessible_name in ['']:
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable(button)).click()
        else:
            pass
    
    # Convert HTML data
    table = driver.find_element(By.XPATH,"//div[@class='table svelte-1pgoo1f']").text
    table_text = table.strip().split('   ')
    
    heading = {} # Heading of the financial statement
    cash_flow_st = {} # To store values of the financial statement
    
    no_period = len(table_text[0].split(' '))
        
    heading[' '.join(table_text[0].split(' ')[:-(no_period-1)])] = table_text[0].split(' ')[-(no_period-1):]
    for row in table_text[1:]:
        cash_flow_st[' '.join(row.split(' ')[:-(no_period-1)])] = row.split(' ')[-(no_period-1):]
    
    temp = pd.DataFrame(cash_flow_st).transpose() # Temporary dataframe to store financial statement
    temp.columns = heading['Breakdown']
    
    cash_flow_st_dir[ticker] = temp
    driver.quit()

# Remove comma and -- and convert to numerical data   
for ticker in tickers:
    for col in income_statement_dir[ticker].columns:
        income_statement_dir[ticker][col] = income_statement_dir[ticker][col].str.replace('--','')
        income_statement_dir[ticker][col] = income_statement_dir[ticker][col].str.replace(',','')
        income_statement_dir[ticker][col] = pd.to_numeric(income_statement_dir[ticker][col],errors='coerce')
for ticker in tickers:
    for col in balance_sheet_dir[ticker].columns:
        balance_sheet_dir[ticker][col] = balance_sheet_dir[ticker][col].str.replace('--','')
        balance_sheet_dir[ticker][col] = balance_sheet_dir[ticker][col].str.replace(',','')
        balance_sheet_dir[ticker][col] = pd.to_numeric(balance_sheet_dir[ticker][col],errors='coerce')
for ticker in tickers:
    for col in cash_flow_st_dir[ticker].columns:
        cash_flow_st_dir[ticker][col] = cash_flow_st_dir[ticker][col].str.replace('--','')
        cash_flow_st_dir[ticker][col] = cash_flow_st_dir[ticker][col].str.replace(',','')
        cash_flow_st_dir[ticker][col] = pd.to_numeric(cash_flow_st_dir[ticker][col],errors='coerce')
