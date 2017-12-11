from fst import FST
import string, sys
from fsmutils import composechars, trace

def letters_to_numbers():
    """
    Returns an FST that converts letters to numbers as specified by
    the soundex algorithm
    """
    # Let's define our first FST
    f1 = FST('soundex-generate')
    # Indicate that '1' is the initial state
    f1.add_state('start')
    f1.add_state('1')
    f1.add_state('2')
    f1.add_state('3')
    f1.add_state('4')
    f1.add_state('5')
    f1.add_state('6')
    f1.add_state('7')
    f1.add_state('next')
    f1.initial_state = 'start'
    # Set all the final states
    f1.set_final('7')
    #setting the rules
    non_in = ['a', 'e', 'i', 'o', 'u','h','w','y','A','E','I','O','U','H','W','Y']
    rep1 =['b','f','p','v','B','F','P','V']
    rep2 =['c','g','j','k','q','s','x','z','C','G','J','K','Q','S','X','Z']
    rep3 =['d','t','D','T']
    rep4 =['l','L']
    rep5 =['m','n','M','N']
    rep6 =['r','R']
    
    # Add the rest of the arcs
    for letter in string.ascii_letters:
        if letter in non_in:
            f1.add_arc('start','next',(letter),(letter))
        if letter in rep1:
            f1.add_arc('start','1',(letter),(letter))
        if letter in rep2 :
            f1.add_arc('start','2',(letter),(letter))
        if letter in rep3:
            f1.add_arc('start','3',(letter),(letter))
        if letter in rep4:
            f1.add_arc('start','4',(letter),(letter))
        if letter in rep5:
            f1.add_arc('start','5',(letter),(letter))
        if letter in rep6:
            f1.add_arc('start','6',(letter),(letter))
    
        
    for letter in string.ascii_letters:
        if letter in non_in:
            f1.add_arc('next','next',(letter),())
        if letter in rep1:
            f1.add_arc('next','1',(letter),('1'))
        if letter in rep2 :
            f1.add_arc('next','2',(letter),('2'))
        if letter in rep3:
            f1.add_arc('next','3',(letter),('3'))
        if letter in rep4:
            f1.add_arc('next','4',(letter),('4'))
        if letter in rep5:
            f1.add_arc('next','5',(letter),('5'))
        if letter in rep6:
            f1.add_arc('next','6',(letter),('6'))

    f1.add_arc('next','7',(),())
    
    for letter in string.ascii_letters:
        if letter in non_in:
            f1.add_arc('1','next',(letter),())
        if letter in rep1:
            f1.add_arc('1','1',(letter),())
        if letter in rep2 :
            f1.add_arc('1','2',(letter),('2'))
        if letter in rep3:
            f1.add_arc('1','3',(letter),('3'))
        if letter in rep4:
            f1.add_arc('1','4',(letter),('4'))
        if letter in rep5:
            f1.add_arc('1','5',(letter),('5'))
        if letter in rep6:
            f1.add_arc('1','6',(letter),('6'))
    f1.add_arc('1','7',(),())
            
    for letter in string.ascii_letters:
        if letter in non_in:
            f1.add_arc('2','next',(letter),())
        if letter in rep1:
            f1.add_arc('2','1',(letter),('1'))
        if letter in rep2 :
            f1.add_arc('2','2',(letter),())
        if letter in rep3:
            f1.add_arc('2','3',(letter),('3'))
        if letter in rep4:
            f1.add_arc('2','4',(letter),('4'))
        if letter in rep5:
            f1.add_arc('2','5',(letter),('5'))
        if letter in rep6:
            f1.add_arc('2','6',(letter),('6'))

    f1.add_arc('2','7',(),())
            
    for letter in string.ascii_letters:
        if letter in non_in:
            f1.add_arc('3','next',(letter),())
        if letter in rep1:
            f1.add_arc('3','1',(letter),('1'))
        if letter in rep2 :
            f1.add_arc('3','2',(letter),('2'))
        if letter in rep3:
            f1.add_arc('3','3',(letter),())
        if letter in rep4:
            f1.add_arc('3','4',(letter),('4'))
        if letter in rep5:
            f1.add_arc('3','5',(letter),('5'))
        if letter in rep6:
            f1.add_arc('3','6',(letter),('6')) 
    f1.add_arc('3','7',(),())
    
    for letter in string.ascii_letters:
        if letter in non_in:
            f1.add_arc('4','next',(letter),())
        if letter in rep1:
            f1.add_arc('4','1',(letter),('1'))
        if letter in rep2 :
            f1.add_arc('4','2',(letter),('2'))
        if letter in rep3:
            f1.add_arc('4','3',(letter),(''))
        if letter in rep4:
            f1.add_arc('4','4',(letter),())
        if letter in rep5:
            f1.add_arc('4','5',(letter),('5'))
        if letter in rep6:
            f1.add_arc('4','6',(letter),('6')) 
    f1.add_arc('4','7',(),())
    
    for letter in string.ascii_letters:
        if letter in non_in:
            f1.add_arc('5','next',(letter),())
        if letter in rep1:
            f1.add_arc('5','1',(letter),('1'))
        if letter in rep2 :
            f1.add_arc('5','2',(letter),('2'))
        if letter in rep3:
            f1.add_arc('5','3',(letter),(''))
        if letter in rep4:
            f1.add_arc('5','4',(letter),('4'))
        if letter in rep5:
            f1.add_arc('5','5',(letter),())
        if letter in rep6:
            f1.add_arc('5','6',(letter),('6')) 
    f1.add_arc('5','7',(),())
            
    for letter in string.ascii_letters:
        if letter in non_in:
            f1.add_arc('6','next',(letter),())
        if letter in rep1:
            f1.add_arc('6','1',(letter),('1'))
        if letter in rep2 :
            f1.add_arc('6','2',(letter),('2'))
        if letter in rep3:
            f1.add_arc('6','3',(letter),(''))
        if letter in rep4:
            f1.add_arc('6','4',(letter),('4'))
        if letter in rep5:
            f1.add_arc('6','5',(letter),('5'))
        if letter in rep6:
            f1.add_arc('6','6',(letter),()) 
    f1.add_arc('6','7',(),())
    
    return f1


