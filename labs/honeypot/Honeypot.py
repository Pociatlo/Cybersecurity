import socket
import threading
import datetime
import os

# === Ustawienia od użytkownika ===
def get_user_settings():
    try:
        port = int(input("Enter port to listen on (default = 22): ").strip() or 22)
        if port < 1 or port > 65535:
            raise ValueError
    except ValueError:
        print("[-] Invalid port.")
        exit()

    log_file = input("Enter log file name (default = honeypot.log): ").strip()
    if not log_file:
        log_file = "honeypot.log"

    banner = input("Enter fake banner to send (default = SSH-2.0-OpenSSH_7.4p1 Debian-10+deb9u7): ").strip()
    if not banner:
        banner = "SSH-2.0-OpenSSH_7.4p1 Debian-10+deb9u7"
    banner += "\r\n"

    return port, log_file, banner

# === Logowanie zdarzeń ===
def log_event(message, log_file):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}\n"
    print(entry.strip())
    with open(log_file, "a") as f:
        f.write(entry)

# === Obsługa pojedynczego połączenia ===
def handle_connection(conn, addr, banner, log_file):
    client_ip, client_port = addr
    log_event(f"Connection from {client_ip}:{client_port}", log_file)
    try:
        conn.settimeout(5.0)
        data = conn.recv(1024)
        if data:
            decoded = data.decode(errors='ignore')
            log_event(f"Received from {client_ip}:{client_port} -> {decoded}", log_file)
        conn.sendall(banner.encode())
    except socket.timeout:
        log_event(f"Connection from {client_ip}:{client_port} timed out", log_file)
    except Exception as e:
        log_event(f"Error with {client_ip}:{client_port}: {e}", log_file)
    finally:
        conn.close()
        log_event(f"Closed connection from {client_ip}:{client_port}", log_file)

# === Główna pętla serwera ===
def main():
    port, log_file, banner = get_user_settings()
    if not os.path.exists(log_file):
        open(log_file, "w").close()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', port))
        s.listen(10)
        log_event(f"Honeypot listening on 0.0.0.0:{port}", log_file)
        while True:
            try:
                conn, addr = s.accept()
                threading.Thread(
                    target=handle_connection,
                    args=(conn, addr, banner, log_file),
                    daemon=True
                ).start()
            except KeyboardInterrupt:
                log_event("Shutting down honeypot...", log_file)
                break
            except Exception as e:
                log_event(f"Main loop error: {e}", log_file)


if __name__ == "__main__":
    main()
