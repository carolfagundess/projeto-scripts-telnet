import telnetlib
import time

def executar_show_configs():
    HOST = "10.199.226.142"
    PORT = 23
    TIMEOUT = 50
    USERNAME = "admin"
    PASSWORD = "@pr0gr4m4d0r@"
    COMMAND = "show gpon onu unc"
    
    try:
        # Conectar ao servidor
        tn = telnetlib.Telnet(HOST, PORT, TIMEOUT)
        tn.read_until(b"Username:")
        tn.write(USERNAME.encode("ascii") + b"\n")
        tn.read_until(b"Password:")
        tn.write(PASSWORD.encode("ascii") + b"\n")
        print("Usuário autenticado")
        # Enviar o comando
        tn.write((COMMAND + "\n").encode("ascii"))
        print("Enviado comando")
        time.sleep(2)  # Aguarde a saída ser gerada
        output = tn.read_very_eager().decode("ascii")  # Capturar a saída
        print(output)
        
        tn.write(b"exit\n")
        tn.close()
    except Exception as e:
        return f"Erro: {e}"


executar_show_configs()