def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final states
    f2.add_state('1')
    f2.add_state('2')
    f2.add_state('3')
    f2.add_state('4')
    f2.initial_state = '1'
    f2.set_final('4')

    # Add the arcs
    for letter in string.letters:
        f2.add_arc('1', '1', (letter), (letter))
    f2.add_arc('1', '4', (), ())
    for n in range(10):
        f2.add_arc('1', '2', (str(n)), (str(n)))
    f2.add_arc('2', '4', (), ())
    for n in range(10):
        f2.add_arc('2', '3', (str(n)), (str(n)))
    f2.add_arc('3', '4', (), ())
    for n in range(10):
        f2.add_arc('3', '4', (str(n)), (str(n)))
    for n in range(10):
        f2.add_arc('4', '4', (str(n)), ())
    return f2



def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    f3.add_state('1')
    f3.add_state('1a')
    f3.add_state('1b')
    f3.add_state('2')
    
    f3.initial_state = '1'
    f3.set_final('2')

    for letter in string.letters:
        f3.add_arc('1', '1', (letter), (letter))
    f3.add_arc('1', '1a', (), ('0'))
    for number in xrange(10):
        f3.add_arc('1', '1a', (str(number)), (str(number)))
    f3.add_arc('1a', '1b', (), ('0'))
    for number in xrange(10):
        f3.add_arc('1a', '1b', (str(number)), (str(number)))
    f3.add_arc('1b', '2', (), ('0'))
    for number in xrange(10):
        f3.add_arc('1b', '2', (str(number)), (str(number)))
    return f3

    # The above code adds zeroes but doesn't have any padding logic. Add some!

if __name__ == '__main__':
    user_input = raw_input().strip()
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()

    if user_input:
        #print trace(f1, user_input)
        print("%s -> %s" % (user_input, composechars(tuple(user_input), f1,f2,f3)))
