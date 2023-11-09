import random
import datetime

# Define the variables
ip_addresses = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]
request_types = ["GET", "POST", "PUT", "DELETE"]
apis = ["/usr/login", "/usr/cart", "/usr/checkout", "/usr/product"]
status_codes = [200, 404, 500]
user_agents = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"]

# Define the time period for generating logs
start_date = datetime.datetime(2022, 1, 1, 0, 0, 0)
end_date = datetime.datetime(2023, 12, 31, 23, 59, 59)

# Define the failure probability (1.2% downtime for 98.8% uptime)
failure_probability = 0.012

# Define the outage settings
outage_duration_min = 18  # Minimum outage duration in minutes
outage_duration_max = 57  # Maximum outage duration in minutes
outage_frequency = 2  # Number of outages per month

# Generate logs for 2 years
num_logs = 1000  # Adjust as needed

logs = []

for _ in range(num_logs):
    timestamp = start_date + datetime.timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    timestamp = timestamp.strftime('%d/%b/%Y:%H:%M:%S %z')
    
    ip = random.choice(ip_addresses)
    user_id = "-"
    request_type = random.choice(request_types)
    api = random.choice(apis)
    protocol_version = "HTTP/1.1"

    if random.random() < (outage_frequency / 30):  
        outage_start_date = start_date + datetime.timedelta(
            days=random.randint(0, (end_date - start_date).days)
        )
        outage_start_time = datetime.time(random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))
        outage_start = datetime.datetime.combine(outage_start_date, outage_start_time)
        
        outage_end = outage_start + datetime.timedelta(
            minutes=random.randint(outage_duration_min, outage_duration_max)
        )

        if outage_start <= datetime.datetime.strptime(timestamp, '%d/%b/%Y:%H:%M:%S %z') <= outage_end:
            status_code = 503  
            response_time = random.uniform(60, 3600)  
        else:
            status_code = random.choices(status_codes, weights=[988, 11, 1], k=1)[0]
            response_time = random.uniform(0.1, 2.0)
    else:
        status_code = random.choices(status_codes, weights=[988, 11, 1], k=1)[0]
        response_time = random.uniform(0.1, 2.0)  

    byte = random.randint(100, 10000)
    referrer = "-"
    user_agent = random.choice(user_agents)

    log_entry = f'{ip} - {user_id} [{timestamp}] "{request_type} {api} {protocol_version}" {status_code} {byte} "{referrer}" "{user_agent}" {response_time:.2f}'
    logs.append(log_entry)

# Save logs to a file
with open('synthetic_server_logs.txt', 'w') as f:
    f.write('\n'..join(logs))
    
    print(f'Synthetic server logs generated and saved to synthetic_ser.txt')
