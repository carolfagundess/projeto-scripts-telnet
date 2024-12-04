# Comandos como funções que retornam strings
def comando_naounc(serial=None, placa=None, pon=None, alias=None, id=None, vlan=None):
    return "show gpon onu uncfg"


def comando_mostraratenucao(placa, pon, id, serial=None):
    if placa is not None:
        return f"show pon power attenuation gpon-onu_1/{placa}/{pon}:{id}"
    else:
        return ""


def comando_mostrarids(placa, pon, serial=None, alias=None, id=None, vlan=None):
    if placa is None or pon is None:
        raise ValueError(
            "Parâmetros 'placa' e 'pon' são obrigatórios para este comando."
        )
    return f"show gpon onu state gpon-olt_1/{placa}/{pon}"


def comando_mostrarprovisionamento(placa, pon, id, serial=None, alias=None, vlan=None):
    return f"""
show ru interface gpon-onu_1/{placa}/{pon}:{id}
show onu run conf gpon-onu_1/{placa}/{pon}:{id}
"""


def comando_mostrarsinal(placa, pon, id, serial=None):
    return f"show onu run conf gpon-onu_1/{placa}/{pon}:{id}"


def comando_mostrarquedas(placa, pon, id, serial=None):
    return f"show gpon onu detail-info gpon-onu_1/{placa}/{pon}:{id}"


def comando_localizaronu(serial, placa=None, pon=None, alias=None, id=None, vlan=None):
    return f"show gpon onu by sn {serial}"


# Script provisionamento 
def comando_configurar_pppoe(slot_olt, porta_olt, id_onu, serial, user_pppoe, vlan_id):
    return f"""
configure terminal
interface gpon-olt_1/{slot_olt}/{porta_olt}
onu {id_onu} type ZTE-F660 sn {serial}
!
interface gpon-onu_1/{slot_olt}/{porta_olt}:{id_onu}
name {user_pppoe}
tcont 1 name INTERNET profile T1-1G
gemport 1 name INTERNET tcont 1
switchport mode hybrid vport 1
service-port 1 vport 1 user-vlan {vlan_id} vlan {vlan_id}
!
pon-onu-mng gpon-onu_1/{slot_olt}/{porta_olt}:{id_onu}
service INTERNET gemport 1 cos 0 vlan {vlan_id}
security-mgmt 212 mode forward state enable ingress-type wan protocol web
!
end
write
"""


# Dicionário de comandos mapeado para funções
comandos = {
    "unc": comando_naounc,
    "localizar_onu": comando_localizaronu,
    "atenuacao_onu": comando_mostraratenucao,
    "mostrar_ids": comando_mostrarids,
    "provisionamento": comando_mostrarprovisionamento,
    "quedas_onu": comando_mostrarquedas,
    "sinal_onu": comando_mostrarsinal,
}
