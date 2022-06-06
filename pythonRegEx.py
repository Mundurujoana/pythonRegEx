#Regular Expressions
# A regular expression or RegEx is a special text string that helps to find patterns in data. A RegEx can be used to check 
# if some pattern exists in a different data type.

# The re Module
import re
# After importing the module we can use it to detect or find patterns.


#MATCH
# re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
text = "i love to teach python"
match = re.match("i love to teach", text,re.I)
print(match)
span = match.span()
print(span)
start,end= span
print(start,end)

substring = text[start:end]
print(substring)

tech="I do courses in tech like html, css, python"
techmatch = re.match("i do courses in tech like html",tech,re.I)
print(techmatch)

spantech = match.span()
print(spantech)

sbstring = tech[start:end]
print(sbstring)

print(start,end)
txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)


#SEARCH
# re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

search = re.search("first",txt,re.I)
print(search)

span = search.span()
print(span)

substr = txt[start:end]
print(substr)

print(start,end)

#FINDALL
# re.findall: Returns a list containing all matches
language = "Python is the most beautiful language that a human being has ever created"
findall = re.findall("language",language,re.I)
print(findall)

matches = re.findall('python',language,re.I)
print(matches)

#Replacing a Substring
# re.sub: Rere.sub: Replaces one or many matches within a string
match_replaced = re.sub('Python|python','javascript',language,re.I)
print(match_replaced)

#Let us add one more example. The following string is really hard to read 
# unless we remove the % symbol. Replacing the % with an empty string will
#  clean the text.
txt1 = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
match_rem = re.sub('%','',txt1)
print(match_rem)

# Splitting Text Using RegEx Split
# re.split: Takes a string, splits it at the match points, returns a list
teaches = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''

split_teaches = re.split('\n',teaches)
print(split_teaches)

# Writing RegEx Patterns
# To declare a string variable we use a single or double quote. 
# To declare RegEx variable r''
apple = '''Apple and banana are fruits. 
An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'''

regex_pattern = r'apple'
txt_apple = re.findall(regex_pattern,apple)
print(txt_apple)

# To make case insensitive adding flag'
flag_apple=re.findall(regex_pattern,apple,re.I)
print(flag_apple)

apple_matches = re.findall(regex_pattern,apple)
print(apple_matches)