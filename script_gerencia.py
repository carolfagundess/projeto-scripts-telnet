import telnetlib
import time


def executar_gerencia(host, command):
    """
    Executa o Telnet para se conectar à OLT e retorna o resultado do comando.
    Possui o comando enable
    """
    PORT = 23
    TIMEOUT = 50
    USERNAME = "admin"
    PASSWORD = "@pr0gr4m4d0r@"
    PASSWORD_ENABLE = "g3r3nc1@"

    try:
        # Conectar ao servidor
        tn = telnetlib.Telnet(host, PORT, TIMEOUT)
        tn.read_until(b"Username:")
        tn.write(USERNAME.encode("ascii") + b"\n")
        tn.read_until(b"Password:")
        tn.write(PASSWORD.encode("ascii") + b"\n")

        # Enviar comandos
        tn.write(b"enable\n")
        time.sleep(1)
        tn.write(PASSWORD_ENABLE.encode("ascii") + b"\n")
        time.sleep(1)
        tn.write(b"terminal length 512\n")
        tn.write((command + "\n").encode("ascii"))
        time.sleep(1)
        tn.write(b"exit\n")

        # Captura da saída
        output = tn.read_very_eager().decode("ascii")
        tn.close()

        return output
    except Exception as e:
        return f"Erro ao executar Telnet: {e}"

