# 1) Searching for a pattern in re using re.search() Method ==>>
import re
# Define a regular expression pattern
pattern = r"expression"
# Match the pattern against a string
text = "Hello, world!"
match = re.search(pattern, text)
if match:
    print("Match found!")
else:
    print("Match not found.")
    print("______________________________________")
    
    
# 2) Searching for a pattern in re using re.findall() Method ==>>
import re
pattern = r"expression"
text = "The cat is in the hat."
matches = re.findall(pattern, text)
print(matches)
print("______________________________________")


# 3) The following example shows how to replace a pattern in a string ==>> 
import re
pattern = r"[a-z]+at"
text = "The cat is in the hat."
matches = re.findall(pattern, text)
print(matches)
new_text = re.sub(pattern, "dog", text)
print(new_text)
print("______________________________________")



# 4) The following example shows how to extract information from a string using regular expressions: ==>>
import re
text = "The email address is example@example.com."
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)
if match:
    email = match.group()
    print(email)
print("______________________________________")