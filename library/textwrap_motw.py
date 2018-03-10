import textwrap

sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''

def text_wrap_fill():
    print(textwrap.fill(sample_text, width=50))

def dedent():
    dedented_text = textwrap.dedent(sample_text)
    print('Dedent:')
    print(dedented_text)

def fill_width():
    dedent_text = textwrap.dedent(sample_text).strip()
    for width in [45,60]:
        print('{} Columns: \n'.format(width))
        print(textwrap.fill(dedent_text, width=width))
        print()    

def should_indent(line):
    print('Indent {!r}?'.format(line))
    return len(line.strip()) % 2 == 0

def indent_predicate():
    dedent_text = textwrap.dedent(sample_text)
    wrapped = textwrap.fill(dedent_text, width=50)
    final = textwrap.indent(wrapped, 'EVEN', predicate=should_indent)
    print(final)

def handing_indent():
    dedented_text = textwrap.dedent(sample_text).strip()
    print('dedented_text: ' + dedented_text)
    print('-----------------------------------')
    print(textwrap.fill(dedented_text,
                        initial_indent='----',
                        subsequent_indent=' ' * 4,
                        width=50,))

def shorted():
    dedented_text = textwrap.dedent(sample_text)
    original = textwrap.fill(dedented_text, width=50)

    print('Original: \n')
    print(original)

    shortened = textwrap.shorten(original, 100)
    print('\nShorten: \n')
    print(shortened)
    shortened_wrapper = textwrap.fill(shortened, width=50)

    print('\nShortened: \n')
    print(shortened_wrapper)