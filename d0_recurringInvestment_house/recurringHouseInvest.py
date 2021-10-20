#!/usr/bin/env python
# coding: utf-8

# # Recurring Housing Investment Procedure

from d0_recurringInvestmentArt import logo

print(logo)


# ## Part 1 - Mortgage and Refinance Calculators

# ### 1. House appreciation calculator
# This function is aiming to calculate house price raising by user giving initial house price, years, annual interest
# 
# 1. function name: *house_appreciation*
# 2. function arguments: 
#     - a: _initial house price_
#     -  i: _annual interest rate, float number with decimal_
#     -  n: _number of years_

# In[1]:


def house_appreciation(a=1000000, i=0.07, n=2):
    return a * (1 + i) ** n


# ###  2. Monthly Install Payment calculator
# This function is aiming to calculate monthly install payment by user giving mortgage amount,
# annual interest rate and amortization years
# ---
# 1. function name: *monthly_payment*
# 2. function arguments: 
#     -  m: _mortgage amount_
#     -  i: _annual interest rate, float number with decimal_
#     -  n: _amortization years_


def monthly_payment(m, i, n):
    ani = (1 - (1 + i / 12) ** (-n * 12)) / (i / 12)
    return m / ani, ani


# ###  3. Principal Balance calculator
# **This function is aiming to calculate pricipal balance amount at the end of months by user giving number of month, initial mortgage amount and anuual interest rate**
# 
# ---
# 1. function name: *ending_balance*
# 2. function arguments: 
#     -  m: _mortgage amount_
#     -  i: _annual interest rate, float number with decimal_
#     -  n: _user defined number of months_
#     -  p: monthly install payment


def ending_balance(m, i, n, p):
    sni = (((1 + i / 12) ** (n * 12)) - 1) / (i / 12)
    return m * (1 + i / 12) ** (n * 12) - p * sni


# ###  4. Refinance Amount calculator
# **This function is aiming to how many fund you can refinance from existing property by user giving house price, proportion of LTV (Loan to Value) and mortgage balance amount**
# 
# ---
# 1. function name: *refinance_amt*
# 2. function arguments: 
#     -  s: _house price_
#     -  p: _LTV proportion_
#     -  b: _mortgage balance on that property_

# In[4]:


def refinance_amt(s, p, b):
    return s * p - b


# ## Part 2 - Investment 1 - Year 0
# ### Property 1 - Current 1st Primary Residence Finance Situation
# Property 1 market price at beginning
print("//////////////////////////////Investment 1/////////////////////////////////////////////////////////\n \n")
print("+++++++++++++++++++Let's see your property 1 financial situation at the beginning+++++++++++++++++++++\n")
p1_price_0 = float(input("Please input your current house price: "))
print(f"${p1_price_0:.2f}")
max_ltv = float(input("What is the maximum refinance proportion (like 0.7, 0.8): "))
print(f"{max_ltv: 1.2%}")
# Property 1 mortgage balance at beginning
p1_loan_bal_0 = float(input("What is your current mortgage balance: "))
print(f"${p1_loan_bal_0:.2f}")

# #### Property 1 Refinance Amount
p1_refin_0 = refinance_amt(p1_price_0, max_ltv, p1_loan_bal_0)
# property 1 consolidate loan balance (mortgage + refinance)
p1_loan_bal_0 = p1_loan_bal_0 + p1_refin_0
# property 1 loan monthly payment at the beginning
print("you need to provide input for calculation at the beginning year \n")
r_0 = float(input("What is your annual interest rate for your refinance and mortgage at the beginning: "))
print(f"{r_0:1.2%}")
amort_0 = int(input("What is amortization years for your refinance and mortgage at the beginning: "))
print(f"{amort_0}")
p1_avg_rental = float(input("What is your 1st house average rental income: "))
print(f"${p1_avg_rental} \n")
p1_payment_0 = monthly_payment(p1_loan_bal_0, r_0, amort_0)[0]
print("========================================================================================\n")
print(f"Based on your input, your 1st house at the beginning has \n \n"
      f"market price: ${p1_price_0:.2f} \n \n"
      f"maximum refinance LTV is {max_ltv:2.0%} \n \n"
      f"refinance amount is ${p1_refin_0:.2f} \n \n"
      f"new consolidate loan balance including original and refinance is ${p1_loan_bal_0} \n \n"
      f"monthly payment is ${p1_payment_0:.2f}")
