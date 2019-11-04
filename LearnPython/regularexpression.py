#!/usr/local/bin/python3

# this is regular expression example program

# REFER THE RegEx Text file for regular expression keys.

import re

sampleText = '''
It is a major effort to even build a standard corpus of the language and decode the writing on existing artefacts
and map them to this standard corpus. The most widely accepted corpora of Indus scripts was brought together by the efforts of Iravatham Mahadevan,
noted Indian epigraphist, from the 3,700 texts and 417 unique signs collected so far.
It is a major effort to even build a standard corpus of the language and decode the writing on existing artefacts
and map them to this standard corpus. The most widely accepted corpora of Indus scripts was brought together by the efforts of Iravatham Mahadevan,
noted Indian epigraphist, from the 3,700 texts and 417 unique signs collected so far.
It is a major effort to even build a standard corpus of the language and decode the writing on existing artefacts
and map them to this standard corpus. The most widely accepted corpora of Indus scripts was brought together by the efforts of Iravatham Mahadevan,
noted Indian epigraphist, from the 3,700 texts and 417 unique signs collected so far.
It is a major effort to even build a standard corpus of the language and decode the writing on existing artefacts
and map them to this standard corpus. The most widely accepted corpora of Indus scripts was brought together by the efforts of Iravatham Mahadevan,
noted Indian epigraphist, from the 3,700 texts and 417 unique signs collected so far.
It is a major effort to even build a standard corpus of the language and decode the writing on existing artefacts
and map them to this standard corpus. The most widely accepted corpora of Indus scripts was brought together by the efforts of Iravatham Mahadevan,
noted Indian epigraphist, from the 3,700 texts and 417 unique signs collected so far.
'''

resultText = re.findall(r'\d{1,9}', sampleText)
resultName = re.findall(r'[A-Z]h+', sampleText)

print(resultText)
print(resultName)
