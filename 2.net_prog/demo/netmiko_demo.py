from netmiko import ConnectHandler

router = {"device_type": "cisco_ios",
          "host": "10.124.41.193",
          "user": "cisco",
          "pass": "cisco"}

net_connect = ConnectHandler(ip=router["host"],
                             username=router["user"],
                             password=router["pass"],
                             device_type=router["device_type"])

interface_cli = net_connect.send_command("show ip int b")

print(interface_cli)

cfg_commands = ["int g2", "ip add 200.1.1.1 255.255.255.0"]


interface_cli = net_connect.send_config_set(cfg_commands)

print(interface_cli)