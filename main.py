def find_anagram(word, anagram):
    lower_case_word = word.lower()
    lower_case_anagram = anagram.lower()
    sort_the_word = sorted(lower_case_word)
    sort_the_anagram = sorted(lower_case_anagram)
    if sort_the_word == sort_the_anagram:
        return True
    else:
        return False

do = find_anagram("below", "elbow")
print(do)
   