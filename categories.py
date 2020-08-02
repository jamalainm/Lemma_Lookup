# coding: utf8

categories = {
        "inv" : "inv",
        "lupus": "noun",  # added stem
        "amo": "verb",
        "cometes": "noun", # added stem
        "doctus": "adj", # added stem
        "ciuis": "noun", # stems already there
        "lego": "verb",
        "manus": "noun", # added stem
        "roma": "noun", # added stem
        "templum": "noun", # added stem
        "corpus": "noun", # stems already there
        "dico": "verb",
        "eo": "verb", # changed to verb from "eo"
        "infans": "noun", # stems already there
        "moneo": "verb",
        "capio": "verb",
        "miles": "noun", # stems already there
        "liberi": "noun",  # added stem
        "adve": "adverb",
        "fortis": "adj", # most stems already there
        "uita": "noun", # added stem
        "imitor": "verb",
        "opes": "noun", # already added
        "potior": "verb",
        "sequor": "verb",
        "abraham": "indeclinable",
        "audio": "verb",
        "aureus": "adj", # stems added;  no comparative / superlative
        "advr": "adv",
        "absum": "verb",
        "delos": "noun", # added stem
        "castra": "noun", # added stem
        "diues": "adj", # stems already there; not an i-stem
        "mare": "noun",  # added stem
        "acer": "adj", # added stems; changed "celer"; r-stem
        "epulae": "noun", # added stem
        "filius": "noun", # added stem
        "manes": "noun", # stems already there
        "perseus": "noun", # added stem
        "aer": "noun", # stems already there
        "aeneas": "noun", # added stems
        "ilion": "noun", # added stem
        "dies": "noun", # added stem
        "artios": "adj", # added stems; additional greek forms
        "acriter": "adv",
        "cybele": "noun", #added stem
        "deus": "noun", # added stem
        "acus": "noun", # added stem
        "isaac": "noun", # added stem
        "fero": "verb",
        "patior": "verb",
        "clio": "noun", # added stem
        "ager": "noun", # added stem
        "sum": "verb",
        "puer": "noun", # added stem
        "miser": "adj", # added stem
        "pulcher": "adj", # added stem
        "thales": "noun", # added stem
        "moenia": "noun", # stems already there
        "aio": "verb",
        "turris": "noun", # stems already there
        "qui": "pronoun", # added forms
        "quis": "pronoun", # added forms
        "unus": "determiner", # added endings
        "animal": "noun", # stems already there
        "alter": "determiner", # added endings
        "uter": "determiner", # added endings
        "edo": "verb",
        "deni": "adj", # stems added; no singular, comparative, or superlative
        "dea": "noun", # added stem
        "poesis": "noun", # stems already there
        "apis": "noun", # stems already there
        "honor": "noun", # stems already there
        "facio": "verb",
        "arpinum": "noun", # changed -ium to "consilium"; added other stems
        "lacus": "noun", # added stem
        "leda": "noun", # added stem
        "misere": "adv",
        "tethys": "noun", # changed cat for Briseis; stem for Erinys
        "fio": "verb",
        "nonus": "adj", # added stem;  no comparative or superlative
        "deterior": "adj", # added stem (-3); no positive, but there is a superlative
        "dos": "noun", # stems already there
        "uereor": "verb",
        "scio": "verb",
        "samus": "noun",# added stems
        "cornu": "noun", # stems already there
        "licet": "verb",
        "res": "noun", # added stems
        "facile": "adv",
        "do": "verb",
        "domus": "noun", # added stems
        "duo": "adj", # stems already there; singlet
        "ego": "pronoun", # added forms
        "adv": "adv",
        "fortiter": "adv",
        "hic": "determiner", # added endings
        "humiliter": "adv",
        "idem": "composite", # added endings
        "ille": "determiner", # added endings
        "ipse": "determiner", # added endings
        "is": "determiner", # added endings
        "jesus": "noun", # added stems
        "malo": "verb",
        "meus": "adj", # split "suus" from "meus"; each is a singlet no comparative or superlative; other unique forms
        "suus": "adj", # probably like "aureus"
        "mille": "noun", # stem adjusted
        "morior": "verb",
        "multus": "adj", # added stem; no comparative or superlative
        "nauis": "noun", # stems already theyre
        "nemo": "pronoun", # added forms
        "nihil": "inv",
        "nolo": "verb",
        "nos": "pronoun", # added forms
        "virus": "noun", # added stems
        "plerique": "composite", # added endings
        "plus": "noun", # stems already there
        "possum": "verb",
        "prosum": "verb",
        "qualiscumque": "composite", # added endings
        "quantuscumque": "composite", # added endings
        "quicumque": "composite", # added endings
        "prcum": "inv",
        "quidam": "composite", # added endings
        "quilibet": "composite", # added endings
        "quinam": "composite", # added endings
        "quisnam": "composite", # added endings
        "quispiam": "composite", # added endings
        "quisquam": "composite", # added endings
        "quisque": "composite", # added endings
        "quisquis": "double", # added endings
        "quiuis": "composite", # added endings
        "se": "pronoun", # added forms
        "siquis": "double", # added endings
        "tu": "pronoun", # added forms
        "uetus": "adj", # stems already there; r-stem
        "unusquisque": "double", # added endings
        "uterque": "composite", # added endings
        "uis": "noun", # stem adjusted
        "uolo": "verb",
        "uos": "pronoun", # added forms
        "consilium" : "noun", # added stems
        "briseis" : "noun", # added stems
        "celer" : "adj", # added myself
        "noster" : "adj", # added myself - don't want comparatives
        "facilis": "adj", # added myself; want special superlative
        "tres" : "adj", # added myself; don't want comparatives
        "ADJ" : "ADJ",
        "ADP" : "ADP",
        "ADV" : "ADV",
        "AUX" : "AUX",
        "CONJ" : "CONJ",
        "CCONJ" : "CCONJ",
        "DET" : "DET",
        "INTJ" : "INTJ",
        "NOUN" : "NOUN",
        "NUM" : "NUM",
        "PART" : "PART",
        "PRON" : "PRON",
        "PROPN" : "PROPN",
        "PUNCT" : "PUNCT",
        "SCONJ" : "SCONJ",
        "SYM" : "SYM",
        "VERB" : "VERB",
        "X" : "X",
        "SPACE" : "SPACE",
        }
