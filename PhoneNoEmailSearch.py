import re, pyperclip

phone_regex = re.compile(r'''(
                            (\d{3}| \(\d{3}\))?                 # Area code, sometimes in parenthesis
                            (\s|-|\.)?                          # separator
                            (\d{3})                             # First three digits                          
                            (\s|-|\.)?                          # separator
                            (\d{4})                             # last four digits
                            )''', re.VERBOSE)

# TODO Create email regex

email_regex = re.compile(r'''(
                              [a-zA-Z0-9._%+-]+                  # email address  
                              @                                  # @ symbol
                              [a-zA-Z0-9._%+-]+
                               (\.[a-zA-Z]{2,4})                            # final 'com' in an email address
                              )''', re.VERBOSE)

pypertext = str(pyperclip.paste())

# paste un-sorted text
print(pypertext)

matches = []

for groups in phone_regex.findall(pypertext):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    phoneNum.replace('(', '')
    phoneNum.replace(')', '')
    matches.append(phoneNum)

for groups in email_regex.findall(pypertext):
    matches.append(groups[0])


if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

PhoneEmailMatches = open('PhoneEmailMatches.txt', 'w')
PhoneEmailMatches.write(str(matches))
PhoneEmailMatches.close()


