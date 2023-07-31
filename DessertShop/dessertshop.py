from dessert import DessertItem, Candy, Cookie, IceCream, Sundae, Order
from receipt import make_receipt
# import receipt


class DessertShop:

    @staticmethod
    def user_prompt_candy():
        name = DessertShop.get_str_input("Enter the type of candy: ")
        weight = DessertShop.get_float_input("Enter the candy weight in pounds: ")
        price_per_pound = DessertShop.get_float_input("Enter the price per pound: ")
        return Candy(name, weight, price_per_pound)

    @staticmethod
    def user_prompt_cookie():
        name = DessertShop.get_str_input("Enter the type of cookie: ")
        quantity = DessertShop.get_float_input("Enter the quantity purchased: ")
        price_per_dozen = DessertShop.get_float_input("Enter the price per dozen: ")
        return Cookie(name, quantity, price_per_dozen)

    @staticmethod
    def user_prompt_icecream():
        name = DessertShop.get_str_input("Enter the type of ice cream: ")
        scoop_count = DessertShop.get_float_input("Enter the number of scoops: ")
        price_per_scoop = DessertShop.get_float_input("Enter the price per scoop: ")
        return IceCream(name, scoop_count, price_per_scoop)

    @staticmethod
    def user_prompt_sundae():
        name = DessertShop.get_str_input("Enter the type of ice cream for the sundae: ")
        scoop_count = DessertShop.get_float_input("Enter the number of scoops for the sundae: ")
        price_per_scoop = DessertShop.get_float_input("Enter the price per scoop for the sundae: ")
        topping_name = DessertShop.get_str_input("Enter the topping for the sundae: ")
        topping_price = DessertShop.get_float_input("Enter the price for the topping: ")
        return Sundae(name, scoop_count, price_per_scoop, topping_name, topping_price)

    @staticmethod
    def get_float_input(prompt):
        while True:
            try:
                value = float(input(prompt))
                if value < 0:
                    print("Please enter a non-negative number.")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")


    @staticmethod
    def get_str_input(prompt):
        while True:
            value = input(prompt)
            if value.isnumeric():
                print("Please enter a valid name (non-numeric characters only).")
            else:
                return value

def main():
    
    order = Order()
    shop = DessertShop() 
    
    order.add(Candy('Candy Corn', 1.5, 0.25))
    order.add(Candy('Gummy Bears', 0.25, 0.35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(IceCream('Pistachio', 2, 0.79))
    order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    
    # boolean done = false
    done: bool = False
    pay: bool = False
    # build the prompt string once
    prompt1 = '\n'.join([ '\n',
            '1: Candy',
            '2: Cookie',            
            '3: Ice Cream',
            '4: Sunday',
            '\nWhat would you like to add to the order? (1-4,) Enter for done'])
    
    prompt2 = '\n'.join([ '\n',
            '1: CASH',
            '2: CARD',
            '3: PHONE',
            '\nPlease choose a payment method. (Press enter for cash default):'])
    
    while not done:
      choice = input(prompt1)
      match choice:
        case '':
          done = True
        case '1':            
          item = shop.user_prompt_candy()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '2':            
          item = shop.user_prompt_cookie()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '3':            
          item = shop.user_prompt_icecream()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '4':            
          item = shop.user_prompt_sundae()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case _:            
          print('Invalid response: Please enter a choice from the menu (1-4) or Enter')
    
    while not pay:
      choice = input(prompt2)
      match choice:
        case '':
          pay = True
        case '1':            
          order.set_pay_type(    )
          print('Your chosen payment method is cash.')
          pay = True
        case '2':            
          order.set_pay_type("CARD")
          print('Your chosen payment method is card.')
          pay = True
        case '3':            
          order.set_pay_type("PHONE")
          print('Your chosen payment method is phone.')
          pay = True
        case _:            
          print('Invalid response:  Please pick a payment option (1-3) or press enter to default to cash')
    print()

    data = [["Name", "Quantity", "Unit Price", "Cost", "Tax"]]
    for item in order:
        item_data = item.__str__()  # The __str__ method now returns a tuple
        if len(item_data) == 2:  # If the tuple contains base info and toppings info
            data.append(item_data[0])
            data.append(item_data[1])
        else:  # For other items, use the existing __str__ format
            data.append(item_data)


    order.__str__()
    total_cost = order.order_cost()
    total_tax = order.order_tax()
    data.append(["------------------------------------------------------"])
    data.append([f"Order Subtotals", "", "", f"${total_cost}", f'${total_tax}'])
    data.append([f'Order Total', "", "", "", f'${total_cost + total_tax}'])
    data.append([f'Total number of items in order', "", "", "", f'{len(order)}'])
    data.append(["------------------------------------------------------"])
    data.append([f'Paid with {order.get_pay_type}'])
    make_receipt(data, "python.pdf")

if __name__ == "__main__":
    main()


