"""
Problema 5: Caluclo de horas trabajadas semanales
Curso: Fundamento de programacion (213022)
Estudiante: Jhonatan Barreto Robinson
"""

horas_semana = [
    ["Ana Perez", 8, 8, 8, 8, 8],
    ["Luis Gomez", 7, 8, 6, 8, 7],
    ["Maria Rodriguez", 8, 8, 8, 7, 6],
    ["Carlos Sanchez", 6, 7, 8, 8, 8],
    ["Sofia Martinez", 9, 9, 9, 9, 9]
]

UMBRAL_HORAS = 40

def calcular_jornada(horas):
    """Calcular total de horas y clasificar jornada"""
    total= sum(horas)
    if total > UMBRAL_HORAS:
        return total, "Sobretiempo"
    else:
        return total, "Horario Estandar"
def mostrar_informe():
        """Muestra el informe completo"""
        print("=" * 50)
        print("INFORME DE HORAS TRABAJADAS")
        print("=" * 50) 
    
        for recurso in horas_semana:
            nombre = recurso[0]
            horas = recurso[1:]
            total, clasificacion = calcular_jornada(horas)

            print (f"\nRecurso: {nombre}")
            print (f" horas: L:{horas[0]} M:{horas[1]} Mi:{horas[2]} J:{horas[3]} V:{horas[4]}")
            print (f" Total semanales: {total} horas")
            print (f"Clasificación: {clasificacion}")
            print("=" * 50)
mostrar_informe() 