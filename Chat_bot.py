from nltk.chat.util import Chat, reflections

# Pares de patrones y respuestas
pares = [
    [r"hola|buenas", 
     ["Hola, ¿cómo puedo ayudarte hoy?"]],
    [r"Ofrecen alguna carrera de tecnico?", 
     ["Sí, ofrecemos una variedad de carreras en la universidad de oriente. ¿Te gustaría saber más?"]],
    [r"cuales son los horarios de la carrera?", 
     ["Los horarios de la universidad de oriente son de lunes a viernes de 8:00 a 18:00."]],
    [r"como puedo contactar a la universidad", 
     ["Puedes contactar a la universidad de oriente enviando un correo a www.univo.edu.sv"]],
    [r"gracias|adios", 
     ["¡De nada! ¡Hasta luego!"]],
]

# Función para iniciar el chat
def chatear():
    print("Hola, soy el chip el bot de la universidad de oriente. Escribe algo para comenzar.")
    chat = Chat(pares, reflections)
    chat.converse()

if __name__ == "__main__":
    chatear()
