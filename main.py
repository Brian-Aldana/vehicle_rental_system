# Módulo principal----------------------
import vehicle
import functions

def main():
    #meter placas aca----------------
    vehicle_1 = vehicle.Vehicle("Sentra", "Nissan", 1982, 500, "KJE 243")
    vehicle_2 = vehicle.Vehicle("Tacoma", "Toyota", 1995, 700, "DFS 464")
    vehicle_3 = vehicle.Vehicle("HR-V", "Honda", 2014, 800, "GYT 845")
    vehicle_4 = vehicle.Vehicle("Fusion", "Ford", 2020, 1000, "FVH 674")
    vehicle_5 = vehicle.Vehicle("Wrangler", "Jeep", 2024, 11000, "PSD 375")

    vehicle_list = [vehicle_1, vehicle_2, vehicle_3, vehicle_4, vehicle_5]
    
    vehicle_wear_list = []
    vehicle_reserve_list = []
    client_list = []
    employee_list = []

    while True:
        print("""
--- Menú Principal ---
1. Menu de empleado.
2. Menú Administrativo.
3. Salir.""")
        
        try:
            option = int(input("Opción: "))
            if option == 1:
                functions.booking_menu(client_list, employee_list, vehicle_list, vehicle_wear_list, vehicle_reserve_list)
            elif option == 2:
                functions.administrative_menu(employee_list, vehicle_wear_list, vehicle_reserve_list, client_list)
            elif option == 3:
                print("\n¡Hasta luego!")
                exit()
            else:
                print("\nError: Opción no válida.")
        except ValueError:
            print("\nError: Ingrese un número.")

if __name__ == "__main__":
    main()