first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

fs = len(first_strings)
first_result = [len(fs) for fs in first_strings if len(fs) >= 5]

fs1 = len(first_strings)
ss = len(second_strings)
second_result = [(fs1,ss) for fs1 in first_strings for ss in second_strings if len(fs1) == len(ss)]

tr = first_strings + second_strings
third_result = {i: len(i) for i in tr if len(i) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)