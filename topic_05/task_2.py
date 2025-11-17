import requests
def get_exchange_rates () :
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json' 
    response = requests.get(url)
    if response.status_code == 200 :
        return response.json()
    else:
        print('Error, status code is: ', response.status_code)
        return None


def convert_curency (amount, currency, rates) :
    if currency in rates :
        exchange_rate = rates[currency]
        return amount * exchange_rate
    else :
        print('Wrong currency')
        return None


def main () :
    rates_data = get_exchange_rates()
    if rates_data :
        rates = {}
        target_currencies = ['EUR', 'USD', 'PLN']
        for item in rates_data :
            if item['cc'] in target_currencies :
                rates[item['cc']] = item['rate']
        print("Available currencies: EUR, USD, PLN")
        currency = input('Enter currency code (EUR, USD, PLN): ').upper()
        if currency in rates:
            try :
                amount = float(input(f'Input amount in {currency}: '))
                converted_curency = convert_curency(amount, currency, rates)
                if converted_curency is not None:
                    print(f"{amount} {currency} is equal to {converted_curency:.2f} UAH")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print('Unlown currency')         

main()