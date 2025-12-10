# ProyectoPOO_Parcial1

Este proyecto consiste en un Sistema de Gestión de Transporte Urbano desarrollado en Python bajo el paradigma de Programación Orientada a Objetos, diseñado para administrar y cotizar servicios de transporte heterogéneos como rutas fijas y viajes expresos. La solución implementa una arquitectura robusta basada en herencia (con una superclase ServicioTransporte), encapsulamiento (para validar datos críticos como costos y distancias) y polimorfismo, lo que permite procesar listas mixtas de servicios para generar reportes unificados y calcular la recaudación total aplicando reglas de negocio específicas (recargos por hora pico o tarifas por kilometraje) de manera automática y escalable.

# 1. ServicioTransporte (Superclase / Clase Padre)
Es la base de todo el sistema. Su función es establecer la estructura común que compartirán todos los tipos de transporte, evitando la duplicidad de código.
Responsabilidad: Define los atributos básicos (identificador, ruta y costo base) y los métodos fundamentales.
Encapsulamiento: Protege el atributo _costo_base utilizando un setter que impide que se ingresen valores monetarios negativos (automáticamente los convierte a 0).
Importancia: Contiene el método mágico __str__, lo que permite que cualquier objeto hijo pueda imprimirse como texto legible en la consola sin necesidad de código extra.
# 2. RutaFija (Subclase / Clase Hija)
Representa servicios de transporte masivo como autobuses o metrovías, que operan con horarios establecidos.
Herencia: Hereda todo de ServicioTransporte.
Atributo Propio: _es_hora_pico (booleano), que indica si el viaje ocurre en un horario de alta demanda.
Polimorfismo: Sobrescribe el método calcular_costo_final(). En lugar de devolver solo el costo base, verifica si es horario pico y, de ser así, aplica un recargo del 20%.
# 3. ServicioExpreso (Subclase / Clase Hija)
Representa servicios personalizados bajo demanda, como taxis o transporte privado (Uber/Cabify).
Herencia: Hereda todo de ServicioTransporte.
Atributo Propio: _distancia_km (flotante), que almacena cuánto recorrió el vehículo. Incluye validación para evitar distancias negativas.
Constante: Define TARIFA_KM (0.50) como un valor fijo para el cálculo.
Polimorfismo: Sobrescribe calcular_costo_final() aplicando una fórmula matemática distinta: Costo Base + (Distancia * Tarifa por Km).
# 4. Cliente (Clase Independiente)
Representa al usuario que consume el servicio. Es una clase sencilla diseñada para interactuar con el sistema a nivel de datos.
Responsabilidad: Almacena la información del usuario (nombre y saldo).
Función: Sirve para darle contexto al sistema (saber quién está viajando), aunque en esta versión no hereda de transporte, ya que es una entidad lógica distinta.
# 5. GestorServicios (Clase Gestora / Controlador)
Es el "cerebro" administrativo del proyecto. No representa un vehículo, sino la administración de la flota.
Manejo de Listas: Contiene una lista (self._servicios) donde almacena objetos mezclados (tanto autobuses como taxis).
Polimorfismo Puro: Sus métodos estáticos (imprimir_reporte_masivo y calcular_recaudacion_total) reciben la lista de servicios y los tratan a todos por igual.
Al llamar a .calcular_costo_final(), el gestor no necesita saber si el objeto es un Bus o un Taxi; Python decide automáticamente qué fórmula usar dependiendo del objeto, logrando un cálculo total preciso sin if/else complejos.
