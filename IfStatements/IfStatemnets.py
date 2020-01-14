# age = int(input())
# if age >= 18:
#     print("You can buy a ticket")
#
# elif age < 18:
#     print("Soz peeps, no tickets for you")
#
#
#
# print("End of script")

cinema_open = True

film_rating = input()

if cinema_open:

    if film_rating == "universal":
        print("Anyone can watch this film!")

    elif film_rating == "pg":
        print("You can watch this film with consent!")

    elif film_rating == "12":
        print("If under 12, must have an adult with you")

    elif film_rating == "15":
        print("If you are 15 or over, you can see this film")

    elif film_rating == "18":
        print("If you are 18 or over, you can see this film")

    else:
        print("Wha..?")

else:
    print("Sorry the movies are closed for today!")
