class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, order):
        if self.is_full():
            print("Storage is full. Cannot add more orders.")
            return
        
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = order
        print(f"Order added: {order}")

    def dequeue(self):
        if self.is_empty():
            print("Storage is empty. No orders to remove.")
            return
        
        removed_order = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        
        print(f"Order removed: {removed_order}")

    def get_all_orders(self):
        if self.is_empty():
            return []
        
        orders = []
        i = self.front
        while True:
            orders.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.max_size
        return orders

    def show_queue(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        print("Orders in the storage:")
        for order in self.get_all_orders():
            print(order)

class Order:
    def __init__(self, order_id, customer_name, car_model, priority):
        self.order_id = order_id
        self.customer_name = customer_name
        self.car_model = car_model
        self.priority = priority

    def __repr__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer_name}, Car: {self.car_model}, Priority: {self.priority}"

def counting_sort(orders, max_priority):
   
    count = [0] * (max_priority + 1)

   
    for order in orders:
        count[order.priority] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    sorted_orders = [None] * len(orders)

    
    for order in reversed(orders):
        position = count[order.priority] - 1
        sorted_orders[position] = order
        count[order.priority] -= 1

    return sorted_orders


if __name__ == "__main__":
    
    rental_queue = CircularQueue(max_size=5)

    rental_queue.enqueue(Order(1, "Bahati", "Toyota Corolla", 2))
    rental_queue.enqueue(Order(2, "Dior", "Honda Civic", 1))
    rental_queue.enqueue(Order(3, "Olovier", "Ford Mustang", 3))
    rental_queue.enqueue(Order(4, "Diana", "Chevrolet Malibu", 0))
    rental_queue.enqueue(Order(5, "John", "Tesla Model S", 2))

    print("Original data:")
    rental_queue.show_queue()

    
    orders = rental_queue.get_all_orders()
    sorted_orders = counting_sort(orders, max_priority=3)

    print("\nSorted Orders by Priority:")
    for order in sorted_orders:
        print(order)
