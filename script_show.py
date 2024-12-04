import telnetlib

def executar_show_configs():
    # Configurações do servidor Telnet
    HOST = "10.199.226.142"  # endereço do servidor
    PORT = 23  # Porta padrão do Telnet
    TIMEOUT = 50  # Tempo de espera para conexão
    USERNAME = "admin"  # Substitua pelo nome de usuário
    PASSWORD = "@pr0gr4m4d0r@"  # Substitua pela senha
    PASSWORD_ENABLE = "g3r3nc1@"  # Senha de Gerencia

    COMMAND = "show gpon onu unc"  # Substitua pelo comando desejado

    try:
        # Conectar ao servidor
        tn = telnetlib.Telnet(HOST, PORT, TIMEOUT)
        tn.read_until(b"Username:")  # Aguarda o prompt de username
        tn.write(USERNAME.encode("ascii") + b"\n")
        tn.read_until(b"Password:")  # Aguarda o prompt de senha
        tn.write(PASSWORD.encode("ascii") + b"\n")

        # Enviar comando
        tn.write((COMMAND + "\n").encode("ascii"))
        tn.write(b"exit\n")

        # Captura a saída do comando
        output = tn.read_all().decode("ascii")
        tn.close()
        return output

    except Exception as e:
        return f"Erro: {e}"
