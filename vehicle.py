#modulo en donde se crea la clase vehiculo------------------------

class Vehicle:
    def __init__(self, model, brand, year, rate_per_day, vehicle_license_plate):
        self.model = model
        self.brand = brand
        self.year = year
        self.rate_per_day = rate_per_day
        self.vehicle_wear = 0
        self.possession_days = 0
        self.booking_cost = 0
        self.vehicle_license_plate = vehicle_license_plate
        self.in_possession_of = None
        self.damaged_by = None
        self.availability = True

    def show_info(self):
        def __str__():
            return f"{self.brand} {self.model} ({self.year}) placa: {self.vehicle_license_plate} - Tarifa: ${self.rate_per_day}/día"
        return __str__()

    def fix_vehicle(self, vehicle_wear_list):

        print("\n--- Menu der reparacion ---")

        while True:
            try:
                menu_option = int(input("""
¿Desea reparar el vehiculo? 
1. Si.
2. No.
Escoja una opcion (1/2): """))
            
                if menu_option == 1:
                    self.vehicle_wear = 0
                    self.damaged_by = None
                    vehicle_wear_list.remove(self)
                    print("\nEl vehiculo ha sido reparado.")
                    break
                elif menu_option == 2:
                    break
                else:
                    print("\nError: Ingrese un indice valido.")
                    continue
            except ValueError:
                print("\nError: Ingrese un indice valido.")
                continue