print("=========================================================================================\n")

# #### Mortgage amount evaluation at the beginning
print(f"Let's estimate your mortgage capability at the beginning")
income_family = float(input("What is your household annual income: "))
print(f"${income_family:.2f}")
cashflow_month = float(input("What is your monthly rental cash flow: "))
print(f"${cashflow_month:.2f}")
p1_mortgage_0 = income_family * 5 + (cashflow_month * 12) * 0.8 - p1_loan_bal_0
print(f"Your evaluated mortgage limit is ${p1_mortgage_0: .2f}\n")
# ### Property 2 - Your 2nd Purchased House
print("+++++++++++++++++++Let's see your property 2 purchase situation at the beginning+++++++++++++++++++++\n")
p_purc_fee = float(input("How much closing fee (like layer, land transfer tax etc) for your investment: "))
print(f"${p_purc_fee:.2f}")
avail_downpay = p1_refin_0 - p_purc_fee
downpay_per = float(input("how many percentage (at least 0.2) you want to pay for down payment: "))
print(f"{downpay_per:1.2%} \n")
p2_price_0 = avail_downpay / downpay_per
p2_loan_bal_0 = p2_price_0 * (1 - downpay_per)
# property 2 monthly payment at the beginning
# print("your need to provide input for calculating property 2 payment at the beginning")
# amort = int(input("What is property 2 amortization years at the beginning: "))
# r = float(input("What is your property 2 annual interest rate at the beginning: "))
p2_payment_0 = monthly_payment(p2_loan_bal_0, r_0, amort_0)[0]
print("=================================================================================================\n")
print(f"Based on your inputs, your 2nd house at beginning has \n"
      f"proposal price: ${p2_price_0: .2f} \n"
      f"your down payment: ${p2_price_0 - p2_loan_bal_0} \n"
      f"down payment percentage: {downpay_per: 2.0%} \n"
      f"mortgage at purchase date is ${p2_loan_bal_0: .2f} \n"
      f"monthly payment is ${p2_payment_0:.2f}")
print("===================================================================================================\n")

print("/////////////////////////////Investment 2/////////////////////////////////////////////////////////\n \n")

# ## Part 3 - Investment 2 - n1 years After Investment 1
# ### Property 1 Financial Situation
# #### Property 1 Value Appreciation n1 years after investment 1refinance
n1 = int(input("how many year you want to buy next house?: "))
print(f"{n1}")
i = float(input("What is your property value appreciation percent? (like 0.05, 0.06): "))
print(f"{i:1.2%}")
print(f"+++++++++++++++++++Let's see your property 1 financial situation {n1} years after investment 1+++++++++++++\n")
p1_price_1 = house_appreciation(p1_price_0, i, n1)
# #### Property 1 mortgage balance after n1 years
p1_loan_bal_1 = ending_balance(p1_loan_bal_0, r_0, n1, p1_payment_0)
# p1_loan_bal_1 = p1_loan_bal_1*(1+r/12)**(n*12) - p1_payment_1 * ((((1+r/12)**(n*12))-1)/(r/12))
# #### Property 1 refinance amount after n1 years
print(f"you need to provide input for calculation {n1} years after your investment 1 \n")
r_1 = float(input(f"What is your annual interest rate {n1} years after your investment 1: "))
print(f"{r_1:1.2%} \n")
amort_1 = int(input("What is amortization years: "))
print(f"{amort_1}")
p1_refin_1 = refinance_amt(p1_price_1, max_ltv, p1_loan_bal_1)
# p1_loan_bal_1 = p1_loan_bal_1 + p1_refin_1
# p1_payment_1 = monthly_payment(p1_loan_bal_1, r, amort)[0]
print("=============================================================================================================\n")
print(f"Based on your inputs, your 1st house after {n1} years your investment 1 has \n"
      f"market price: ${p1_price_1: .2f} \n"
      f"refinance amount is ${p1_refin_1: .2f} \n"
      f"mortgage balance: {p1_loan_bal_1: .2f} \n"
      # f"new loan monthly payment is ${p1_payment_1: .2f} \n"
      # f"minimum downpay can buy house price is {p1_refin_1 / 0.2: .2f} \n"
      # f"minimum mortgage is {p1_refin_1 / 0.2 - p1_refin_1: .2f}")
      )
