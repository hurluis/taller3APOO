#Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, monto):
        self.balance += monto
        print(f"Depósito de {monto} realizado. Nuevo balance: {self.balance}")

    def retirar(self, monto):
        if monto <= self.balance:
            self.balance -= monto
            print(f"Retiro de {monto} realizado. Nuevo balance: {self.balance}")
        else:
            print("Saldo insuficiente para realizar el retiro.")