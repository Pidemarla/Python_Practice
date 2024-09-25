import psutil
import time

def monitor_cpu(interval):
    while True:
        cpu_percent = psutil.cpu_percent(interval=interval)
        print(f"CPU Usage: {cpu_percent}%")
        
if __name__ == "__main__":
    monitoring_interval = 5  # Monitor every 5 seconds
    monitor_cpu(monitoring_interval)
def get_disk_space():
    partitions = psutil.disk_partitions()
    disk_info = []

    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_info.append({
            "mountpoint": partition.mountpoint,
            "total": usage.total,
            "used": usage.used,
            "free": usage.free,
            "percent": usage.percent
        })

    return disk_info

if __name__ == "__main__":
    disk_info = get_disk_space()

    for disk in disk_info:
        print(f"Mountpoint: {disk['mountpoint']}")
        print(f"Total Space: {disk['total']} bytes")
        print(f"Used Space: {disk['used']} bytes")
        print(f"Free Space: {disk['free']} bytes")
        print(f"Used Percentage: {disk['percent']}%\n")