print("============================================================================================================\n")
# ### Property 2 Financial Situation
# #### Property 2 Value Appreciation
print(f"+++++++++++++++++++Let's see your property 2 financial situation {n1} years after investment 1+++++++++++++\n")
p2_price_1 = house_appreciation(p2_price_0, i, n1)
# #### Property 2 mortgage balance after n1 years
# Property 2 ending balance after n1 years
if p2_loan_bal_0 > 0:
    if_prepayback = input("Do you want to pay back loan in advanced every year 15% (y/n): ").lower()
    print(f"{if_prepayback}")
    if if_prepayback == 'y':
        p2_loan_bal_1 = ending_balance(p2_loan_bal_0, r_1, n1, p2_payment_0) - p2_loan_bal_0 * 0.15 * n1
    else:
        p2_loan_bal_1 = ending_balance(p2_loan_bal_0, r_1, n1, p2_payment_0)
else:
    p2_loan_bal_1 = 0
if p2_loan_bal_1 <= 0:
    p2_loan_bal_1 = 0
# #### Property 2 refinance amount after n1 years
p2_refin_1 = refinance_amt(p2_price_1, max_ltv, p2_loan_bal_1)
# p2_loan_bal_1 = p2_loan_bal_1 + p2_refin_1
# p2_payment_1 = monthly_payment(p2_loan_bal_1, r, amort)[0]
print(f"The 2nd house is primary then we don't take fund from it only estimate refinance amount")
print("=========================================================================================================\n")
print(f"Based on your inputs, your 2nd house after {n1} years your investment 1 has \n"
      f"market price: ${p2_price_1: .2f} \n"
      f"mortgage balance: {p2_loan_bal_1: .2f} \n"
      f"refinance amount is ${p2_refin_1: .2f} \n"
      )
print("==========================================================================================================\n")
# #### Mortgage amount evaluation after n1 years
print(f"Let's estimate your mortgage capability for property 3 on the {n1} years after your investment 1")
income_family = float(input("What is your household annual income: "))
print(f"${income_family:.2f}")
cashflow_month = float(input("What is your monthly rental cash flow: "))
print(f"${cashflow_month:.2f}")
p3_mortgage_1 = income_family * 5 + (cashflow_month * 12) * 0.8 - p2_loan_bal_1
print(f"Your evaluated mortgage limit is ${p3_mortgage_1: .2f}\n")

# ### Property 3 - Your 3rd purchased house after n1 years
# property 3 monthly payment
# print(f"you need to provide input for calculating property 3 mortgage monthly payment amount when you purchase")
# amort = int(input("What is property 3 amortization years: "))
# r = float(input("What is your property 3 annual interest rate: "))
print("The principal of maximum monthly payment must lower than rental income")
p3_avg_rental = float(input("What is property 3 average rental income: "))
print(f"${p3_avg_rental:.2f} \n")
p3_price_1 = p3_avg_rental * monthly_payment(0, r_1, amort_1)[1]
p3_downpay_1 = p3_price_1 * 0.2
p3_loan_bal_1 = p3_price_1 - p3_downpay_1
p3_payment_1 = monthly_payment(p3_loan_bal_1, r_1, amort_1)[0]
p1_loan_bal_1 = p1_loan_bal_1 + p3_downpay_1
p1_payment_1 = monthly_payment(p1_loan_bal_1, r_1, amort_1)[0]

