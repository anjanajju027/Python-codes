import string  # Correct module

# Input string with punctuation
input_text = "Hello, World! Let's remove punctuation: isn't it fun?!"

# Remove punctuation using str.translate() and string.punctuation
cleaned_text = input_text.translate(str.maketrans('', '', "'!?"))

# Output the cleaned text
print("Original Text:", input_text)
print("Text without Punctuation:", cleaned_text)