# Este archivo me ayuda a convertir la carpeta "logic" en un paquete de Python. (package)

from .inventory_tools import get_total_stock, get_low_stock_count

__all__ = ["get_total_stock", "get_low_stock_count"]