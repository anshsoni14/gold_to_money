import requests

# Your GoldAPI API Key
GOLD_API_KEY = "goldapi-3tb84sm9sdol0v-io"

def get_gold_price_usd_per_gram():
    url = "https://www.goldapi.io/api/XAU/USD"
    headers = {
        "x-access-token": GOLD_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if 'price' in data:
        usd_per_ounce = data['price']
        usd_per_gram = usd_per_ounce / 31.1035
        return usd_per_gram
    else:
        raise Exception(f"Error fetching gold price: {data.get('error', 'Unknown error')}")

def get_usd_to_inr():
    response = requests.get("https://open.er-api.com/v6/latest/USD")
    data = response.json()
    return data["rates"]["INR"]

def main():
    try:
        weight = float(input("Enter gold weight in grams: "))
        karat = input("Enter gold purity (22K or 24K): ").strip().lower()

        if karat not in ['22k', '24k']:
            raise ValueError("Please enter either '22K' or '24K'.")

        gold_price_usd_per_gram = get_gold_price_usd_per_gram()
        usd_to_inr = get_usd_to_inr()

        gold_price_inr = gold_price_usd_per_gram * usd_to_inr

        if karat == '22k':
            gold_price_inr *= 0.916  # Adjust for 22K gold

        total_cost = gold_price_inr * weight

        print(f"\nCurrent {karat.upper()} gold price per gram in INR: ₹{gold_price_inr:.2f}")
        print(f"Total cost for {weight} grams: ₹{total_cost:.2f}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
