import requests

def fetch_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["type"] == "single":
            print(f"Joke: {data['joke']}")
        else:
            print(f"Setup: {data['setup']}\nDelivery: {data['delivery']}")
    else:
        print("Failed to fetch joke, please try again later.")

if __name__ == "__main__":
    fetch_joke()
