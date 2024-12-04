import telnetlib
import time
from comandos_zte import comandos  # Importa o dicionário de comandos


def executar_zte(
    host,
    tipo_comando,
    serial=None,
    placa=None,
    pon=None,
    alias=None,
    id=None,
    vlan=None,
):
    # Configurações do servidor Telnet
    USERNAME = "admin"
    PASSWORD = "@pr0gr4m4d0r@"
    PORT = 23  # Porta padrão do Telnet
    TIMEOUT = 50  # Tempo de espera para conexão
    PASSWORD_ENABLE = "g3r3nc1@"

    # Verifica se o comando existe no dicionário, senão usa o comando default
    comando_func = comandos.get(tipo_comando, comandos["unc"])
    # Comando formado para enviar para a olt
    comando = comando_func(
        placa=placa, pon=pon, serial=serial, alias=alias, id=id, vlan=vlan
    )

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
        tn.write((comando + "\n").encode("ascii"))
        print(comando)
        time.sleep(2)  # Aguarde a saída ser gerada
        output = tn.read_very_eager().decode("ascii")  # Capturar a saída
        print(output)

        tn.write(b"exit\n")
        tn.close()
    except Exception as e:
        print(f"Erro:  {e}")
        raise


# Teste com os comandos novos
# executar_zte("10.199.162.71", "unc")
# executar_zte("10.199.162.71", "localizar_onu", serial="ZTEGD2A1E0DD")
# executar_zte("10.199.162.71", "mostrar_ids", placa=5, pon=9)

