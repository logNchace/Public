def spell_backward(input_string):
    # Split the string into words
    words = input_string.split()
    # Reverse each word individually
    reversed_words = [word[::-1] for word in words]
    # Join the reversed words back into a string
    backward_string = ' '.join(reversed_words)
    return backward_string

# Prompt the user for input
user_input = input("Enter a string: ")

# Call the function to spell the string backward
result = spell_backward(user_input)

# Print the backward spelling
print("Backward spelling:", result)
