#!/usr/bin/env python3

class MyString:
  class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("Value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Replace all punctuation marks with periods for uniformity
        modified_string = self.value.replace('?', '.').replace('!', '.')
        # Split the modified string into sentences based on period as separator
        sentences = [sentence.strip() for sentence in modified_string.split('.') if sentence.strip()]
        return len(sentences)

# Test the implementation
string = MyString("This is a string! It has three sentences. Right?")
print("Is a sentence?", string.is_sentence())
print("Is a question?", string.is_question())
print("Is an exclamation?", string.is_exclamation())
print("Number of sentences:", string.count_sentences())
