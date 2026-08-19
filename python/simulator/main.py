import json
import random
from datetime import datetime, timezone

def generate_server_metric(server_id):
    return {
       "event_type": "server_metric",
       "timestamp": datetime.now(timezone.utc).isoformat(),
       "server_id": server_id,
       "environment": "production",
       "region": "europe-west2",
       "cpu_percent":round(random.uniform(20, 90), 2),
       "memory_percent": round(random.uniform(30, 85), 2),
       "disk_percent": round(random.uniform(10, 80), 2),
       "network_in_mb": round(random.uniform(100, 500), 2),
       "network_out_mb": round(random.uniform(100, 500), 2),
    }

servers = [
    "server-001",
    "server-002",
    "server-003",
    "server-004",
    "server-005",
]

for server in servers:
    metric = generate_server_metric(server)
    print(json.dumps(metric))