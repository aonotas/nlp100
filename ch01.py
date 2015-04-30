#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

def q_00():
    seed = "stressed"
    print seed[::-1]

def q_01():
    s = u"パタトクカシーー"
    print s[1::2]

def q_02():
    s = u"パトカー"
    s2 = u"タクシー"
    print "".join(reduce(lambda x,y:x+y , zip(s,s2)))

def q_03():
    s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    print [len(i) for i in s[:-1].split(" ")]

def q_04():
    s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    l = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    d = {}
    split_s = s[:-1].split(" ")
    for i,w in enumerate(split_s):
        if i+1 in l:
            key = split_s[i][0]
        else:
            key = split_s[i][:2]
        d[key] = i+1
    print d

def q_05(s="I am an NLPer"):
    result = [s[i:i+2] for i in range(len(s))]
    print result
    return result
         

def q_06():
    X = q_05("paraparaparadise")
    Y = q_05("paragraph")
    print set(X).union(set(Y))
    print set(X).intersection(set(Y))
    print set(X).difference(set(Y))


    # print set(X) & set(Y)
    # print (set(X) | set(Y)) - (set(X) & set(Y))
    # print set(X) | set(Y)


    

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=str, dest='n', required=True, default=0, help='question number (default: 00)')    

    args = parser.parse_args()
    args_dict =  vars(args)
    number = args_dict["n"]
    func_name = lambda x: x if "q_" in x else "q_"+x
    name = func_name(number.zfill(2))
    
    import __main__
    f = getattr(__main__, name)
    f()