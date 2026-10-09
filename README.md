# danifer24-todo-list-cli-python

Gestor de tareas de terminal con Python 3 y su biblioteca estandar.
No requiere instalar dependencias.

## Ejecutar

```sh
python3 main.py
```

## Menu

```text
TODO LIST CLI

1. Agregar tarea
2. Mostrar tareas
3. Eliminar tarea
4. Guardar tareas
5. Cargar tareas
6. Salir
```

El menu se repite tras cada accion: puedes agregar tantas tareas como necesites
en una misma ejecucion. Los titulos no pueden estar vacios. Las posiciones
empiezan en 1 y se recalculan al eliminar una tarea. Para cambiar un titulo,
elimina la tarea y agrega otra.

## Guardar y cargar

La lista empieza vacia. Usa la opcion 4 para guardar y la opcion 5 para recuperar
las tareas despues de reiniciar. El archivo `todos.csv` se crea junto a
`main.py`, independientemente del directorio desde el que ejecutes el programa.
Se utiliza UTF-8 y una columna por fila, sin cabecera. Se admiten tildes,
comas y comillas en los titulos.

Guardar sobrescribe el archivo; cargar reemplaza la lista en memoria, no agrega
duplicados a la lista existente. Un archivo vacio carga una lista vacia.
Si el archivo no existe o no es valido, la lista en memoria se conserva.
Se pide confirmacion antes de cargar o salir cuando hay cambios sin guardar.
Cancelar permite volver al menu para guardarlos. Ctrl+C o el fin de la entrada
terminan la sesion sin guardar automaticamente.

## Funciones

- `add_one_task(title)`: agrega un titulo a la lista en memoria.
- `print_list()`: muestra las tareas con sus posiciones numericas.
- `delete_task(number_to_delete)`: elimina por posicion, empezando en 1.
- `save_todos()`: guarda la lista en `todos.csv`.
- `load_todos()`: carga el archivo hacia la lista en memoria.

Las funciones que modifican o persisten la lista devuelven `True` si tienen
exito y `False` si encuentran una entrada invalida o un error de archivo.