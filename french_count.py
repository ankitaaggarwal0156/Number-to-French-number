import sys
from fst import FST
from fsmutils import composewords,trace

kFRENCH_TRANS = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4:
                 "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13:
                 "treize", 14: "quatorze", 15: "quinze", 16: "seize",
                 20: "vingt", 30: "trente", 40: "quarante", 50:
                 "cinquante", 60: "soixante", 100: "cent"}

kFRENCH_AND = 'et'

def prepare_input(integer):
    assert isinstance(integer, int) and integer < 1000 and integer >= 0, \
      "Integer out of bounds"
    return list("%03i" % integer)

def french_count():
    f = FST('french')

    f.add_state('1')
    f.add_state('2')
    f.add_state('3')
    f.add_state('4')
    f.add_state('5')
    f.add_state('6')
    f.add_state('7')
    f.add_state('8')
    f.add_state('9')
    f.add_state('10')
    f.initial_state = '1'
    f.set_final('4')

    #hundred's place
    for i in range(1):
        f.add_arc('1','2',[str(i)],())
    for i in range(1,2):
        f.add_arc('1','9',[str(i)],[kFRENCH_TRANS[100]])
    for i in range(2,10):
        f.add_arc('1','9',[str(i)],[kFRENCH_TRANS[i]]+[kFRENCH_TRANS[100]])
    
    #ten's place when hundred's place was 0   
    for i in range (0,10):
        if i==0:
            f.add_arc('2','3',[str(i)],())
        if i==1:
            f.add_arc('2','5',[str(i)],())
        if i>1 and i<7:
            f.add_arc('2','6',[str(i)],[kFRENCH_TRANS[i*10]])
        if i==7:
            f.add_arc('2','7',[str(i)],[kFRENCH_TRANS[60]])
        if i==8:
            f.add_arc('2','8',[str(i)],[kFRENCH_TRANS[4]]+ [kFRENCH_TRANS[20]])
        if i==9:
            f.add_arc('2','5',[str(i)],[kFRENCH_TRANS[4]]+ [kFRENCH_TRANS[20]])
    
    #ten's place when hundred's place was 1-9
    for i in range (0,10):
        if i==0:
            f.add_arc('9','10',[str(i)],())
        if i==1:
            f.add_arc('9','5',[str(i)],())
        if i>1 and i<7:
            f.add_arc('9','6',[str(i)],[kFRENCH_TRANS[i*10]])
        if i==7:
            f.add_arc('9','7',[str(i)],[kFRENCH_TRANS[60]])
        if i==8:
            f.add_arc('9','8',[str(i)],[kFRENCH_TRANS[4]]+ [kFRENCH_TRANS[20]])
        if i==9:
            f.add_arc('9','5',[str(i)],[kFRENCH_TRANS[4]]+ [kFRENCH_TRANS[20]])

    #one's place
    #state 10-->4
    for ii in xrange(0,10):
        if ii==0:
            f.add_arc('10', '4', [str(ii)], ())
        else:
            f.add_arc('10', '4', [str(ii)], [kFRENCH_TRANS[ii]])
    
    #state 3-->4
    for ii in xrange(0,10):
        f.add_arc('3', '4', [str(ii)], [kFRENCH_TRANS[ii]])
        
    #state 5-->4 
    for i in range(0,10):
        if i<7:
            f.add_arc('5','4',[str(i)],[kFRENCH_TRANS[10+i]])
        else:
            f.add_arc('5','4',[str(i)],[kFRENCH_TRANS[10]]+[kFRENCH_TRANS[i]])
    
    #state 6-->4
    for i in range(0,10):
        if i==0:
            f.add_arc('6','4',[str(i)],())
        if i==1:
            f.add_arc('6','4',[str(i)],[kFRENCH_AND]+[kFRENCH_TRANS[i]])
        if i>1:
            f.add_arc('6','4',[str(i)],[kFRENCH_TRANS[i]])
    #state 7-->4
    for i in range(0,10):
        if i==1:
            f.add_arc('7','4',[str(i)],[kFRENCH_AND]+[kFRENCH_TRANS[10+i]])
        elif i>1 and i<7:
            f.add_arc('7','4',[str(i)],[kFRENCH_TRANS[10+i]])
        elif i==0:
            f.add_arc('7','4',[str(i)],[kFRENCH_TRANS[10+i]])
        else:
            f.add_arc('7','4',[str(i)],[kFRENCH_TRANS[10]]+[kFRENCH_TRANS[i]])
    
    #state 8-->4
    for ii in xrange(0,10):
        if ii==0:
            f.add_arc('8', '4', [str(ii)], ())
        else:
            f.add_arc('8', '4', [str(ii)], [kFRENCH_TRANS[ii]])
    
    
    

    return f

if __name__ == '__main__':
    string_input = raw_input()
    user_input = int(string_input)
    f = french_count()
    if string_input:
        print user_input, '-->',
        #print trace(f,prepare_input(user_input))
        print " ".join(f.transduce(prepare_input(user_input)))
