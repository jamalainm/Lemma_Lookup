import json

def ue_words(word):
    if len(word) > 1:
        if word[-2:] == "ue":
            if  len(word) > 2:
                if word[-3:] != "que":
                    return word
            else:
                return word

if __name__ == '__main__':
    with open('la_lemma_lookup.json','r') as f:
        vocab = json.load(f)

    ue_list = []

    for word in vocab:
        if ue_words(word):
            ue_list.append({"ORTH": word, "NORM": word, "LEMMA": vocab[word]})

    with open('ue_list.json','w') as f:
        json.dump(ue_list,f)
