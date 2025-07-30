import pandas as pd


data = { "Date": [ "2024-01-05", "2024-01-07", "2024-01-10", "2024-01-15", "2024-02-01", "2024-02-08", "2024-02-12", "2024-02-20" ],
         "Type": ["Income", "Expense", "Expense", "Income", "Income", "Expense", "Expense", "Expense"], "Category": ["Salary", "Groceries", "Utilities", "Freelance", "Salary", "Rent", "Entertainment", "Groceries"],
         "Amount": [4000, -150, -90, 500, 4000, -1200, -200, -160] }

df=pd.DataFrame(data)
print(df)
"""  #ex1
print("\n")
#tranzactii de tip expense
print(df[df["Type"]=="Expense"])

#ex suma totala income
print("\n")

print(df[df["Type"]=="Income"]["Amount"].sum())


#suma totala a cheltuielilor
print("\n")

print(df[df["Type"]=="Expense"]["Amount"].sum())
"""
"""
#ex 2
l=[1,2,3]
suma=np.cumsum(l)

print(suma[-1])

print(df["Amount"])

#df.insert(len(df),"Balance")

df["Balance"]=df["Amount"].cumsum()

print(df)

"""
"""
#niv2ex2 -suma groupata dupa type

print(df.groupby(["Type"])["Amount"].sum())


#niv2ex3 -grupeaza dupa categorie si face med de suma
print(df.groupby(["Category"])["Amount"].sum().mean())

#niv2e4 -sortare desc dupa suma
print(df.sort_values("Amount",ascending=False))

#niv2 e5 nou df cu amount >300 abs

df_nou = df[abs(df["Amount"]) > 300]
print(df_nou)


"""

#niv 3
#1 cheltuieli lunare totale

"""
df["Date"]=pd.to_datetime(df["Date"])
df["luna"]=df["Date"].dt.month
print(df)
#print(df.groupby(["luna"])[df["Type"]=="Expense"]["Amount"].sum())
print(df[df["Type"]=="Expense"].groupby(["luna"])["Amount"].sum())

"""
#2 coloana cu abs amount


df["AmAbs"]=abs(df["Amount"])

print(df)
print(df.sort_values("AmAbs"))

# 4 ,procent
total_expenses=df[df["Type"]=="Expense"]["Amount"].sum()
print(total_expenses)

df["PROCENT"]=abs(df["Amount"])*100/abs(total_expenses)


print(df[df["Type"]=="Expense"].groupby(["Category"])["PROCENT"].sum())