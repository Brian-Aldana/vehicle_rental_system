# Módulo de funciones
import user
import booking
import re
from datetime import datetime

# Función para reservar un vehículo---------
def vehicle_reserve(client, employee, vehicle_list, vehicle_reserve_list, vehicle_wear_list):
    print("\n--- Menú de reserva ---")
    for i, vehicle in enumerate(vehicle_list, 1):
        print(f"{i}. {vehicle.__str__()}")
    print(f"{len(vehicle_list)+1}. Regresar")

    while True:
        try:
            option = int(input("\nÍndice del vehículo: ")) - 1
            if 0 <= option < len(vehicle_list):
                vehicle = vehicle_list[option]
                break
            elif option == len(vehicle_list):
                return
            else:
                print("\nError: Índice fuera de rango.")
        except ValueError:
            print("\nError: Ingrese un número.")

    # Capturar fechas con datetime----------------
    while True:
        try:
            start_str = input("Fecha inicio (DD/MM/AAAA): ")
            start_date = datetime.strptime(start_str, "%d/%m/%Y").date()
            break
        except ValueError:
            print("\nFormato incorrecto. Use DD/MM/AAAA.")

    while True:
        try:
            end_str = input("Fecha fin (DD/MM/AAAA): ")
            end_date = datetime.strptime(end_str, "%d/%m/%Y").date()
            if end_date <= start_date:
                print("\nLa fecha fin debe ser posterior.")
            else:
                break
        except ValueError:
            print("\nFormato incorrecto. Use DD/MM/AAAA.")

    new_booking = booking.Booking(client, employee, vehicle, start_date, end_date, vehicle_list, vehicle_wear_list, vehicle_reserve_list)
    new_booking.reserve_vehicle()

#funcion para devolver vehiculo---------
def return_vehicles(client, employee, vehicle_list, vehicle_wear_list, vehicle_reserve_list):
    if not vehicle_reserve_list:
        print("\nNo tiene vehículos rentados actualmente.")
        return None
    
    print("\n--- Menú de devolución ---")
    print("Vehículos rentados:")
    for i, vehicle in enumerate(vehicle_reserve_list, 1):
        print(f"{i}. {vehicle.__str__()} (ID Cliente: {vehicle.in_possession_of})")
    
    while True:
        try:
            option = int(input("\nÍndice del vehículo a devolver: ")) - 1
            if 0 <= option < len(vehicle_reserve_list):
                vehicle = vehicle_reserve_list[option]
                break
            else:
                print("\nError: Índice fuera de rango.")
        except ValueError:
            print("\nError: Ingrese un número válido.")

    # Registro de fecha de devolución------------
    return_date = datetime.now().date()
    print(f"\nFecha de devolución: {return_date.strftime('%d/%m/%Y')}")
    
    booking_return = booking.Booking(client, employee, vehicle, None, return_date, vehicle_list, vehicle_wear_list, vehicle_reserve_list)
    booking_return.return_vehicle()

