import re

""" # 1. Match the word "cat" in a string.
pattern = r"cat"
text = "The cat sat on the mat."
match = re.search(pattern, text)
print(match.group() if match else "No match") """



""" # 2. Match "cat" regardless of its case.
pattern = r"cat"
text = "The Cat sat on the mat."
match = re.search(pattern, text, re.IGNORECASE)
print(match.group() if match else "No match") """

""" # 3. Match any three-letter word ending with 'at'.
pattern = r"[a-z]at"
text = "The cat sat on the mat."
matches = re.findall(pattern, text)
print(matches) """

""" # 4. Match any sequence of digits.
pattern = r"[0-9]+"
text = "There are 123 apples."
matches = re.findall(pattern, text)
print(matches) """

""" # 5. Match sequences not containing digits.
pattern = r""
text = "There are 123 apples."
matches = re.findall(pattern, text)
print(matches) """

""" # 6. Match "cat" as a whole word.
pattern = r"\bcat\b"
text = "The cat sat on the concatenate."
matches = re.findall(pattern, text)
print(matches) """

""" # 7. Match "cat" or "bat".
pattern = r"cat|bat"
text = "The cat and the bat."
matches = re.findall(pattern, text)
print(matches) """

""" # 8. Match any word starting with a letter in the range 'a' to 'c'.
pattern = r"[a-c]at"
text = "cat, bat, rat, mat."
matches = re.findall(pattern, text)
print(matches) """

""" # 9. Match any three-letter word not starting with 'b' or 'c'.
pattern = r"[^b-c]at"
text = "cat, bat, rat, mat."
matches = re.findall(pattern, text)
print(matches) """

""" # 10. Check if the string starts with "The".
pattern = r"^The"
text = "The cat sat."
match = re.search(pattern, text)
print(match.group() if match else "No match") """

""" # 11. Check if the string ends with "sat."
pattern = r"sat.$"
text = "The cat sat."
match = re.search(pattern, text)
print(match.group() if match else "No match") """

""" # 12. Match "color" and "colour".
pattern = r"colou?r"
text = "Both color and colour are correct."
matches = re.findall(pattern, text)
print(matches) """

""" # 13. Match "o" followed by any number of "o"s.
pattern = r"o+"
text = "The book is on the stool."
matches = re.findall(pattern, text)
print(matches) """

""" # 14. Match "o" followed by one or more "o"s.
pattern = r"o{1+}"
text = "The book is on the stool."
matches = re.findall(pattern, text)
print(matches) """

""" # 15. Match "o" exactly twice.
pattern = r"oo"
text = "The book is on the stool."
matches = re.findall(pattern, text)
print(matches) """

""" # 16. Match "o" between two and three times.
pattern = r"o{2,3}"
text = "The book is on the stool."
matches = re.findall(pattern, text)
print(matches) """

""" # 17. Match the smallest possible string of "o"s.
pattern = r"o+?"
text = "The booooook is long."
match = re.search(pattern, text)
print(match.group() if match else "No match") """

""" # 18. Match and group "cat" or "bat".
pattern = r"cat | bat"
text = "The cat in the hat chased the bat."
matches = re.findall(pattern, text)
print(matches) """

""" # 19. Match and capture nested groups.
pattern = r"(\d{3})-(\d{3})-(\d{4})"
text = "The number is 123-456-7890."
match = re.search(pattern, text)
print(match.groups() if match else "No match") """

""" # 20. Match repeated words.
pattern = r"\b(\w+)( \1)+\b"
text = "The the cat sat sat on the the mat."
matches = re.findall(pattern, text)
print(matches) """

""" # 21. Match simple email addresses.
pattern = r"\b\w+@\w+\.\w+\b"
text = "Contact us at info@example.com."
matches = re.findall(pattern, text)
print(matches) """

""" # 22. Match web URLs.
pattern = r"https?://(?:www\.)?\w+\.\w+"
text = "Visit https://www.example.com for more info."
matches = re.findall(pattern, text)
print(matches) """

""" # 23. Match phone numbers in various formats.
pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
text = "Call 123-456-7890 or (123) 456-7890."
matches = re.findall(pattern, text)
print(matches) """

""" # 24. Case-insensitive match of "python".
pattern = r"python"
text = "Python is fun. python is powerful."
matches = re.findall(pattern, text, re.IGNORECASE)
print(matches) """

""" # 25. Split a string at each space or comma.
pattern = r"[, ]"
text = "The,quick brown,fox jumps"
words = re.split(pattern, text)
print(words) """

""" # 26. Replace "cat" with "dog".
pattern = r"cat"
text = "The cat sat on the mat."
new_text = re.sub(pattern, "dog", text)
print(new_text) """

""" # 27. Match "color" or "colour" without capturing the group.
pattern = r"\b(?:colou?r)\b"
text = "Both color and colour are correct."
matches = re.findall(pattern, text)
print(matches) """

""" # 28. Match "John" only if followed by "Smith".
pattern = r"John (?=Smith)"
text = "John Smith vs. John Doe"
matches = re.findall(pattern, text)
print(matches) """

""" # 29. Match "Smith" only if preceded by "John".
pattern = r"(?<=John) Smith"
text = "John Smith vs. John Doe"
matches = re.findall(pattern, text)
print(matches) """

""" # 30. Match any Unicode letter.
pattern = r"\p{L}"
text = "Résumé"
matches = re.findall(pattern, text, re.UNICODE)
print(matches) """

""" # 31. Match hexadecimal numbers (e.g., #a3c113).
pattern = r"#([0-9a-fA-F]+)"
text = "The color code is #a3c113."
matches = re.findall(pattern, text)
print(matches) """

""" # 32. Match words containing 'ing'.
pattern = r"\b\w*ing\w*\b"
text = "Playing, singing, and swimming are fun."
matches = re.findall(pattern, text)
print(matches) """

""" # 33. Match sentences ending with a question mark.
pattern = r"[^.!?]+\?"
text = "What is your name? How old are you?"
matches = re.findall(pattern, text)
print(matches) """

""" # 34. Match all words starting with 's' and ending with 'e'.
pattern = r"\b[sS]\w*e\b"
text = "Store and sell are similar words."
matches = re.findall(pattern, text)
print(matches) """

""" # 35. Match all HTML tags.
pattern = r"<[^>]+>"
text = "<html><head><title>Title</title></head></html>"
matches = re.findall(pattern, text)
print(matches) """

""" # 36. Match all Twitter handles (e.g., @username).
pattern = r"@\w+"
text = "Follow me on Twitter @example_user."
matches = re.findall(pattern, text)
print(matches) """

""" # 37. Match dates in the format YYYY-MM-DD.
pattern = r"\b\d{4}-\d{2}-\d{2}\b"
text = "Today's date is 2023-01-01."
matches = re.findall(pattern, text)
print(matches) """

""" # 38. Match all words longer than 5 letters.
pattern = r"\b\w{6,}\b"
text = "Regular expressions are powerful."
matches = re.findall(pattern, text)
print(matches) """

""" # 39. Match all floating-point numbers.
pattern = r"-?\d+\.\d+"
text = "The temperature is -3.14 degrees."
matches = re.findall(pattern, text)
print(matches) """

""" # 40. Match all XML tags.
pattern = r"<[^>]+>"
text = "<note><to>User</to><from>Admin</from></note>"
matches = re.findall(pattern, text)
print(matches) """

