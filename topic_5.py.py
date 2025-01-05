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
            print("sttorage is full. Cannot add more orders.")
            return
        
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = order
        print(f"Order added: {order}")

    def dequeue(self):
        if self.is_empty():
            print("storage is empty. No orders to remove.")
            return
        
        removed_order = self.queue[self.front]
        if self.front == self.rear:
           
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        
        print(f"Order removed: {removed_order}")

    def show_queue(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        print("Orders in the storage:")
        i = self.front
        while True:
            print(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.max_size

    def current_size(self):
        if self.is_empty():
            return 0
        if self.rear >= self.front:
            return self.rear - self.front + 1
        return self.max_size - self.front + self.rear + 1


class Order:
    def __init__(self, order_id, customer_name, car_model):
        self.order_id = order_id
        self.customer_name = customer_name
        self.car_model = car_model

    def __repr__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer_name}, Car: {self.car_model}"


if __name__ == "__main__":
  
    rental_queue = CircularQueue(max_size=3)

    order1 = Order(1, "Bahati", "Toyota Corolla")
    order2 = Order(2, "dior", "Honda Civic")
    order3 = Order(3, "olovier", "Ford Mustang")
    order4 = Order(4, "Diana", "Chevrolet Malibu")

  
    rental_queue.enqueue(order1)
    rental_queue.enqueue(order2)
    rental_queue.enqueue(order3)

    
    rental_queue.enqueue(order4)

    
    rental_queue.show_queue()

    
    rental_queue.dequeue()

    
    rental_queue.enqueue(order4)

    
    rental_queue.show_queue()

    print(f"Current storage size: {rental_queue.current_size()}")
