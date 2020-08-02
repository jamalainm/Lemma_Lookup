# coding: utf8

declensions = {
        "roma" : ["a","ae","am","ā","ārum","īs","ās","āī"],
        "uita" : ["a","ae","am","ā","ārum","īs","ās","āī"],
        "dea" : ["a","ae","am","ā","ārum","īs","ās","ābus","āī"],
        "aeneas" : ["ae","am","an","ā","a","āī"],
        "epulae" : ["ae","ārum","īs","ās"],
        "cybele" : ["ē","a","ēs","ae","ēn","ām","ā"],
        "cometes" : ["ēs","ae","ēn","ā","a","am","ē"],
        "lupus" : ["us","ī","ō","um","e","ōrum","īs","ōs","os","om"],
        "liberi" : ["ī","ōrum","īs","ōs"],
        "filius" : ["ius","iī","iō","ium","ī","iōrum","iīs","iōs"],
        "ager" : ["ī","ō","um","ī","ōrum","īs","ōs","om"],
        "puer" : ["ī","ō","um","ōrum","īs","ōs","om"],
        "samus" : ["us","os","ī","ō","um","e","om"],
        "deus" : ["eus","eī","eō","eum","iī","ī","eōrum","eīs","eōs","iīs","īs","ee","os","om"],
        "templum" : ["um","ī","ō","a","ōrum","īs","om"],
        "virus" : ["us","ī","ō","a","ōrum","īs","os"],
        "arpinum" : ["um","ī","ō","a","ōrum","īs","om"],
        "castra" : ["a","ōrum","īs"],
        "leda" : ["a","ae","am","ā","ārum","īs","ās","on","ī","ō","a","ōrum","īs","āī"],
        "delos" : ["os","ī","ō","um","e","on","us","om"],
        "ilion" : ["on","um","ī","ō"],
        "ciuis" : ["is","ī","em","e","ēs","ium","ibus","īs"],
        "apis" : ["is","ī","em","e","ēs","ium","ibus","īs","es","um"],
        "aer" : ["is","os","a","em","ēs","ium","ibus","īs"],
        "manes" : ["ēs","ium","ibus","īs"],
        "miles" : ["is","ī","em","e","ēs","um","ibus"],
        "dos" : ["is","ī","em","e","ēs","um","ibus","ium"],
        "infans" : ["is","ī","em","e","ēs","ium","um","ibus","īs"],
        "turris" : ["is","im","em","ī","e","ēs","īs","ibus","ium","um"],
        "nauis" : ["is","im","em","ī","e","ēs","īs","ibus","ium"],
        "poesis" : ["is","ī","im","ēs","ium","ibus","īs"],
        "honor" : ["or","os","ōris","ōrem","ōrī","ōrēs","ōrum","ōribus"],
        "corpus" : ["is","ī","e","a","um","ibus"],
        "mare" : ["is","ī","e","ia","ium","ibus"],
        "animal" : ["is","ī","ia","ium","ibus"],
        "moenia" : ["ia","ium","iōrum","ibus","iīs","e"],
        "manus" : ["us","ūs","uī","um","ū","uum","ibus","ubus"],
        "domus" : ["us","ūs","uī","um","ū","uum","ibus","ubus","ī","ō","ōrum","ōs"],
        "lacus" : ["us","ūs","uī","um","ū","uum","ibus","ubus","īs"],
        "acus" : ["us","ūs","uī","um","ū","uum","ibus","ubus"],
        "cornu" : ["ū","ūs","ua","uum","ubus","ibus"],
        "opes" : ["ēs","um","ibus","īs"],
        "perseus" : ["eī","eōs","eō","ea","eum","eu"],
        "dies" : ["ēs","ēī","em","ē","ērum","ēbus"],
        "res" : ["ēs","eī","em","ē","ērum","ēbus"],
        "isaac" : [""],
        "abraham" : [""],
        "clio" : ["ō","ūs"],
        "thales" : ["es","is","ētis","ī","ētī","em","ēn","ēta","ētem","e"],
        "tethys" : ["is","os","ī","n","e",""],
        "jesus" : ["ūs","ū","um"],
        "plus" : ["s","ris","re","rēs","ra","rium","ribus"],
        "uis" : ["īs","ī","im","īrēs","īribus","īrium","īrīs"],
        "consilium" : ["ium","ī","iī","iō","ia","iōrum","iīs","īs","iom"],
        "mille": ["ia","ium","ibus"],
        "briseis": ["is","em","a","os","e","ēs","as","um","ibus"],
        "comparative" : ["ior","ius","iōris","iōrī","iōrem","iōre","iōrēs","iōra","iōrum","iōribus"],
        }

