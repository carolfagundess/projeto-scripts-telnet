import tkinter as tk
from script_zte import executar_zte

def executar_comando(tipo_comando):
    host = entry_host.get()
    serial = entry_serial.get()
    placa = entry_placa.get()
    pon = entry_pon.get()
    pppoe = entry_pppoe.get()
    id = entry_id.get()
    vlan = entry_vlan.get()

    try:
        comando = f"Host: {host}, Tipo: {tipo_comando}, Serial: {serial}, Placa: {placa}, PON: {pon}, PPPoE: {pppoe}, ID: {id}, VLAN: {vlan}"
        command_text.delete("1.0", tk.END)
        command_text.insert(tk.END, comando)

        executar_zte(
            host=host,
            tipo_comando=tipo_comando,
            serial=serial,
            placa=placa if placa else None,
            pon=pon if pon else None,
            pppoe=pppoe,
            id=id if id else None,
            vlan=vlan if vlan else None,
        )
    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Erro: {e}")

# Criação da janela principal
root = tk.Tk()
root.title("Interface de Comandos ZTE")

# Campos de entrada
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

labels = ["Host:", "Serial:", "Placa:", "PON:", "PPPoE:", "ID:", "VLAN:"]
entries = []

for label_text in labels:
    frame = tk.Frame(frame_inputs)
    frame.pack(fill=tk.X, pady=2)
    label = tk.Label(frame, text=label_text, width=10, anchor="w")
    label.pack(side=tk.LEFT)
    entry = tk.Entry(frame)
    entry.pack(fill=tk.X, expand=True, padx=5)
    entries.append(entry)

entry_host, entry_serial, entry_placa, entry_pon, entry_pppoe, entry_id, entry_vlan = entries

# Botões para comandos
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

comandos = [
    ("Unconfigured", "unc"),
    ("Provisionamento", "provisionamento"),
    ("Localizar ONU", "localizar_onu"),
    ("Atenuação ONU", "atenuacao_onu"),
    ("Mostrar IDs", "mostrar_ids"),
    ("Quedas ONU", "quedas_onu"),
    ("Sinal ONU", "sinal_onu"),
]

for texto, tipo_comando in comandos:
    botao = tk.Button(frame_buttons, text=texto, command=lambda tc=tipo_comando: executar_comando(tc))
    botao.pack(side=tk.LEFT, padx=5)

# Áreas de texto para exibir comando e saída
frame_output = tk.Frame(root)
frame_output.pack(pady=10, fill=tk.BOTH, expand=True)

command_label = tk.Label(frame_output, text="Comando enviado:")
command_label.pack(anchor="w")
command_text = tk.Text(frame_output, height=5)
command_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

output_label = tk.Label(frame_output, text="Saída do comando:")
output_label.pack(anchor="w")
output_text = tk.Text(frame_output, height=10)
output_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Loop principal
root.mainloop()
