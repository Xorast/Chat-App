# string = "bonjour je m'appelle xavier"
# string = string.replace("xavier","Miguel")
# print(string)
text = "@bonjour blablabla"
user = text.split(' ', 1)[0]
user = user[1:]
print(user)