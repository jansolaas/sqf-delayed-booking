import requests
from bs4 import BeautifulSoup

# ---- KONFIG ----
BASE_URL = "https://sqf.book247.com"
USERNAME = "jansolaas@pm.me"
PASSWORD = "Thrift7-Washer2-Zips1-Bulldozer3-Splice0"

# Start en session (håndterer cookies automatisk)
session = requests.Session()

# 1) Hent først hovedsiden for å få XSRF-token fra cookies/HTML
r = session.get(BASE_URL)
r.raise_for_status()

# XSRF-token ligger i en cookie
xsrf_token = session.cookies.get("XSRF-TOKEN")

if not xsrf_token:
    raise RuntimeError("Fant ikke XSRF-token i cookies!")

print("XSRF-TOKEN:", xsrf_token)

# 2) POST til login-endpointet
login_url = f"{BASE_URL}/ajax/auth_autorize"
payload = {
    "login": USERNAME,
    "password": PASSWORD,
    "remember": "1"
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-CSRF-TOKEN": xsrf_token,
    "X-Requested-With": "XMLHttpRequest"
}

resp = session.post(login_url, data=payload, headers=headers)
resp.raise_for_status()

print("Response:", resp.text)
print("Cookies:", session.cookies.get_dict())

# Nå har du en gyldig session-cookie (laravel_session) som kan brukes
# til å kalle andre API-endepunkter som get_friends_list, get_booking_hours osv.
