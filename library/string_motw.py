import string

def capwords():
    s = 'The quick brown fox jumped over the lazy dog.'
    print(s)
    print(string.capwords(s))

def templates():
    values = {'var': 'foo'}
    t = string.Template("""
    Variable        : $var
    Escape          : $$
    Variable in text: ${var}iable
    """)

    print('TEMPLATE', t.substitute(values))

    s = """
    Variable        : %(var)s
    Escape          : %%
    Variable in text: %(var)siable
    """

    print('INTERPOLATION:', s % values)

    f = """
    Variable        : {var}
    Escape          : {{}}
    Variable in text: {var}iable
    """

    print('FORMAT:', f.format(**values))


def missing():
    values = {'var': 'foo'}

    t = string.Template("$var is here but $missing is not provided")

    try:
        print('substitute()     :', t.substitute(values))
    except KeyError as err:
        print('ERROR:', str(err))

def temp_defpattern():
    t = string.Template('$var')
    print(t.pattern.pattern)