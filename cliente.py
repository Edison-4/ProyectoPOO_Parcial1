# Integrante:
# -- Chinga Michelle
# -- Ortiz Michael
# -- Plaza Edison
# -- Villao Carla

# cliente.py

class Cliente:
    """
    Clase independiente. Cumple encapsulamiento estricto.
    """

    def __init__(self, nombre: str, saldo: float):
        self._nombre = ""
        self._saldo = 0.0

        # Asignación vía setters para activar validaciones
        self.nombre = nombre
        self.saldo = saldo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or len(valor.strip()) == 0:
            print("  [AVISO CLIENTE] Nombre vacío no permitido. Se asigna 'Anónimo'.")
            self._nombre = "Anónimo"
        else:
            self._nombre = valor.strip().title()

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float):
        if valor < 0:
            print("  [AVISO CLIENTE] Saldo negativo no permitido. Se asigna 0.")
            self._saldo = 0.0
        else:
            self._saldo = valor

    def mostrar_cliente(self):
        return f"Cliente: {self._nombre} | Saldo: ${self._saldo:.2f}"

    def __str__(self):
        return self.mostrar_cliente()


# Zona de prueba
if __name__ == "__main__":
    c = Cliente("", -10)  # Prueba de validaciones
    print(c)# cliente.py

class Cliente:
    """
    Clase independiente. Cumple encapsulamiento estricto.
    """
    def __init__(self, nombre: str, saldo: float):
        self._nombre = ""
        self._saldo = 0.0

        # Asignación vía setters para activar validaciones
        self.nombre = nombre
        self.saldo = saldo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or len(valor.strip()) == 0:
            print("  [AVISO CLIENTE] Nombre vacío no permitido. Se asigna 'Anónimo'.")
            self._nombre = "Anónimo"
        else:
            self._nombre = valor.strip().title()

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float):
        if valor < 0:
            print("  [AVISO CLIENTE] Saldo negativo no permitido. Se asigna 0.")
            self._saldo = 0.0
        else:
            self._saldo = valor

    def mostrar_cliente(self):
        return f"Cliente: {self._nombre} | Saldo: ${self._saldo:.2f}"

    def __str__(self):
        return self.mostrar_cliente()

# Zona de prueba
if __name__ == "__main__":
    c = Cliente("", -10) # Prueba de validaciones
    print(c)