import tkinter as tk
from tkinter import messagebox, ttk , PhotoImage
from ttkbootstrap import Style
from PIL import ImageTk, Image
# Establecer las preguntas para cada jugador
questions_player1 = [
    {
        "question": "¿Cuál de estos es el lenguaje de alto nivel?",
        "choices": ["A. C++", "B. vim", "C. Cobol", "D. P.H.P."],
        "answer": "D"
    },
    {
        "question": "¿Cuáles son los componentes internos de la computadora?",
        "choices": ["A. Mouse", "B. Procesador", "C. Teclado", "D. Batería"],
        "answer": "B"
    },
    {
        "question": "¿Cómo o qué es el sistema binario?",
        "choices": ["A. Cifra", "B. Entero", "C. Binario", "D. De dos dígitos"],
        "answer": "D"
    },
    {
        "question": "¿Cuál es el nombre del dueño de Microsoft?",
        "choices": ["A. Ricardo Blue", "B. Leonardo González", "C. Ricardo Martinelli", "D. Bill Gates"],
        "answer": "D"
    },
    {
        "question": "¿Transformación del modelo Entidad-Relación?",
        "choices": ["A. Cardinalidad", "B. Atributos", "C. Cadena", "D. Código"],
        "answer": "A"
    }
]

questions_player2 = [
    {
        "question": "¿Cuál es el país más grande del mundo?",
        "choices": ["A. Estados Unidos", "B. China", "C. Rusia", "D. Canadá"],
        "answer": "C"
    },
    {
        "question": "¿Qué fue el Holocausto Nazi?",
        "choices": ["A. Un terremoto", "B. Una masacre", "C. Un tornado", "D. Un arma"],
        "answer": "B"
    },
    {
        "question": "¿Quién fue Francisco Franco?",
        "choices": ["A. Poeta chileno", "B. Dictador español", "C. Escritor venezolano", "D. Independentista ecuatoriano"],
        "answer": "B"
    },
    {
        "question": "¿Quién es el mayor asesino en la historia?",
        "choices": ["A. Adolf Hitler", "B. Mao Zedong", "C. Iósif Stalin", "D. Ninguno de los anteriores"],
        "answer": "B"
    },
    {
        "question": "¿Cuál es el libro más vendido de la historia?",
        "choices": ["A. El Principito", "B. 100 años de soledad", "C. Harry Potter", "D. La Biblia"],
        "answer": "D"
    }
]

# Establecer quiz_data combinando las preguntas de ambos jugadores
quiz_data = questions_player1 + questions_player2

# Global variables
current_player = 1
player_scores = [0, 0]
current_question = 0
questions_per_player = 5

# Function to display the current question and choices for the current player
def show_question():
    global current_question
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")

    feedback_label.config(text="")
    next_btn.config(state="disabled")

# Function to check the selected answer and provide feedback
def check_answer(choice):
    global current_question, current_player
    question = quiz_data[current_question]
    selected_choice = chr(65 + choice)  # Convertir índice a letra: A, B, C, D

    if selected_choice == question["answer"]:
        player_scores[current_player - 1] += 1
        score_label.config(text="Puntuación Jugador {}: {}/{}".format(current_player, player_scores[current_player - 1], questions_per_player))
        feedback_label.config(text="¡Correcto!", foreground="green")
    else:
        feedback_label.config(text="Incorrecto", foreground="red")
        next_question()

    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Function to move to the next question or player
def next_question():
    global current_question, current_player
    current_question += 1

    if current_question % questions_per_player == 0:
        if current_player == 1:
            current_player = 2
            messagebox.showinfo("Turno del Jugador 2", "¡Turno del Jugador 2!")
            current_question -= questions_per_player  # Reiniciar preguntas para el Jugador 2
        else:
            messagebox.showinfo("Quiz Completado",
                                "Quiz Completado! Puntuación Jugador 1: {}/{} - Puntuación Jugador 2: {}/{}".format(player_scores[0], questions_per_player, player_scores[1], questions_per_player))
            root.destroy()
    show_question()

# Create the main window
root = tk.Tk()
root.title("Quiz App para 2 Jugadores")
root.geometry("600x500")
style = Style(theme="flatly")
barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

# Crear los menús desplegables
menu_archivo = tk.Menu(barra_menu)
menu_edicion = tk.Menu(barra_menu)
menu_visualizar = tk.Menu(barra_menu)
menu_ayuda = tk.Menu(barra_menu)

def seguridad():
       messagebox.showinfo("Seguridad", "Has seleccionado la opción de seguridad")
def Guardar():
       messagebox.showinfo("Guardar", "Has Guardado los Registro")  
       
       
def opcion_1():
    messagebox.showinfo("Seguridad", "Has seleccionado la opción de seguridad")

def opcion_2():
    messagebox.showinfo("Guardar", "Has seleccionado la opción Guardar registros")

def opcion_3():
    messagebox.showinfo("Actualizar", "Has seleccionado la opción Actualizar registros")

def opcion_4():
    messagebox.showinfo("Eliminar", "Has seleccionado la opción Eliminar registros")
    
def opcion_5():
    messagebox.showinfo("Acerca de", "Autor del programa:  Erick Miranda / Panamá 2024. Ejemplo de menú en Python")

def opcion_6():
    messagebox.showinfo("Visualizar", "Has seleccionado la opcion de Mostrar")

# Agregar opciones al menú Archivo
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Seguridad", command=seguridad)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)

# Agregar opciones al menú Edición
barra_menu.add_cascade(label="Registros", menu=menu_edicion)
menu_edicion.add_command(label="Guardar", command=Guardar)
menu_edicion.add_separator()
menu_edicion.add_command(label="Actualizar", command=opcion_3)
menu_edicion.add_separator()
menu_edicion.add_command(label="Eliminar", command=opcion_4)
menu_edicion.add_separator()
menu_edicion.add_command(label="Consultar", command=opcion_4)

# menu de visualizar 
barra_menu.add_cascade(label="Visualizar", menu=menu_visualizar)
menu_visualizar.add_command(label="Imagen", command=opcion_6)
menu_visualizar.add_separator()
menu_visualizar.add_command(label="Video", command=opcion_6)

# Agregar opciones al menú Ayuda
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Ver ayuda", command=opcion_5)
menu_ayuda.add_separator()
menu_ayuda.add_command(label="Acerca de", command=opcion_5)

#fondo++
image = PhotoImage(file = "imagen/fondo.png")
fondo=ttk.Label(root,image=image).place(x=0,y=0,relwidth=1,relheight=1)

# Configure the font size for the question and choice buttons
style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

# Create the question label
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)

# Create the choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Create the feedback label
feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

# Create the score label
score_label = ttk.Label(
    root,
    text="Puntuación Jugador 1: 0/{} - Puntuación Jugador 2: 0/{}".format(questions_per_player, questions_per_player),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Create the next button
next_btn = ttk.Button(
    root,
    text="Siguiente",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)
#boton invisble no tocar ni borrar

# Show the first question for the first player
show_question()


# Start the main event loop
root.mainloop()
