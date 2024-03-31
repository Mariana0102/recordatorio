from datetime import datetime, timedelta

class Tarea:
    def __init__(self, titulo, descripcion, fecha_vencimiento=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.completada = False

    def completar(self):
        self.completada = True

class GestorTareas:
    def __init__(self):
        self.tareas_pendientes = []
        self.tareas_completadas = []

    def agregar_tarea(self, titulo, descripcion, fecha_vencimiento=None):
        tarea = Tarea(titulo, descripcion, fecha_vencimiento)
        self.tareas_pendientes.append(tarea)

    def marcar_completada(self, tarea):
        tarea.completar()
        self.tareas_pendientes.remove(tarea)
        self.tareas_completadas.append(tarea)

    def obtener_tareas_pendientes(self):
        return self.tareas_pendientes

    def obtener_tareas_completadas(self):
        return self.tareas_completadas

class NotificadorTareas:
    def __init__(self, gestor_tareas):
        self.gestor_tareas = gestor_tareas

    def notificar_tareas_proximas(self):
        tareas_proximas = [tarea for tarea in self.gestor_tareas.obtener_tareas_pendientes() if tarea.fecha_vencimiento is not None and tarea.fecha_vencimiento - datetime.now() <= timedelta(days=1)]
        for tarea in tareas_proximas:
            print(f"¡Recordatorio! La tarea '{tarea.titulo}' está próxima a su fecha de vencimiento.")

class VistaConsola:
    def __init__(self, gestor_tareas):
        self.gestor_tareas = gestor_tareas

    def mostrar_menu(self):
        print("===== Gestor de Tareas =====")
        print("1. Agregar Tarea")
        print("2. Marcar Tarea como Completada")
        print("3. Ver Tareas Pendientes")
        print("4. Ver Tareas Completadas")
        print("5. Salir")

    def ejecutar(self):
        notificador = NotificadorTareas(self.gestor_tareas)
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                titulo = input("Ingrese el título de la tarea: ")
                descripcion = input("Ingrese la descripción de la tarea: ")
                fecha_vencimiento = input("Ingrese la fecha de vencimiento (formato: YYYY-MM-DD): ")
                if fecha_vencimiento:
                    fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
                self.gestor_tareas.agregar_tarea(titulo, descripcion, fecha_vencimiento)
            elif opcion == "2":
                tareas_pendientes = self.gestor_tareas.obtener_tareas_pendientes()
                if tareas_pendientes:
                    print("Tareas Pendientes:")
                    for i, tarea in enumerate(tareas_pendientes):
                        print(f"{i+1}. {tarea.titulo}")
                    idx = int(input("Seleccione el número de la tarea que desea marcar como completada: "))
                    tarea = tareas_pendientes[idx-1]
                    self.gestor_tareas.marcar_completada(tarea)
                else:
                    print("No hay tareas pendientes.")
            elif opcion == "3":
                tareas_pendientes = self.gestor_tareas.obtener_tareas_pendientes()
                if tareas_pendientes:
                    print("Tareas Pendientes:")
                    for i, tarea in enumerate(tareas_pendientes):
                        print(f"{i+1}. {tarea.titulo} - {tarea.descripcion}")
                else:
                    print("No hay tareas pendientes.")
            elif opcion == "4":
                tareas_completadas = self.gestor_tareas.obtener_tareas_completadas()
                if tareas_completadas:
                    print("Tareas Completadas:")
                    for i, tarea in enumerate(tareas_completadas):
                        print(f"{i+1}. {tarea.titulo} - {tarea.descripcion}")
                else:
                    print("No hay tareas completadas.")
            elif opcion == "5":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    gestor_tareas = GestorTareas()
    vista = VistaConsola(gestor_tareas)
    vista.ejecutar()


