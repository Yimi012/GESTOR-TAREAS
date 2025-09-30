from repository import TaskRepository

def main():
    repo = TaskRepository()

    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            title = input("Título de la tarea: ")
            task = repo.add_task(title)
            print(f"Tarea agregada: {task.title}")

        elif opcion == "2":
            tasks = repo.list_tasks()
            if not tasks:
                print("No hay tareas registradas.")
            else:
                for t in tasks:
                    estado = "✔" if t.completed else "✘"
                    print(f"{t.id}. {t.title} [{estado}]")

        elif opcion == "3":
            task_id = int(input("ID de la tarea a completar: "))
            task = repo.complete_task(task_id)
            if task:
                print(f"Tarea completada: {task.title}")
            else:
                print("Tarea no encontrada.")

        elif opcion == "4":
            task_id = int(input("ID de la tarea a eliminar: "))
            if repo.delete_task(task_id):
                print("Tarea eliminada.")
            else:
                print("Tarea no encontrada.")

        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
