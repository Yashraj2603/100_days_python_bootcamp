def band_name_generator(city , pet):
    print("Your band name can be ", city +" "+ pet)


def query_band():
    city = input("Enter name of your city ")
    pet = input("Enter name of your pet ")
    band_name_generator(city,pet)
query_band()
