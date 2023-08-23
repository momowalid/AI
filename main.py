import re
file=open("task6.txt","r")
motext=file.read()
phones=[]
names=[]
emails=[]
pattern=re.compile("01\d{9}")
matches=pattern.finditer(motext)
for match in matches:
    start=match.span()[0]
    end=match.span()[1]
    phones.append(motext[start:end])
pattern=re.compile("\w+@\D+com")
matches=pattern.finditer(motext)
for match in matches:
    start=match.span()[0]
    end=match.span()[1]
    emails.append(motext[start:end])
pattern=re.compile("[A-Z][a-z]+\s[A-Z][a-z]+\s")
matches=pattern.finditer(motext)
for match in matches:
    start=match.span()[0]
    end=match.span()[1]
    names.append(motext[start:end])
print("names are :")
for name in names:
    print(name)
print("phones numbers are :")
for phone in phones:
    print(phone)
print("emails are :")
for email in emails:
    print(email)