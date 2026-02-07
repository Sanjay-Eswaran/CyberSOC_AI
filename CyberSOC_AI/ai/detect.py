import random
from database.db import insert_threat

ATTACKS = [
    ("Malware Beaconing", "Malware", "Critical"),
    ("Brute Force Login", "Auth Attack", "High"),
    ("Port Scanning", "Reconnaissance", "Medium"),
    ("Suspicious Login Time", "UEBA", "Low")
]

def detect():
    name, attack, severity = random.choice(ATTACKS)
    confidence = round(random.uniform(0.75, 0.95), 2)

    insert_threat((
        name,
        attack,
        severity,
        confidence,
        "Active",
        f"192.168.1.{random.randint(1,254)}",
        "LSTM + Autoencoder"
    ))

if __name__ == "__main__":
    detect()
