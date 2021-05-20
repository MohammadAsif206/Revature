# A lot of times you want to generate a list based of a range or another list
# A list comprehension is a really compact syntax

nums = [1,2,-5,6,-6,10,12,-13]
negs = []

for n in nums:
    if n < 0:
        negs.append(n)
print(negs)

# num2 = [element for element in iterable if boolea_condition]
nums2 = [n*-1 +10 for n in nums if n<0]
print(nums2)

#this is doing the same as nums2 above
num2 = []
for in nums:
    if n < 0:
      nums.append(n*-1)

names = ["tim", " Adam", "steven"]
#[map(x) for iterable if filterable]
super_names = ["super"+name for name in names]
print(super_names)