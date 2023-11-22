# def make_list(number):
#     names = []
#     for item in number:
#         names.append(input('Enter name with a capital letter: '))
#     print(names)

# number = int(input('How many names need to be entered?'))
# names = make_list(number)
# for name in names:
#     if name [1] == 'A':
#         print('Name ', name, ' start with an A')

# ================================================================================

def make_list(number):
    names = []
    for item in range(number):
        names.append(input('Enter name with a capital letter: '))
    return names

number = int(input('How many names need to be entered?'))
names = make_list(number)

for name in names:
    if name[0] == 'A':
        print('Name', name, 'starts with an A')

