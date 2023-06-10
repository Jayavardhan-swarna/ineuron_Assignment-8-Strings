from collections import Counter

def findAnagrams(s, p):
    result = []
    p_counter = Counter(p)
    s_counter = Counter(s[:len(p)])  # Counter for the first window

    if s_counter == p_counter:
        result.append(0)

    for i in range(len(p), len(s)):
        left_char = s[i - len(p)]
        new_char = s[i]

        s_counter[left_char] -= 1
        if s_counter[left_char] == 0:
            del s_counter[left_char]

        s_counter[new_char] += 1

        if s_counter == p_counter:
            result.append(i - len(p) + 1)

    return result

s = "cbaebabacd"
p = "abc"
result = findAnagrams(s, p)
print(result)  # Output: [0, 6] 
