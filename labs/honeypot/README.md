# Honeypot

Prosty serwer honeypot w Pythonie, który nasłuchuje na wskazanym porcie, loguje połączenia i odsyła baner.

---

## Wymagania

- Python 3.x
- Moduły: `socket`, `threading`, `datetime`, `os`

---

## Sposób użycia

```bash
cd labs/honeypot
python Honeypot.py
```

1. **Port** – numer portu do nasłuchiwania (domyślnie 22)  
2. **Log file** – nazwa pliku do zapisu logów (domyślnie `honeypot.log`)  
3. **Banner** – ciąg znaków wysyłany do klienta po nawiązaniu połączenia  

Wszystkie zdarzenia (połączenia, otrzymane dane, timeouty, błędy) są zapisywane w pliku logu.

---

## Licencja

Projekt na licencji MIT — swobodnie korzystaj i modyfikuj.

---

## Kontakt

Pociatlo — [https://github.com/Pociatlo](https://github.com/Pociatlo)
