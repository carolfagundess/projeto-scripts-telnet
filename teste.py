import tkinter as tk

def capturar_texto():
    # Obtém o texto do campo de entrada
    texto = entrada.get()
    # Exibe o texto capturado
    print(f"Texto capturado: {texto}")
    # Você pode armazenar o valor em uma variável para uso posterior
    variavel_string = texto

# Criando a janela principal
janela = tk.Tk()
janela.title("Captura de Input")

# Criando o campo de entrada
entrada = tk.Entry(janela, width=30)
entrada.pack(pady=10)

# Botão para capturar o texto
botao = tk.Button(janela, text="Capturar", command=capturar_texto)
botao.pack(pady=10)

# Inicia o loop principal da interface
janela.mainloop()
