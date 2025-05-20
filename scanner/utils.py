import json
import os
from datetime import datetime

def save_results(data, folder="results"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = f"{folder}/scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"[+] Results saved to {filename}")
