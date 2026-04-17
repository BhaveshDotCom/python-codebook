# any object capable of returning its members one at a time

my_list = [1, 2, 3]
for item in reversed(my_list):
    print(item, )

my_dict = {
    1:"A",
    2:"B",
    3:"C"
}

for key, value in my_dict.items():
    print(f"{key} = {value}")