rates_to_inr = {
    "USD": 83,
    "EUR": 90,
    "JPY": 0.62,
    "GBP": 105,
    "AUD": 55
}

while True:
    amount = float(input("Enter the amount: "))
    currency = input("Enter the currency (USD/EUR/JPY/GBP/AUD): ")

    if not currency.isupper():
        print("Please type the currency in CAPITAL letters.")
        continue

    currency = currency.upper()
    break

if currency in rates_to_inr:
    inr_amount = amount * rates_to_inr[currency]
    print(f"{amount} {currency} = {inr_amount:.2f} INR")
else:
    print("Currency not supported!")
