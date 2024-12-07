import tkinter as tk
from script_parks import executar_parks

# Dicionário de comandos mapeado para strings
comandos = {
    "unc": "unc",
    "summary": "summary",
    "ver_config": "ver_config",
    "provisionar": "provisionar",
    "ver_blacklist": "ver_blacklist",
}

def handle_command(command):
    """
    Função intermediária que recebe o comando do botão, coleta os inputs do usuário e executa a função.
    """
    host = entry_host.get()
    username = entry_username.get()
    password = entry_password.get()
    serial = entry_serial.get() or None
    placa = entry_placa.get() or None
    pon = entry_pon.get() or None
    alias = entry_alias.get() or None
    flow = entry_flow.get() or None

    # Chama a função executar_parks com os parâmetros coletados
    try:
        result = executar_parks(host, username, password, command, serial, placa, pon, alias, flow)
        output_text.insert(tk.END, f"Comando: {command}\n")
        output_text.insert(tk.END, f"Resultado: {result}\n\n")
    except Exception as e:
        output_text.insert(tk.END, f"Erro ao executar o comando '{command}': {str(e)}\n\n")

# Configuração da janela principal
root = tk.Tk()
root.title("Comandos Parks com Tkinter")
root.geometry("800x600")

# Frame principal para organização
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Frame esquerdo para inputs e botões
frame_left = tk.Frame(main_frame, width=200)
frame_left.pack(side="left", fill="y", padx=10, pady=10)

# Campos de entrada para parâmetros
tk.Label(frame_left, text="Host:").pack(anchor="w")
entry_host = tk.Entry(frame_left, width=25)
entry_host.pack(anchor="w")

tk.Label(frame_left, text="Username:").pack(anchor="w")
entry_username = tk.Entry(frame_left, width=25)
entry_username.pack(anchor="w")

tk.Label(frame_left, text="Password:").pack(anchor="w")
entry_password = tk.Entry(frame_left, width=25, show="*")
entry_password.pack(anchor="w")

tk.Label(frame_left, text="Serial:").pack(anchor="w")
entry_serial = tk.Entry(frame_left, width=25)
entry_serial.pack(anchor="w")

tk.Label(frame_left, text="Placa:").pack(anchor="w")
entry_placa = tk.Entry(frame_left, width=25)
entry_placa.pack(anchor="w")

tk.Label(frame_left, text="PON:").pack(anchor="w")
entry_pon = tk.Entry(frame_left, width=25)
entry_pon.pack(anchor="w")

tk.Label(frame_left, text="Alias:").pack(anchor="w")
entry_alias = tk.Entry(frame_left, width=25)
entry_alias.pack(anchor="w")

tk.Label(frame_left, text="Flow:").pack(anchor="w")
entry_flow = tk.Entry(frame_left, width=25)
entry_flow.pack(anchor="w")

# Botões para cada comando
def create_command_buttons():
    tk.Label(frame_left, text="Comandos:", font=("Arial", 12, "bold")).pack(anchor="w", pady=5)
    for command, command_string in comandos.items():
        button = tk.Button(frame_left, text=command.capitalize(), command=lambda c=command_string: handle_command(c), width=20)
        button.pack(anchor="w", pady=2)

create_command_buttons()

# Frame direito para exibir saída
frame_right = tk.Frame(main_frame, bg="white")
frame_right.pack(side="right", fill="both", expand=True, padx=10, pady=10)

output_text = tk.Text(frame_right, wrap="word", bg="white", fg="black", font=("Arial", 10))
output_text.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(frame_right, command=output_text.yview)
scrollbar.pack(side="right", fill="y")
output_text.config(yscrollcommand=scrollbar.set)

# Loop principal da interface gráfica
root.mainloop()