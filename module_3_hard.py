data_structure = [

[1, 2, 3],

{'a': 4, 'b': 5},

(6, {'cube': 7, 'drum': 8}),

"Hello",

((), [{(2, 'Urban', ('Urban2', 35))}])

]
def calculate_structure_sum(data_structure):
    sum = 0
    if isinstance(data_structure, list):
        for i in data_structure:
            sum += calculate_structure_sum(i)

    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            sum += calculate_structure_sum(key)
            sum += calculate_structure_sum(value)

    elif isinstance(data_structure, tuple):
        for i in data_structure:
            sum += calculate_structure_sum(i)

    elif isinstance(data_structure, str):
        sum = len(data_structure)

    elif isinstance(data_structure, int):
        sum += data_structure

    elif isinstance(data_structure, set):
        for i in data_structure:
            sum += calculate_structure_sum(i)
    return sum
result = calculate_structure_sum(data_structure)
print(result)
# print(type(data_structure[0]))
# print(type(data_structure[1]))
# print(type(data_structure[2]))
# print(type(data_structure[3]))
# print(type(data_structure[4]))