adjectives = {
        "doctus" : declensions['roma'] + declensions['lupus'] + declensions['templum'],
        "fortis" : declensions['ciuis'] + declensions['mare'],
        "facilis" : declensions['ciuis'] + declensions['mare'],
        "aureus" : declensions['roma'] + declensions['lupus'] + declensions['templum'],
        "diues" : declensions['miles'] + declensions['corpus'],
        "acer" : declensions['ciuis'] + declensions['mare'],
        "artios" : declensions['delos'] + declensions['templum'],
        "miser" : declensions['roma'] + declensions['puer'] + declensions['templum'],
        "pulcher" : declensions['roma'] + declensions['ager'] + declensions['templum'],
        "noster" : declensions['roma'] + declensions['ager'] + declensions['templum'],
        "deni" : declensions['epulae'] + declensions['liberi'] + declensions['castra'],
        "nonus" : declensions['roma'] + declensions['lupus'] + declensions['templum'],
        "deterior" : declensions['comparative'],
        "duo" : ["ōrum","ī","ōs","ōbus","ae","ās","ārum","ābus"],
        "meus" : ["ea","eum","eī","eae","eō","eum","eam","eā","ī","eōrum","eārum","eīs","eōs","eās"],
        "suus" : declensions['roma'] + declensions['lupus'] + declensions['templum'],
        "multus" : declensions['roma'] + declensions['lupus'] + declensions['templum'],
        "uetus" : declensions['miles'] + declensions['corpus'],
        "celer" : declensions['apis'] + declensions['mare'],
        "tres" : ["ēs","ia","ium","ibus","īs"],
        }

adverbs_in_e = ["doctus","aureus","miser","pulcher"]

adverbs_in_iter = ["fortis","diues","acer","uetus","celer"]

comparatives = ["doctus","fortis","diues","acer","artios","miser","pulcher","uetus","celer","facilis"]

pronouns = {
        "qui" : ["quī","quae","quod","cuius","cui","quem","quam","quō","quā","quōrum","quārum","quibus","quōs","quās","quīs"],
        "quis" : ["quis","quae","quid","cuius","cui","quem","quam","quō","quī","quōrum","quibus","quōs","quīs","qua"],
        "ego" : ["ego","meī","mihi","mī","mē","mēd"],
        "nos" : ["nōs","nostrum","nostrī","nōbīs"],
        "nemo" : ["nēmō","nēminis","nēminī","nēminem","nēmine"],
        "se" : ["suī","sibi","sē","sēd"],
        "tu" : ["tū","tuī","tibi","tē","tēd"],
        "uos" : ["vōs","vestrum","vestrī","vostrum","vostrī","vōbīs"],
        }

determiners = {
        "unus" : adjectives['doctus'] + ['ius','īus'],
        "ipse" : adjectives['doctus'] + ['ius','īus'],
        "uter" : adjectives['doctus'] + ['ius','īus'],
        "alter" : adjectives['doctus'] + ['ius','īus'],
        "ille" : adjectives['doctus'] + ['ius','īus','ud'],
        "is" : ["is","ea","id","eius","eī","eum","eam","eō","eā","iī","eae","eōrum","eārum","eīs","iīs","eōs","eās"],
        "hic" : ["ic","ice","īce","īc","icce","aec","aece","oc","oce","uius","uiusce","uic","unc","anc","unce","ance","ōc","āc","ī","ae","ōrum","ōrumce","ōrunce","ārum","ārumce","ārunce","īs","īsce","ōs","ōsce","ās","āsce"],
        "i" : ["ī","ea","i","eius","eī","eun","ean","eō","eā","iī","eae","eōrun","eārun","eīs","iīs","eōs","eās","eum","eam","eōrum","eārum"],
        }

