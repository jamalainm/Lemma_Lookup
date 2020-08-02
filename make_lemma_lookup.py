# coding: utf8

import json
import phonology
from categories import categories
from endings import declensions,adjectives,comparatives,pronouns,determiners
from endings import composites, doubles,conjugations,present_system,perfect_system
from endings import perfect_syncopated
from endings import adverbs_in_e, adverbs_in_iter
from unidecode import unidecode

class Word:
    """

    Takes an entry from a cleaned-up version of Collatinus' data and splits it off
    into the relevant part of speech classes

    ...

    Attributes
    ----------
    entry : list
        This will be used to pass on useful principal part info

    category : string
        This is the name of the subclass that the word will be
        reassigned to in order to create all of its forms

    lemma : string
        This is the accented lemma

    headword : string
        This is the unaccented lemma, minus any numbers

    stem1 : string
        If it exists, this is an unaccented string; for nouns and
        adjectives this is often the word minus the genitive ending;
        for verbs this is often the perfect active stem

    stem2: string
        If it exists, this is an unaccented string; common for supine
        stem of verbs

    all_forms : dict
        This will have the form on the left and the lemma on the right

    Methods
    -------
    classify()
        Returns the category the word belongs w

    remove_breve(form)
        Given a string, if any of the vowels are marked with
        a breve, the string will be returned with an unmarked
        vowel instead

    show_broken_entries()
        This is a diagnostic method that will change as different
        parts of speech are being evaluated

    group_into_pos()
        Reclassifies the categories into the pre-defined POSs in
        spacy

    add_lookup(lemma,stem,ending="")
        This adds an entry in the all_forms dict

    """
    
    def __init__(self,entry):
        self.entry = entry
        self.category = entry[2]
        self.lemma = entry[-1]
        self.headword = unidecode(entry[0]).replace('j','i')
        self.stem1 = ""
        if isinstance(entry[3],str):
            self.stem1 = unidecode(entry[3]).replace('j','i')
        self.stem2 = ""
        if isinstance(entry[4],str):
            self.stem2 = unidecode(entry[4]).replace('j','i')

        self.all_forms = {}

    def classify(self):
        """ Return the part of speech to which the word belongs """

        return categories[self.entry[2]]

    def remove_breve(self,form):
        """ Remove breve accents from form vowels """

        old_form = form

        new_form = ""

        for character in old_form:
            if character in phonology.explicitly_short_vowels:
                new_form += phonology.short_vowels[phonology.explicitly_short_vowels.index(character)]
            else:
                new_form += character

        return new_form

    def show_broken_entries(self):
        """ a changing function to evaluate lexicon data """
        if categories[self.category] == "adj":
            if isinstance(self.entry[3], str):
                print(self.entry)

    def group_into_pos(self):
        """ interprets results of classify method to return POS """

        category = self.classify()

        parts_of_speech = {
                "ADJ" : "adj",
                "adj" : "adj",
                "ADP" : "adp",
                "ADV" : "adv",
                "adv" : "adv",
                "adverb" : "adv",
                "AUX" : "aux",
                "CCONJ" : "cconj",
                "SCONJ" : "sconj",
                "CONJ" : "conj",
                "DET" : "det",
                "composite" : "det",
                "double" : "det",
                "determiner" : "det",
                "INTJ" : "intj",
                "NOUN" : "noun",
                "PROPN" : "propn",
                "noun" : "noun",
                "indeclinable" : "noun",
                "PART" : "part",
                "PRON" : "pron",
                "pronoun" : "pron",
                "NUM" : "num",
                "SYM" : "sym",
                "VERB" : "verb",
                "verb" : "verb",
                "inv" : "X",
                "PUNCT" : "sym",
        }

        return parts_of_speech[self.entry[1]]
#        return parts_of_speech[category]

    def add_lookup(self,lemma,stem,ending=""):
        word_form = stem + ending
        Word_Form = word_form.capitalize()
        self.all_forms[word_form] = unidecode(lemma)
        self.all_forms[Word_Form] = unidecode(lemma)

