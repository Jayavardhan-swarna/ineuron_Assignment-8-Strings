def compress(chars):
    anchor = 0  # Anchor pointer to mark the start of a group
    write = 0  # Write pointer to overwrite the original array
    
    for read in range(len(chars)):
        # Check if the current group ends
        if read + 1 == len(chars) or chars[read + 1] != chars[read]:
            chars[write] = chars[anchor]  # Write the character
            
            # If the group has more than one character, write the group's length
            if read > anchor:
                count = str(read - anchor + 1)
                chars[write + 1:write + 1 + len(count)] = count
                write += len(count)
            
            write += 1  # Move the write pointer
            anchor = read + 1  # Move the anchor pointer
            
    return write  # Return the new length of the array


chars = ["a", "a", "b", "b", "c", "c", "c"]
result = compress(chars)
print(result)  # Output: 6
print(chars[:result])  # Output: ['a', '2', 'b', '2', 'c', '3'] 
