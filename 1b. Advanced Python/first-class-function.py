def square(n):
    return n * n


# A function is called First order function
# If it can be assigned to variables
# It can be assigned as arguments
# Can be returned from other functions
# Can be stored in data structures.
f = square
print(square)
print(f(4))


def cube(x):
    return x * x * x


def my_map(func, lst):
    result = []
    for i in lst:
        result.append(func(i))
    return result


cubes = my_map(cube, [1, 2, 3, 4, 5])
print(cubes)


def logger(msg):
    def log_msg():
        print(f"Log: {msg}")

    return log_msg


log_hi = logger("Hii")
log_hi()


def html_tag(tag):
    def wrapper(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))

    return wrapper


p = html_tag("H1")
p("text headline")
p("Another headline")
