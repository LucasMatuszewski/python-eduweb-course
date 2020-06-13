print("Hello World")

crypto_price = int(input("Your Crypto price: "))
crypto_name = input("Crypto name: ")

crypto_dictionary = {"bitcoin": 3000, "ethereum": 200, "iota": 30, "pln": -1}

try:
    if crypto_name == "pln":
        raise KeyError("pln is not a crypto!")
    if crypto_price > crypto_dictionary[crypto_name]:
        print("Waiting for better price")
    else:
        print("Good price!")
except KeyError as e:
    print(e)
    print("We don't know this crypto...")
finally:
    print("this code is always executed on the end, eg. to close a file")
