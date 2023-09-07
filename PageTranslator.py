#! python3
# a script that opens a new webpage translated into
# language of choice
"""

     Translating a data frame 
     is the process of changing a data frame 
     values language to another language 
     without changing the context, meaning, or content. 
  Translating a Pandas Data Frame with Python can be done with Google’s 
  “googletrans” library.
"""
#TODO: ENABLE activation via terminal Get the whole page
#TODO: 


import translate


translator = translate.Translator(to_lang='cs')
translation=translator.translate('why are you like this?')
print(translation)
