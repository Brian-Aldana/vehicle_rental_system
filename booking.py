# Módulo para la clase de reserva
import random
from datetime import date

class Booking:
    def __init__(self, client, employee, vehicle, start_date: date, end_date: date, vehicle_list, vehicle_wear_list, vehicle_reserve_list):
        self.client = client
        self.employee = employee
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date
        self.vehicle_list = vehicle_list
        self.vehicle_wear_list = vehicle_wear_list
        self.vehicle_reserve_list = vehicle_reserve_list
        self.payment_processed = False
    
    def process_payment(self):
        while True:
            try:
                option = int(input("""
¿Desea reservar el vehiculo?
1. Si
2. No
Escoja una opcion (1/2): """))
                
                if option == 1:
                    self.vehicle_reserve_list.append(self.vehicle)
                    self.employee.vehicle_reservations.append(self.vehicle)
                    self.vehicle.in_possession_of = self.client.__str__()
                    self.employee.bookings_number += 1
                    self.vehicle.availability = False
                    self.payment_processed = True
                    break
                elif option == 2:
                    print("\nReserva cancelada.")
                    break
                else:
                    print("\nError: Opción no válida.")
            except ValueError:
                print("\nError: Ingrese un número válido.")

    def process_return(self):
        self.vehicle.in_possession_of = None
        self.vehicle.availability = True
        self.vehicle_reserve_list.remove(self.vehicle)

        wear_probability = random.randint(1, 3)
        if wear_probability == 1:
            self.vehicle.vehicle_wear += 1
            print("\nSe han registrado daños. Se cobrará una cuota extra.")
            self.vehicle.damaged_by = self.client.__str__()
            self.vehicle_wear_list.append(self.vehicle)
        
        if self.vehicle.vehicle_wear >= 5:
            self.vehicle.availability = False

        print("\nDevolución completada.")

    def reserve_vehicle(self):
        total_days = (self.end_date - self.start_date).days + 1
        total_cost = self.vehicle.rate_per_day * total_days

        self.process_payment()

        if self.payment_processed:
            print(f"""
--- Recibo ---
Vehículo: {self.vehicle.__str__()}
Cliente: {self.client.user_name}
Empleado: {self.employee.user_name}
Fecha inicio: {self.start_date.strftime('%d/%m/%Y')}
Fecha fin: {self.end_date.strftime('%d/%m/%Y')}
Total días: {total_days}
Costo total: ${total_cost}""")

    def return_vehicle(self):
        while True:
            try:
                option = int(input("""
1. Devolver vehículo
2. Cancelar
Opción (1/2): """))
                if option == 1:
                    self.process_return()
                    break
                elif option == 2:
                    print("\nDevolución cancelada.")
                    break
                else:
                    print("\nError: Opción no válida.")
            except ValueError:
                print("\nError: Ingrese un número.")