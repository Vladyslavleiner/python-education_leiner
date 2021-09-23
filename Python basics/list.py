numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]
for i in range(1,4):
    numbers.append(i)
s = "hello world"
for i in s.split(" "):
    strings.append(i)


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)