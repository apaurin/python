sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
# ovo se može riješiti ovako:
#if (san_francisco_pop_density > rio_de_janeiro_pop_density):
#    print (True)
# else:
#    print (False)
print(san_francisco_pop_density > rio_de_janeiro_pop_density)
# iako je najjednostavnije ovako



first_word = 'Hello'
print(first_word[3])
print(len("ababa") / len("ab"))
coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)

username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
print(username + " " + "accessed the site " + url + " at " + timestamp)

given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name) + len(middle_names) + len(family_name)
print(name_length)
# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)

# print(len(835))   ovo vraća error i to syntax jer nemožeš vadit len od integera

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.
week_total = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
week_sales = week_total / 7
week_message = "This week's total sales: " + str(week_sales)
print(week_message)

print("one fish, two fish, more fish".count('fish'))

print("Mohammed has {} balloons".format(27))
animal = "dog Perry"
action = "eat shit Bob!"
print("Does your {} {}?".format(animal, action))
maria_string = "Maria loves {} and {}"
print(maria_string.format("sarme", "kumpirove zlatice"))
print(13.37.islower())