print("########################################################################################## \n"
      f"Based on your inputs, your 3rd house on the purchase has \n"
      f"market price: ${p3_price_1: .2f} \n"
      f"your down payment from refinance is ${p3_downpay_1:.2f} \n"
      f"your mortgage is ${p3_loan_bal_1: .2f} \n"
      f"Your monthly payment is ${p3_payment_1: .2f} \n"
      f"Your property 1 new consolidate monthly payment is ${p1_payment_1: .2f} \n"
      "#############################################################################################\n")

# ## Part 4 - Investment 3 - n2 years After Investment 2
# ### Property 1 Financial Situation
# #### Property 1 value appreciation n2 years after investment 2
print("////////////////////////Investment 3/////////////////////////////////////////////////////////\n \n")
n2 = int(input("how many year you want to buy next house?: "))
print(f"{n2}")
i = float(input("What is your property value appreciation percent (like 0.05, 0.06): "))
print(f"{i:1.2%}")
print(f"+++++++++++++++++++Let's see your property 1 financial situation {n2} years after investment 2+++++++++++++\n")
p1_price_2 = house_appreciation(p1_price_1, i, n2)
# #### Property 1 mortgage balance n2 years after your investment 2
# Property 1 mortgage balance
p1_loan_bal_2 = ending_balance(p1_loan_bal_1, r_1, n2, p1_payment_1)
# #### Property 1 refinance amount n2 years after your investment 2
p1_refin_2 = refinance_amt(p1_price_2, max_ltv, p1_loan_bal_2)
# p1_loan_bal_2 = p1_loan_bal_2 + p1_refin_2
# Property 1 consolidate loan monthly payment amount
print(f"your need to provide input for calculation {n2} years after your investment 2")
r_2 = float(input(f"What is your annual interest rate {n2} years after your investment 2: "))
print(f"{r_2:1.2%}")
amort_2 = int(input("What is amortization years: "))
print(f"{amort_2} \n")
# p1_payment_2 = monthly_payment(p1_loan_bal_2, r, amort)[0]
print("=============================================================================================\n"
      f"Based on your inputs, your 1st house after {n2} years your investment 2 has \n"
      f"market price: ${p1_price_2: .2f} \n"
      f"refinance amount is ${p1_refin_2: .2f} \n"
      # f"new consolidation loan balance: {p1_loan_bal_2: .2f} \n"
      # f"monthly payment: ${p1_payment_2: .2f} \n"
      )
print("===============================================================================================\n")
# ### Property 2 Financial Situation
# #### Property 2 value appreciation n2 years after your investment 2
print(f"+++++++++++++++++++Let's see your property 2 financial situation {n2} years after investment 2+++++++++++++\n")
p2_price_2 = house_appreciation(p2_price_1, i, n2)
# #### Property 2 mortgage balance n2 years after your investment 2
if p2_loan_bal_1 > 0:
    if_prepayback = input("Do you want to pay back loan in advanced every year 15% (y/n): ").lower()
    print(f"{if_prepayback} \n")
    if if_prepayback == 'y':
        p2_loan_bal_2 = ending_balance(p2_loan_bal_1, r_1, n2, p2_payment_0) - p2_loan_bal_0 * 0.15 * n2
    else:
        p2_loan_bal_2 = ending_balance(p2_loan_bal_1, r_1, n2, p2_payment_0)
else:
    p2_loan_bal_2 = 0
if p2_loan_bal_2 <= 0:
    p2_loan_bal_2 = 0
# #### Property 2 refinance amount n2 years after your investment 2
p2_refin_2 = refinance_amt(p2_price_2, max_ltv, p2_loan_bal_2)
print("==================================================================================================\n")
print(f"Based on your inputs, your 2nd house after {n2} years your investment 2 has \n"
      f"market price: ${p2_price_2: .2f} \n"
      # f"monthly payment: ${p1_payment_2: .2f} \n"
      f"mortgage balance: {p2_loan_bal_2: .2f} \n"
      f"refinance amount is ${p2_refin_2: .2f} \n"
      )
