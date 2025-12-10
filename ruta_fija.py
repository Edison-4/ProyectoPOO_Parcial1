# Integrante:
# -- Chinga Michelle
# -- Ortiz Michael
# -- Plaza Edison
# -- Villao Carla

# ruta_fija.py
from servicio_transporte import ServicioTransporte


class RutaFija(ServicioTransporte):
    """
    Clase hija 1: Transporte con ruta y horarios fijos (Bus).
    """

    def __init__(self, identificador: str, nombre_ruta: str, costo_base: float, es_hora_pico: bool):
        super().__init__(identificador, nombre_ruta, costo_base)
        self._es_hora_pico = es_hora_pico

    # ---------------------------------------------------------
    # ENCAPSULAMIENTO
    # ---------------------------------------------------------
    @property
    def es_hora_pico(self):
        return self._es_hora_pico

    @es_hora_pico.setter
    def es_hora_pico(self, valor: bool):
        if not isinstance(valor, bool):
            raise TypeError("El valor debe ser True o False")
        self._es_hora_pico = valor

    # ---------------------------------------------------------
    # POLIMORFISMO (Sobrescritura)
    # ---------------------------------------------------------
    def calcular_costo_final(self):
        # Llama al padre para obtener la base
        costo = super().calcular_costo_final()

        # Aplica lógica específica: Recargo del 20% si es hora pico
        if self._es_hora_pico:
            return costo * 1.20
        return costo

    def mostrar_info(self):
        base = super().mostrar_info()
        estado = "HORA PICO" if self._es_hora_pico else "NORMAL"
        return f"[Ruta Fija] {base} | Estado: {estado}"


# Zona de prueba
if __name__ == "__main__":
    bus = RutaFija("B-01", "Centro", 1.00, True)
    print(f"{bus} | Costo: {bus.calcular_costo_final()}")