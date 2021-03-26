# textwrap.wrap(text, width=70, **kwargs)
import textwrap

value = """This function wraps the input paragraph such that each line 
in the paragraph is at most width characters long. The wrap method 
returns a list of output lines. The returned list 
is empty if the wrapped 
output has no content."""

# Wrap this text.
wrapper = textwrap.TextWrapper(width=50)

word_list = wrapper.wrap(text=value)

# Print each line.
for element in word_list:
    print(element)
# textwrap.fill(text, width=70, **kwargs):
value = """This function returns the answer as STRING and not LIST."""

# Wrap this text.
wrapper = textwrap.TextWrapper(width=50)

string = wrapper.fill(text=value)

print(string)
# textwrap.dedent(text):

wrapper = textwrap.TextWrapper(width=50)

s = '''\ 
    hello 
      world 
    '''
print(repr(s))  # prints '    hello\n      world\n    '

text = textwrap.dedent(s)
print(repr(text))  # prints 'hello\n  world\n'
# textwrap.shorten(text, width, **kwargs):

sample_text = """This function wraps the input paragraph such that each line 
n the paragraph is at most width characters long. The wrap method 
returns a list of output lines. The returned list 
is empty if the wrapped 
output has no content."""

wrapper = textwrap.TextWrapper(width=50)

dedented_text = textwrap.dedent(text=sample_text)
original = wrapper.fill(text=dedented_text)

print('Original:\n')
print(original)

shortened = textwrap.shorten(text=original, width=100)
shortened_wrapped = wrapper.fill(text=shortened)

print('\nShortened:\n')
print(shortened_wrapped)
# textwrap.indent(text, prefix, predicate=None)
s = 'hello\n\n \nworld'
s1 = textwrap.indent(text=s, prefix=' ')

print(s1)
print("\n")

s2 = textwrap.indent(text=s, prefix='+ ', predicate=lambda line: True)
print(s2)