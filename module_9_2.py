first_string = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_string if len(x) > 5]
print(first_result)

second_result = [(x, y) for x in first_string for y in second_strings if len(x) == len(y)]
print(second_result)

first_second_strings = first_string + second_strings
third_result = {x: len(x) for x in first_second_strings if len(x) % 2 == 0}
print(third_result)
