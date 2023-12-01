with open('input') as f:
    lines = f.readlines()

letter_to_number = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six" : 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
dict_list = []
number_list = []
for line in lines:
    letter_dict = {}
    for letter in letter_to_number.keys():
        first_hit= line.find(letter)
        last_hit = line.rfind(letter)
        if first_hit == -1:
            continue
        letter_dict[first_hit] = letter_to_number[letter]
        letter_dict[last_hit] = letter_to_number[letter]
    for i in range(10):
        if str(i) in line:
            letter_dict[line.find(str(i))] = i
            letter_dict[line.rfind(str(i))] = i
    first_hit = min(letter_dict.keys())
    last_hit = max(letter_dict.keys())
    dict_list.append(letter_dict)
    number_list.append(letter_dict[first_hit] * 10 + letter_dict[last_hit])


print(sum(number_list))