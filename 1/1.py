with open('input') as f:
    lines = f.readlines()

number_list = []
for line in lines:
    first_number = None
    last_number = None
    for character in line:
        try:
            number = int(character)
            if first_number is None:
                first_number = number
            else:
                last_number = number
        except ValueError:
            pass
    if last_number is None:
        last_number = first_number
    number_list.append(first_number * 10 + last_number)

print(sum(number_list))