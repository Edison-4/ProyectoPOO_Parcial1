# Integrante:
# -- Chinga Michelle
# -- Ortiz Michael
# -- Plaza Edison
# -- Villao Carla

# servicio_expreso.py
from servicio_transporte import ServicioTransporte


class ServicioExpreso(ServicioTransporte):
    """
    Clase hija 2: Transporte bajo demanda (Taxi/Uber).
    """

    TARIFA_KM = 0.50  # Constante

    def __init__(self, identificador: str, nombre_ruta: str, costo_base: float, distancia_km: float):
        super().__init__(identificador, nombre_ruta, costo_base)
        self._distancia_km = 0.0
        self.distancia_km = distancia_km  # Usa setter

    # ---------------------------------------------------------
    # ENCAPSULAMIENTO
    # ---------------------------------------------------------
    @property
    def distancia_km(self):
        return self._distancia_km

    @distancia_km.setter
    def distancia_km(self, valor: float):
        if valor <= 0:
            print("  [AVISO EXPRESO] Distancia inválida. Se asigna 1.0 km.")
            self._distancia_km = 1.0
        else:
            self._distancia_km = valor

    # ---------------------------------------------------------
    # POLIMORFISMO (Sobrescritura)
    # ---------------------------------------------------------
    def calcular_costo_final(self):
        base = super().calcular_costo_final()
        # Lógica específica: Costo base + (Km * Tarifa)
        extra = self._distancia_km * self.TARIFA_KM
        return base + extra

    def mostrar_info(self):
        base = super().mostrar_info()
        return f"[Expreso]   {base} | Distancia: {self._distancia_km}km"


# Zona de prueba
if __name__ == "__main__":
    taxi = ServicioExpreso("TX-01", "Norte", 2.00, 10.0)
    print(f"{taxi} | Costo: {taxi.calcular_costo_final()}")