computer_name = input ("Enter the computer name: ")
computer_brand = input ("Enter the computer brand: ")
computer_Model = input ("Enter the computer model: ")
computer_Ram = input ("Enter the computer RAM size: ")

computer = {
    "name": computer_name,
    "brand": computer_brand,
    "model": computer_Model,
    "ram": computer_Ram
}

print("---------------COMPUTER INFORMATION---------------")
print(f"Name: {computer['name']}")
print(f"Brand: {computer['brand']}")
print(f"Model: {computer['model']}")
print(f"RAM: {computer['ram']}")
