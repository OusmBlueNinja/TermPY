# ["randomquote", "packages.randomquote", ["randomquote"]]
# Made By OusmBlueNinja
import requests

def randomquote(command: list):
    if len(command) != 0:
        print("Usage: randomquote")
        return

    try:
        # Fetch a random quote from the Zen Quotes API
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            quote_data = response.json()
            if quote_data and "q" in quote_data[0]:
                quote = quote_data[0]["q"]
                print("Random Zen Quote:")
                print(quote)
            else:
                print("Failed to retrieve a quote.")
        else:
            print("Failed to retrieve a quote.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

