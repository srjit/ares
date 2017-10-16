import re
import string
from bs4 import BeautifulSoup

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"


null = 0
empty = 0


foo = []



def replace_null_with_empty_string(html):
    '''
      Replace null cells in "value" with an empty string
      and creates a corresponding new string to put in 
      "cleaned_value" column
    '''

    global null
    global empty
    if html is not None:
        if html.strip() == "":
            print("Empty string")
            empty  += 1
            return ""
    else:
        #print("Null")
        null += 1
        return ""
    return html



def clean_html_and_extract_text(raw_html):
    
    '''
       Clean an html string that comes from "cleaned_value"  column
    '''
    global foo
    
    ## use regular expressions to remove roman numberals inside brackets
    ## eg. (iv), (ix) etc.
    raw_html = re.sub('\([v|i|x]+\)', '', raw_html)
    raw_html = re.sub('\s\d+\s', '', raw_html)


    ## clear off the non ascii characters, remove the html tags 
    ## and get just the text from the document
    raw_html = bytes(raw_html, 'utf-16').decode("utf-16", 'ignore')
    cleantext = BeautifulSoup(raw_html).text
    cleantext = " ".join(cleantext.split())

    foo.append(cleantext)


    ## clear off punctuations in the text
    table = cleantext.maketrans("","", string.punctuation)
    cleantext = cleantext.translate(table)

    ## clear off all arabic numerals / digits in the text which are attached 
    ## together with text
    numbers = re.findall('\d+', cleantext)
    for number in numbers:
        cleantext = cleantext.replace(number, " ")

    ## clear off numbers and normalize spaces between words
    ## and lowercase it
    cleantext = " ".join([text for text in cleantext.split(" ") 
                              if text.strip() is not "" and text.isdigit() is False]).lower()

    ## remove any non-printable (non-ascii) characters in the text
    printable = set(string.printable)
    cleantext = list(filter(lambda x: x in printable, cleantext))
    cleantext = "".join(cleantext)
    
    ## remove roman numberals from string which
    ## are not in brackets
    toremove = [' ii ',' iii ', ' iv ', ' v ', ' vi ', ' vii ', ' viii ', ' ix ', ' x ']
    text_array = cleantext.split("\s+")
    cleantext = [word.strip() for word in text_array if word not in toremove]
    cleantext = " ".join(cleantext)
    
    return cleantext.strip()

