import os
import string
import math
from stop_words import get_stop_words

stop = get_stop_words('en')

#import nltk
lis = []
i = 1
ind = {}


def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:
                break
            lower = x
        elif target < val:
            upper = x

def ngfy(lis, n):
    return zip(*[lis[n:] for n in range(n)])

def setify(phrase):
    sets = set()
    if phrase in ugram:
        sets = set(ugram[phrase].keys())
        sets.discard(0)
        sets.discard(t)
    return sets
    
def eng(query):
    probt = 1.0
    qterm = ''
    term = query.lower().split()
    if terms[-1] not in ugram.keys():
        p = 0.0
        psum = 0.0
        for word in ugram:
            if word.startswith(term[-1]):
                psum += ugram[word]['t']
        for word in ugram:
            if word.startswith(term[-1]):
                ptemp = ugram[word]['t']/psum
                if ptemp > psum:
                    qterm = word
        del term[-1]
    for ngram in bgram:
        if term:
            if term in ngram:
                pdocs = len(bgram[ngram]) - 2



    )

def gind(gram, ind, n):
    gram['.freq'] = {}
    gram['.freq'][0] = 0
    for id in ind.keys():
        for ngram in ngfy(ind[id], n):

           # print(ngram, type(ngram))
            if ngram in gram:
                if id not in gram[ngram]:
                    gram[ngram][id] = {}
                    gram[ngram][id] = 1
                else:
                    gram[ngram][id] += 1
            else:
                gram[ngram] = {}
                gram[ngram][id] = {}
                gram[ngram][id] = 1
                gram[ngram][0] = 0
            gram[ngram][0] += 1
            gram['.freq'][0] += 1
    afreq = math.log10(gram['.freq'][0]/len(gram))
    for dat in gram.values():
        for freq in dat.values() :
            freq /= afreq
        #print(dat) #freq /= afreq
    if (n==1):
        for ngrams in gram.keys():
            ndoc = list(gram[ngrams].keys())
            num = max(ndoc, key=int)
            if(num):
                tfidf = gram[ngrams][0] * math.log10(len(ind)/num)
                gram[ngrams]['t'] = tfidf

for filename in os.listdir('nltk_data/corpora/webtext'):
    doc = open('nltk_data/corpora/webtext/'+filename, encoding="ISO-8859-1")
    s = ""
    for t in list(doc):
        s = s + str(t).translate(string.punctuation)
    lis = s.lower().split()
    lis = [word for word in lis if word not in stop]
    lis = sorted(lis)
    lis = *lis,
    ind[i] = lis
    i += 1

ugram = {}
bgram = {}
tgram = {}
gind(ugram, ind, 1)
gind(bgram, ind, 2)
gind(tgram, ind, 3)
print(bgram)
