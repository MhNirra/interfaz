import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text.config(state="normal")  # Habilitar edición temporalmente
            text.delete('1.0', tk.END)
            text.insert(tk.END, content)
            text.config(state="disabled")  # Deshabilitar edición nuevamente

def generate():
    selected_option = options_combo.get()
    if selected_option == "Execute Analysis":
        print("Execute Analysis selected")
    elif selected_option == "View Output":
        print("View Output selected")
    elif selected_option == "Other":
        print("Other selected")

root = tk.Tk()
root.title("Interfaz de Archivos")

# Barra de menú
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Menú Archivo
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Abrir archivo", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=root.quit)

# Marco principal
frame = ttk.Frame(root)
frame.pack(pady=20)

# Marco izquierdo
left_frame = ttk.Frame(frame)
left_frame.pack(side=tk.LEFT)

# Marco de opciones
options_frame = ttk.LabelFrame(left_frame, text="Opciones")
options_frame.pack(pady=10)

options_label = ttk.Label(options_frame, text="Seleccione una opción:")
options_label.pack(pady=10)

options_combo = ttk.Combobox(options_frame, values=["Execute Analysis", "View Output", "Other"], state="readonly")
options_combo.pack()

generate_button = ttk.Button(options_frame, text="Generar", command=generate)
generate_button.pack(pady=10)

# Marco central
center_frame = ttk.Frame(frame)
center_frame.pack(side=tk.LEFT, padx=10)

content_label = ttk.Label(center_frame, text="Contenido del archivo:")
content_label.pack(pady=10)

text = tk.Text(center_frame, state="disabled")  # Establecer el estado inicial a "disabled"
text.pack()

# Marco derecho
right_frame = ttk.Frame(frame)
right_frame.pack(side=tk.RIGHT)

# Marco de configuración
settings_frame = ttk.LabelFrame(right_frame, text="Configuración")
settings_frame.pack(pady=10)

# Valores predeterminados
default_values_frame = ttk.Frame(settings_frame)
default_values_frame.pack(pady=10)

temperature_label = ttk.Label(default_values_frame, text="Temperature:    0")
temperature_label.grid(row=0, column=0, padx=5, pady=5)
temperature_scale = ttk.Scale(default_values_frame, from_=0, to=2, length=200, orient=tk.HORIZONTAL)
temperature_scale.set(0)
temperature_scale.grid(row=0, column=1, padx=5, pady=5)
temperature_range_label = ttk.Label(default_values_frame, text="2")
temperature_range_label.grid(row=0, column=2, padx=5, pady=5)

top_p_label = ttk.Label(default_values_frame, text="Top_P: \t            0")
top_p_label.grid(row=1, column=0, padx=5, pady=5)
top_p_scale = ttk.Scale(default_values_frame, from_=0, to=1, length=200, orient=tk.HORIZONTAL)
top_p_scale.set(0)
top_p_scale.grid(row=1, column=1, padx=5, pady=5)
top_p_range_label = ttk.Label(default_values_frame, text="1")
top_p_range_label.grid(row=1, column=2, padx=5, pady=5)

# Marco de selección de modelos
model_frame = ttk.LabelFrame(right_frame, text="Modelo")
model_frame.pack(pady=10)

model_label = ttk.Label(model_frame, text="Seleccione un modelo:")
model_label.pack(pady=10)

model_combo = ttk.Combobox(model_frame, values=["Modelo 1", "Modelo 2", "Modelo 3"], state="readonly")
model_combo.pack()

root.mainloop()
