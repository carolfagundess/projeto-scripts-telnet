# Comandos como funções que retornam strings
def comando_naounc(serial=None, placa=None, pon=None, pppoe=None, id=None, vlan=None):
    return "show gpon onu uncfg"


def comando_mostraratenucao(placa, pon, id, serial=None, pppoe=None, vlan=None):
    if placa is not None:
        return f"show pon power attenuation gpon-onu_1/{placa}/{pon}:{id}"
    else:
        return ""


def comando_mostrarids(placa, pon, serial=None, pppoe=None, id=None, vlan=None):
    if placa is None or pon is None:
        raise ValueError(
            "Parâmetros 'placa' e 'pon' são obrigatórios para este comando."
        )
    return f"show gpon onu state gpon-olt_1/{placa}/{pon}"


def comando_mostrarprovisionamento(placa, pon, id, serial=None, pppoe=None, vlan=None):
    return f"""
show ru interface gpon-onu_1/{placa}/{pon}:{id}
show onu run conf gpon-onu_1/{placa}/{pon}:{id}
"""


def comando_mostrarsinal(placa, pon, id, serial=None, pppoe=None, vlan=None):
    return f"show pon power onu-rx gpon-onu_1/{placa}/{pon}:{id}"


def comando_mostrarquedas(placa, pon, id, serial=None, pppoe=None, vlan=None):
    return f"show gpon onu detail-info gpon-onu_1/{placa}/{pon}:{id}"


def comando_localizaronu(serial, placa=None, pon=None, pppoe=None, id=None, vlan=None):
    return f"show gpon onu by sn {serial}"


# Script provisionamento
def comando_configurar_pppoe(placa,pon, id, serial, pppoe, vlan):
    return f"""
configure terminal
interface gpon-olt_1/{placa}/{pon}
onu {id} type ZTE-F660 sn {serial}
!
interface gpon-onu_1/{placa}/{pon}:{id}
name {pppoe}
tcont 1 name INTERNET profile T1-1G
gemport 1 name INTERNET tcont 1
switchport mode hybrid vport 1
service-port 1 vport 1 user-vlan {vlan} vlan {vlan}
!
pon-onu-mng gpon-onu_1/{placa}/{pon}:{id}
service INTERNET gemport 1 cos 0 vlan {vlan}
security-mgmt 212 mode forward state enable ingress-type wan protocol web
!
end
write
"""


# Dicionário de comandos mapeado para funções
comandos = {
    "unc": comando_naounc,
    "provisionamento": comando_mostrarprovisionamento,
    "localizar_onu": comando_localizaronu,
    "atenuacao_onu": comando_mostraratenucao,
    "mostrar_ids": comando_mostrarids,
    "quedas_onu": comando_mostrarquedas,
    "sinal_onu": comando_mostrarsinal,
    "configurar_onu": comando_configurar_pppoe,
}
