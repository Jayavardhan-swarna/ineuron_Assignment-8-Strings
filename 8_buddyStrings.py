def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False

    if s == goal:
        # Check if s has any repeated characters
        return len(set(s)) < len(s)

    pairs = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            pairs.append((s[i], goal[i]))

        if len(pairs) > 2:
            return False

    return len(pairs) == 2 and pairs[0] == pairs[1][::-1]

# Example usage:
s = "ab"
goal = "ba"
result = buddyStrings(s, goal)
print(result)  # Output: True 
