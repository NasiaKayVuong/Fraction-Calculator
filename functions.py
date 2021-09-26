from fraction_class import Fraction

# Converts string input of mixed number
# to array representation of improper fraction


def convert_mixed(arg):
    new_arg = arg.split("_")
    whole = int(new_arg[0])
    frac = new_arg[1].split("/")
    n, d = int(frac[0]), int(frac[1])
    frac_list = [whole, n, d]
    single_whole = Fraction(d, d)
    new_whole = single_whole * whole
    new_frac = Fraction(n, d)

    imp_frac = new_whole + new_frac
    imp_frac = str(imp_frac)
    frac_list = imp_frac.split("/")
    frac_list = [int(i) for i in frac_list]

    return frac_list


# Converts string input whole number
# to array representation of improper fraction
def convert_whole(arg):
    whole_frac = [int(arg), 1]
    return whole_frac


# Converts improper fraction created by Fraction class
# to equivalent mixed number
def convert_imp(arg):
    str_arg = str(arg)
    list_arg = str_arg.split("/")
    n = int(list_arg[0])
    d = int(list_arg[1])

    w = n // d
    t = n % d

    if t == 0 and w > 0:
        return w
    elif w == 0:
        return "{}/{}".format(t, d)
    else:
        return "{}_{}/{}".format(w, t, d)


# Parses string input of a number (whole, mixed, proper or improper fraction)
# and returns array representation of an equivalent fraction
def fraction_parse(a):
    if "_" in a:
        a_list = convert_mixed(a)
    elif "/" in a:
        str_list = a.split("/")
        a_list = [int(i) for i in str_list]
    else:
        a_list = convert_whole(a)
    return a_list


def calculate(input):
    input_list = input.split(" ")

    operator = input_list[1]
    num1 = fraction_parse(input_list[0])
    num2 = fraction_parse(input_list[2])
    frac1 = Fraction(num1[0], num1[1])
    frac2 = Fraction(num2[0], num2[1])

    if operator == "+":
        result = frac1 + frac2
    elif operator == "-":
        result = frac1 - frac2
    elif operator == "*":
        result = frac1 * frac2
    else:
        result = frac1 / frac2

    print(convert_imp(result))

# TESTS


# addition
calculate("3/4 + 1_1/4")
# subtraction
calculate("3 - 6/8")
# multiplication
calculate("1_2/3 * 3")
# division
calculate("6_1/2 / 4/7")


# Unit Tests
print(convert_mixed("1_1/2"))
print(convert_whole("1"))
print(convert_imp("17/4"))
print(fraction_parse("1_1/2"))
print(convert_imp("2/1"))
