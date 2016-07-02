import codecs
import sys
import base64



User = raw_input("Please enter the text: \n")

decode_codecs = codecs.encode(User[::-1], 'rot13')

text = base64.b64decode (decode_codecs)

print text
