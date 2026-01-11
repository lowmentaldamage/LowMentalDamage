# Word Abbreviation ("Too Long Words") Problem:
# For each word in the input:
#   - If its length ≤ 10: output the word unchanged.
#   - If its length > 10: abbreviate it as:
#         <first_letter> + str(length - 2) + <last_letter>
#     (e.g., "localization" → len=14 → "l" + "12" + "n" → "l12n" → wait: actually 14-2=12? 
#      But example says "l10n" for "localization" — let's verify: 
#        'localization' has 13 letters? Let's count: l-o-c-a-l-i-z-a-t-i-o-n → 12? Actually:
#        l(1) o(2) c(3) a(4) l(5) i(6) z(7) a(8) t(9) i(10) o(11) n(12) → 12 letters.
#        So abbreviation: first 'l', last 'n', middle count = 12 - 2 = 10 → "l10n" 
#     So rule: middle_count = len(word) - 2
# 
# Input: 
#   First line: n (number of words, 1 ≤ n ≤ 100)
#   Next n lines: one word each (lowercase, length 1–100)
# Output:
#   n lines: each word either unchanged or abbreviated per rule.
#
# Example: 
#   "pneumonoultramicroscopicsilicovolcanoconiosis" → len=45 → 'p' + str(45-2) + 's' → "p43s"

# Inputing starting value
n = int(input())

# THE LOOP
for _ in range(n):
    word = input().strip()

    # Checking the size of word
    if len(word) > 10:
        new = word[0] + str(len(word) - 2) + word[-1]
        print(new)

    # if word is less than 10 characters it skips it
    else:
        print(word)


