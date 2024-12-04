# Comandos como funções que retornam strings
def comando_unc(serial=None):
    return "show gpon onu unc"


def comando_summary(serial=None):
    if serial is not None:
        return f"show gpon onu {serial} summary"
    else:
        return ""  # Comando padrão sem serial


def comando_provisionamento(serial=None):
    if serial is not None:
        return f"show gpon onu {serial}"
    else:
        return ""  # Comando padrão sem serial


# Dicionário de comandos mapeado para funções
comandos = {
    "unc": comando_unc,
    "summary": comando_summary,
    "provisionamento": comando_provisionamento,
}
