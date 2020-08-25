# table1: 1500, 3人
# table2: 2000, 3人
# table3: 3647, 4人

total_amount = 1500
number_of_people = 3

amount_per_person = total_amount // number_of_people

print(f'一人あたり:{amount_per_person}円, 端数:{total_amount % number_of_people}円')


def dutch_treat(total_amount, number_of_people):
    amount_per_person = total_amount // number_of_people
    fraction = total_amount % number_of_people
    return f"一人あたりの金額:{amount_per_person}円\n端数:{fraction}円"


print(dutch_treat(1500, 3))
print(dutch_treat(2000, 3))
print(dutch_treat(3647, 4))


total_amount = int(input('合計金額(¥)>>>'))
number_of_people = int(input('支払い人数(人)>>>'))

r = dutch_treat(total_amount, number_of_people)
print(r)
