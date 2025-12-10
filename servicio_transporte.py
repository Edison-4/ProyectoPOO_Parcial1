# Integrante:
# -- Chinga Michelle
# -- Ortiz Michael
# -- Plaza Edison
# -- Villao Carla

# servicio_transporte.py
class ServicioTransporte:
    """
    Superclase padre. Define la estructura base.
    """

    def __init__(self, identificador: str, nombre_ruta: str, costo_base: float):
        # Atributos protegidos (privados)
        self._identificador = identificador
        self._nombre_ruta = nombre_ruta
        self._costo_base = 0.0

        # Usamos el setter para validar desde el inicio
        self.costo_base = costo_base

    # ---------------------------------------------------------
    # ENCAPSULAMIENTO (Getters y Setters)
    # ---------------------------------------------------------
    @property
    def identificador(self):
        return self._identificador

    @property
    def nombre_ruta(self):
        return self._nombre_ruta

    @property
    def costo_base(self):
        return self._costo_base

    @costo_base.setter
    def costo_base(self, valor: float):
        if valor < 0:
            print(f"  [AVISO SUPERCLASE] Costo negativo ({valor}) no permitido. Se ajusta a 0.0.")
            self._costo_base = 0.0
        else:
            self._costo_base = valor

    # ---------------------------------------------------------
    # MÉTODOS
    # ---------------------------------------------------------
    def calcular_costo_final(self):
        """Metodo base para ser sobrescrito (Polimorfismo)."""
        return self._costo_base

    def mostrar_info(self):
        return f"ID: {self._identificador} | Ruta: {self._nombre_ruta}"

    def __str__(self):
        """Permite imprimir el objeto directamente."""
        return self.mostrar_info()


# Zona de prueba
if __name__ == "__main__":
    s = ServicioTransporte("S-01", "Ruta Test", -5.0)
    print(s)  # Debe mostrar costo 0.0 por validación