import tkinter as tk
from tkinter import ttk, scrolledtext
from primeira_part import executar_gerencia
from script_show import executar_show_configs


def executar_ids_interface():
    resultado = executar_gerencia()
    texto_saida.delete(1.0, tk.END)
    texto_saida.insert(tk.END, resultado)


def executar_nao_configuradas():
    resultado = executar_show_configs()
    texto_saida.delete(1.0, tk.END)
    texto_saida.insert(tk.END, resultado)


# Funções placeholder para os novos botões
def placeholder_acao(nome):
    texto_saida.delete(1.0, tk.END)
    texto_saida.insert(tk.END, f"Ação executada: {nome}")


# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Configuração de ONUs em OLT ZTE")
janela.geometry("900x700")
janela.resizable(False, False)

# Definir estilo do ttk
style = ttk.Style(janela)
style.theme_use("clam")

# Estilo para LabelFrame
style.configure("Custom.TLabelframe", font=("Arial", 12))
style.configure("Custom.TLabelframe.Label", font=("Arial", 12))

# Frame principal
frame_principal = ttk.Frame(janela)
frame_principal.pack(fill="both", expand=True, padx=5, pady=5)
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)

# Frame esquerdo para informações da ONU
frame_esquerdo = ttk.LabelFrame(
    frame_principal, text="Informações da ONU", style="Custom.TLabelframe"
)
frame_esquerdo.grid(row=0, column=0, sticky="nsw", padx=10, pady=10)

label_iphost = ttk.Label(frame_esquerdo, text="IP da OLT", font=("Arial", 10))
label_iphost.grid(row=0, column=0, pady=10, sticky="w")
entry_iphost = ttk.Entry(frame_esquerdo, font=("Arial", 10), width=14)
entry_iphost.grid(row=0, column=1, pady=10)

# Inputs para informações da ONU
label_placas = ttk.Label(frame_esquerdo, text="Placa/Slot", font=("Arial", 10))
label_placas.grid(row=1, column=0, pady=10, sticky="w")
combo_placas = ttk.Combobox(
    frame_esquerdo, values=[str(i) for i in range(1, 21)], font=("Arial", 12), width=10
)
combo_placas.grid(row=1, column=1, pady=10)

label_pons = ttk.Label(frame_esquerdo, text="Pon", font=("Arial", 10))
label_pons.grid(row=2, column=0, pady=10, sticky="w")
combo_pons = ttk.Combobox(
    frame_esquerdo, values=[str(i) for i in range(1, 21)], font=("Arial", 12), width=10
)
combo_pons.grid(row=2, column=1, pady=10)

label_ids = ttk.Label(frame_esquerdo, text="ID:", font=("Arial", 12))
label_ids.grid(row=3, column=0, pady=10, sticky="w")
entry_ids = ttk.Entry(frame_esquerdo, font=("Arial", 8), width=12)
entry_ids.grid(row=3, column=1, pady=10)

# Frame direito para botões classificados
frame_direito = ttk.Frame(frame_principal)
frame_direito.grid(row=0, column=1, sticky="nse", padx=5, pady=5)

# Subframe para botões de "Provisionamento de ONU"
frame_provisionamento_onu = ttk.LabelFrame(
    frame_direito, text="Provisionamento de ONU ZTE", style="Custom.TLabelframe"
)
frame_provisionamento_onu.grid(row=0, column=1, sticky="ew", pady=5, padx=5)

botoes_provisionamento = [
    ("Mostrar ID da interface", executar_ids_interface),
    (
        "Provisionar ONU F670L - C650",
        lambda: placeholder_acao("Provisionar ONU F670L - C650"),
    ),
    ("Provisionar ONU F670L", lambda: placeholder_acao("Provisionar ONU F670L")),
    (
        "Provisionar ONU 601 BDG - C650",
        lambda: placeholder_acao("Provisionar ONU 601 BDG - C650"),
    ),
    ("Provisionar ONU 601 BDG", lambda: placeholder_acao("Provisionar ONU 601 BDG")),
    ("ONUs Não Configuradas", executar_nao_configuradas),
]

# Subframe para botões de "Informações de uma ONU"
frame_informacoes_onu = ttk.LabelFrame(
    frame_direito, text="Informações de uma ONU - OLT ZTE", style="Custom.TLabelframe"
)
frame_informacoes_onu.grid(row=0, column=2, sticky="ew", pady=5, padx=5)

botoes_informacoes = [
    "Mostrar atenuação sinal",
    "Mostrar provisionamento da ONU",
    "Mostrar sinal da ONU",
    "Mostrar quedas da ONU",
    "Reiniciar ONU",
    "Mostrar status da LAN na ONU - C650",
    "Mostrar provisionamento da ONU - C650",
    "Localizar ONU pelo serial",
]

for i, nome in enumerate(botoes_informacoes):
    botao = ttk.Button(
        frame_informacoes_onu,
        text=nome,
        command=lambda n=nome: placeholder_acao(n),
        style="Accent.TButton",
    )
    botao.grid(row=i, column=0, pady=2, sticky="ew")


for i, (nome, comando) in enumerate(botoes_provisionamento):
    botao = ttk.Button(
        frame_provisionamento_onu, text=nome, command=comando, style="Accent.TButton"
    )
    botao.grid(row=i, column=0, pady=2, sticky="ew")

# Área de texto para saída
frame_saida = ttk.Frame(frame_principal)
frame_saida.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=10)
frame_saida.grid_rowconfigure(0, weight=1)
frame_saida.grid_columnconfigure(0, weight=1)

texto_saida = scrolledtext.ScrolledText(
    frame_saida,
    width=80,
    height=20,
    wrap=tk.WORD,
    font=("Courier", 8),
    borderwidth=2,
    relief="solid",
)
texto_saida.grid(row=0, column=0, sticky="nsew")

# Configuração do tema Accent
style.configure(
    "Accent.TButton", background="#0078d7", foreground="white", font=("Arial", 8)
)

# Rodar a interface
janela.mainloop()
