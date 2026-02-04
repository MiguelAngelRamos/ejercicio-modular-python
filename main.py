# Punto de entrada (UI y ejecución del programa)
# from logic.inventory_tools import get_total_stock, get_low_stock_count

from logic import get_total_stock, get_low_stock_count

def run_app():
    # Datos de ejemplo
    inventory = [50, 20, 5, 0, 15, 100, 3]
    MINIMUM_REQUIRED = 15 # Constante para stock critico

    is_running = True

    while is_running:
        print("=== Gestión de Inventario ===")
        print("1. Ver reporte general")
        print("2. Salir")

        choice = input("Seleccione una opción (1-2): ")

        if choice == '1':
            # Invocamos las funciones del módulo de lógica
            total = get_total_stock(inventory)
            critical = get_low_stock_count(inventory, MINIMUM_REQUIRED)

            print(f"\nReporte de Inventario:")
            print(f"Stock Total: {total}")
            print(f"Productos con Stock Crítico (menos de {MINIMUM_REQUIRED}): {critical}\n")

        elif choice == '2':
            print("Saliendo de la aplicación.")
            is_running = False
        else:
            print("Opción inválida. Por favor, intente de nuevo.\n")

## Este es el punto de entrada del programa, donde se ejecuta la función principal `run_app()`, que maneja la interfaz de usuario y la lógica de ejecución del programa.
if __name__ == "__main__":
    run_app()