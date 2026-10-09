import csv
from pathlib import Path


todos = []
TODOS_FILE = Path(__file__).resolve().parent / "todos.csv"


def add_one_task(title):
    title = title.strip()
    if not title:
        print("El titulo no puede estar vacio.")
        return False
    todos.append(title)
    print("Tarea agregada.")
    return True


def print_list():
    if not todos:
        print("No hay tareas pendientes.")
        return
    print("\nTareas pendientes:")
    for position, title in enumerate(todos, start=1):
        print(f"{position}. {title}")


def delete_task(number_to_delete):
    if isinstance(number_to_delete, bool) or not isinstance(
        number_to_delete, (str, int)
    ):
        print("Introduce una posicion numerica entera.")
        return False
    try:
        position = int(number_to_delete)
    except ValueError:
        print("Introduce una posicion numerica entera.")
        return False
    if not 1 <= position <= len(todos):
        print("La posicion no existe en la lista.")
        return False
    title = todos.pop(position - 1)
    print(f"Tarea eliminada: {title}")
    return True


def save_todos():
    try:
        with TODOS_FILE.open("w", encoding="utf-8", newline="") as todos_file:
            writer = csv.writer(todos_file)
            writer.writerows([title] for title in todos)
    except (OSError, UnicodeError, csv.Error) as error:
        print(f"No se pudieron guardar las tareas: {error}")
        return False
    print("Tareas guardadas en todos.csv.")
    return True


def load_todos():
    loaded_todos = []
    try:
        with TODOS_FILE.open("r", encoding="utf-8", newline="") as todos_file:
            reader = csv.reader(todos_file, strict=True)
            for row in reader:
                if not row:
                    continue
                if len(row) != 1 or not row[0].strip():
                    raise ValueError(
                        f"Fila {reader.line_num}: se esperaba un titulo no vacio."
                    )
                loaded_todos.append(row[0].strip())
    except FileNotFoundError:
        print("No existe todos.csv. Guarda las tareas para crearlo.")
        return False
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        print(f"No se pudieron cargar las tareas: {error}")
        return False
    todos[:] = loaded_todos
    print("Tareas cargadas desde todos.csv.")
    return True


def main():
    saved_todos = todos.copy()
    print("TODO LIST CLI")
    print(f"Archivo de tareas: {TODOS_FILE}")
    try:
        while True:
            print(
                "\n1. Agregar tarea\n"
                "2. Mostrar tareas\n"
                "3. Eliminar tarea\n"
                "4. Guardar tareas\n"
                "5. Cargar tareas\n"
                "6. Salir"
            )
            option = input("Elige una opcion: ").strip()
            if option == "1":
                add_one_task(input("Titulo de la tarea: "))
            elif option == "2":
                print_list()
            elif option == "3":
                print_list()
                if todos:
                    delete_task(input("Posicion de la tarea a eliminar: "))
            elif option == "4":
                if save_todos():
                    saved_todos = todos.copy()
            elif option in ("5", "6"):
                if todos != saved_todos:
                    confirmation = input(
                        "Hay cambios sin guardar. Descartarlos? (s/n): "
                    ).strip().lower()
                    if confirmation != "s":
                        print("Operacion cancelada. Puedes guardar con la opcion 4.")
                        continue
                if option == "5":
                    if load_todos():
                        saved_todos = todos.copy()
                else:
                    print("Hasta luego.")
                    return
            else:
                print("Opcion invalida. Elige un numero del 1 al 6.")
    except (EOFError, KeyboardInterrupt):
        print("\nSesion terminada.")
        if todos != saved_todos:
            print("Los cambios sin guardar no se han escrito en todos.csv.")


if __name__ == "__main__":
    main()