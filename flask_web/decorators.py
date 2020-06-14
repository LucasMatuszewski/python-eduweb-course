# Annotations in Python:
# https://www.python.org/dev/peps/pep-3107/

# DECORATORS - design pattern
# decorators wrap a function, modifying its behavior.
# https://realpython.com/primer-on-python-decorators/
# https://www.python.org/dev/peps/pep-0318/

# In Python functions are First-Class Objects (Like in JS)
# That means that function can be passed around and used as arguments in other function.

# We can also define a function inside another function.
# Then we can use it immediately inside this function or return it to use it letter.
# If we return it we could save it to an variable. Decorators use this possibility:

from datetime import datetime


def not_during_the_night(func):
    def wrapper():  # inner wrapper function to return
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper


def say_whee():
    print("Whee!")


# Here we decorate say_we function with not_during_the_night decorator (wrapper)
say_whee = not_during_the_night(say_whee)

# Now as say_whee whe have a reference to returned wrapper function and we can call it:
say_whee()

# But it's not a nice way to use decorators. We have to use "say_whee" three times...

# Python gives us simpler way to use decarators with @ symbol (a syntactic sugar).
# It's sometimes called "pie syntax". Belows code do exactly the same thing:


@not_during_the_night
def say_whee2():
    print("Whee!!")


say_whee2()

# Descorators are not the same as annotations in JAVA.
# Java's annotation just adds metadata, and Python's decorators modify usage of the function.

# In JavaScript there is an proposal for syntactic sugar for decorators like in Python with @.
# This is a concept well known as functional composition, or higher-order functions.
# We can use decorators in JS now, but we have to transpile our code with Babel plugin:
# https://github.com/loganfsmyth/babel-plugin-transform-decorators-legacy
# https://www.sitepoint.com/javascript-decorators-what-they-are/
