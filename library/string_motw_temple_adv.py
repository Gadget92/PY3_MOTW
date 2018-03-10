import string
import re

class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'


def temp_adv():

    template_text = '''
    Delimiter : %%
    Replaced  : %with_underscore
    Ignored   : %notunderscored
    '''

    d = {
        'with_underscore': 'replaced',
        'notunderscored': 'not replaced',
    }

    t = MyTemplate(template_text)
    print('Modified ID pattern: ')
    print(t.safe_substitute(d))


class MyTemplate2(string.Template):
    delimeter = '{{'
    pattern = r'''
    \{\{(?:
    (?P<escaped>\{\{)|
    (?P<named>[_a-z][_a-z0-9]*)\}\}|
    (?P<braced>[_a-z][_a-z0-9]*)\}\}|
    (?P<invalid>)
    )
    '''

def temp_newsyntax():
    t =MyTemplate2('''
    {{{{
    {{var}}
    ''')

    print('MATCHES:', t.pattern.findall(t.template))
    print('SUBSTITUTED:', t.safe_substitute(var='replacement'))