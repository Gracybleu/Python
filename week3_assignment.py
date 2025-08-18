def calculate_discount (price,discount_price):
    payment = price - (price * discount_price) 
    if discount_price <= 0.2:
        return price 
    else:
        return payment
    
original_price = float(input("Enter price:"))
discount = int(input("Enter Discount:")) / 100

print("Total: ", calculate_discount(original_price, discount))