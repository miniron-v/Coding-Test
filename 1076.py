# values = {
#     "black": 0,
#     "brown": 1,
#     "red": 2,
#     "orange": 3,
#     "yellow": 4,
#     "green": 5,
#     "blue": 6,
#     "violet": 7,
#     "grey": 8,
#     "white": 9
# }

# multiple = {
#     "black": 1,
#     "brown": 10,
#     "red": 100,
#     "orange": 1000,
#     "yellow": 10000,
#     "green": 100000,
#     "blue": 1000000,
#     "violet": 10000000,
#     "grey": 100000000,
#     "white": 1000000000
# }

# a = str(input())
# b = str(input())
# c = str(input())

# print((values[a] * 10 + values[b]) * multiple[c])

values = {
    "black": '0',
    "brown": '1',
    "red": '2',
    "orange": '3',
    "yellow": '4',
    "green": '5',
    "blue": '6',
    "violet": '7',
    "grey": '8',
    "white": '9'
}

multiple = {
    "black": '',
    "brown": '0',
    "red": '00',
    "orange": '000',
    "yellow": '0000',
    "green": '00000',
    "blue": '000000',
    "violet": '0000000',
    "grey": '00000000',
    "white": '000000000'
}

a = str(input())
b = str(input())
c = str(input())

print(values[a] + values[b] + multiple[c] if a != 'black' else(values[b] + multiple[c] if b != 'black' else 0))