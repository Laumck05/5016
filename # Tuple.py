# Tuple.py
#
# @ author: A. N. Other
# date: September 2016
 
bank_accounts = (("Joe", 33, "234 Great South Road", "022629107"),
                 ("Tama", 6000),
                 ("Suzanne", 21025, "45 Green Lane"),
                 ("Anihera", -75),
                 ("Sam", 543, "5 Long Road", "0274634934"))
                 
 
print("The number of bank accounts is ", len(bank_accounts))
 
# showing names and balances
for i in bank_accounts:
    print("\nThe name is ", i[0], " and the balance is $", i[1])
 
# showing only names with addresses
for i in bank_accounts:
    if len(i)>2:
        print("\nThe name is ", i[0], " and the address is ", i[2])
        
# showing only names with phone numbers
for i in bank_accounts:
    if len(i)>3:
        print("\nThe name is ", i[0], " and the phone number is ", i[3])        