print("==================================================================================================\n")
# ### Property 3 Financial Situation
# #### Property 3 value appreciation n2 years after investment 2
print(f"+++++++++++++++++++Let's see your property 3 financial situation {n2} years after investment 2+++++++++++++\n")
p3_price_2 = house_appreciation(p3_price_1, i, n2)
# #### Property 3 mortgage balance n years after your investment 2
p3_loan_bal_2 = ending_balance(p3_loan_bal_1, r_1, n2, p3_payment_1)
# #### Property 3 refinance amount n years after your investment 2
p3_refin_2 = refinance_amt(p3_price_2, max_ltv, p3_loan_bal_2)
# p3_loan_bal_2 = p3_loan_bal_2 + p3_refin_2
# p3_payment_2 = monthly_payment(p3_loan_bal_2, r, amort)[0]
print("===============================================================================================\n")
print(f"Based on your inputs, your 3rd house after {n2} years your investment 2 has \n"
      f"market price: ${p3_price_2: .2f} \n"
      f"refinance amount is ${p3_refin_2: .2f} \n"
      # f"new consolidate loan balance: {p3_loan_bal_2: .2f} \n"
      # f"monthly payment: ${p3_payment_2: .2f} \n"
      )
print("===============================================================================================\n")
# #### Mortgage amount evaluation after n2 years
print(f"Let's estimate your mortgage capability for property 4 on the {n2} years after your investment 2 \n")
income_family = float(input("What is your household annual income: "))
print(f"${income_family:.2f}")
cashflow_month = float(input("What is your monthly rental cash flow: "))
print(f"${cashflow_month:.2f}")
mortgage_2 = income_family * 5 + (cashflow_month * 12) * 0.8 - p2_loan_bal_2
print(f"Your evaluated mortgage limit is ${mortgage_2: .2f}")

# ### Property 4 your 4th purchased house n2 year after your investment 2
print("The principal of maximum monthly payment must lower than rental income")
p4_avg_rental = float(input("What is property 4 average rental income: "))
print(f"${p4_avg_rental:.2f} \n")
p4_price_2 = p4_avg_rental * monthly_payment(0, r_2, amort_2)[1]
p4_downpay_2 = p4_price_2 * 0.2
p4_avail_downpay_2 = p1_refin_2 + p3_refin_2
p4_loan_bal_2 = p4_price_2 - p4_downpay_2
# property 4 monthly payment
p4_payment_2 = monthly_payment(p4_loan_bal_2, r_2, amort_2)[0]
if p1_payment_1 > p1_avg_rental and p3_payment_1 > p3_avg_rental:
    raise ValueError(f"all your investment properties don't have cash flow, it's risky, stop investing!")
elif p1_payment_1 < p1_avg_rental and p3_payment_1 > p3_avg_rental:
    p1_loan_bal_2 = p1_loan_bal_2 + p4_downpay_2
elif p1_payment_1 > p1_avg_rental and p3_payment_1 < p3_avg_rental:
    p3_loan_bal_2 = p3_loan_bal_2 + p4_downpay_2
elif p1_payment_1 < p1_avg_rental and p3_payment_1 < p3_avg_rental:
    p4_dp_splitrate = (p1_avg_rental - p1_payment_1) / ((p3_avg_rental - p3_payment_1) +
                                                        p1_avg_rental - p1_payment_1)
    if p4_dp_splitrate > 1:
        p4_dp_splitrate = 1 / p4_dp_splitrate
    p1_loan_bal_2 = p1_loan_bal_2 + (p4_downpay_2 * p4_dp_splitrate)
    p3_loan_bal_2 = p3_loan_bal_2 + (p4_downpay_2 * (1 - p4_dp_splitrate))
else:
    p1_loan_bal_2 = p1_loan_bal_2 + (p4_downpay_2 * 0.5)
    p3_loan_bal_2 = p3_loan_bal_2 + (p4_downpay_2 * 0.5)
