# Integrante:
# -- Chinga Michelle
# -- Ortiz Michael
# -- Plaza Edison
# -- Villao Carla

# gestor_servicios.py

class GestorServicios:
    """
    Administra la lista de servicios y ejecuta métodos polimórficos.
    """

    def __init__(self):
        self._servicios = []

    def agregar_servicio(self, servicio):
        self._servicios.append(servicio)

    @property
    def servicios(self):
        return self._servicios

    # ---------------------------------------------------------
    # REQUISITO: MÉTODOS POLIMÓRFICOS QUE RECIBEN UNA LISTA
    # ---------------------------------------------------------

    @staticmethod
    def imprimir_reporte_masivo(lista_servicios: list):
        """Recorre la lista y ejecuta el mostrar_info() de cada objeto."""
        print("\n--- REPORTE DETALLADO (Polimorfismo) ---")
        if not lista_servicios:
            print("No hay servicios registrados.")

        for srv in lista_servicios:
            # Polimorfismo: Cada objeto se describe a sí mismo
            print(f" -> {srv}")
        print("----------------------------------------")

    @staticmethod
    def calcular_recaudacion_total(lista_servicios: list):
        """Recorre la lista y suma el resultado de calcular_costo_final()."""
        total = 0.0
        for srv in lista_servicios:
            # Polimorfismo: Cada objeto calcula su costo según su propia fórmula
            total += srv.calcular_costo_final()
        return total


# =========================================================
# ZONA DE PRUEBA (Se ejecuta solo al correr este archivo)
# =========================================================
if __name__ == "__main__":
    # Importamos las clases hijas SOLO para la prueba
    # (Asegúrate de que ruta_fija.py y servicio_expreso.py estén en la misma carpeta)
    try:
        from ruta_fija import RutaFija
        from servicio_expreso import ServicioExpreso

        print("--- TEST INDEPENDIENTE DEL GESTOR DE SERVICIOS ---\n")

        # 1. Instanciamos el gestor
        gestor = GestorServicios()

        # 2. Creamos datos de prueba
        print("1. Agregando servicios al gestor...")
        s1 = RutaFija("TEST-BUS", "Ruta A", 1.0, False)  # Costo: 1.0
        s2 = ServicioExpreso("TEST-TAXI", "Ruta B", 2.0, 4.0)  # Costo: 2.0 + (4*0.5) = 4.0

        gestor.agregar_servicio(s1)
        gestor.agregar_servicio(s2)

        # 3. Probamos los métodos estáticos
        print("2. Probando Reporte Masivo:")
        GestorServicios.imprimir_reporte_masivo(gestor.servicios)

        print("3. Probando Cálculo Total:")
        total = GestorServicios.calcular_recaudacion_total(gestor.servicios)
        print(f"   -> Total calculado: ${total:.2f} (Esperado: $5.00)")

    except ImportError:
        print("ERROR: No se encontraron los archivos 'ruta_fija.py' o 'servicio_expreso.py'.")
        print("Para probar el gestor, necesitas que esos archivos existan en la misma carpeta.")