# Cybersecurity Toolkit

Zbiór narzędzi do pentestów i bezpieczeństwa aplikacji webowych, podzielonych na trzy główne kategorie:  
- **scanners** – narzędzia wykrywające podatności (XSS, SQL Injection)  
- **exploits** – skrypty wykorzystujące znalezione podatności (RCE, reverse shell)  
- **attacks** – narzędzia do aktywnych ataków, np. brute force, fuzzing

---

## Struktura katalogów

```
Cybersecurity/
├── scanners/        # Skany podatności i testy automatyczne
├── exploits/        # Exploity do wykorzystania luk
├── attacks/         # Ataki aktywne i bruteforce
├── README.md        # Ten plik
```

---

## Wymagania

- Python 3.x  
- Biblioteka `requests`

---

## Jak używać?

1. Sklonuj repozytorium:
   ```
   git clone https://github.com/Pociatlo/Cybersecurity.git
   cd Cybersecurity
   ```

2. Zainstaluj wymagania:
   ```
   pip install -r requirements.txt
   ```

3. Uruchom wybrany skrypt, np.:
   ```
   python3 scanners/Vulnscaner.py
   python3 exploits/RCEexploit.py
   python3 attacks/Bruteforce.py
   ```

---

## Przykładowe narzędzia

### scanners/

- `Vulnscaner.py` — wykrywa podatności XSS i SQL Injection

### exploits/

- `RCEexploit.py` — exploit RCE z interaktywną powłoką oraz wysyła payload reverse shell  

### attacks/

- `Bruteforce.py` — brute force na login (numery i litery, case sensitive)   

---

## Wsparcie i rozwój

Repozytorium jest w trakcie rozwoju — wszelkie sugestie i poprawki są mile widziane!  
Zapraszam do zgłaszania issue i pull requestów.

---

## Licencja

Projekt na licencji MIT — swobodnie korzystaj i modyfikuj.

---

## Kontakt

Pociatlo — [https://github.com/Pociatlo](https://github.com/Pociatlo)