p1_payment_2 = monthly_payment(p1_loan_bal_2, r_2, amort_2)[0]
p3_payment_2 = monthly_payment(p3_loan_bal_2, r_2, amort_2)[0]
print("===============================================================================================\n")
print(f"Based on your inputs, your 4th house on the purchase has \n"
      f"market price: ${p4_price_2: .2f} \n"
      f"your down payment: ${p4_downpay_2: .2f} \n"
      f"your mortgage is ${p4_loan_bal_2: .2f} \n"
      f"Your monthly payment is ${p4_payment_2: .2f} \n"
      f"Your property 1 new consolidate payment is ${p1_payment_2:.2f} \n"
      f"Your Property 3 new consolidate payment is ${p3_payment_2:.2f} \n"
      )
print("=================================================================================================\n")

# ## Part 5 - Investment 4 - n3 years After Investment 3
# ### Property 1 Financial Situation
# #### Property 1 value appreciation n3 years after investment 3
print("//////////////////////////////Investment 4/////////////////////////////////////////////////////////\n \n")
n3 = int(input("how many year you want to buy next house? "))
print(f"{n3}")
i = float(input("What is your property value appreciation percent (like 0.05, 0.06): "))
print(f"{i:1.2%}")
print(f"+++++++++++++++++++Let's see your property 1 financial situation {n3} years after investment 3+++++++++++++\n")
print(f"you need to provide input for calculation {n3} years after your investment 3")
r_3 = float(input(f"What is your annual interest rate {n3} years after your investment 3: "))
print(f"{r_3:1.2%}")
amort_3 = int(input("What is amortization years: "))
print(f"{amort_3} \n")
p1_price_3 = house_appreciation(p1_price_2, i, n2)
# #### Property 1 mortgage balance n3 years after your investment 3
# Property 1 mortgage balance
p1_loan_bal_3 = ending_balance(p1_loan_bal_2, r_2, n3, p1_payment_2)
# #### Property 1 refinance amount n3 years after your investment 3
p1_refin_3 = refinance_amt(p1_price_3, max_ltv, p1_loan_bal_3)
print("===================================================================================================\n")
print(f"Based on your inputs, your 1st house after {n3} years your investment 3 has \n"
      f"market price: ${p1_price_3: .2f} \n"
      f"mortgage balance: {p1_loan_bal_3: .2f} \n"
      f"refinance amount is ${p1_refin_3: .2f} \n"
      )
print("====================================================================================================\n")

# ### Property 2 Financial Situation
# #### Property 2 value appreciation n3 years after your investment 3
print(f"+++++++++++++++++++Let's see your property 2 financial situation {n3} years after investment 3+++++++++++++\n")
p2_price_3 = house_appreciation(p2_price_2, i, n3)
# #### Property 2 mortgage balance n3 years after your investment 3
if p2_loan_bal_2 > 0:
    if_prepayback = input("Do you want to pay back loan in advanced every year 15% (y/n): ").lower()
    print(f"{if_prepayback} \n")
    if if_prepayback == 'y':
        p2_loan_bal_3 = ending_balance(p2_loan_bal_2, r_2, n3, p2_payment_0) - p2_loan_bal_0 * 0.15 * n3
    else:
        p2_loan_bal_3 = ending_balance(p2_loan_bal_2, r_2, n3, p2_payment_0)
else:
    p2_loan_bal_3 = 0
if p2_loan_bal_3 <= 0:
    p2_loan_bal_3 = 0
# #### Property 2 refinance amount n3 years after your investment 3
p2_refin_3 = refinance_amt(p2_price_3, max_ltv, p2_loan_bal_3)
print("===================================================================================================\n")
print(f"Based on your inputs, your 2nd house after {n3} years your investment 3 has \n"
      f"market price: ${p2_price_3: .2f} \n"
      f"mortgage balance: {p2_loan_bal_3: .2f} \n"
      f"refinance amount is ${p2_refin_3: .2f} \n"
      )
