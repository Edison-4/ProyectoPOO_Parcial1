# Integrante:
# -- Chinga Michelle
# -- Ortiz Michael
# -- Plaza Edison
# -- Villao Carla

# main.py

from ruta_fija import RutaFija
from servicio_expreso import ServicioExpreso
from gestor_servicios import GestorServicios
from cliente import Cliente


def main():
    print("=== VERIFICACIÓN DE REQUISITOS FINAL ===\n")

    # 1. Crear objetos de clases hijas (RutaFija y ServicioExpreso)
    bus_normal = RutaFija("BUS-100", "Centro-Norte", 0.50, False)
    bus_pico = RutaFija("BUS-200", "Sur-Centro", 0.50, True)  # +20%
    taxi_vip = ServicioExpreso("TAXI-01", "Aeropuerto", 2.50, 10.0)

    # Prueba de validación (Distancia negativa)
    print(">>> Probando validación automática:")
    taxi_error = ServicioExpreso("TAXI-X", "Corta", 2.00, -50.0)  # Se corregirá a 1.0 km

    # 2. Crear Cliente (con validación de nombre)
    cliente = Cliente("  carlos andres  ", 50.00)

    # 3. Guardarlos en una lista (usando el Gestor)
    gestor = GestorServicios()
    gestor.agregar_servicio(bus_normal)
    gestor.agregar_servicio(bus_pico)
    gestor.agregar_servicio(taxi_vip)
    gestor.agregar_servicio(taxi_error)

    lista = gestor.servicios  # Esta es la lista de la superclase solicitada

    # 4. Ejecutar métodos heredados y propios
    print(f"\n[Heredado] ID Bus: {bus_normal.identificador}")
    print(f"[Propio] Distancia Taxi: {taxi_vip.distancia_km} km")

    # 5. Imprimir objetos usando __str__()
    print(f"\n[Impresión Objeto] {cliente}")
    print(f"[Impresión Objeto] {bus_pico}")

    # 6. Ejecutar los 2 MÉTODOS POLIMÓRFICOS obligatorios con la lista
    # Metodo 1: Reporte
    GestorServicios.imprimir_reporte_masivo(lista)

    # Metodo 2: Cálculo Matemático
    total = GestorServicios.calcular_recaudacion_total(lista)
    print(f"Recaudación Total Calculada: ${total:.2f}")


if __name__ == "__main__":
    main()