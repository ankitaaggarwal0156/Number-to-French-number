# Number-to-French-number
Using Finite State Automata to convert number to french number

### import the fst module | FST usage
2 import fst

4 # import the string module
5 import string
7 # Define a list of all vowels for convenience
8 vowels = [’a’, ’e’, ’i’, ’o’, ’u’]
10 # Instantiate an FST object with some name
11 f = fst.FST(’devowelizer’)
13 # All we need is a single state ...
14 f.add_state(’1’)
16 # and this same state is the initial and the final state
17 f.initial_state = ’1’
18 f.set_final(’1’)
20 # Now, we need to add an arc for each letter; if the letter is a vowel
21 # then the transition outputs nothing but otherwise it outputs the same
22 # letter that it consumed.
23 for letter in string.ascii_lowercase:
24 if letter in vowels:
25 _ = f.add_arc(’1’, ’1’, (letter), ())
26 else:
27 _ = f.add_arc(’1’, ’1’, (letter), (letter))
29 # Evaluate it on some example words
30 print ’’.join(f.transduce([’v’, ’o’, ’w’, ’e’, ’l’]))
31 print ’’.join(f.transduce(’e x c e p t i o n’.split()))
32 print ’’.join(f.transduce(’c o n s o n a n t’.split()))

## Problem 1: Soundex 
The Soundex algorithm is a phonetic algorithm commonly used by libraries and the Census Bureau to represent people’s names as they are pronounced in English. It has the advantage that name variations with minor spelling differences will map to the same representation, as long as they have the same pronunciation in English. Here is how the algorithm works:
Step 1: Retain the first letter of the name. This may be uppercased or lowercased.

Step 2: Remove all non-initial occurrences of the following letters: a, e, h, i, o, u, w, y. (To clarify, this step removes all occurrences of the given characters except when they occur in the first position.)

Step 3: Replace the remaining letters (except the first) with numbers: 
  
• b, f, p, v → 1

• c, g, j, k, q, s, x, z → 2 • d, t → 3

•l→4

• m, n → 5

•r→6


If two or more letters from the same number group were adjacent in the original name (i.e. before any letter removal is done), then only replace the first of those letters with the corresponding number and ignore the others.

Step 4: If there are more than 3 digits in the resulting output, then drop the extra ones.

Step 5: If there are less than 3 digits, then pad at the end with the required number of trailing zeros.
The final output of applying Soundex algorithm to any input string should be of the form Letter Digit Digit Digit. Table 1 shows the out- put of the Soundex algorithm for some example names.
Input        Output
Jurafsky     J612
Jarovski     J612

Table 1: Example outputs for the Soundex algorithm.

## Problem 2: French Numbers 
In the French language, Arabic numerals that we use in everyday can be spelled out just like they can in English. For example, the numeral 175 is written as one hundred seventy five in English and <strong>cent soixante quinze </strong> in French.
French is interesting becuase they have a mixture of a decimal (base 10) and vegesimal (base 20) system, created by committee to placate two different regions of French that used different systems.