class Noun(Word):
    """

    sub-categorizes nouns into declensions and irregular behavior; 
    ultimately returns the different forms for a word

    ...

    Attributes
    ----------
    stem : string
        This is the form of the word to which endings for the oblique
        cases/numbers are added to

    Methods
    -------
    make_noun_forms()
        return a list of word forms

    """
    def __init__(self,entry):
        super().__init__(entry)
    
    def make_noun_forms(self):
        """ return noun forms """

        self.add_lookup(self.lemma,self.headword)

        for ending in declensions[self.category]:
            ending = unidecode(ending)
            self.add_lookup(self.lemma,self.stem1,ending)

class Adjective(Word):
    """

    sub-categorizes adjectives into declensions and irregular behavior; 
    ultimately returns the different forms for a word; eventually will
    create comparative and superlative forms for appropriate adjectives

    ...

    Attributes
    ----------
    stem : string
        This is the form of the word to which endings for the oblique
        cases/numbers are added to

    Methods
    -------
    make_positive_forms()
        return a list of word forms

    make_comparative_forms()
        return a list of comparative forms after performing a check
        as to whether the adjective belongs to a class that takes
        comparatives

    make_superlative_forms()
        return a list of superlative forms after confirming that
        they are the sorts of adjectives to have superlatives and
        distributing them between typical, -llimus, and -rrimus
        stems

    """
    def __init__(self,entry):
        super().__init__(entry)
    
    def make_positive_forms(self):
        """ return adjective forms """

        self.add_lookup(self.lemma,self.headword)

        for ending in adjectives[self.category]:
            ending = unidecode(ending)
            self.add_lookup(self.lemma,self.stem1,ending)

        if self.category in adverbs_in_e:
            self.add_lookup(self.lemma,self.stem1,'e')
        elif self.category in adverbs_in_iter:
            self.add_lookup(self.lemma,self.stem1,'iter')

    def make_comparative_forms(self):
        """ check if comparative forms available; if so return list """

        if self.category in comparatives:

            for ending in declensions['comparative']:
                ending = unidecode(ending)
                self.add_lookup(self.lemma,self.stem1,ending)

    def make_superlative_forms(self):
        """ check if superlative forms available; if so return list """

        if self.category in comparatives:

            if self.category == 'facilis':
                self.stem1 += "lim"
            elif self.headword[-1] == 'r':
                self.stem1 = self.headword + 'rim'
            elif self.category == 'uetus':
                self.stem1 += 'rim'
            else:
                self.stem1 += 'issim'

            for ending in adjectives['doctus']:
                ending = unidecode(ending)
                self.add_lookup(self.lemma,self.stem1,ending)

        self.add_lookup(self.lemma,self.stem1,'e')

    def make_all_forms(self):
        self.make_positive_forms()
        self.make_comparative_forms()
        self.make_superlative_forms()

class Pronoun(Word):
    """

    Returns a list of the forms for the various pronouns
    ...

    Attributes
    ----------
    stem : string
        This is the form of the word to which endings for the oblique
        cases/numbers are added to

    Methods
    -------
    make_pronoun_forms()
        return a list of word forms

    """
    def __init__(self,entry):
        super().__init__(entry)
    
    def make_pronoun_forms(self):
        """ return pronoun forms """

        for form in pronouns[self.category]:
            form = unidecode(form)
            self.add_lookup(self.lemma,form)

class Determiner(Word):
    """

    Returns a list of the forms for the various determiners, including
    demonstratives
    ...

    Attributes
    ----------
    stem : string
        This is the form of the word to which endings for the oblique
        cases/numbers are added to

    Methods
    -------
    make_determiner_forms()
        return a list of word forms

    """
    def __init__(self,entry):
        super().__init__(entry)
    
    def make_determiner_forms(self):
        """ return noun forms """

        self.add_lookup(self.lemma,self.headword)

        for ending in determiners[self.category]:
            ending = unidecode(ending)
            self.add_lookup(self.lemma,self.stem1,ending)