print("====================================================================================================\n")
# ### Property 3 Financial Situation
# #### Property 3 value appreciation n3 years after your investment 3
print(f"+++++++++++++++++++Let's see your property 3 financial situation {n3} years after investment 3+++++++++++++\n")
p3_price_3 = house_appreciation(p3_price_2, i, n3)
# #### Property 3 mortgage balance n3 years after you investment 3
p3_loan_bal_3 = ending_balance(p3_loan_bal_2, r_2, n3, p3_payment_2)
# #### Property 3 refinance amount n3 years after your investment 3
p3_refin_3 = refinance_amt(p3_price_3, max_ltv, p3_loan_bal_3)
print("===================================================================================================\n")
print(f"Based on your inputs, your 3rd house after {n3} years your investment 3 has \n"
      f"market price: ${p3_price_3: .2f} \n"
      f"mortgage balance: {p3_loan_bal_3: .2f} \n"
      f"refinance amount is ${p3_refin_3: .2f} \n"
      )
print("===================================================================================================\n")
# ### Property 4 Financial Situation
# #### Property 4 value appreciation n3 years after investment 3
print(f"+++++++++++++++++++Let's see your property 4 financial situation {n3} years after investment 3+++++++++++++\n")
p4_price_3 = house_appreciation(p4_price_2, i, n3)
# #### Property 4 mortgage balance n3 years after you investment 3
p4_loan_bal_3 = ending_balance(p4_loan_bal_2, r_2, n3, p4_payment_2)
# #### Property 4 refinance amount n3 years after your investment 3
p4_refin_3 = refinance_amt(p4_price_3, max_ltv, p4_loan_bal_3)
print("===================================================================================================\n")
print(f"Based on your inputs, your 4th house after {n3} years your investment 3 has \n"
      f"market price: ${p4_price_3: .2f} \n"
      f"mortgage balance: {p4_loan_bal_3: .2f} \n"
      f"refinance amount is ${p4_refin_3: .2f} \n"
      )
print("===================================================================================================\n")

print(f"Let's estimate your mortgage capability for property 5 {n3} years after your investment 3 \n")
income_family = float(input("What is your household annual income: "))
print(f"${income_family:.2f}")
cashflow_month = float(input("What is your monthly rental cashflow: "))
print(f"${cashflow_month:.2f}")
mortgage_3 = income_family * 5 + (cashflow_month * 12) * 0.8 - p2_loan_bal_3
print(f"Your evaluated mortgage limit is ${mortgage_2: .2f} \n")

# ### Property 5 your 5th purchased house n3 year after your investment 3
# print("The principal of maximum monthly payment must lower than rental income")
# p5_avg_rental = float(input("What is property 4 average rental income: "))
# p4_price_2 = p4_avg_rental * monthly_payment(0, r_2, amort_2)[1]
# p4_downpay_2 = p4_price_2 * 0.2
# p4_avail_downpay_2 = p1_refin_2 + p3_refin_2
# p4_loan_bal_2 = p4_price_2 - p4_downpay_2
# available downpayment
p5_avail_downpay_3 = p1_refin_3 + p2_refin_3 + p3_refin_3 + p4_refin_3
# Property 5 house price
print(f"according to the principle of mortgage, mortgage amount between 2 to 3 times household annual income"
      f"your income is ${income_family:.2f} and you have available down payment is ${p5_avail_downpay_3:.2f}")
income_times = int(input("how many times of your income do you want to become your mortgage: "))
print(f"{income_times} \n")
p5_price_3 = p5_avail_downpay_3 + income_family * income_times
# Property 5 mortgage
p5_loan_bal_3 = income_family * income_times
# property 5 monthly payment
p5_payment_3 = monthly_payment(p5_loan_bal_3, r_3, amort_3)[0]

print("===================================================================================================\n")
print(f"Based on your inputs, your 5th house on the purchase has \n"
      f"market price: ${p5_price_3: .2f} \n"
      f"your available down payment: ${p5_avail_downpay_3: .2f} \n"
      f"down payment percentage: {p5_avail_downpay_3 / p5_price_3: 2.0%} \n"
      f"your mortgage is ${p5_loan_bal_3: .2f} \n"
      f"Your monthly payment is ${p5_payment_3: .2f}")
print("===================================================================================================\n")
