#sets

#sets are mutable add, remove, edit
# sets do not allow duplicates
# sets can store any types, dynamically resize
# sets do not keep the order of the elements inside of them
# sets does not maintain the insertion order of elements inside of them

wvu_employees = {"Adam", "Richard", " Siera", " Rayn"}
wvu_employees.add("Steven")

print(wvu_employees) # Error. cannot get by index print(wvu_employees[2])
wvu_employees.add("Steven")
wvu_employees.add("Steven")
for employee in wvu_employees:
    print(employee)

# it can ignore duplicates
names = set(["tim", " jhon", "tim", "bill"])
print(names)

# to check one element
print("Adam" in wvu_employees)
