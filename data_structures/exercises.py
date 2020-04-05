from pprint import pprint
# find the most repeated character
sentence = "This is the most common inteview question"
most_repeated_char = {}
for char in sentence:
    if char in most_repeated_char:
        most_repeated_char[char] += 1
    else:
        most_repeated_char[char] = 1

most_repeated_char_sorted = sorted(
    most_repeated_char.items(),
    key=lambda kv: kv[1],
    reverse=True
)
pprint(most_repeated_char_sorted[1], width=1, indent=2)