composites = {
        "idem" : (determiners['i'],"dem"),
        "plerique" : (declensions['liberi'] + declensions['epulae'] + declensions['castra'], "que"),
        "qualiscumque" : (adjectives['fortis'],"cumque"),
        "quantuscumque" : (adjectives['doctus'],"cumque"),
        "quicumque" : (pronouns['qui'] + ['quis'],"cumque"),
        "quidam" : (pronouns['qui'] + ['quid','quōrun','quārun','quen','quan'],'dam'),
        "quilibet" : (pronouns['qui'] + ['quid'],'libet'),
        "quinam" : (pronouns['qui'],'nam'),
        "quisnam" : (pronouns['quis'],'nam'),
        "quispiam" : (pronouns['qui'] + ['quis','quid'],"piam"),
        "quisquam" : (pronouns['qui'] + ['quis','quid'],"quam"),
        "quisque" : (pronouns['qui'] + ['quis','quid'],"que"),
        "quiuis" : (pronouns['qui'] + ['quis','quid'],"vīs"),
        "uterque" : (determiners['uter'],"que"),
        }

doubles = {
        "quisquis" : ["quisquis","quidquid","quodquod","cuiuscuius","cuicui","quemquem","quamquam","quōquō","quāquā","quīquī","quaequae","quōrumquōrum","quārumquārum","quibusquibus","quōsquōs","quāsquās","quaqua"],
        "unusquisque" : ["ūnusquisque","ūnusquīque","ūnaquaeque","ūnumquidque","ūnumquodque","ūniuscuiusque","ūnīuscuiusque","ūnīcuique","ūnumquemque","ūnamquamque","ūnōquōque","ūnāquāque","ūnīquīque","ūnaequaeque","ūnaquaeque","ūnōrumqhōrumque","ūnārumquārumque","ūnīsquibusque","ūnōsquōsque","ūnāsquāsque"],
        "siquis" : ["sīquis","sīquī","sīquae","sīquod","sīquid","sīcuius","sīcui","sīquem","sīquam","sīquō","sīquā","sīquī","sīqua","sīquōrum","sīquārum","sīquibus","sīquōs","sīquās"],
        }

conjugations = {
        "amo" : "first",
        "lego" : "third",
        "dico" : "third",
        "moneo" : "second",
        "capio" : "third_io",
        "imitor" : "first",
        "potior" : "fourth",
        "sequor" : "third",
        "audio" : "fourth",
        "absum" : "sum",
        "fero" : "fero",
        "patior" : "third_io",
        "sum" : "sum",
        "aio" : "fourth",
        "edo" : "edo",
        "facio" : "third_io",
        "fio" : "fio",
        "uereor" : "second",
        "scio" : "fourth",
        "licet" : "second",
        "do" : "do",
        "malo" : "malo",
        "morior" : "third_io",
        "nolo" : "nolo",
        "possum" : "possum",
        "prosum" : "sum",
        "uolo" : "uolo",
        "eo" : "eo",
        }


