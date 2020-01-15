# def square_number(number): #this makes a function!! and can add a defult value in the arg brackets
#     return number ** 2
#
#
# def add_double(num1, num2):
#     total = num1 + num2
#     return total * 2
#
#
# def loud(string):
#     return string.upper() * 3
#
#
#
# def fizzBuzz(number):
#     '''
#     it takes in a number, and plays fizzbuzz
#     :param number:
#     :return:
#     '''
#
#     if number % 3 == 0 and number % 5 == 0:
#         return 'fizzbuzz'
#     elif number % 3 == 0:
#         return 'fizz'
#     elif number % 5 == 0:
#         return 'buzz'

# def loud_list(*muliargs):
#     for item in muliargs:
#         print(item.upper)
#
# shopping = (' a,s,d,f,,g,h,j')
#
#
#
# def get_choc(*muiltiargu):
#     new = list(muiltiargu)
#     for items in muiltiargu:
#         if items != "chocolate":
#             return print(items)
#
#         else:
#             items += "chocolate"
#             return print(items)
#
#
# get_choc(shopping)


def repeat_loud(number_of_repeats,*things_to_shout):
    for exc in things_to_shout:
        print(exc.upper()) * number_of_repeats
repeat_loud(3,"hello","I'm happy")