import telnetlib
from comandos_parks import comandos  # Importa o dicionário de comandos


def executar_parks(
    host,
    username,
    password,
    tipo_comando,
    serial=None,
    placa=None,
    pon=None,
    alias=None,
    flow=None,
):
    # Configurações do servidor Telnet
    PORT = 23  # Porta padrão do Telnet
    TIMEOUT = 50  # Tempo de espera para conexão

    # Verifica se o comando existe no dicionário, senão usa o comando default
    comando_func = comandos.get(tipo_comando, comandos["unc"])
    comando = comando_func(
        serial, placa, pon, alias, flow
    )  # Chama a função correspondente com os parâmetro

    try:
        # Conectar ao servidor
        tn = telnetlib.Telnet(host, PORT, TIMEOUT)

        # Tratar o prompt inicial ("Press <RETURN> to get started")
        tn.read_until(b"Press <RETURN> to get started")
        tn.write(b"\n")  # Envia o Enter para avançar

        # Login
        tn.read_until(b"Username:")
        tn.write(username.encode("ascii") + b"\n")
        tn.read_until(b"Password:")
        tn.write(password.encode("ascii") + b"\n")

        # Confirmar que chegou ao prompt da OLT
        prompt = tn.read_until(b"#", timeout=10)
        print(prompt.decode("ascii"))

        # Enviar comando
        tn.write((comando + "\n").encode("ascii"))

        # Capturar resposta do comando até o próximo prompt
        output = tn.read_until(b"#", timeout=10).decode("ascii")

        # Fechar a conexão
        tn.write(b"exit\n")
        tn.close()

        # Retornar ou imprimir o resultado
        print(output)
        return output

    except Exception as e:
        print(f"Erro: {e}")
        raise  # Relevantar exceção para depuração


# Testes com diferentes comandos
# executar_parks("10.199.163.21", "admin", "tcamp@gpon", "unc")
# executar_parks("10.199.163.21", "admin", "tcamp@gpon", "ver_config", serial=serial)
# executar_parks("10.199.163.21", "admin", "tcamp@gpon", "sinal_onus", placa=1, pon=2)
# executar_parks("10.199.163.21", "admin", "tcamp@gpon", "ver_blacklist")

# Em teste
# Provisionar (serial, placa e pon, alias, flow)
# executar_parks()
