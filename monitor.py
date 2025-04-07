import subprocess

hosts = ["8.8.8.8", "1.1.1.1", "192.168.1.1"]

for host in hosts:
    result = subprocess.run(["ping", "-c", "2", host], stdout=subprocess.PIPE)
    if result.returncode == 0:
        print(f"{host} ist erreichbar.")
    else:
        print(f"{host} ist NICHT erreichbar.")
