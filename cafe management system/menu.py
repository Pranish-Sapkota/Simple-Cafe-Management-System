#menu of a hotel
menu = {
    'Chiya':23,
    'Coffe':35,
    'Green Tea':50,
    'Mo:Mo':150,
    'Noodels':150,
    'Sea Food':550,
    'Burgur':80,
    'Pizza':680,
}

#message for customer
print("Welcome to Namaste Hotel")
print(" Chiya: Rs23\n Coffe: Rs35\n Green Tea: Rs50\n Mo:Mo: Rs150\n Noodels: Rs150\n Sea Food: Rs550\n Burgur: Rs80\n Pizza: Rs680") 

total_order = 0

item = input("Enter the name of the item you want to order = ")
if item in menu:
    total_order += menu[item]
    print(f" {item} has been addes to your order list")

else:
    print(f"order item {item} is not available in this time! Select listed items")

add_order = input("Do you want to order anathoer items?(Yes/No) ")
if add_order == "Yes":
    add_item = input("Enter the name of item = ")
    if add_item in menu:
        total_order += menu[add_item]
        print(f"{add_item} has been added to order")

    else:
        print(f"This item {add_item} is not available this time")


print(f"The total amount of items is {total_order}. Thank You!! Visit again❤️")