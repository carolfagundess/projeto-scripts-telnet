# Comandos como funções que retornam strings
def comando_configurar(serial, placa, pon, alias, flow):
    if serial is not None:
        # Retorna a sequência de comandos com o serial inserido
        return f"""
configure terminal
interface gpon{placa}/{pon}
onu {serial} alias {alias}
onu {serial} flow-profile {flow}
end
copy r s
"""
    else:
        # Em branco
        return ""


def comando_summary(serial, placa=None, pon=None, alias=None, flow=None):
    if serial is not None:
        return f"show gpon onu {serial} summary"
    else:
        return ""  # Em branco


def comando_provisionamento(serial, placa=None, pon=None, alias=None, flow=None):
    if serial is not None:
        return f"show gpon onu {serial}"
    else:
        return ""  # Em branco


def comando_unc(serial=None, placa=None, pon=None, alias=None, flow=None):
    return "show gpon onu unc"  # Comando fixo que não precisa de parâmetros


def comando_ver_blacklist(serial=None, placa=None, pon=None, alias=None, flow=None):
    return "show gpon blacklist"


# Dicionário de comandos mapeado para funções
comandos = {
    "unc": comando_unc,
    "summary": comando_summary,
    "ver_config": comando_provisionamento,
    "provisionar": comando_configurar,
    "ver_blacklist": comando_ver_blacklist,
}
