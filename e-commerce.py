# E-Commerce Management System 

class Product:
    def __init__(self, product_id, name, category, stock, price, seller_id):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.stock = stock
        self.price = price
        self.seller_id = seller_id

    def update_stock(self, quantity):
        if quantity <= 0:
            print("Invalid quantity")
            return

        if quantity > self.stock:
            print("Insufficient stock")
            return

        self.stock -= quantity
        print("Updated Stock:", self.stock)

    def apply_discount(self, discount):
        if discount < 0 or discount > 100:
            print("Invalid discount")
            return self.price

        final_price = self.price * (1 - discount / 100)
        print("Price after discount:", final_price)
        return final_price

    def get_details(self):
        print("\n--- Product Details ---")
        print("Product ID :", self.product_id)
        print("Name       :", self.name)
        print("Category   :", self.category)
        print("Stock      :", self.stock)
        print("Price      :", self.price)
        print("Seller ID  :", self.seller_id)


class Cart:
    def __init__(self, cart_id, customer_id):
        self.cart_id = cart_id
        self.customer_id = customer_id
        self.items = []

    def add_item(self, product):
        self.items.append(product)
        print(product.name, "added to cart")

    def remove_item(self, product_name):
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                print(product_name, "removed from cart")
                return
        print("Item not found")

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        print("Total Amount:", total)
        return total

    def clear_cart(self):
        self.items.clear()
        print("Cart cleared")


class Order:
    def __init__(self, order_id, customer_id, items):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items
        self.status = "Created"

    def place_order(self):
        if not self.items:
            print("Cart is empty")
            return
        self.status = "Confirmed"
        print("Order placed successfully")

    def cancel_order(self):
        self.status = "Cancelled"
        print("Order cancelled")


class Payment:
    def __init__(self, payment_id, order_id, amount, method):
        self.payment_id = payment_id
        self.order_id = order_id
        self.amount = amount
        self.method = method
        self.status = "Pending"

    def process_payment(self):
        if self.amount <= 0:
            print("Invalid payment")
            return
        self.status = "Success"
        print("Payment Successful")

product_id = int(input("Enter Product ID: "))
name = input("Enter Product Name: ")
category = input("Enter Category: ")
stock = int(input("Enter Stock: "))
price = float(input("Enter Price: "))
seller_id = int(input("Enter Seller ID: "))

product = Product(product_id, name, category, stock, price, seller_id)

print("""
1. Product Details
2. Add to Cart
3. Place Order
4. Payment
""")

choice = int(input("Enter your choice: "))

if choice == 1:
    product.get_details()

    discount = float(input("Enter Discount %: "))
    product.apply_discount(discount)

    quantity = int(input("Enter quantity to purchase: "))
    product.update_stock(quantity)

elif choice == 2:
    cart = Cart("C101", "Customer01")
    cart.add_item(product)

    remove = input("Enter product name to remove (or type no): ")
    if remove.lower() != "no":
        cart.remove_item(remove)

    cart.calculate_total()

elif choice == 3:
    cart = Cart("C101", "Customer01")
    cart.add_item(product)

    order = Order("O101", "Customer01", cart.items)
    order.place_order()

elif choice == 4:
    amount = float(input("Enter Payment Amount: "))
    method = input("Enter Payment Method (UPI/Card/Cash): ")

    payment = Payment("P101", "O101", amount, method)
    payment.process_payment()

else:
    print("Invalid Choice")
