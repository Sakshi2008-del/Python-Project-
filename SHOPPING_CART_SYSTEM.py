cart = {}

while True :
    print("\n1. ADD ITEM TO CART")
    print("\n2. REMOVE ITEM FROM CART")
    print("\n3. VIEW CART")
    print("\n4. TOTAL CART")
    print("\n5. EXIT")

    choice = input("enter your choice :")

    if choice == "1":
        item = input(" enter item name :")
        price = input("enter price of item :")
        quantity = input("enter quantity of item :")
        cart[item]= { "price" , price ," quantity" , quantity}

    elif choice == "2" :
        item = input(" enter item to remove : ")
        if item in cart :
            del cart[item]
            print(item , " removed")
        else :
            print("item not found ")

    elif choice =="3":
        if not cart :
            print(" cart is empty")
        else :
            print(" \nitem in carts")
            for item, details in cart.items():
                print( "items: ", item ,
                       " -price:" , details["price"],
                 "quantity :", details[quantity])
            
    elif choice == "4" :
        total = 0 
        for details in cart.values():
            total += details["price"] * details["quantity"]
            print("total bill :" , total)

    elif choice == 5:
        print("thankyou for shopping !")
        break

    else :
        print("invaid choice .")

