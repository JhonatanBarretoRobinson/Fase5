"""
Problema 5: Caluclo de horas trabajadas semanales
Curso: Fundamento de programacion (213022)
Estudiante: Jhonatan Barreto Robinson
"""

horas_semana = [
    ["Ana Perez", 8,8,8,8,8],
    ["Luis Gomez", 7,8,6,8,7],
    ["Maria Rodriguez", 8,8,8,7,6],
    ["Carlos Sanchez", 6,7,8,8,8],
    ["Sofia Martinez", 9,9,9,9,9]
]

UMBRAL_HORAS = 40

def calcular_Jornada(horas):
    """Calcular total de horas y clasificar jornada"""
    total= sum(horas)
    if total > UMBRAL_HORAS:
        return total, "Sobretiempo"
    else:
        return total, "Horario Estandar"
