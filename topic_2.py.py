from collections import deque


class Car:
    def __init__(self, car_id, model, is_available=True):
        self.car_id = car_id
        self.model = model
        self.is_available = is_available

    def __repr__(self):
        return f"{self.model} (ID: {self.car_id})"


class CarRentalSystem:
    def __init__(self):
        
        self.car_inventory = []
       
        self.customer_queue = deque()

   
    def add_car(self, car):
        self.car_inventory.append(car)

  
    def remove_car(self, car_id):
        for car in self.car_inventory:
            if car.car_id == car_id:
                self.car_inventory.remove(car)
                break


    def show_available_cars(self):
        available_cars = [car for car in self.car_inventory if car.is_available]
        return available_cars


    def add_customer_to_queue(self, customer_name):
        self.customer_queue.append(customer_name)

 
    def process_next_customer(self):
        if self.customer_queue:
            customer_name = self.customer_queue.popleft()
            available_cars = self.show_available_cars()
            if available_cars:
                rented_car = available_cars[0] 
                rented_car.is_available = False
                print(f"{customer_name} rented {rented_car}.")
            else:
                print(f"No cars available for {customer_name}.")
        else:
            print("No customers in the queue.")

   
    def return_car(self, car_id):
        for car in self.car_inventory:
            if car.car_id == car_id:
                car.is_available = True
                print(f"Car {car} is now available for rental.")


if __name__ == "__main__":
   
    rental_system = CarRentalSystem()

    
    rental_system.add_car(Car(1, "Toyota Corolla"))
    rental_system.add_car(Car(2, "Toyota RAV4"))
    rental_system.add_car(Car(3, "Ford Mustang"))
    rental_system.add_car(Car(4, "Chevrolet Silverado"))
    rental_system.add_car(Car(5, "Toyota Tacoma"))


    print("Available cars:", rental_system.show_available_cars())


    rental_system.add_customer_to_queue("Bahati")
    rental_system.add_customer_to_queue("dior")

   
    rental_system.process_next_customer() 
    rental_system.process_next_customer() 

  
    print("Available cars:", rental_system.show_available_cars())

    
    rental_system.return_car(1)

   
    print("Available cars after return:", rental_system.show_available_cars())

  
    rental_system.process_next_customer()  
