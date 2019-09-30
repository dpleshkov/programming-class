#This is called a hash-map or (in python) a dictionary (dict for short)

#Built with key-value pairs
age_dict = {
    "Kabir": 14,
    "Dmitry": 14,
    "Sidd": 15
}

#Adds names and ages to dictionary indefinitely
while True:
    name = input("Enter name: ")
    age = input("Enter age: ")

    age_dict[name] = age
    print("\n{}".format(age_dict))
