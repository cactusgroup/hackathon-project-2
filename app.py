from alchemyapi import AlchemyAPI
import difflib as dl
import sys
import json
import re

API_KEY = '18e02f747ea9c20133e9daf16409bbb8990c6355'

alchemyapi = AlchemyAPI()

def init():
    raw = str(sys.argv[1])
    data = json.loads(raw)

    text1 = data["text1"]
    text2 = data["text2"]

    result_text = []
    result_string = ""

    sentence1 = re.sub(r'', '', text1).split('. ')
    sentence2 = re.sub(r'', '', text2).split('. ')

    print run(sentence2, sentence1)

    # if len(sentence1) >= len(sentence2):
    #     result_text.append(run(sentence1, sentence2))
    # else:
    #     result_text.append(run(sentence2, sentence1))

    # for text in result_text:
    #     result_string += str(text.encode('utf8'))+". "

    # print result_string



def run(s1, s2):

    sentences = ""

    for sentence1 in s1:
        sentence_num = 0
        for sentence2 in s2:
            if similarity(sentence1, sentence2):
                if len(sentence1.split()) > len(sentence2.split()):
                    sentences += "<span style='color:red'>"+sentence1+"</span>"
                else:
                    sentences += "<span style='color:blue'>"+sentence2+"</span>"
                break
            else:
                if context(sentence1, sentence2):
                    sentences += "<span style='color:red'>"+sentence1+"</span>"
                    break
                else:
                    print "Not the same"
                    # result_text.append(sentence1)
                    # result_text.append(sentence2)
            if sentence_num == 5:
                break
            else:
                sentence_num += 1

    return sentences



def similarity(sentence1, sentence2):
    sim = dl.get_close_matches

    s = 0
    wa = sentence1.split()
    wb = sentence2.split()

    for i in wa:
        if sim(i, wb):
            s += 1

    n = float(s) / float(len(wa))

    return n > 0.6

def context(sentence1, sentence2):
    response1 = alchemyapi.keywords("text", sentence1)
    response2 = alchemyapi.keywords("text", sentence2)

    keywords1 = response1['keywords']
    keywords2 = response2['keywords']

    word_bank = []

    n = 0

    if len(keywords1) > len(keywords2):
        for k1 in keywords1:
            for k2 in keywords2:
                if k1['text'] == k2['text']:
                    word_bank.append(k1['text'])
        n = float(len(word_bank)) / float(len(keywords1))
    else:
        for k2 in keywords2:
            for k1 in keywords1:
                if k2['text'] == k1['text']:
                    word_bank.append(k2['text'])
        n = float(len(word_bank)) / float(len(keywords2))

    return n > 0.4

init()

