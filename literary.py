# Juliane x Sarah Abowitz x Minyue Dai | HH16
# teaching computers lit for science

# memespeak?? meme recognition?? 
# ~S

# anyone is invited to help with lists/finding text samples!


'''
IDEAS

also a word radius thing that determines like what gets the best spin or
something idk

could we make a tonal identifier? like a ver of spin that can id serious v silly
or something like that idk
'''

import re
from graphics import *

def main():
    win = GraphWin("title",400,400)
    win.setCoords(-100,-100,100,100)
    words=open('veldt.txt',encoding='utf-8').read().split()
    #CatcherInTheRye.txt and AdventuresSherlockHolmes.txt are interesting ones
    #to look at!

    #choose aliceOne.txt, Sherlock, veldt.txt, or Catcher
    #or implement a howto get files to put through
    
    p1 = Point(-100,0)
    
    wordsDivided = divvy(words)
    sector = 1
    spinsum = 0
    for i in wordsDivided:
        print("sector",sector)
        
        print("spin",spin(i))
        spinsum += spin(i) 
        p2 = Point(-100+(sector*20),(spinsum*10))
        wordline = Line(p1,p2)
        wordline.draw(win)
        p1 = p2.clone()        

        
        print("onomatopoeia",onomatopoeia(i))
        print("assonance",assonance(i))
        print("alliteration", alliteration(i))
        print("----")
        sector +=1

    wordfreq = words
 
    insignificant = [".",",","!","?",";",":","-","(",")","*",'a','an','the',
    'of', 'off', 'over', 'under', 'for', 'to', 'from', 'by','{',"}","[","]"]

    for line in wordfreq:
        for i in insignificant:
            line = line.replace(i,"")
            
    #print(word_frequency(wordfreq))
    '''
    print(spin(words))
    print("onomatopoeia",onomatopoeia(words)) #naknak.txt has ~10 naks
    print("assonance",assonance(words)) #naknak.txt has ~14 assonance
    '''
    
def spin(txt):
    neglist = ['bad','fear','rage','fury','terror','death','worse','worst',
    'horrible','terrible','horrendous','severely','badly','sick','cruel']
    poslist = ['admire','pretty','beautiful','amazing', 'great', 'brilliant',
    'positive','smart', 'good', 'better','best', 'happy']
    
    neg = 0
    pos = 0
    for i in neglist:
        neg += wordSearch(i,txt)

    for i in poslist:
        pos += wordSearch(i,txt)

    factor = pos - neg

    return factor

def wordSearch(keyword,txt):
    result = 0
    for i in txt:
        Lwords = i.split()
        for n in Lwords:
            if keyword in n:
                result += 1
                #print(n)
    return result

def word_frequency(wordfreq):
    frequency = {}
    for w in wordfreq:
        w=w.lower()
        w = re.findall('[a-zA-Z0-9]+',w)
        w = ''.join(w)
        frequency[w] = frequency.get(w, 0) + 1
        
    frequency=list(frequency.items())
    frequency.sort(key=lambda x:x[1])
    frequency=frequency[::-1]
    return frequency

'''
    for word, count in frequency:
        if (count > 9):
            #print(word,count,sep='\t')
'''

def onomatopoeia(txt):
    '''
    made by Lepidopterane 
    '''
    
    noise = ['pop','buzz','meow','neigh','baa','bark','bang','squeak','slam',
             'thud','glub','moo','nak','roar','moan','groan','ding']
    result = 0
    debug = False
    if debug:
        foundsound = []
    for i in noise:
        n = wordSearch(i,txt)
        result += n 
        if debug:
            foundsound.append(n*i)
    if debug:
        print(foundsound)
    return result
'''
~Don't delete~
This function is dedicated to my sister Jess, who is the most talented
noisemaker I know. I'm sorry I can't see the play bc I'm Hacking Holyoke.
Love you, make them clap and squeak and shriek and shout with praise! ~S
'''

def assonance(txt):
    counter = 0
    total = 0
    lim = len(txt)

    for j in range(1,lim):
        prevVowel = firstVowel(txt[j-1])
        #print("prev",prevVowel,end=' ')
        nowVowel = firstVowel(txt[j])
        #print("now",nowVowel)
        if (prevVowel == nowVowel):
            counter += 1
        elif ((prevVowel != nowVowel) and counter>0):
            counter = 0
            total += 1
                
    
    return total

def alliteration(txt):
    counter = 0
    total = 0
    lim = len(txt)

    for j in range(1,lim):
        prevFirst = txt[j-1]
        prevFirst = prevFirst[0]
        #print("prev",prevVowel,end=' ')
        nowFirst = txt[j]
        nowFirst = nowFirst[0]
        #print("now",nowVowel)
        if (prevFirst == nowFirst):
            counter += 1
        elif ((prevFirst != nowFirst) and counter>1):
            counter = 0
            total += 1
                
    
    return total

def firstVowel(word):
    vowels = 'aeiou'
    lowest = len(word)
    no = 0
    for i in vowels:
        x = word.find(i)
        if (-1<x<lowest):
            lowest = x
        elif(x<0):
            no += 1
    if (no == len(vowels)):
        return 0
    #print(lowest)
    return word[lowest]

'''
The following  is a WIP

def cliche(txt):
    cliches = ['in the nick of time','only time will tell','a matter of time',
'at the speed of light','lasted an eternity','lost track of time',
'a diamond in the rough','frightened to death','all is fair in love and war',
'all is well that ends well','the writing on the wall','time heals all wounds',
'haste makes waste','they all lived happily ever after','read between the lines',
'the quiet before the storm']
    
    total = 0
    for i in txt:
       txt = txt.join()
       for j in cliches:
           if j in txt:
               total += 1
               
    return total
'''

#def anaphora(words):
    #    

def divvy(words):
    '''
    Divides the word list into a list of lists of a certain length. returns
    all lists. Good if you want to see trends over the course of a text.
    '''
    metaList = []
    count = 0
    listicle = []

    lim = len(words)
    div = lim//100

    for i in range(0,lim,div):
        if (i+div > lim):
            listicle =words[i:]
        else:
            listicle = words[i:i+div]
        metaList.append(listicle)
    
    return metaList

main()
