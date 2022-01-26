"""""
1. Import the regex module with import re.
2. Create a Regex object with the re.compile() function. (Remember to use
a raw string.)
3. Pass the string you want to search into the Regex object’s search()
method. This returns a Match object.
4. Call the Match object’s group() method to return a string of the actual
matched text.
"""

import re

"""
Note:
Most of the examples that follow in this training will require the re module, so remember to import it at
the beginning of any script you write or any time you restart IDLE. Otherwise, you’ll get a NameError:
name 're' is not defined error message.
"""
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # Now the phoneNumRegex variable contains a Regex object
""""
To create a Regex object that matches the phone number pattern, enter the
following into the interactive shell. (Remember that \d means “a digit character”
and \d\d\d-\d\d\d-\d\d\d\d is the regular expression for the correct phone
number pattern.)

PASSING RAW STRINGS TO RE.COMPILE( )

Remember that escape characters in Python use the backslash (\). The string value '\n' represents a
single newline character, not a backslash followed by a lowercase n. You need to enter the escape
character \\ to print a single backslash. So '\\n' is the string that represents a backslash followed by a
lowercase n. However, by putting an r before the first quote of the string value, you can mark the string
as a raw string, which does not escape characters.
Since regular expressions frequently use backslashes in them, it is convenient to pass raw strings to the
re.compile() function instead of typing extra backslashes. Typing r'\d\d\d-\d\d\d-\d\d\d\d' is
much easier than typing '\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d'.
"""

mo = phoneNumRegex.search('My number is 415-555-4242.')
"""""
A Regex object’s search() method searches the string it is passed for any
matches to the regex. The search() method will return None if the regex pattern
is not found in the string. If the pattern is found, the search() method returns a
Match object. Match objects have a group() method that will return the actual
matched text from the searched string."""

print('Phone number found: ' + mo.group())

""""
The mo variable name is just a generic name to use for Match objects. This
example might seem complicated at first, but it is much shorter than the earlier
isPhoneNumber.py program and does the same thing.
Here, we pass our desired pattern to re.compile() and store the resulting Regex
object in phoneNumRegex. Then we call search() on phoneNumRegex and pass
search() the string we want to search for a match. The result of the search gets
stored in the variable mo. In this example, we know that our pattern will be found
in the string, so we know that a Match object will be returned. Knowing that mo
contains a Match object and not the null value None, we can call group() on mo
to return the match. Writing mo.group() inside our print statement displays the
whole match, 415-555-4242."""
