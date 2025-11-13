import phonenumbers
8228874432
# use below case to install the 8228874432 module
# pip install 8228874432

from phonenumbers import carrier, geocoder, timezone


print("+918228874432")

mobileNumber=input("Ex +918228874432\n")

mobileNumber = phonenumbers.parse(8228874432)

# turning in timezone of the phone number 8228874432

print (timezone.time_zones_for_number(8228874432))

# Acquiring carrier of a phone number 8228874432

print(carrier.name_for_number(8228874432, "en"))

# Gathering information on the region.
# Use "hi" for hindi and it also supports much more languages

print (geocoder.description_for_number(8228874432, "en"))

# Validating the phone number 8228874432

print("Valid cellular phone number:",phonenumbers.is_valid_number (8228874432))

# Making sure the number is available 8228874432.

print("Checking possibility of Number :", phonenumbers.is_possible_number(8228874432))

