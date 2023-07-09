def get_full_name(first, middle, last):

    try:
        full_name = "{0} {1} {2}".format(first,middle, last)

    except:
        full_name = "{0} {1}".format(first, last)

    else:
        full_name = "{0} {1}".format(first, middle)

    return full_name.title()


print(get_full_name('Kumail', 'Haider'))