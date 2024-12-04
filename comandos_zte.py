# Comandos como funções que retornam strings
def comandos_naounc():
    return f"return 
enable
g3r3nc1@
terminal length 512
show gpon onu uncfg
!
"""

def comando_mostraratenucao(placa, pon, id, serial=None):
    if placa is not None:
        return f"""
enable
g3r3nc1@
show pon power attenuation gpon-onu_1/{placa}/{pon}:{id}
"""
    else: 
        return ""

def comando_mostrarids(placa, pon, serial=None, id=None):
    if placa is not None:
        return f"""
enable
g3r3nc1@
terminal length 512
show gpon onu state gpon-olt_1/{placa}/{pon}
exit
"""
    else:
        return ""

def comando_mostrarprovisionamento(placa, pon, id, serial=None):
    return f"""
enable
g3r3nc1@
show ru interface gpon-onu_1/{placa}/{pon}:{id}
show onu run conf gpon-onu_1/{placa}/{pon}:{id}
"""

def comando_mostrarsinal(placa, pon, id, serial=None):
    return f"""
enable
g3r3nc1@
show onu run conf gpon-onu_1/{placa}/{pon}:{id}
!
"""

def comando_mostrarquedas(placa, pon, id, serial=None):
    return f"""
enable
g3r3nc1@
terminal length 512
show gpon onu detail-info gpon-onu_1/{placa}/{pon}:{id}    
"""

def comando_localizaronu(serial):
    return f"""
enable
g3r3nc1@
show gpon onu by sn {serial}
!
"""