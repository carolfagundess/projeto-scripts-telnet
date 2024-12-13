import tkinter as tk
from tkinter import ttk, messagebox
from script_zte import executar_zte  # Importa a função que executa o comando
from comandos_zte import comandos

# Função para configurar os inputs conforme o tipo de comando
def configurar_inputs(tipo_comando):
    # Limpa os inputs anteriores
    for widget in input_frame.winfo_children():
        widget.grid_forget()

    if tipo_comando == "unc":
        placa_label.grid(row=0, column=0, sticky="e")
        placa_combobox.grid(row=0, column=1)

    elif tipo_comando == "mostrar_ids":
        placa_label.grid(row=0, column=0, sticky="e")
        placa_combobox.grid(row=0, column=1)
        pon_label.grid(row=1, column=0, sticky="e")
        pon_combobox.grid(row=1, column=1)

    elif tipo_comando == "configurar_onu":
        placa_label.grid(row=0, column=0, sticky="e")
        placa_combobox.grid(row=0, column=1)
        pon_label.grid(row=1, column=0, sticky="e")
        pon_combobox.grid(row=1, column=1)
        pppoe_label.grid(row=2, column=0, sticky="e")
        pppoe_entry.grid(row=2, column=1)
        vlan_label.grid(row=3, column=0, sticky="e")
        vlan_entry.grid(row=3, column=1)
        serial_label.grid(row=4, column=0, sticky="e")
        serial_entry.grid(row=4, column=1)
        id_label.grid(row=5, column=0, sticky="e")
        id_combobox.grid(row=5, column=1)

# Função para executar o comando com os dados fornecidos
def executar_comando(tipo_comando):
    host = host_entry.get()
    serial = serial_entry.get()
    placa = placa_combobox.get()
    pon = pon_combobox.get()
    pppoe = pppoe_entry.get()
    id_val = id_combobox.get()
    vlan = vlan_entry.get()

    if not host or not tipo_comando:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios.")
        return

    try:
        resultado = executar_zte(host, tipo_comando, serial, placa, pon, pppoe, id_val, vlan)
        resultado_text.delete(1.0, tk.END)  # Limpa a área de texto
        resultado_text.insert(tk.END, f"Comando executado: {resultado['comando']}\n")
        resultado_text.insert(tk.END, f"Resultado: {resultado['output']}\n")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao executar o comando: {e}")

# Interface Gráfica
root = tk.Tk()
root.title("Interface Telnet ZTE")

# Host
tk.Label(root, text="Host:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
host_entry = tk.Entry(root, width=30)
host_entry.grid(row=0, column=1, padx=10, pady=5)

# Tipo de Comando
tk.Label(root, text="Tipo de Comando:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
tipo_comando_var = ttk.Combobox(root, values=list(comandos.keys()), state="readonly", width=27)
tipo_comando_var.grid(row=1, column=1, padx=10, pady=5)

# Frame para inputs específicos do comando
input_frame = tk.Frame(root)
input_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Labels e inputs dos parâmetros
placa_label = tk.Label(input_frame, text="Placa:")
placa_combobox = ttk.Combobox(input_frame, values=["1", "2", "3"], state="readonly")
pon_label = tk.Label(input_frame, text="PON:")
pon_combobox = ttk.Combobox(input_frame, values=["1", "2", "3"], state="readonly")
pppoe_label = tk.Label(input_frame, text="PPPoE:")
pppoe_entry = tk.Entry(input_frame)
serial_label = tk.Label(input_frame, text="Serial:")
serial_entry = tk.Entry(input_frame)
id_label = tk.Label(input_frame, text="ID:")
id_combobox = ttk.Combobox(input_frame, values=["1", "2", "3"], state="readonly")
vlan_label = tk.Label(input_frame, text="VLAN:")
vlan_entry = tk.Entry(input_frame)

# Botões de comando
def criar_botoes_comando():
    comandos_list = list(comandos.keys())
    for idx, comando in enumerate(comandos_list):
        button = tk.Button(root, text=comando, command=lambda c=comando: configurar_inputs(c))
        button.grid(row=3 + idx, column=0, columnspan=2, pady=5, padx=10, sticky="ew")

criar_botoes_comando()

# Botão de execução
executar_button = tk.Button(root, text="Executar Comando", command=lambda: executar_comando(tipo_comando_var.get()))
executar_button.grid(row=4 + len(comandos), column=0, columnspan=2, pady=10)

# Área de texto para mostrar o resultado
resultado_text = tk.Text(root, width=60, height=15)
resultado_text.grid(row=5 + len(comandos), column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
