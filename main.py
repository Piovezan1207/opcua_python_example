# Biblioteca OPCUA -  https://github.com/FreeOpcUa
#pip install freeopcua
#pip install cryptography
from opcua import Client, ua
import time

ip = "192.168.150.10"

if __name__ == "__main__":
    client = Client("opc.tcp://{}:4840".format(ip))
    try:

        client.connect() #Conectar com server

        #Setar valor
        print("Ligando esteira...")
        dv = ua.DataValue(ua.Variant(True, ua.VariantType.Boolean)) #Valor e tipo da variável
        teste = client.get_node("ns=4;i=627") #Endereço
        teste.set_value(dv) #Seta valor
        
        time.sleep(2)
        
        print("Desligando esteira...")
        dv = ua.DataValue(ua.Variant(False, ua.VariantType.Boolean)) #Valor e tipo da variável
        teste = client.get_node("ns=4;i=627") #Endereço
        teste.set_value(dv) #Seta valor
        
        while True:
            valor = client.get_node("ns=4;i=91").get_value() #Lê valor
            print("Valor lido:" , valor)
            time.sleep(2)            
    finally:
        client.disconnect()