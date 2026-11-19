tareas = []
def agregar_tarea(titulo):
	if not titulo.strip():
		raise ValueError("Titulo Vacio")
	tareas.append(titulo.strip())
def listar_tareas():
	return tareas
def eliminar_tarea(i):
	tareas.pop(i)