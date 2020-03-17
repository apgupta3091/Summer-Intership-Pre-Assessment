# Summer-Intership-Pre-Assessment
Kargo Summer Internship pre-assessment 
This script compares two strings and determines whether a one-to-one mapping exists between the strings (s1,s2).
It returns false in the case that one of the strings has more characters than the other
It also returns false when given "foo" as string 1, and "bar as string 2 because 'o' cannot map to more than one character.
It returns True if 'bar' is the first case, and 'foo' is the second string because 'a',and 'r' can both map to 'o'.
ie:
Enter a string: adcgr
Enter a second string: ast
False

Enter a string: abcde
Enter a second string: defgh
{'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
{'d': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1}
[1, 1, 1, 1, 1]
[1, 1, 1, 1, 1]
True

Enter a string: foo
Enter a second string: bar
{'f': 1, 'o': 2}
{'a': 1, 'b': 1, 'r': 1}
[1, 2]
[1, 1, 1]
False

Enter a string: foo
Enter a second string: bar
{'f': 1, 'o': 2}
{'a': 1, 'b': 1, 'r': 1}
[1, 2]
[1, 1, 1]
False
