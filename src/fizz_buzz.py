def fizz_buzz(number):
    if number % 3 == 0:
        if number % 5 == 0:
            return "FizzBuzz"
        return "Fizz"     
    elif number % 5 == 0:
        return "Buzz"
    else:
        return f"{number}"    

# return "Fizz" if the number is divisible by 3 (e.g. fizz_buzz(3) == "Fizz")
# return "Buzz" if the number is divisible by 5 (e.g. fizz_buzz(5) == "Buzz")
# return "FizzBuzz" if the number is divisible by 3 and 5 (e.g. fizz_buzz(15) == "FizzBuzz")
# return the input as a String otherwise (e.g. fizz_buzz(7) == "7" ).

# if number % 3 == 0:
#   if number % 5 == 0:
#       return FizzBuzz
#   return Fizz

# if number % 3 == 0 and number % 5 == 0:
#   return FizzBuzz

# if number % 15 == 0:
#   