present_system = {
        "first": {
            "active" : {
                "pres_indic" : ["ō","ās","at","āmus","ātis","ant"],
                "pres_subj" : ["em","ēs","et","ēmus","ētis","ent"],
                "impf_indic" : ["ābam","ābās","ābat","ābāmus","ābātis","ābant"],
                "impf_subj" : ["ārem","ārēs","āret","ārēmus","ārētis","ārent"],
                "fut_indic" : ["ābō","ābis","ābit","ābimus","ābitis","ābunt"],
                "pres_impv" : ["ā","āte","ātō","ātōte","antō"],
                "pres_inf" : ["āre"],
                },
            "passive" : {
                "pres_indic" : ["or","āris","āre","ātur","āmur","āminī","antur"],
                "pres_subj" : ["er","ēris","ēre","ētur","ēmur","ēminī","entur"],
                "impf_indic" : ["ābar","ābāris","ābāre","ābātur","ābāmur","ābāminī","ābantur"],
                "impf_subj" : ["ārer","ārēris","ārēre","ārētur","ārēmur","ārēminī","ārentur"],
                "fut_indic" : ["ābor","āberis","ābere","ābitur","ābimur","ābiminī","ābuntur"],
                "pres_impv" : ["āre","āminī","ātor","antor"],
                "pres_inf" : ["ārī","ārier"],
                },
            "participles" : {
                "pres_ptcpl" : ["āns","ant"],
                "gerundive" : ["and"],
                }
            },
        "second": {
            "active" : {
                "pres_indic" : ["eō","ēs","et","ēmus","ētis","ent"],
                "pres_subj" : ["eam","eās","eat","eāmus","eātis","eant"],
                "impf_indic" : ["ēbam","ēbās","ēbat","ēbāmus","ēbātis","ēbant"],
                "impf_subj" : ["ērem","ērēs","ēret","ērēmus","ērētis","ērent"],
                "fut_indic" : ["ēbō","ēbis","ēbit","ēbimus","ēbitis","ēbunt"],
                "pres_impv" : ["ē","ēte","ētō","ētōte","entō"],
                "pres_inf" : ["ēre"],
                },
            "passive" : {
                "pres_indic" : ["eor","ēris","ēre","ētur","ēmur","ēminī","entur"],
                "pres_subj" : ["ear","eāris","eāre","eātur","eāmur","eāminī","eantur"],
                "impf_indic" : ["ēbar","ēbāris","ēbāre","ēbātur","ēbāmur","ēbāminī","ēbantur"],
                "impf_subj" : ["ērer","ērēris","ērēre","ērētur","ērēmur","ērēminī","ērentur"],
                "fut_indic" : ["ēbor","ēberis","ēbere","ēbitur","ēbimur","ēbiminī","ēbuntur"],
                "pres_impv" : ["ēre","ēminī","ētor","entor"],
                "pres_inf" : ["ērī","ērier"],
                },
            "participles" : {
                "pres_ptcpl" : ["ēns","ent"],
                "gerundive" : ["end"],
                }
            },
        "third": {
            "active" : {
                "pres_indic" : ["ō","is","it","imus","itis","unt"],
                "pres_subj" : ["am","ās","at","āmus","ātis","ant"],
                "impf_indic" : ["ēbam","ēbās","ēbat","ēbāmus","ēbātis","ēbant"],
                "impf_subj" : ["erem","erēs","eret","erēmus","erētis","erent"],
                "fut_indic" : ["am","ēs","et","ēmus","ētis","ent"],
                "pres_impv" : ["e","ite","itō","itōte","untō"],
                "pres_inf" : ["ere"],
                },
            "passive" : {
                "pres_indic" : ["or","eris","ere","itur","imur","iminī","untur"],
                "pres_subj" : ["ar","āris","āre","ātur","āmur","āminī","antur"],
                "impf_indic" : ["ēbar","ēbāris","ēbāre","ēbātur","ēbāmur","ēbāminī","ēbantur"],
                "impf_subj" : ["erer","erēris","erēre","erētur","erēmur","erēminī","erentur"],
                "fut_indic" : ["ar","ēris","ēre","ētur","ēmur","ēminī","entur"],
                "pres_impv" : ["ere","iminī","itor","untor"],
                "pres_inf" : ["ī","erier"],
                },
            "participles" : {
                "pres_ptcpl": ["ēns","ent"],
                "gerundive" : ["end"],
                }
            },
        "third_io": {
            "active" : {
                "pres_indic" : ["iō","is","it","imus","itis","iunt"],
                "pres_subj" : ["iam","iās","iat","iāmus","iātis","iant"],
                "impf_indic" : ["iēbam","iēbās","iēbat","iēbāmus","iēbātis","iēbant"],
                "impf_subj" : ["erem","erēs","eret","erēmus","erētis","erent"],
                "fut_indic" : ["iam","iēs","iet","iēmus","iētis","ient"],
                "pres_impv" : ["e","ite","itō","itōte","iuntō"],
                "pres_inf" : ["ere"],
                },
            "passive" : {
                "pres_indic" : ["ior","eris","ere","itur","imur","iminī","iuntur"],
                "pres_subj" : ["iar","iāris","iāre","iātur","iāmur","iāminī","iantur"],
                "impf_indic" : ["iēbar","iēbāris","iēbāre","iēbātur","iēbāmur","iēbāminī","iēbantur"],
                "impf_subj" : ["erer","erēris","erēre","erētur","erēmur","erēminī","erentur"],
                "fut_indic" : ["iar","iēris","iēre","iētur","iēmur","iēminī","ientur"],
                "pres_impv" : ["ere","iminī","itor","iuntor"],
                "pres_inf" : ["ī","irier"],
                },
            "participles" : {
                "pres_ptcpl": ["iēns","ient"],
                "gerundive" : ["iend"],
                }
            },
        "fourth": {
            "active" : {
                "pres_indic" : ["iō","īs","it","īmus","ītis","iunt"],
                "pres_subj" : ["iam","iās","iat","iāmus","iātis","iant"],
                "impf_indic" : ["iēbam","iēbās","iēbat","iēbāmus","iēbātis","iēbant"],
                "impf_subj" : ["īrem","īrēs","īret","īrēmus","īrētis","īrent"],
                "fut_indic" : ["iam","iēs","iet","iēmus","iētis","ient"],
                "pres_impv" : ["ī","īte","ītō","ītōte","iuntō"],
                "pres_inf" : ["īre"],
                },
            "passive" : {
                "pres_indic" : ["ior","īris","īre","ītur","īmur","īminī","iuntur"],
                "pres_subj" : ["iar","iāris","iāre","iātur","iāmur","iāminī","iantur"],
                "impf_indic" : ["iēbar","iēbāris","iēbāre","iēbātur","iēbāmur","iēbāminī","iēbantur"],
                "impf_subj" : ["īrer","īrēris","īrēre","īrētur","īrēmur","īrēminī","īrentur"],
                "fut_indic" : ["iar","iēris","iēre","iētur","iēmur","iēminī","ientur"],
                "pres_impv" : ["īre","īminī","ītor","iuntor"],
                "pres_inf" : ["īrī","īrier"],
                },
            "participles" : {
                "pres_ptcpl" : ["iēns","ient"],
                "gerundive" : ["iend"],
                }
            },
        "eo": {
            "active" : {
                "pres_indic" : ["eō","īs","it","īmus","ītis","eunt"],
                "pres_subj" : ["eam","eās","eat","eāmus","eātis","eant"],
                "impf_indic" : ["ībam","ībās","ībat","ībāmus","ībātis","ībant"],
                "impf_subj" : ["īrem","īrēs","īret","īrēmus","īrētis","īrent"],
                "fut_indic" : ["ībō","ībis","ībit","ībimus","ībitis","ībunt"],
                "pres_impv" : ["ī","īte","ītō","ītōte","euntō"],
                "pres_inf" : ["īre"],
                },
            "passive" : {
                "pres_indic" : ["eor","īris","īre","ītur","īmur","īminī","iuntur"],
                "pres_subj" : ["ear","eāris","eāre","eātur","eāmur","eāminī","iantur"],
                "impf_indic" : ["ībar","ībāris","ībāre","ībātur","ībāmur","ībāminī","ībantur"],
                "impf_subj" : ["īrer","īrēris","īrēre","īrētur","īrēmur","īrēminī","īrentur"],
                "fut_indic" : ["ībor","īberis","ībere","ībitur","ībimur","ībiminī","ībuntur"],
                "pres_impv" : ["īre","īminī","ītor","euntor"],
                "pres_inf" : ["īrī","īrier"],
                },
            "participles" : {
                "pres_ptcpl" : ["iēns","eunt"],
                "gerundive" : ["iend"],
                }
            },
        "sum": {
            "active" : {
                "pres_indic" : ["sum","es","est","sumus","estis","sunt"],
                "pres_subj" : ["sim","sīs","sit","sīmus","sītis","sint","siem","sies","siet","siemus","sietis","sient"],
                "impf_indic" : ["eram","erās","erat","erāmus","erātis","erant"],
                "impf_subj" : ["essem","essēs","esset","essēmus","essētis","essent"],
                "fut_indic" : ["erō","eris","erit","erimus","eritis","erunt"],
                "pres_impv" : ["es","este","estō","estōte"],
                "pres_inf" : ["esse"],
                "fut_inf" : ["fore"],
                },
            "participles" : {
                "pres_ptcpl" : ["sēns","sent"],
                "gerundive" : ["end"],
                }
            },
        "possum": {
            "active" : {
                "pres_indic" : ["possum","potes","potest","possumus","potestis","possunt"],
                "pres_subj" : ["possim","possīs","possit","possīmus","possītis","possint","possiem","possies","possiet","possiemus","possietis","possient"],
                "impf_indic" : ["poteram","poterās","poterat","poterāmus","poterātis","poterant"],
                "impf_subj" : ["possem","possēs","posset","possēmus","possētis","posesent"],
                "fut_indic" : ["poterō","poteris","poterit","poterimus","poteritis","poterunt"],
                "pres_impv" : ["potes","poteste","potestō","potestōte"],
                "pres_inf" : ["posse"],
                },
            "participles" : {
                "pres_ptcpl" : ["potēns","potent"],
                "gerundive" : ["potend"],
                }
            },
        "uolo": {
            "active" : {
                "pres_indic" : ["volō","vīs","vult","volt","volumus","vultus","voltis","volunt"],
                "pres_subj" : ["velim","velīs","velit","velīmus","velītis","velint"],
                "impf_indic" : ["volēbam","volēbās","volēbat","volēbāmus","volēbātis","volēbant"],
                "impf_subj" : ["vellem","vellēs","vellet","vellēmus","vellētis","vellent"],
                "fut_indic" : ["volam","volēs","volet","volēmus","volētis","volent"],
                "pres_impv" : [],
                "pres_inf" : ["velle"],
                },
            "participles" : {
                "pres_ptcpl" : ["volēns","volent"],
                "gerundive" : ["volend"],
                }
            },
        "malo": {
            "active" : {
                "pres_indic" : ["mālō","māvīs","māvult","māvolt","mālumus","māvultus","māvoltis","mālunt"],
                "pres_subj" : ["mālim","mālīs","mālit","mālīmus","mālītis","mālint"],
                "impf_indic" : ["mālēbam","mālēbās","mālēbat","mālēbāmus","mālēbātis","mālēbant"],
                "impf_subj" : ["māllem","māllēs","māllet","māllēmus","māllētis","māllent"],
                "fut_indic" : ["mālam","mālēs","mālet","mālēmus","mālētis","mālent"],
                "pres_impv" : [],
                "pres_inf" : ["mālle"],
                },
            "participles" : {
                "pres_ptcpl" : ["mālēns","mālent"],
                "gerundive" : ["mālend"],
                }
            },
        "nolo": {
            "active" : {
                "pres_indic" : ["nōlō","nōlumus","nōlunt"],
                "pres_subj" : ["nōlim","nōlīs","nōlit","nōlīmus","nōlītis","nōlint"],
                "impf_indic" : ["nōlēbam","nōlēbās","nōlēbat","nōlēbāmus","nōlēbātis","nōlēbant"],
                "impf_subj" : ["nōllem","nōllēs","nōllet","nōllēmus","nōllētis","nōllent"],
                "fut_indic" : ["nōlam","nōlēs","nōlet","nōlēmus","nōlētis","nōlent"],
                "pres_impv" : ["nōlī","nōlīte","nōlītō","nōluntō","nōlītōte"],
                "pres_inf" : ["nōlle"],
                },
            "participles" : {
                "pres_ptcpl" : ["nōlēns","nōlent"],
                "gerundive" : ["nōlend"],
                }
            },
        "fero": {
            "active" : {
                "pres_indic" : ["ferō","fers","fert","ferimus","fertis","ferunt"],
                "pres_subj" : ["feram","ferās","ferat","ferāmus","ferātis","ferant"],
                "impf_indic" : ["ferēbam","ferēbās","ferēbat","ferēbāmus","ferēbātis","ferēbant"],
                "impf_subj" : ["ferrem","ferrēs","ferret","ferrēmus","ferrētis","ferrent"],
                "fut_indic" : ["feram","ferēs","feret","ferēmus","ferētis","ferent"],
                "pres_impv" : ["fer","ferte","fertō","fertōte","feruntō"],
                "pres_inf" : ["ferre"],
                },
            "passive" : {
                "pres_indic" : ["feror","ferris","ferre","fertur","ferimur","feriminī","feruntur"],
                "pres_subj" : ["ferar","ferāris","ferāre","ferātur","ferāmur","ferāminī","ferantur"],
                "impf_indic" : ["ferēbar","ferēbāris","ferēbāre","ferēbātur","ferēbāmur","ferēbāminī","ferēbantur"],
                "impf_subj" : ["ferrer","ferrēris","ferrēre","ferrētur","ferrēmur","ferrēminī","ferrentur"],
                "fut_indic" : ["ferar","ferēris","ferēre","ferētur","ferēmur","ferēminī","ferentur"],
                "pres_impv" : ["ferre","feriminī","fertor","feruntor"],
                "pres_inf" : ["īrī"],
                },
            "participles" : {
                "pres_ptcpl" : ["ferēns","ferent"],
                "gerundive" : ["ferend"],
                }
            },
        "edo": {
            "active" : {
                "pres_indic" : ["edō","edis","ēs","edit","ēst","edimus","editis","ēstis","edunt"],
                "pres_subj" : ["edam","edim","edās","edīs","edat","edit","edāmus","edīmus","edātis","edītis","edant","edint"],
                "impf_indic" : ["edēbam","edēbās","edēbat","edēbāmus","edēbātis","edēbant"],
                "impf_subj" : ["ederem","ederēs","ēssēs","ederet","ēsset","ederēmus","ēssēmus","ederētis","ēssētis","ederent","ēssent"],
                "fut_indic" : ["edam","edēs","edet","edēmus","edētis","edent"],
                "pres_impv" : ["ede","ēs","edite","ēste","editō","ēstō","editōte","ēstōte","eduntō"],
                "pres_inf" : ["edere","ēsse"],
                },
            "passive" : {
                "pres_indic" : ["edor","ederis","edere","editur","ēstur","edimur","ediminī","eduntur"],
                "pres_subj" : ["edar","edāris","edāre","edātur","edāmur","edāminī","edantur"],
                "impf_indic" : ["edēbar","edēbāris","edēbāre","edēbātur","edēbāmur","edēbāminī","edēbantur"],
                "impf_subj" : ["ederer","ederēris","ederēre","ederētur","ederēmur","ederēminī","ederentur","ēssētur"],
                "fut_indic" : ["edar","edēris","edēre","edētur","edēmur","edēminī","edentur"],
                "pres_impv" : ["edere","ediminī","editor","eduntor"],
                "pres_inf" : ["edī","ederier"],
                },
            "participles" : {
                "pres_ptcpl" : ["edēns","edent"],
                "gerundive" : ["edend"],
                }
            },
        "fio": {
            "active" : {
                "pres_indic" : ["fiō","fīs","fit","fīmus","fītis","fiunt"],
                "pres_subj" : ["fiam","fiās","fiat","fiāmus","fiātis","fiant"],
                "impf_indic" : ["fiēbam","fiēbās","fiēbat","fiēbāmus","fiēbātis","fiēbant"],
                "impf_subj" : ["fierem","fierēs","fieret","fierēmus","fierētis","fierent"],
                "fut_indic" : ["fiam","fiēs","fiet","fiēmus","fiētis","fient"],
                "pres_impv" : ["fī","fīte","fītō","fītōte","fiuntō"],
                "pres_inf" : ["fierī"],
                },
            "participles" : {
                "pres_ptcpl" : ["fiēns","fient"],
                "gerundive" : ["fiend"],
                }
            },
        "do": {
            "active" : {
                "pres_indic" : ["ō","as","at","amus","atis","ant"],
                "pres_subj" : ["em","ēs","et","ēmus","ētis","ent"],
                "impf_indic" : ["abam","abās","abat","abāmus","abātis","abant"],
                "impf_subj" : ["arem","arēs","aret","arēmus","arētis","arent"],
                "fut_indic" : ["abō","abis","abit","abimus","abitis","abunt"],
                "pres_impv" : ["ā","ate","atō","atōte","antō"],
                "pres_inf" : ["are"],
                },
            "passive" : {
                "pres_indic" : ["or","aris","are","atur","amur","aminī","antur"],
                "pres_subj" : ["er","ēris","ēre","ētur","ēmur","ēminī","entur"],
                "impf_indic" : ["abar","abāris","abāre","abātur","abāmur","abāminī","abantur"],
                "impf_subj" : ["arer","arēris","arēre","arētur","arēmur","arēminī","arentur"],
                "fut_indic" : ["abor","aberis","abere","abitur","abimur","abiminī","abuntur"],
                "pres_impv" : ["are","aminī","ator","antor"],
                "pres_inf" : ["arī","arier"],
                },
            "participles" : {
                "pres_ptcpl" : ["āns","ant"],
                "gerundive" : ["and"],
                }
            },
        }

perfect_system = {
        "pf_indic" : ["ī","istī","īt","imus","īstis","ērunt","ēre"],
        "pf_subj" : ["erim","eris","erit","erimus","eritis","erint"],
        "plpf_indic" : ["eram","erās","erat","erāmus","erātis","erant"],
        "plpf_subj" : ["issem","issēs","isset","issēmus","issētis","issent"],
        "fpf_indic" : ["erō","eris","erit","erimus","eritis","erint"],
        "pf_inf" : ["isse"]
        }

perfect_syncopated = {
        "Vv" : ["stī","stis","rim","ris","rit","rimus","ritis","rant","ram","rās","rat","rāmus","rātis","rant","sse"],
        "iv" : ["stī","stis","sse","ssem","ssēs","sset","ssēmus","ssētis","ssent"],
        }
