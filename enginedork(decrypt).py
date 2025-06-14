#!/usr/bin/env/python3



from __future__ import print_function
try:
    from googlesearch import search

except ImportError:
    print("")
from datetime import timedelta
import os as _0xZer0r
import platform as rzkyp
import subprocess as a
import psutil as z
import getpass as r
import sys as X
import time as V


class colors:
    CGREEN2 = "\033[1;32m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"

def get_ip():
    try:
        return a.check_output(['hostname', '-I']).decode().strip().split()[0]
    except Exception:
        return "N/A"

def get_uptime():
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            return str(timedelta(seconds=int(uptime_seconds)))
    except Exception:
        return "N/A"

def get_disk_usage():
    usage = z.disk_usage('/')
    return f"{usage.used // (2**30)}G / {usage.total // (2**30)}G"

def get_ram_usage():
    mem = z.virtual_memory()
    return f"{mem.used // (2**20)}MB / {mem.total // (2**20)}MB"


user = r.getuser()
ip = get_ip()
os_info = rzkyp.system() + " " + rzkyp.release()
kernel = rzkyp.version()
uptime = get_uptime()
disk = get_disk_usage()
ram = get_ram_usage()

logo = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢀⡀⣄⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⣠⡤⣖⣾⣿⠟⠁⠈⠙⢿⣿⣶⣦⣁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢐⣮⣽⣾⣿⠏⠁⠀⠀⠀⠀⠀⠙⢿⣿⣿⣮⣕⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣢⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣮⣖⡄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡟⠿⠿⠿⠛⠋⠐⠀⠀⠈⠉⠉⠉⠁⠀⠐⠘⠛⠻⠟⠻⠛⢺⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠇⠇   ⠀I N S I D E R⠀⠀⠀⠀⢸⣿⣿⡖⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣧⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣇⣀⣀⣀⣀⡀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣸⣿⣿⡟⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣿⣿⡟⢛⣯⡍⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠈⠻⣿⣇⢠⡿⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⠋⣧⡀⠀⠈⠈⠀⠀⣠⡎⢿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⡿⠿⠛⠁⠀⣿⣿⣶⣄⢀⣴⣾⣿⡇⠀⠙⠻⢿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠉⠀⠀⠀⠀⠀⠀⢸⣿⢋⠀⠀⢈⢿⡿⠀⠀⠀⠀⠀⠈⠙⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⠁⠀⢻⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡏⠀⠀⠘⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠃⠀⠀⠀⢹⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""


judul = "\t\t\t\t\033[1;91m{DORKS ENGINE | INSIDER}"


info_lines = [
    "", "", "", "",
    f"User: {user}",
    f"IP: {ip}",
    f"OS: {os_info}",
    f"Kernel: {kernel}",
    f"Uptime: {uptime}",
    f"Disk: {disk}",
    f"RAM: {ram}",
    f"Version: 1.0",
    f"Author: 0xZer0r",
    f"Github: github.com/rzkyp",
]


logo_lines = logo.split('\n')


max_lines = max(len(logo_lines), len(info_lines))
logo_width = max(len(line) for line in logo_lines)

print("\n" + judul + "\n") 

for i in range(max_lines):
    logo_part = logo_lines[i] if i < len(logo_lines) else " " * logo_width
    info_part = info_lines[i] if i < len(info_lines) else ""
    print(colors.CGREEN2, f"{logo_part}   {info_part}")

y = "\n\t\t\t\t{..::~~Selamat Bersenang Senang~~::..}\n"
for col in y:
    print(colors.CBLUE2 + col, end="")
    X.stdout.flush()
    V.sleep(0.0040)

z = "\n"
for col in z:
    print(colors.ENDC + col, end="")
    X.stdout.flush()
    V.sleep(0.4)


try:
    data = input("\n\033[1;34m[•] Apakah Ingin Menyimpan Hasil dalam File? (Y/N) ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print ("\033[1;91m[!] User Mengalami Ganguan [!]\033[0")
        V.sleep(0.5)
        X.exit(1)


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()


if data.startswith("y" or "Y"):
    l0g = input("\033[1;34m[N/A] Buat nama File: ")
    print ("\n\033[34m" + "  " + "#" * 78 + "\n")
    logger(data)
else:
    print ("\033[1;91m[!] Tidak Disimpan [!]")
    print ("\n\033[34m" + "  " + "#" * 78 + "\n")


def dorks():
    try:
        dork = input("\n\033[1;34m[•] Masukan Dork anda : ")
        amount = input("\033[1;34m[•] Masukan Berapa Web yang ingin di tampilkan : ")
        print ("\n ")

        requ = 0
        counter = 0

        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            counter = counter + 1
            print ("\033[32m[•] ", counter, results)
            V.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            data = (counter, results)

            logger(data)
            V.sleep(0.1)

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] User Mengalami Ganguan [!]\033[0")
            V.sleep(0.5)
            X.exit(1)

    print ("\n\n\t\t\t\033[1;32m[•] Selesai [•]")
    print ("\t\t\033[1;31m[!] Gunakan Dengan Bijak [!]\n\n")
    X.exit()


# =====# Main #===== #
if __name__ == "__main__":
    dorks()
