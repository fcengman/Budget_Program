import numpy as np
import pandas as pd
import datetime as dt

path = "C:\\Users\\f-eng\\OneDrive\\Documents\\Python\\Projects\\Budget_Program\\"

data = pd.read_excel(
    path + "Accounting_2020.xlsx", engine="openpyxl")

columns = ["Date", "Day", "Month", "Year", "Item", "Debit",
           "Credit", "Category", "SubCategory", "Breakdown"]

credit = data[data.CREDIT.notnull()]
debit = data[data.DEBIT.notnull()]
freya_income = credit[credit.CATEGORY == "Freya"]
madalene_income = credit[credit.CATEGORY == "Madalene"]
# print(freya_income.to_string())
freya_income_total = freya_income['CREDIT'].sum()
freya_income_average = freya_income_total/12
madalene_income_total = madalene_income['CREDIT'].sum()
madalene_income_average = madalene_income_total/12


def print_stats(income, average):
    print("Yearly Income: {0:.2f}".format(income))
    print("Monthly Income Average: {0:.2f}".format(average))


print_stats(freya_income_total, freya_income_average)
print_stats(madalene_income_total, madalene_income_average)
print(madalene_income_total)
