import requests
import time

BASE_URL = "https://speed.cloudflare.com"

# DOWNLOAD — fichier de 100MB au lieu de 25MB
print("Download en cours...")
debut = time.time()
r = requests.get(f"{BASE_URL}/__down?bytes=100000000", timeout=60)
duree = time.time() - debut
print(f"Download : {round(len(r.content)*8/duree/1_000_000,1)} Mbps")

# UPLOAD — 25MB au lieu de 10MB
print("Upload en cours...")
data = bytes(25 * 1024 * 1024)
debut = time.time()
requests.post(f"{BASE_URL}/__up", data=data, timeout=60)
duree = time.time() - debut
print(f"Upload   : {round(len(data)*8/duree/1_000_000,1)} Mbps")

# LATENCE
debut = time.time()
requests.get(f"{BASE_URL}/__down?bytes=0", timeout=5)
print(f"Latence  : {round((time.time()-debut)*1000,1)} ms")