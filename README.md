# Number-to-French-number
Using Finite State Automata to convert number to french number

### import the fst module | FST usage
<ol> 
<li> import fst</li>
<li># import the string module</li>
<li>import string</li>
<li># Define a list of all vowels for convenience</li>
<li>vowels = [’a’, ’e’, ’i’, ’o’, ’u’]</li>
<li># Instantiate an FST object with some name
<li>f = fst.FST(’devowelizer’)
<li> # All we need is a single state ...
<li>f.add_state(’1’)
<li> # and this same state is the initial and the final state
<li> f.initial_state = ’1’
<li> f.set_final(’1’)
<li> # Now, we need to add an arc for each letter; if the letter is a vowel
<li> # then the transition outputs nothing but otherwise it outputs the same
<li> # letter that it consumed.
<li> for letter in string.ascii_lowercase:
<li> if letter in vowels:
<li> _ = f.add_arc(’1’, ’1’, (letter), ())
<li>else:
<li> _ = f.add_arc(’1’, ’1’, (letter), (letter))
<li># Evaluate it on some example words
<li> print ’’.join(f.transduce([’v’, ’o’, ’w’, ’e’, ’l’]))
<li> print ’’.join(f.transduce(’e x c e p t i o n’.split()))
<li> print ’’.join(f.transduce(’c o n s o n a n t’.split()))

## Problem 1: Soundex 
The Soundex algorithm is a phonetic algorithm commonly used by libraries and the Census Bureau to represent people’s names as they are pronounced in English. It has the advantage that name variations with minor spelling differences will map to the same representation, as long as they have the same pronunciation in English. Here is how the algorithm works:
Step 1: Retain the first letter of the name. This may be uppercased or lowercased.

Step 2: Remove all non-initial occurrences of the following letters: a, e, h, i, o, u, w, y. (To clarify, this step removes all occurrences of the given characters except when they occur in the first position.)

Step 3: Replace the remaining letters (except the first) with numbers: 
  
<li> b, f, p, v → 1 </li>
<li> c, g, j, k, q, s, x, z → 2 • d, t → 3</li>
<li> l→4</li>
<li> m, n → 5</li>
<li> r→6</li>

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