#creacion del menu del cliente----------
def booking_menu(client_list, Employee_list, vehicle_list, vehicle_wear_list, vehicle_reserve_list):
    print("\n--- Datos del cliente --- ")
    
    # Validación de nombre con caracteres especiales-----------------
    while True:
        user_name = input("Ingrese el nombre del cliente: ")
        if re.fullmatch(r"[A-Za-zÁ-Úá-úÑñÜüÇç\s]+", user_name):
            break
        else:
            print("Error: Solo letras y espacios.")
    
    # Validación de ID único--------------------
    while True:
        try:
            user_id = int(input("Ingrese el ID del cliente: "))
            if user_id <= 0:
                print("\nError: El ID debe estar compuesto por numeros positivos.")
                continue
            
            # Buscar cliente existente----------------
            existing_client = next((c for c in client_list if c.user_id == user_id), None)
            if existing_client:
                client = existing_client
                print("\nCliente existente recuperado.")
                break
            else:
                client = user.Client(user_name, user_id)
                client_list.append(client)
                print("\nNuevo cliente registrado.")
                break
        except ValueError:
            print("\nError: Ingrese un número.")

    print("\n--- Datos del vendedor --- ")
    
    # Validación de empleado--------------------
    while True:
        employee_name = input("Ingrese el nombre del vendedor: ")
        if re.fullmatch(r"[A-Za-zÁ-Úá-úÑñÜüÇç\s]+", employee_name):
            break
        else:
            print("Error: Solo letras y espacios")
    
    while True:
        try:
            employee_id = int(input("Ingrese el ID del vendedor: "))
            if employee_id <= 0:
                print("\nError: El ID debe estar compuesto por numeros positivos.")
                continue
            
            # Buscar empleado existente--------------------
            existing_employee = next((e for e in Employee_list if e.user_id == employee_id), None)
            if existing_employee:
                employee = existing_employee
                print("\nEmpleado existente recuperado.")
                break
            else:
                employee = user.Employee(employee_name, employee_id)
                Employee_list.append(employee)
                print("\nNuevo empleado registrado.")
                break
        except ValueError:
            print("\nError: Ingrese un número.")

    # Menú principal-----------------
    while True:
        print(f"""
--- Menú Principal ---
1. Reservar vehículo
2. Devolver vehículo
3. Ver vehículos disponibles
4. Regresar""")
        
        try:
            option = int(input("Opción: "))
            if option == 1:
                vehicle_reserve(client, employee, vehicle_list, vehicle_reserve_list, vehicle_wear_list)
            elif option == 2:
                return_vehicles(client, employee, vehicle_list, vehicle_wear_list, vehicle_reserve_list)
            elif option == 3:
                print("\n--- Vehículos Disponibles ---")
                for i, vehicle in enumerate(vehicle_list, 1):
                    status = "Disponible" if vehicle.availability else "No disponible"
                    print(f"{i}. {vehicle.brand} {vehicle.model} - {status}")
            elif option == 4:
                break
            else:
                print("\nError: Opción no válida.")
        except ValueError:
            print("\nError: Ingrese un número.")

#creacion del menu del empleado----------
def administrative_menu(Employee_list, vehicle_wear_list, vehicle_reserve_list, client_list):

    while True:
        print(f"""
--- menu administrativo ---
1. Ver vehiculos reservados.
2. Ver listado de clientes.
3. Ver vehiculos dañados.
4. Ver desempeño de empleados. 
5. Salir.""")
        
        try:
            menu_option = int(input("\nIngrese la opcion (1/2/3/4): "))

            if menu_option == 1:
                if len(vehicle_reserve_list) <= 0:
                    print("\nNo hay vehiculos reservados.")
                else:
                    for i, vehicle in enumerate(vehicle_reserve_list, 1):
                        print(f""" 
{i}: {vehicle.__str__()}. {vehicle.in_possession_of}""")       
            elif menu_option == 2:
                if len(client_list) <= 0:
                    print("\nNo hay clientes registrados.")
                else:
                    for i, client in enumerate(client_list, 1):
                        print(f""" 
{i}: {client.__str__()}.
""")
            elif menu_option == 3:
                if len(vehicle_wear_list) <= 0:
                    print("\nNo hay vehiculos con daños.")
                else:
                    for i, vehicle in enumerate(vehicle_wear_list, 1):
                        print(f""" 
{i}: {vehicle.__str__()}.
    daños registrados: {vehicle.vehicle_wear} 
    Realizados por: {vehicle.damaged_by}""")
                    
                    while True:
                        try:
                            vehicle_index = int(input("\nIngrese el indice del vehiculo que desee reparar: ")) - 1

                            if 0 <= vehicle_index < len(vehicle_wear_list):
                                vehicle_wear_list[vehicle_index].fix_vehicle(vehicle_wear_list)
                                break
                            else:
                                print("\nError: Indice fuera de rango.")
                                continue
                        except ValueError:
                            print("\nError: Ingrese un indice valido.")
                            continue
            elif menu_option == 4:
                for i, employee in enumerate(Employee_list, 1):
                    print(f"""
{i}: {employee.__str__()}:
    Reservaciones hechas: {employee.bookings_number}""")
            elif menu_option == 5:
                break
            else:
                print("\nError: Ingrese valores numericos.")
                continue
        except ValueError:
            print("\nError: Ingrese valores numericos.")
            continue