class Composite(Word):
    """

    Returns a list of the forms for the complex determiners, including
    those made up of a declinable word and an indeclinable suffix
    ...

    Attributes
    ----------
    stem : string
        This is the form of the word to which endings for the oblique
        cases/numbers are added to

    Methods
    -------
    make_composite_forms()
        return a list of word forms

    """
    def __init__(self,entry):
        super().__init__(entry)
    
    def make_composite_forms(self):
        """ return composite determiner forms """

        self.add_lookup(self.lemma,self.headword)

        for form in composites[self.category][0]:
            form = unidecode(form)
            word_form = self.stem1 + form + composites[self.category][1]
            word_form = unidecode(word_form)
            self.add_lookup(self.lemma,word_form)


class Double(Word):
    """

    Returns a list of the forms for complex determiners, including
    those made up of multiple declinable words mashed together
    ...

    Attributes
    ----------
    stem : string
        This is the form of the word to which endings for the oblique
        cases/numbers are added to

    Methods
    -------
    make_composite_forms()
        return a list of word forms

    """
    def __init__(self,entry):
        super().__init__(entry)
    
    def make_double_forms(self):
        """ return noun forms """

        self.add_lookup(self.lemma,self.headword)

        forms = doubles[self.category]
        
        for form in forms:
            form = unidecode(form)
            self.add_lookup(self.lemma,form)

class Verb(Word):
    """

    Returns a list of the forms for verbs, finite and non-finite
    ...

    Attributes
    ----------
    stem : string
        This is the form of the word to which endings for the oblique
        cases/numbers are added to

    Methods
    -------
    make_present_stem()
        return the present stem or the form that the stored endings
        will be added to

    id_conjugation()
        return the conjugation type

    make_pres_sys_active_forms()
        return a list of word forms

    make_pres_sys_passive_forms()
        return a list of word forms

    make_pf_active()
        return a list of word forms if there is a pf. active stem

    make_participles()
        return a list of present active, pf. passive, gerund,
        and future active participles, where the stem is available

    """
    def __init__(self,entry):
        super().__init__(entry)

    def id_conjugation(self):
        """ return the conjugation type """

        return conjugations[self.category]

    def make_present_stem(self):
        """ return the present stem """

        conjugation = self.id_conjugation()

        deponent = 0

        if self.headword[-1] == "r":
            deponent -= 1

        if conjugation in ["first","third","do","eo"]:
            return self.headword[:-1 + deponent]
        elif conjugation in ["second","third_io","fourth"]:
            return self.headword[:-2 + deponent]
        elif conjugation in ["sum","edo","fio"]:
            return self.headword[:-3 + deponent]
        elif conjugation in ["fero","uolo","malo","nolo"]:
            return self.headword[:-4 + deponent]
        elif conjugation == "possum":
            return self.headword[:-6 + deponent]
    
    def make_pres_sys_active_forms(self):
        """ return noun forms """

        conjugation = self.id_conjugation()

        present_stem = self.make_present_stem()

        if self.headword[-1] != "r":

            for paradigm in present_system[conjugation]["active"]:
                for ending in present_system[conjugation]["active"][paradigm]:
                    ending = unidecode(ending)
                    self.add_lookup(self.lemma,present_stem,ending)

    def make_pres_sys_passive_forms(self):
        """ return noun forms """

        conjugation = self.id_conjugation()

        present_stem = self.make_present_stem()

        if "passive" in present_system[conjugation].keys():

            for paradigm in present_system[conjugation]["passive"]:
                for ending in present_system[conjugation]["passive"][paradigm]:
                    ending = unidecode(ending)
                    self.add_lookup(self.lemma,present_stem,ending)

    def make_pf_active(self):
        """ return perfect active forms """

        if isinstance(self.entry[3], str):
            pf_stem = self.stem1
            for paradigm in perfect_system:
                for ending in perfect_system[paradigm]:
                    ending = unidecode(ending)
                    self.add_lookup(self.lemma,pf_stem,ending)

            if pf_stem[-1] == "v":
                if self.entry[3][-2] in ["ā","ē","ō"]:
                    new_pf = pf_stem[:-1]
                    for ending in perfect_syncopated['Vv']:
                        ending = unidecode(ending)
                        self.add_lookup(self.lemma,new_pf,ending)
                elif self.entry[3][-2] == "ī":
                    new_pf = pf_stem[:-1]
                    for ending in perfect_syncopated['iv']:
                        ending = unidecode(ending)
                        self.add_lookup(self.lemma,new_pf,ending)

    def make_participles(self):
        """ return supine, pf. pass, pres, act,, fut. act., gerundive """

        conjugation = self.id_conjugation()
        present_stem = self.make_present_stem()

        supine = None

        if isinstance(self.entry[4], str):
            supine = self.stem2

        if supine:
            self.add_lookup(self.lemma,supine,'u')
