# variables & Types
server_name = "web-server-01"
cpu_percentage = 78.5
memory_percentage = 89.5
is_healthy = True
alert_threshold = 85
memory_threshold = 90
print(f"Server Name: {server_name}")
print(f"CPU Usage: {cpu_percentage}%")
print(f"Memory Usage: {memory_percentage}%")
print(f"Is Healthy: {is_healthy}")
# Conditional Statements
if cpu_percentage > alert_threshold:
    print("Alert: CPU usage is above threshold!")
elif cpu_percentage > 70:
    print(f"warning: CPU usage is at {cpu_percentage}%")
else:    print("CPU usage is within normal limits.")

if memory_percentage > alert_threshold:
    print("alert: memory usage is above threshold!")
else:
    print(f"memory usage is at {memory_percentage}%")
    # Variables & Types

servers =[
    {"name": "Web-Server-1", "CPU": 74.8, "memory":80},
    {"name": "Web-Server-2", "CPU": 82.3,"memory": 88.3}, 
    {"name": "db-Server-3", "CPU": 68.5, "memory": 75.0},
    {"name": "cache-Server-4", "CPU": 90.2, "memory": 92.1},
]
def health_Check(name ,cpu_usage, memory, alert_threshold=85, memory_threshold=90):

    if cpu_usage > alert_threshold or memory > memory_threshold:
        return f"Alert: usage usage is above threshold for {name}!"
    elif cpu_usage > 70:
        return f"Warning:{name} | CPU usage is at {cpu_usage}%, Memory usage is at {memory}%"
    else:
        return f"Normal {name}: CPU usage is at {cpu_usage}% Memory usage is at {memory}%"


for server in servers:
    result = health_Check(server["name"], server["CPU"], server["memory"])
    print(result)
