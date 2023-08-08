#Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, monto):
        self.balance += monto
        print(f"Depósito de {monto} realizado. Nuevo balance: {self.balance}")