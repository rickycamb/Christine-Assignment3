import re

# I. Extract all email addresses from a given text
def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)

# II. Validate a date in the format "YYYY-MM-DD"
def validate_date(date_string):
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    return re.match(date_pattern, date_string) is not None

# III. Replace all occurrences of a word with another word in a string
def replace_word(text, old_word, new_word):
    return re.sub(old_word, new_word, text)

# IV. Split a string by all non-alphanumeric characters
def split_string(text):
    return re.split(r'\W+', text)

# Example Usage
text = "Contact us at support@example.com or visit our website."
print("Extracted Emails:", extract_emails(text))

date = "2023-04-05"
print("Is the date valid?", validate_date(date))

replaced_text = replace_word("Hello world! Hello everyone!", "Hello", "Hi")
print("Replaced Text:", replaced_text)

split_result = split_string("Hello! How are you doing today?")
print("Split String:", split_result)