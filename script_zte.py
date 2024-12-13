import telnetlib
import time
from comandos_zte import comandos  # Importa o dicionário de comandos


def executar_zte(
    host,
    tipo_comando,
    serial=None,
    placa=None,
    pon=None,
    pppoe=None,
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
    # comando_func sera o respectivo comando dentro de comandos zte
    comando_func = comandos.get(tipo_comando, comandos["unc"])
    # Comando formado para enviar para a olt
    comando = comando_func(
        placa=placa, pon=pon, serial=serial, pppoe=pppoe, id=id, vlan=vlan
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
        return {"comando": comando, "output": output}
    except Exception as e:
        print(f"Erro:  {e}")
        raise


# Teste com os comandos novos
# executar_zte("10.199.162.71", "unc")

# executar_zte("10.199.162.71", "mostrar_ids", placa=8, pon=13)
# executar_zte("10.199.221.110", "provisionamento", placa=3, pon=16, id=61)
# executar_zte("10.199.221.110", "localizar_onu",serial="ZTEGD4F3857B")
# executar_zte("10.199.228.68", "atenuacao_onu", placa=1, pon=1, id=1)
# executar_zte("10.199.228.68", "quedas_onu", placa=1, pon=1, id=5)
# executar_zte("10.199.228.68", "sinal_onu", placa=1, pon=1, id=2)

# Funcinou teste de provisionamento na ZTE
# executar_zte("10.199.162.71","configurar_onu", placa=8, pon=13, pppoe="1497377.822066c2cb1", id=44, serial="ZTEGD3239EB2", vlan=593)
