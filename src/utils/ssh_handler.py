import yaml
import time
import paramiko
from utils.matrix import success, reject, empty
from sense_hat import SenseHat

sense = SenseHat()

def load_hosts(config_path='../config.yaml'):
    with open(config_path, 'r') as f:
        data = yaml.safe_load(f)
    return data['hosts']

def run_command(hostname, ip, username, password=None, key_path=None, command='uptime'):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        if key_path:
            client.connect(ip, username=username, key_filename=key_path, timeout=10)
        else:
            client.connect(ip, username=username, password=password, timeout=10)

        client.exec_command(command)
        return "success"

    except Exception as e:
        print(f"Failed to connect to {hostname} ({ip}): {e}")
        return "fail"

    finally:
        client.close()

def ssh():
    hosts = load_hosts()
    status = {}
    for host in hosts:
        result = run_command(
            hostname=host['hostname'],
            ip=host['ip'],
            username=host['user'],
            password=host['password'],
            command='uptime'
        )
        status[host['hostname']] = result

    for hostname, stat in status.items():
        sense.show_message(f"{hostname}", scroll_speed=0.05)
        sense.set_pixels(success() if stat == "success" else reject())
        time.sleep(1)
        sense.set_pixels(empty())
    