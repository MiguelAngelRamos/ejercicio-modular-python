# Lógica de cálculo y filtrado

"""
Crear un programa modular en Python que procese una lista de existencias para identificar productos críticos y calcular métricas de inventario.

Modularización: Crear funciones específicas para:
- Calcular el stock total.
- Filtrar productos con stock bajo (menor a un límite dado).
"""

def get_total_stock(stock_list:list) -> int:
    """Calcula el stock total sumando las cantidades de la lista."""
    total = 0
    for quantity in stock_list:
        total = total + quantity # se puede resumir en  total += quantity
    return total

def get_low_stock_count(stock_list:list, limit:int) -> int:
    """Cuenta cuántos productos tienen stock menor al límite dado."""
    count = 0
    index = 0

    while index < len(stock_list):
        if stock_list[index] < limit:
            count = count + 1 # se puede resumir en count += 1
        index = index + 1 # Necesito moverme al siguiente elemento de la lista
    return count



