import re

# x = re.search(r"Name", "My Name is Dominic, Dominic is the Name")
# print(x)
# x = re.match(r"(My) (Name)", "My Name is Dominic, Dominic is the Name")
# print(x.group())

# Use of special characters
special_char_list = [r".", r"\w", r"\W", r"\s", r"\S", r"\t", r"\n", r"\r", r"\d", "^MY Name", r"\AMy"]
sequence = "MY Name is Anthony GOnsalves1234. Me Duniya ne Akela huuuuu!...\n" \
           "My"

for special_char in special_char_list:
    print(special_char, re.search(special_char, sequence))

print("*" * 50)
print(re.search(r"[abc]", sequence))
print(re.search(r"[a-zA-z0-9]", sequence))
print(re.search(r"(0-9)", sequence))


print("*" * 50)
print(re.search(r".{6,7}", sequence))
print(re.search(r".+?", sequence))
print(re.search(r".??", sequence))