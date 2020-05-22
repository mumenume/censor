import re
# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()

#Censore phrase from text
def censor (phrase, text):
    #making Xs to replace phrase
    phrase_list = phrase.split()
    Xs_list = ['X'*len(x) for x in phrase_list]
    Xs = ' '.join(Xs_list)
    Xs = ' ' + Xs + ' '

    #make regex for perfect match
    phrase_reg = re.compile('\W*{}\W*?'.format(phrase))

    if phrase_reg.search(text):
        text_list = text.split(phrase)
        censored = Xs.join(text_list)
    return censored

#print(censor('learning algorithms', email_one))

#Censore several phrases from text
def censor_list (phrase_list, text):
    #loop through list of phrases and censor each
    for phrase in phrase_list:
        # making Xs to replace phrase
        phrase_list = phrase.split()
        Xs_list = ['X'*len(x) for x in phrase_list]
        Xs = ' '.join(Xs_list)

        # make regex for perfect match
        phrase_reg = re.compile('\W*{}\W*?'.format(phrase))
        if phrase_reg.search(text):
            text_list = text.split(phrase)
            text = Xs.join(text_list)
    censored = text
    return censored

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation",\
                     "learning algorithm", "her", "herself"]
#print(censor_list(proprietary_terms, email_two))


#Censore several phrases and negative words from text
def censor_list_negative (negative_words, phrase_list, text):

    for phrase in phrase_list:
        phrase_list = phrase.split()
        Xs_list = ['X'*len(x) for x in phrase_list]
        Xs = ' '.join(Xs_list)

        phrase_reg = re.compile('\W*{}\W*?'.format(phrase))
        if phrase_reg.search(text):
            text_list = text.split(phrase)
            text = Xs.join(text_list)

    for negative in negative_words:
        negative_list = negative.split()
        Xs_list = ['X'*len(x) for x in negative_list]
        Xs = ' '.join(Xs_list)

        negative_reg = re.compile('\W*{}\W*?'.format(negative))
        x = list(negative_reg.finditer(text))
        if len(x) > 2:
            text_list = text.split(negative)
            text = Xs.join(text_list)

    censored = text
    return censored

negatives = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control",\
                  "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal",\
                  "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
print(censor_list_negative(negatives, proprietary_terms, email_three))
