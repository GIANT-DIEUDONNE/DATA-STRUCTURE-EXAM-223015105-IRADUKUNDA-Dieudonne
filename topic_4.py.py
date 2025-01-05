class Order:
    def __init__(self, order_id, customer_name, car_model):
        self.order_id = order_id
        self.customer_name = customer_name
        self.car_model = car_model
        self.next = None

    def __repr__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer_name}, Car: {self.car_model}"

class SinglyLinkedList:
    def __init__(self, max_orders):
        self.head = None
        self.tail = None
        self.max_orders = max_orders
        self.current_size = 0

    def add_order(self, order_id, customer_name, car_model):
        if self.current_size == self.max_orders:
            print("Order limit reached. Cannot add more orders.")
            return
        
        new_order = Order(order_id, customer_name, car_model)
        if not self.head: 
            self.head = new_order
            self.tail = new_order
        else:
            self.tail.next = new_order
            self.tail = new_order
        
        self.current_size += 1
        print(f"Order added: {new_order}")

    def remove_order(self):
        if not self.head:
            print("No orders to remove.")
            return
        
        removed_order = self.head
        self.head = self.head.next
        self.current_size -= 1
        print(f"Order removed: {removed_order}")

    def show_orders(self):
        if not self.head:
            print("No orders available.")
            return
        
        current = self.head
        while current:
            print(current)
            current = current.next

    def get_order_count(self):
        return self.current_size


if __name__ == "__main__":
    
    order_system = SinglyLinkedList(max_orders=3)

    
    order_system.add_order(1, "Bahati", "Toyota Corolla")
    order_system.add_order(2, "dior", "Honda Civic")
    order_system.add_order(3, "iranzi", "Ford Mustang")

    
    order_system.add_order(4, "David", "Chevrolet Malibu")

    
    print("\nAll Orders:")
    order_system.show_orders()

    
    order_system.remove_order()

    
    print("\nOrders after removal:")
    order_system.show_orders()

    
    order_system.add_order(4, "David", "Chevrolet Malibu")
    
    
    print("\nOrders after adding a new order:")
    order_system.show_orders()

    
    print(f"\nCurrent Order Count: {order_system.get_order_count()}")