#            future = supine + "ūr"
            future = supine + "ur"
            for ending in adjectives["doctus"]:
                ending = unidecode(ending)
                self.add_lookup(self.lemma,supine,ending)
                self.add_lookup(self.lemma,future,ending)

        for ending in adjectives['doctus']:
            infix = present_system[conjugation]['participles']['gerundive'][0]
            gerundive = present_stem + unidecode(infix)
            ending = unidecode(ending)
            self.add_lookup(self.lemma,gerundive,ending)

        for ending in adjectives['fortis']:
            infix = present_system[conjugation]['participles']['pres_ptcpl'][1]
            pres_ptcpl = present_stem + unidecode(infix)
            ending = unidecode(ending)
            self.add_lookup(self.lemma,pres_ptcpl,ending)


        infix = present_system[conjugation]['participles']['pres_ptcpl'][0]
        word_form = present_stem + infix
        word_form = unidecode(word_form)
        self.add_lookup(self.lemma,word_form)

    def make_all_verb_forms(self):
        """ all finite and non finite verb forms """

        self.make_pres_sys_active_forms()
        self.make_pres_sys_passive_forms()
        self.make_pf_active()
        self.make_participles()

def make_lemmata():
    """ write a json file / dictionary of all the lemmata """

    all_lemmata = {}

    with open("lexicon.json","r") as f:
        lexicon = json.load(f)

    for entry in lexicon:
        verbum = Word(entry)
#        verbum.show_broken_entries()
#########
# VERBS #
#########
        if verbum.classify() == "verb":
            verbum = Verb(entry)
#            verbum.make_pres_sys_active_forms()
            verbum.make_all_verb_forms()
            all_lemmata.update(verbum.all_forms)
###########
# DOUBLES #
###########
        elif verbum.classify() == "double":
            verbum = Double(entry)
            verbum.make_double_forms()
            all_lemmata.update(verbum.all_forms)
##############
# COMPOSITES #
##############
        elif verbum.classify() == "composite":
            verbum = Composite(entry)
            verbum.make_composite_forms()
            all_lemmata.update(verbum.all_forms)
###############
# DETERMINERS #
###############
        elif verbum.classify() == "determiner":
            verbum = Determiner(entry)
            verbum.make_determiner_forms()
            all_lemmata.update(verbum.all_forms)
############
# PRONOUNS #
############
        elif verbum.classify() =="pronoun":
            verbum = Pronoun(entry)
            verbum.make_pronoun_forms()
            all_lemmata.update(verbum.all_forms)
##############
# ADJECTIVES #
##############
        elif verbum.classify() == "adj":
            verbum = Adjective(entry)
            verbum.make_all_forms()
            all_lemmata.update(verbum.all_forms)
#########
# NOUNS #
#########
        elif verbum.classify() == "noun":
            verbum = Noun(entry)
            verbum.make_noun_forms()
            all_lemmata.update(verbum.all_forms)

########
# MISC #
########
        else:
            form = unidecode(entry[0])
            lemma = unidecode(entry[-1])
            all_lemmata[form] = unidecode(lemma)
            all_lemmata[form.capitalize()] = unidecode(lemma)

    with open("la_lemma_lookup.json", 'w', encoding='utf-8') as f:
        json.dump(all_lemmata, f, ensure_ascii=False)

if __name__ == "__main__":
    make_lemmata()
