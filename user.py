#modulo en donde se crean las clases usuario, cliente y empleado--------------

#creacion de la clase usuario-------------------
class User:
    def __init__(self, user_name, user_id, user_type):
        self.user_name = user_name
        self.user_id = user_id
        self._user_type = user_type

    def show_info(self):
        def __str__():
            return f"{self._user_type}: {self.user_name} id:{self.user_id}"
        return __str__()
    
#creacion de la clase cliente----------------
class Client(User):
    def __init__(self, user_name, user_id, credit_card):
        super().__init__(user_name, user_id, "Cliente")
        self.credit_card = credit_card

    def show_info(self):
        def __str__():
            return f"{self._user_type}: {self.user_name} Tarjeta de credit: {self.credit_card}, id:{self.user_id} "     

#creacion de la clase empleado------------------
class Employee(User):
    def __init__(self, user_name, user_id):
        super().__init__(user_name, user_id, "Empleado")
        self.vehicle_reservations = []
        self.salary = 100000
        self.bookings_number = 0