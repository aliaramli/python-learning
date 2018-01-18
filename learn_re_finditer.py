# ran using python2.7
import re

# Example code for find keywords appearance using python re.finditer (regex)
search_keywords = ["smart", "high", "confident", "mature"]

# Now we join the keywords with OR operator | , it will looks something like this
# smart|high|confident|mature
search_patterns = "|".join(search_keywords)

text = "This is a story about a girl. Living in a secluded area in Wonderland.\n" \
       "She is small but very smart and smart, how ever she has verly low confident. Dont judge a book" \
       "by its cover.\n The way she thinks shown how mature she is."


# Now we update the pattern again with ( ) - > parenthesis
# The object is to capture the keyword as a group not individual character. it will looks like
# (smart|high|confident|mature)
search_patterns = "(%s)" % search_patterns
regex = re.compile(search_patterns)

# To find all pattern matches we need to use finditer function. because findall/search will
# only return the first match of the keyword in (smart|high|confident)
# If we use online regex parser,
# we can see that to achieve the same thing we need to apply "Global" flag. Unfortunately python
# doesnt support that.
it = regex.finditer(text, re.MULTILINE)

# To check individual match result, iterate and print m.group()
for match in it:
    print match.group()

# When you ran, you will get this result
# smart
# smart
# confident
# mature
