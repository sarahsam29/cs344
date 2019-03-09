'''
A Spam filter based on probability, heavily inspired by the article "A Plan for Spam" by Paul Graham

@author: ss63
@date: March 8, 2019
'''


spam_corpus = [["i", "am", "spam", "spam", "i", "am"], ["i", "do", "not", "like", "that", "spamiam"]]
notspam_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]

def SpamFilter(spam_corpus, notspam_corpus):

    good_words = {}     #1st dictonary to store the words that are not in spam
    num_good = 0        #will decide the length of goof_words dict.
    for i in notspam_corpus:
        num_good +=1
        for n in i:
            if n not in good_words:
                good_words[n] = 1
            else:
                good_words[n] += 1

    bad_words = {}       #2nd dictonary to store the words that are not in spam
    num_bad = 0          #will decide the length of goof_words dict.
    for i in spam_corpus:
        num_bad += 1
        for n in i:
            if n not in bad_words:
                bad_words[n] = 1
            else:
                bad_words[n] += 1

    all_words = []       #create a list that combines both corpuses together
    for token in good_words:
        if token not in all_words:
            all_words.append(token)
    for token in bad_words:
        if token not in all_words:
            all_words.append(token)

    corpus_prob = {}    #3rd dictionary to calculate the probability of each word, to eventually figure out if the word belongs to a spam email
    for token in all_words:
        g = 0;
        b= 0;
        if token in good_words:
            g = 2 * good_words[token]
        if token in bad_words:
            b = bad_words[token]
        probability = max(0.01, min(0.99, min(1.0, b /num_bad) / (min(1.0, g /num_good) + min(1.0, b /num_bad))))
        corpus_prob[token] = probability

    print("Combined corpus words and their probability:")
    return corpus_prob


#figure out the probability that email is spam by checking each word's probability of belonging to spam email
def checkForSpam(text):
    product = 1
    complement_product = 1

    for token in text:
        if token in sort:
            product *= sort[token]
            complement_product  *= 1 - sort[token]

        else:
            sort[token] = 0.4

        prob_of_spam = product / (product + complement_product )
    return prob_of_spam

sort = SpamFilter(spam_corpus, notspam_corpus)
print(sort)


# Test cases using words from both corpuses
spam1 = ["I", "do", "not", "like", "spam"]
spam2 =  ["I", "am", "spam", "that", "I", "am"]

notspam1 = ["I", "dont", "like", "green", "eggs", "and", "ham"]
notspam2 =  ["I", "love", "green", "eggs", "not", "spam"]

print("\nProbability that 'I do not like spam' is spam:", checkForSpam(spam1))
print("\nProbability that 'I am spam that I am' is spam:",checkForSpam(spam2))
print("\nProbability that 'I dont like green eggs' is spam:",checkForSpam(notspam1))
print("\nProbability that 'I do love green eggs not spam:",checkForSpam(notspam2))
