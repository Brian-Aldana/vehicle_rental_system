# Módulo principal
import vehicle
import functions

def main():

    vehicle_1 = vehicle.Vehicle("Sentra", "Nissan", 1982, 500)
    vehicle_2 = vehicle.Vehicle("Tacoma", "Toyota", 1995, 700)
    vehicle_3 = vehicle.Vehicle("HR-V", "Honda", 2014, 800)
    vehicle_4 = vehicle.Vehicle("Fusion", "Ford", 2020, 1000)
    vehicle_5 = vehicle.Vehicle("Wrangler", "Jeep", 2024, 11000)


    vehicle_list = [vehicle_1, vehicle_2, vehicle_3, vehicle_4, vehicle_5]
    
    vehicle_wear_list = []
    vehicle_reserve_list = []
    client_list = []
    employee_list = []

    while True:
        print("""
--- Menú Principal ---
1. Reservas/Devoluciones
2. Menú Administrativo
3. Salir""")
        
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