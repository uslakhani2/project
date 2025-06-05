import requests
from getpass import getpass

def test_qualys_credentials():
    print("🔐 Qualys Credential Tester")

    # Get user input
    base_url = input("Enter Qualys API URL (e.g. https://qualysapi.qualys.com): ").strip().rstrip("/")
    username = input("Enter your Qualys username: ")
    password = getpass("Enter your Qualys password (input hidden): ")

    # Use a safe, minimal API to test the credentials
    url = f"{base_url}/api/2.0/fo/subscription/info/"

    headers = {
        "X-Requested-With": "Python Script"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            auth=(username, password),
            timeout=10
        )

        if response.status_code == 200:
            print("✅ Credentials are valid! Successfully connected to Qualys.")
        elif response.status_code == 401:
            print("❌ Authentication failed: Invalid username or password.")
        else:
            print(f"⚠️ Received unexpected status code: {response.status_code}")
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error: {e}")

if __name__ == "__main__":
    test_qualys_credentials()