#modulo para verificaciones-----------------------

# Función para validar que el nombre y el ID no estén duplicados en clientes o empleados
def validate_global_consistency(client_list, employee_list, user_id):

    # Buscar si existe un cliente o empleado con el mismo ID
    client_with_same_id = next((c for c in client_list if c.user_id == user_id), None)
    employee_with_same_id = next((e for e in employee_list if e.user_id == user_id), None)

    # Si el ID ya existe en clientes o empleados
    if client_with_same_id or employee_with_same_id:
        return False, "Error: El ID ya está en uso por otro cliente o empleado."

    return True, ""

# Función para mostrar la lista de clientes existentes
def show_existing_clients(client_list):
    if not client_list:
        print("\nNo hay clientes registrados.")
    else:
        print("\n--- Lista de Clientes Registrados ---")
        for i, client in enumerate(client_list, 1):
            print(f"{i}. Nombre: {client.user_name}, ID: {client.user_id}")

# Función para mostrar la lista de empleados existentes
def show_existing_employees(employee_list):
    if not employee_list:
        print("\nNo hay empleados registrados.")
    else:
        print("\n--- Lista de Empleados Registrados ---")
        for i, employee in enumerate(employee_list, 1):
            print(f"{i}. Nombre: {employee.user_name}, ID: {employee.user_id}")