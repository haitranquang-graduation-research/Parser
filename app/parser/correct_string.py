from ftfy import fix_encoding, fix_text
dictionary = {
    'á»’': "Ồ",
    'á»“': 'ồ',
    'á»œ': 'Ờ',
    'Æ¡': 'ơ',
    'Æ°': 'ư',
    'á»©': 'ứ',
    'Å©': 'ũ',
    'á»±': 'ự',
    'Ä©': 'ĩ',
    "á»·": 'ỷ'
}

def correct_string(mystr):
    mystr = fix_text(mystr)
    for key in dictionary.keys():
        mystr = mystr.replace(key, dictionary[key])
    return mystr
