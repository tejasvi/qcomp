import os
import string
import math
#import nltk
lis = []
i = 0
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

def gind(gram, ind, n):
    gram['.freq'] = 0
    for id in ind.keys():
        for ngram in ngfy(ind[id], n):

           # print(ngram, type(ngram))
            if ngram in gram:
                print(bool(gram[ngram][id]))
                gram[ngram][id]['freq'] += 1
            else:
                gram[ngram] = {}
                gram[ngram][id] = {}
                gram[ngram][id]['freq'] = 1
                gram[ngram][".freq"] = 0
            gram[ngram]['.freq'] += 1
            gram['.freq'] += 1
    afreq = math.log10(gram['freq']/len(gram))
    for dat in gram.values():
        for freq in dat.values() :
            freq /= afreq
    if (n==1):
        for ngrams in gram.items():
            ndoc = len(gram[ngrams])
            for ids in gram[ngrams]:
                tfidf = gram[ngram][ids] * log10(len(ind)/len(gram[ngrams]))
                gram[ngrams][ids]['tfidf'] = tfidf

for filename in os.listdir('nltk_data/corpora/webtext'):
    doc = open('nltk_data/corpora/webtext/'+filename, encoding="ISO-8859-1")
    s = ""
    for t in list(doc):
        s = s + str(t).translate(string.punctuation)
    lis = s.lower().split()
    lis = sorted(lis)
    lis = *lis,
    ind[i] = lis
    i += 1

ugram = {}
bgram = {}
tgram = {}
gind(ugram, ind, 1)
#ngfy(bgram, ind, 2)
#ngfy(tgram, ind, 3)
