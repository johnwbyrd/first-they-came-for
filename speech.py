# speech.py
# long-winded parody of Martin Niemöller 

# Wrap the output text into 80 columns?
wrap = False

import textwrap

# The list of singular things at the end of a sentence.
# This program makes them plural by adding an s at
# the end.  Also, everything in this list gets an
# automatic 'a' as its determiner.
singulars = [
    'Socialist',
    'Trade Unionist',
    'Jew',
    'sick, the so-called incurables',
    'Catholic',
    'disabled',
    'homosexual',
    'Bohemian',
    'Slovak',
    'Czech',
    'Austrian',
    'West Prussian',
    'Bolshevik',
    'Serb',
    'Protestant',
    'Albanian',
    'Austrian',
    'Latvian',
    'Lithuanian',
    'Estonian',
    'Pole',
    'Freemason',
    'Ukrainian',
    'Byelorussian',
    'Moldavian',
    'Sammarinese',
    'Monacan',
    'Yugoslavians',
    'Romanian',
    'Dutch',
    'Esperantist',
    'Italian',
    'Hungarian',
    'Danish',
    'Belgian',
    'Aegean',
    'Finn',
    'Croatian',
    'Macedonian',
    'Luxembourger',
    'Montenegran',
    'Romani',
    'citizens of Danzig',
    'Soviet',
    'political prisoner',
    'leftist',
    "Jehovah's Witnesses",

    'German Mennonite',

    'Lutheran',
    'Christian clergy',
    'Amish',
    'Hutterite',

    'lesbians',
    'transgender people',
    'deaf',
    ]

# The list of exceptions.  These exceptions do not
# automatically get the automatic 'a' that the 
# singulars do above, nor do they get the 's'.  So
# they must be added if you need it.
exceptions = {
    'sick, the so-called incurables': 'sick or incurable',
    'disabled': 'disabled',
    'citizens of Danzig': 'a citizen of Danzig',
    'French': 'French',
    'Sammarinese': 'Sammarinese',
    'Yugoslavians': 'a Yugoslav',
    'Dutch': 'Dutch',
    'Danish': 'Danish',
    "Jehovah's Witnesses": "a Jehovah's Witness",
    'Christian clergy': 'clergy',
    'Amish': 'Amish',
    'lesbians': 'lesbian',
    'transgender people': 'transgender',
    'deaf': 'deaf',
    }

first = True
speech = ''

def say(phrase):
    global speech
    speech = speech + phrase

for ethnicgroup in singulars:
    plural = ethnicgroup + 's'
    if ethnicgroup[0].lower() in 'aeiou':
        singular = 'an ' + ethnicgroup
    else:
        singular = 'a ' + ethnicgroup
    if ethnicgroup in exceptions:
        singular = exceptions[ ethnicgroup ]
        plural = ethnicgroup
    if first:
        say( 'First, ')
        first = False
    else:
        say( 'Then, ')
    say ('they came for the ')
    say (plural)
    say (', and I did not speak out, because I was not ')
    say (singular)
    say ('.  ')

say ('Then, they came for me, and ')
say ('I told them, what took you so fucking long?')
funny = True

if wrap:
    print( textwrap.fill( speech ))
else:
    print( speech )


