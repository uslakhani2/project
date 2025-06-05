import requests
from requests.auth import HTTPBasicAuth

# ---- CONFIG ----
solarwinds_url = "https://<your-solarwinds-server>:17778"
username = "your_username"
password = "your_password"

# Sample SWQL query to test connectivity
query = "SELECT NodeID, Caption FROM Orion.Nodes"
full_url = f"{solarwinds_url}/SolarWinds/InformationService/v3/Json/Query"

# ---- EXECUTION ----
def test_solarwinds_login():
    try:
        response = requests.get(
            full_url,
            params={"query": query},
            auth=HTTPBasicAuth(username, password),
            verify=False  # Disable SSL verification if using self-signed certs (not recommended for production)
        )

        if response.status_code == 200:
            print("✅ Successfully authenticated to SolarWinds!")
            print("Sample data:", response.json()['results'][:3])  # print first 3 rows
        elif response.status_code == 401:
            print("❌ Authentication failed: Invalid username or password.")
        else:
            print(f"⚠️ Request failed with status {response.status_code}: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error: {e}")

if __name__ == "__main__":
    test_solarwinds_login()