#!/usr/bin/env python3
import os, platform, shutil
def human(n):
    units = ["B","KiB","MiB","GiB","TiB"]
    n = float(n)
    for u in units:
        if n < 1024 or u == units[-1]: return f"{n:.1f} {u}"
        n /= 1024
def main():
    d = shutil.disk_usage("/")
    print("Linux Healthcheck")
    print(f"Host: {platform.node()}")
    print(f"OS: {platform.platform()}")
    print(f"Logical CPUs: {os.cpu_count()}")
    print(f"Disk used: {human(d.used)} / {human(d.total)}")
    print(f"Disk free: {human(d.free)}")
if __name__ == "__main__": main()
