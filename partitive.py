import random
#All thanks to my beautiful girlfriend Maria that helped me with this program <3
def get_first_vowel_in_long_word(word):
    vowels = "aeiouyäö"
    last_five = word[-5:]

    first_vowel = next((ch for ch in last_five if ch in vowels), None)
    return first_vowel

def syllables_decider(word):
    vowels = "aeiouyäö"

    diphthongs = {
        "ai","ei","oi","ui","yi","äi","öi",
        "au","eu","iu","ou","äy","öy","ey","iy",
        "ie","uo","yö","io"
    }

    word = word.lower()
    count = 0
    i = 0

    while i < len(word):
        if word[i] in vowels:
            count += 1
            if i+2 < len(word) and word[i+1:i+3] in diphthongs:
                i += 1

            # normal diphthong or long vowel
            elif i+1 < len(word) and (
                word[i] == word[i+1] or
                word[i:i+2] in diphthongs
            ):
                i += 1

        i += 1

    return count

def sg_pl(decision:str):
    if decision == "s":
        return "singular"
    elif decision == "p":
        return "plural"
    elif decision == "b":
        return "both"


def partitive_pl(word) -> str:

    all_vowels = "aeiouyöä"
    basic_vowels = "aeiou"
    neutral_vowels = "ei"
    neutralising_vowels = "aou"
    changing_vowels = "äyö"
    syllables = syllables_decider(word)
    #si/ us might be exception - file

    #ravintola
#All thanks to my beautiful girlfriend Maria that helped me with this program <3    
    #koe, rikas, mies, puhelin
    #Leimu contribution# - näppäin <3 saippuakauppias
    exceptions = {"kukka": "kukkia","tekijä":"tekijöitä","peli":"peleja","pakka":"pakkoja","vuoro":"vuoroja","hana":"hanoja", "kaappi":"kaappeja", "maailma":"maailmoja", "keskusta":"keskustoja", "sana":"sanoja","etelä":"eteliä","jänis":"jäniksiä","viikko":"viikkoja","kiuas":"kiukaita","suola":"suoloja","veli":"veljiä","ihana":"ihania","näppäin":"näppäimiä","muna":"munia","appelsiini":"appelsiineja", "voi":"voita","hidas":"hitaita", "laite":"laitteita","kausi": "kausia", "taide":"taiteita","laki":"lakeja","hotelli":"hotelleja","pullo":"pulloja","vuoro":"vuoroja","hana":"hanoja","verkko":"verkkoja","lahje":"lahkeita","kirkko":"kirkkoja","omena":"omenoita","ien":"ikeniä","koe":"kokeita", "rikas":"rikkaita", "mies":"miehiä", "puhelin":"puhelimia", "tytär":"tyttäriä", "kannel":"kanteleita", "sävel":"säveliä", "kyynel":"kyyneleitä", "sammal":"sammaleita", "taival":"taipaleita", "askel":"askeleita", "nivel":"niveliä","ommel":"ompeleita", "tanner":"tantereita", "manner":"mantereita", "seitsemän":"seitsemiä", "jääkiekko":"jääkiekkoja", "matala":"matalia","ihana":"ihania", "ahkera":"ahkeria", "sako":"sakkoja", "musiikki":"musiikkeja"}
    
    i_to_e = ["alpi","uni", "appi","arki","arpi","hanhi","hanki","happi","hapsi","hauki","heisi","helmi","henki","hetki","hiili","hiiri","hiisi","hiki",
"hirsi","hirvi","huoli","huuli","impi","joki","jouhi","jousi","juoni","juuri","jälki","jälsi","järki","järvi","Jääski","kaali","kaari","kaihi","kaikki","kaksi",
"kampi","kanki","kansi","karhi","kaski","kieli","kiiski","kilpi","kirsi","kivi","koipi","korpi","korsi","koski","kuori","kurki","kusi",
"kuusi","kylki","Kymi","kynsi","käki","kärki","käsi","köysi","lahti","laki","lampi","lapsi","lehti","lempi","leski","liemi","liesi",
"lohi","loimi","Louhi","lovi","lumi","luomi","länki","länsi","meri","mesi","mieli","moni","mäki","niemi","niini","nimi","noki","nummi","nuoli",
"nuori","nurmi","närhi","onki","onni","orsi","ovi","paasi","parsi","parvi","peitsi","pieli","pieni","piki","pilvi","polvi","ponsi",
"poski","povi","puoli","pursi","putki","pälvi","reki","reisi","retki","riihi","ripsi","rupi","ruuhi","saari","saarni",
"saksi","salmi","sampi","sappi","sarvi","savi","seimi","sieni","siili","siipi","sini","solki","soppi","sormi","suksi","suoli","Suomi","suomi",
"suoni","susi","suuri","suvi","syli","sylki","sysi","sänki","särki","sääri","sääski","taimi","talvi","tammi","teeri","telki",
"tiili","tilhi","toimi","tonki","torvi","tosi","tuki","tuli","tuohi","tuomi","tuoni","tuppi","tuuli","typpi","tyvi","tyyni",
"tähti","täysi","uksi","uuhi","uusi","varsi","veitsi","veli","veri","vesi","vieri","viiksi","viisi","virpi",
"virsi","vuohi","Vuoksi","vuori","vuosi","vyyhti","väki","yksi","ääni","ääri"]


    for item in exceptions:
        if len(item) >= 4 and len(word) >= 7 and item in word[-len(item):]:
            word = word[:-len(item)] + exceptions[item]
            return word
        
        else:
            if item == word:
                word = exceptions[item]
                return word

    for item in i_to_e:
        if len(word) > 7:
            if item == word[-len(item):]:
                if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-5:]  for vowel in neutral_vowels) and not any(vowel in word[-4:] for vowel in neutralising_vowels):
                    word += "ä"
                else:
                    word += "a"
                return word
        else:
            if item == word:
                if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-5:]  for vowel in neutral_vowels) and not any(vowel in word[-4:] for vowel in neutralising_vowels):
                    word += "ä"
                else:
                    word += "a"
                return word



        #mansikka/
    if word[-3:] in ("kka","kko") and syllables >= 3 and not any(vowel in word for vowel in changing_vowels):
        word = word[:-2] + "oita"

    elif word[-3:] in ("hai", "tai"):
        word += "ta"

    elif word[-3:] == "mal":
        word += "ia"    


    
    elif word[-3:] in ("yrä") and syllables == 3:
        word = word[:-1] + "öitä"

    elif word[-3:] in ("ävä", "evä", "ärä") and syllables == 3:
        word = word[:-1] + "iä"
    
    elif word[-2:] in ("lä", "rä", "nä", "iä") and syllables >= 3 and not any(vowel in word for vowel in neutralising_vowels):
        word = word[:-1] + "öitä" 
        
    elif word[-1] == "ä" and word[-2:] != "ää":
        word = word[:-1] + "iä"
        
    elif word[-4:] == "mmas":
        word = word[:-3] + "paita"
    
    elif word[-3:] == "das":
        word = word[:-3] + "taita"

    elif word[-3:] in ("kke"):
        word = word[:-1] + "eja"

    elif word[-4:] == "aite":
        word = word[:-1] + "teita"

        #varvas -> varpaita
    elif word[-4:] == "rvas":
        word = word[:-3] + "paita"

    elif word[-2:] == "pas":
        word = word[:-1] + "paita"
        #taivas -> taivaita
    elif word[-3:] == "vas":
        word = word[:-1] + "ita"

        #kauppias -> kauppiaita
    elif word[-3:] == "ias":
        word = word[:-1] + "ita"

  

    

        #mukava, matala
    elif (word[-3:] in ("ala", "ava", "isa", "era") and syllables == 3) and word[-4:] != "aala":
        word = word[:-1] + "ia"


        #ravintola
    elif word[-2:] in ("la", "ra", "na", "ia") and syllables >= 3 and not any(vowel in word for vowel in changing_vowels):
        word = word[:-1] + "oita"

        #opiskelija 
    elif word[-3:] == "ija" and syllables >= 3:
        word = word[:-1] + "oita"

    elif word[-3:] == "ijä" and syllables >= 3:
        word = word[:-1] + "äitä"

        #korkea
    elif word[-2:] == "ea" and syllables >= 3:
        word = word[:-1] + "ita"

    elif word[-2:] == "eä" and syllables >= 3:
        word = word[:-1] + "itä"
        #vadelma, majava
    elif word[-2:] in ("ma", "va") and syllables >= 3:
        word = word[:-1] + "ia"

    elif word[-2:] in ("mä", "vä")and syllables >= 3:
        word = word[:-1] + "iä"

        #aja -> ia, opettaja
    elif word[-3:] == "aja" and syllables >= 3:
        word = word[:-1] + "ia" 

    elif word[-3:] == "äjä"and syllables >= 3:
        word = word[:-1] + "iä" 

        #kännykkä
    elif word[-3:] in ("kkä", "kkö") and syllables >= 3:
        word = word[:-2] + "öitä"
    


        # o / u
        #and syllables == 2 
    elif word[-1] == "a" and (get_first_vowel_in_long_word(word) in ("a", "e", "i")) and word[-2:] != "aa":
        word = word[:-1] + "oja"

        #2 syllables words with a ending
        # o / u
        #and syllables == 2 #it doesnt work for kauppa
    elif word[-1] == "a" and (get_first_vowel_in_long_word(word) in ("o", "u")) and word[-2:] != "aa":
        word = word[:-1] + "ia"

        #kenkä, leipä

        #tie -> eitä
    elif word[-2:] == "ie":
        word = word[:-2] + "eitä"
        #uo -> oita
    elif word[-2:] == "uo":
        word = word[:-2] + "oita"

        #yö -> öitä
    elif word[-2:] == "yö":
        word = word[:-2] + "öitä"

        #eo -> eoita
    elif word[-2:] == "eo":
        word = word[:-2] +"eoita"
        #io -> ioita
    elif word[-2:] == "io":
        word = word[:-2] +"ioita"
        #iö -> iöitä
    elif word[-2:] == "iö":
        word = word[:-2] +"iöitä"
        #ao -> aoita 
    elif word[-2:] == "ao":
        word = word[:-2] +"aoita"
        #All thanks to my beautiful girlfriend Maria that helped me with this program <3
        #suomalainen 

        #nen -> sia
    elif word[-3:] == "nen":
        if any(vowel in word[-7:] for vowel in changing_vowels) or any(vowel in word[-7:] for vowel in neutral_vowels) and not any(vowel in word[-7:] for vowel in neutralising_vowels):        
            word = word[:-3] +"siä"
        else:
            word = word[:-3] +"sia"

        #vät
    elif word[-3:] == "vät":
        word = word[:-2] +"äitä"
    #nyt -> neitä
    elif word[-3:] == "nyt":
        word = word[:-2] +"eitä"
    #ut -> ita
    elif word[-2:] == "ut":
        word = word[:-1] +"ita"
    #yt -> itä
    elif word[-2:] == "yt":
        word = word[:-1] +"itä"
    #is -> iita
    elif word[-2:] == "is":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):        
            word = word[:-1] +"itä"
        else:
            word = word[:-1] +"ita"

    #double vowel
    # puu, syy,  maa
    elif word[-2:] in ("uu", "ii", "aa"):
        word = word[:-1] + "ita"

    #myy, jää
    elif word[-2:] in ("ää","yy", "ee"):
        word = word[:-1] + "itä"

    #kuuloke     
    elif word[-2:] == "ke":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):        
            word = word[:-1] + "keitä"
        else:
            word = word[:-1] + "keita"

    elif word[-2:] == "de":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):        
            word = word[:-2] + "teitä"
        else:
            word = word[:-2] + "teita"
        
    elif word[-3:] == "ste":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):        

            word += "itä"
        else:
            word += "ita"
                  

    elif word[-2:] == "te":
        word = word[:-1] + "teita"
        
    #tunne -> tunteita 
    elif word[-3:] == "nne":
        word = word[:-2] + "teita"

    #huone, kone
    elif word[-1] == "e":
        if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-5:] for vowel in neutral_vowels) and not any(vowel in word[-5:] for vowel in neutralising_vowels):        
            word += "itä"
        else:
            word += "ita"

        #All thanks to my beautiful girlfriend Maria that helped me with this program <3            
        #rakkaus might need change to aus
    elif word[-2:] in ("us", "es","os"):
        word = word[:-1] + "ksia"

    elif word[-3:] in ("has"):
        word = word[:-1] + "ksia"

    #närästys
    elif word[-2:] == "ys":
        word = word[:-1] + "ksiä"
    
    #rikas -> riKKaita
    #kaunis -> kauniita
    elif word[-3:] == "nis":
        word = word[:-1] + "ita"

    #siemen
    elif word[-2:] == "en":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word += "iä"
        else:
            word += "ia"
    #All thanks to my beautiful girlfriend Maria that helped me with this program <3
    #rasvaton -> rasvatomia
    elif word[-2:] in ("on","an"):
        word = word[:-2] + "tomia"

    #puhelin
    elif word[-3:] in ("lin", "ain"):
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word = word[:-1] + "miä"
        else:
            word = word[:-1] + "mia"

    elif word[-4:] == "stin":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word = word[:-1] + "miä"
        else:
            word = word[:-1] + "mia"


    elif word[-3:] == "tin":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word = word[:-2] + "timiä"
        else: 
            word = word[:-2] + "timia"
    #sydän
    elif word[-3:] == "dän":
        word = word[:-1] + "miä"  

    #työtön -> työtömiä
    elif word[-2:] in ("ön", "än"):
        word = word[:-2] + "tömiä"
    #matala
    elif word[-1:] == "a" and syllables == 3:
        word = word[:-1] + "ia"

    #hämärä
    elif word[-1:] == "ä" and syllables == 3:
        word = word[:-1] + "iä"


    elif word[-2:] == "li" and syllables >= 3:
        if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word[-6:] for vowel in neutralising_vowels):
            word = word[:-1] + "ejä"
        else:
            word = word[:-1] + "eja"

    

    #luettelo
    elif word[-2:] == "lo" and syllables >= 3:
        word += "ita"

    elif word[-2:] == "la" and syllables >= 3:
        word = word[-1] + "oita"

    #henkilö
    elif word[-2:] == "lö" and syllables >= 3:
        word += "itä"

    #sopraano
    elif word[-2:] == "no" and syllables >= 3:
        word += "ja"
    #sammal



    #kaveri
    elif word[-2:] == "ri" and syllables >= 3:
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
           word = word[:-1] + "eitä"
        else:
            word = word[:-1] + "eita"


    elif word[-2:] == "in":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word = word[:-1] + "mpiä"
        else:
            word = word[:-1] + "mpia"
        

    #numero
    elif word[-2:] == "ro" and syllables >= 3:
        word += "ita"

    
    #u, o, ö, y -> + j + a/ä
    elif word[-1] in ("u", "o"):
        word += "ja"

    elif word[-1] in ("y", "ö"):
        word += "jä"


    #i -> e change
    # when there is no change in i -> e sg, there is change in pl, if there is change in i->e > no change in pl
    #kivi

    #pankki        
    elif word[-1] == "i" and word not in i_to_e:
        if len(word) > 7:
            if any(vowel in word[-len(word)//2:] for vowel in changing_vowels) or any(vowel in word[-len(word)//2:] for vowel in neutral_vowels) and not any(vowel in word[-len(word)//2:] for vowel in neutralising_vowels):
                word = word[:-1] + "ejä"
            else:
                word = word[:-1] + "eja"
        else:
            if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                word = word[:-1] + "ejä"
            else:
                word = word[:-1] + "eja"

        #I to E, need to work on 
    #All thanks to my beautiful girlfriend Maria that helped me with this program <3


    elif word[-3:] == "kas":
        word = word[:-2] + "kaita"
    
    elif word[-3:] == "käs":
        word = word[:-2] + "käitä"

    elif word[-3:] == "tar":
        word = word[:-2] + "taria"

    elif word[-2:] == "ar":
        word += "ia"
    
    elif word[-3:] == "pas":
        word = word[:-2] + "paita"

    elif word[-4:] == "rras":
        word = word[:-3] + "taita"

    elif word[-4:] == "ngas":
        word = word[:-3] + "kaita"

    elif word[-4:] == "llas":
        word = word[:-3] + "taita"

    elif word[-2:] == "as":
        word = word[:-1] + "ita"
    
    elif word[-2:] == "äs":
        word = word[:-1] + "itä"
              


    #partitive_sg(word:str)

    return word

def partitive_sg(word:str) -> str:
    exceptions = {"krokotiili":"krokotiilia","arkkitehti":"arkkitehtia","putous":"putousta","kokous":"kokousta", "vastaus":"vastausta","kuvaus":"kuvausta", "esitys":"esitystä", "ajatus":"ajatusta", "seuraus":"seurausta", "tulos":"tulosta", "kysymys":"kysymystä", "kaappi":"kaappia","penkki":"penkkiä","maalaus":"maalausta","koti":"kotia","historia":"historiaa", "musiikki":"musiikkia","laki":"lakia","appelsiini":"appelsiinia", "suurin":"suurimpaa", "vesi":"vettä", "kieli":"kieltä","kansi":"kantta", "kausi":"kautta", "viini": "viiniä","vastaus":"vastausta",
                  "jälsi": "jälttä", "virsi":"virttä", "yksiö":"yksiötä","työhuone":"työhuonetta","ilmoitus":"ilmoitusta", "päätös":"päätöstä","muutos":"muutosta",
                  "veitsi": "veistä", "suuri":"suurta", "suurin":"suurimpaa","mies":"miestä",
                    "seitsemän":"seitsemää", "vasen":"vasempaa", "kivi":"kiveä", "käsi":"kättä", "veli":"veljeä", "lumi":"lunta",
                      "yksi":"yhtä","uusi":"uutta", "susi":"sutta", "kaksi":"kahta", "uksi":"usta", "kuukausi":"kuukautta", "lapsi":"lasta", "onni":"onnea","veri":"verta", "meri":"merta", "hapsi":"hapsea", "ripsi":"ripseä"}
    
    loan_words = ["stadion", "region", "tradition", "version", "design", "slogan", "organ", "vegan", "internet", "chat", "limit", "laser", "server", "scanner",
                  "diesel", "rock", "punk", "hotelli", "naapuri"]
    
    i_to_e = ["alpi","appi","arki","arpi","hanhi","hanki","happi","hapsi","hauki","heisi","helmi","henki","hetki","hiili","hiiri","hiisi","hiki",
"hirsi","hirvi","huoli","huuli","impi","joki","jouhi","jousi","juoni","juuri","jälki","jälsi","järki","järvi","Jääski","kaali","kaari","kaihi","kaikki","kaksi",
"kampi","kanki","kansi","karhi","kaski","kieli","kiiski","kilpi","kirsi","kivi","koipi","korpi","korsi","koski","kuori","kurki","kusi",
"kuusi","kuusi","kylki","Kymi","kynsi","käki","kärki","käsi","köysi","lahti","laki","lampi","lapsi","lehti","lempi","leski","liemi","liesi",
"lohi","loimi","Louhi","lovi","lumi","luomi","länki","länsi","meri","mesi","mieli","moni","mäki","niemi","niini","nimi","noki","nummi","nuoli",
"nuori","nurmi","närhi","onki","onni","orsi","ovi","paasi","parsi","parvi","peitsi","pieli","pieni","piki","pilvi","polvi","ponsi",
"poski","povi","puoli","pursi","putki","pälvi","reki","reisi","retki","riihi","ripsi","rupi","ruuhi","saari","saarni",
"saksi","salmi","sampi","sappi","sarvi","savi","seimi","sieni","siili","siipi","sini","solki","soppi","sormi","suksi","suoli","Suomi","suomi",
"suoni","susi","suuri","suvi","syli","sylki","sysi","sänki","särki","sääri","sääski","taimi","talvi","tammi","teeri","telki",
"tiili","tilhi","toimi","tonki","torvi","tosi","tuki","tuli","tuohi","tuomi","tuoni","tuppi","tuuli","typpi","tyvi","tyyni",
"tähti","täysi","uksi","uni","uuhi","uusi","varsi","veitsi","veli","veri","vesi","vieri","viiksi","viini","viisi","virpi",
"virsi","vuohi","Vuoksi","vuori","vuosi","vyyhti","väki","yksi","ääni","ääri"]
    all_vowels = "aeiouyöä"
    basic_vowels = "aeiou"
    neutral_vowels = "ei"
    neutralising_vowels = "aou"
    changing_vowels = "äyö"
    #for item in exceptions: old version
    #    if item in word[-len(item):]:
    #        word = word[:-len(item)] + exceptions[item]
    #        return word    



    #vesi -> vetta, exceptions
    #if len(word) >= len(min(exceptions, key=len)):
    for item in exceptions:
        if len(item) >= 4 and len(word) > 7 and item in word[-len(item):]:
            word = word[:-len(item)] + exceptions[item]
            return word
        else:
            if item == word:
                word = exceptions[item]
                return word
    
    #I to E, need to work on 
    for item in i_to_e:
        if len(word) > 7 and len(item) >= 4:
            if item == word[-len(item):]:
            # usi -> usta
                if word[-3:] == "usi":
                    if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                        word = word[:-1] +"tä"
                    else:
                        word = word[:-1] + "ta" #tä

                # ni -> nta/ntä
                elif word[-2:] == "ni":
                    if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                        word = word[:-1] + "tä"
                    else:
                        word = word[:-1] +"ta" 

                # ri -> rtä
                elif word[-2:] == "ri":
                    if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                        word = word[:-1] +"tä"
                    else:
                        word = word[:-1] +"ta" #tä

                # hi -> hta 
                elif word[-2:] == "hi":            
                    if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                        word = word[:-1] +"tä"
                    else:
                        word = word[:-1] +"ta" #tä
                #siili, kaali
                elif word[-4:] in ("iili", "aali"):
                    if "a" in word[-4:]:
                        word += "a"
                    else:
                        word += "ä"
                # li -> ltä
                elif word[-2:] == "li":
                    if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                        word = word[:-1] +"tä"
                    else:
                        word = word[:-1] +"ta" #tä

                # si -> ttä
                elif word[-2:] == "si":
                    if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                        word = word[:-2] +"ttä"
                    else:
                        word = word[:-2] +"tta" # checknout to tä

                #i -> e + a/ä
                else:
                    if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-5:] for vowel in neutral_vowels) and not any(vowel in word[-5:] for vowel in neutralising_vowels):
                        word = word[:-1] +"eä"
                    else:
                        word = word[:-1] +"ea"

                return word
        else:
            if item == word:
                if word[-3:] == "usi":
                    if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                        word = word[:-1] +"tä"
                    else:
                        word = word[:-1] + "ta" #tä

                # ni -> nta/ntä
                elif word[-2:] == "ni":
                    if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                        word = word[:-1] + "tä"
                    else:
                        word = word[:-1] +"ta" 

                # ri -> rtä
                elif word[-2:] == "ri":
                    if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                        word = word[:-1] +"tä"
                    else:
                        word = word[:-1] +"ta" #tä
                #hanhi -> hanhea
                elif word[-3:] == "nhi":            
                    if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                        word = word[:-1] +"eä"
                    else:
                        word = word[:-1] +"ea" #tä                
                # hi -> hta 
                elif word[-2:] == "hi":            
                    if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                        word = word[:-1] +"tä"
                    else:
                        word = word[:-1] +"ta" #tä
                #siili, kaali
                elif word[-4:] in ("iili", "aali"):
                    if "a" in word[-4:]:
                        word += "a"
                    else:
                        word += "ä"
                # li -> ltä
                elif word[-2:] == "li":
                    if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                        word = word[:-1] +"tä"
                    else:
                        word = word[:-1] +"ta" #tä

                # si -> ttä
                elif word[-2:] == "si":
                    if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
                        word = word[:-2] +"ttä"
                    else:
                        word = word[:-2] +"tta" # checknout to tä

                #i -> e + a/ä
                else:
                    if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-5:] for vowel in neutral_vowels) and not any(vowel in word[-5:] for vowel in neutralising_vowels):
                        word = word[:-1] +"eä"
                    else:
                        word = word[:-1] +"ea"

                return word

    #nalle
    if word[-3:] == "lle":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word += "ä"
        else:
            word += "a"

    elif word[-2:] == "ia":
        word += "a"

    elif word[-2:] == "ee":
        word += "tä"

    elif word[-2:] in ("oi","ai"):
        word += "ta"

    #nainen -> naista
    elif word[-3:] == "nen":
        if any(vowel in word[-7:] for vowel in changing_vowels) or any(vowel in word[-7:] for vowel in neutral_vowels) and not any(vowel in word[-7:] for vowel in neutralising_vowels):
            word = word[:-3] + "stä"
        else:
            word = word[:-3] + "sta"

    #ahven -> ahventa
    elif word[-2:] == "en" and word[-3:] != "nen":
        if any(vowel in word for vowel in changing_vowels) or any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word += "tä"
        else:
            word += "ta"


    #RAKKAUS -> rakkautta
    elif word[-4:] in ("kaus"):
        word = word[:-1] + "tta"
    #All thanks to my beautiful girlfriend Maria that helped me with this program <3
    #avaruus and kauneus
    elif word[-3:] in ("eus", "uus","ous", "aus"):
        word = word[:-1] + "tta"

    #kokemus
    elif word[-2:] == "us":
        word += "ta" 

    elif word[-3:] in ("yys", "eys"):
        word = word[:-1] + "ttä"
    #ymmärys -> ymmärystä
    elif word[-2:] == "ys":
        word += "tä"
    #kevyt
    elif word[-2:] == "yt":
        word += "tä"
    

    #E vene -> venettä, laite -> laitetta
    elif word[-1] == "e" and word[-2:] != "ie":
        if any(vowel in word[-5:] for vowel in changing_vowels) or any(vowel in word[-6:] for vowel in neutral_vowels) and not any(vowel in word[-6:] for vowel in neutralising_vowels):
            word += "ttä"
        else: word += "tta"

    # Loan words
    elif word[-1] == "i" and word not in i_to_e:
        if any(vowel in word[-5:] for vowel in changing_vowels) or (any(vowel in word[-6:] for vowel in neutral_vowels) and not any(vowel in word[-8:] for vowel in neutralising_vowels)):
            word = word +"ä"
        else:
            word = word +"a"

    elif word in loan_words:
        if word[-1] == "i":
            word += "a"
        else: word += "ia"

    #auto -> autoa / leipää -> leipää
    elif word[-1] in all_vowels and word[-2] not in all_vowels:
        if word[-1] in changing_vowels:
            word += "ä"
        elif any(vowel in word for vowel in neutral_vowels) and not any(vowel in word for vowel in neutralising_vowels):
            word += "ä"
        elif word[-1] in basic_vowels:
            word += "a"

    #samea
    elif word[-2:] == "ea":
        word += "a"

    elif word[-2:] == "eä":
        word += "ä"

    #maa -> maata / yö -> yötä
    elif word[-1] in all_vowels:
        if word[-2] in basic_vowels and not any(vowel in word for vowel in changing_vowels) and word[-2:] not in ("ie"):
            word += "ta"
        else:
            word += "tä"

    elif word[-1] not in all_vowels and word[-2] != "u":
        if any(vowel in word[-6:] for vowel in neutral_vowels) and not any(vowel in word[-6:] for vowel in neutralising_vowels):
            word += "tä" 

        elif any(vowel in word[-6:] for vowel in changing_vowels):
            word += "tä" 
        else: 
            word += "ta"

    #tatar -> tatarta
    elif word[-1] not in all_vowels:
        if word[-2] in basic_vowels and not any(vowel in word for vowel in changing_vowels):
            word += "ta"
        else:
            word += "tä"
    #A word ends in a consonant or a relic consonant, the partitive stem ends in a consonant, 
    # and the strong-grade plural stem ends in a diphthong.



    return word
 
def process_the_word_and_find_partitive (word:str, sg_pl:str) -> str:
    if sg_pl == "both":
        x = random.randint(1,2)
        if x % 2 == 0:
            wanted_partitive = partitive_sg(word)
     
        else:
            wanted_partitive = partitive_pl(word)

    elif sg_pl == "singular":
        wanted_partitive = partitive_sg(word)

    elif sg_pl == "plural":
        wanted_partitive = partitive_pl(word)

    
    return wanted_partitive

def main():
    print("\n\nWelcome!\nIn this little program you can practice your Finnish.\n\nLet's start with the question...\n")
    while True:
        try: 
            pl_or_sg_part = input("Do you want to practive partitive (s)ingular or (p)lural or (b)oth? ")
            if pl_or_sg_part in ("s","p","b"):
                break
            else: 
                print("\nThat is not correct input, please type in s or p and press enter!\n")
        except ValueError:
            print("\nPlease type in only s or p and press enter!")


    while True:
        try: 
            lenght_of_excercise = int(input("How many excercises do you want? "))
            break
        except ValueError:
            print("\nThat is not correct input, please type in number, like 5 or 10!\n")

    print("\nRemember - You can always exit the program by just pressing enter, if you want to practice random word, type (r)")
    type_of_exercise = sg_pl(pl_or_sg_part)


    i = 1
    correct = 0
    wrong = 0
    wrong_words = []
    try:
        with open("practiced_words.txt", "r") as my_file:
            words = [line.strip() for line in my_file if line.strip()]
    except FileNotFoundError:
        words = []

    while lenght_of_excercise >= i:
        print(f"\n{i}. exercise:")

        word_to_practice = input(
            "Write any Finnish word you want to practice for forming the partitive (don't forget the umlaut!): "
        )

        if word_to_practice == "":
            break

        elif word_to_practice == "r":
            if words:
                word_to_practice = random.choice(words)
                print(f"Random word: {word_to_practice}")
            else:
                print("No practiced words saved yet.")
                continue

        else:
            if word_to_practice not in words and len(word_to_practice) < 20:
                with open("practiced_words.txt", "a") as my_file:
                    my_file.write(word_to_practice + "\n")
                words.append(word_to_practice)

        if type_of_exercise == "both":
            current_type = random.choice(["singular", "plural"])
        else:
            current_type = type_of_exercise

        if current_type == "singular":
            partitive = partitive_sg(word_to_practice)
        else:
            partitive = partitive_pl(word_to_practice)


        word_in_partitive = input(f"Please write the {current_type} partitive form of the word {word_to_practice}, don't forget the umlaut!: ")
            #WORK IN PROGRESS
        if partitive == word_in_partitive:
            print("\nYes, that is correct! Amazing job!")
            correct += 1
        else:
            while True:
                print(f"\nUnfortunatelly that is not correct.\n\nIf you want to try it again, write your new answer\nIf you want to just see the right answer, press Enter ")

                word_in_partitive = input(f"\nPlease write the {current_type} partitive form of the word {word_to_practice}, don't forget the umlaut!: ")
                if word_in_partitive == "":
                    print(f"\nThe right answer is {partitive}.")
                    exit = input("\nPress Enter to continue practicing. ")
                    if exit == "":
                        break
                if partitive == word_in_partitive:
                    print("\nYes, that is correct! You corrected yourself!")
                    break
            wrong += 1
            wrong_words.append(word_to_practice)
        i += 1

    print(f"\nOut of {lenght_of_excercise} exercises were {(correct/lenght_of_excercise)*100:.2f} % correct and {(wrong/lenght_of_excercise)*100:.2f} % wrong.")
    if len(wrong_words)> 0:
        decision = input("Do you want to practice the words you had wrong? (y)es or (n)o? ")
        if decision == "y":
            while len(wrong_words) > 0:
                random.shuffle(wrong_words)
                word_to_practice = wrong_words.pop()
                print(f"\nTry this word again: {word_to_practice}")
                if type_of_exercise == "both":
                    current_type = random.choice(["singular", "plural"])
                else:
                    current_type = type_of_exercise

                if current_type == "singular":
                    partitive = partitive_sg(word_to_practice)
                else:
                    partitive = partitive_pl(word_to_practice)

                word_in_partitive = input(f"Please write the {current_type} partitive form of the word {word_to_practice}, don't forget the umlaut!: ")

                if partitive == word_in_partitive:
                    print("\nYes, that is correct! Amazing job!")

                else:
                    print(f"\nUnfortunately that is not correct, the right answer is {partitive}.")
    again = (input("\nDo you want to practice more? (y)es or (n)o? "))
    if again == "y":
        print("Okay! Lets practice a bit more!")
        main()
    else:
                     
        print("\nThat's everything for today, thanks for using my short program!\nMichael Beneš, author of the program\n")
            #All thanks to my beautiful girlfriend Maria that helped me with this program <3
        while True:
            end = input("Press enter to exit the program")
            if end == "":
                break



def run_tests():
    print("\n--- RUNNING TESTS ---\n")

    tests_sg = {
    # --- CLOTHING & ACCESSORIES ---
    "vaate": "vaatetta", "paita": "paitaa", "hame": "hametta", "mekko": "mekkoa", "takki": "takkia",
    "hattu": "hattua", "pipo": "pipoa", "käsine": "käsinettä", "sukka": "sukkaa", "kenkä": "kenkää",
    "saapas": "saapasta", "vyö": "vyötä", "huivi": "huivia", "solmio": "solmiota", "puku": "pukua",
    "tasku": "taskua", "nappi": "nappia", "vetoketju": "vetoketjua", "sateenvarjo": "sateenvarjoa",
    "laukku": "laukkua", "reppu": "reppua", "lompakko": "lompakkoa", "sormus": "sormusta",
    "kaulakoru": "kaulakorua", "rannekello": "rannekelloa", "pusero": "puseroa", "huppari": "hupparia",
    "neule": "neuletta", "liivi": "liiviä", "yöpaita": "yöpaitaa", "kravatti": "kravattia",
    "rusetti": "rusettia", "kaulaliina": "kaulaliinaa", "lapanen": "lapasta", "sormikas": "sormikasta",
    "sandaali": "sandaalia", "tohveli": "tohvelia", "kumisaapas": "kumisaapasta", "solki": "solkea",
    "hihna": "hihnaa", "hiha": "hihaa", "lahje": "lahjetta", "kaulus": "kaulusta", "henkseli": "henkseliä",
    "uimapuku": "uimapukua", "viitta": "viittaa", "otsanauha": "otsanauhaa", "rintakoru": "rintakorua",
    "lippalakki": "lippalakkia", "baretti": "barettia", "turkki": "turkkia", "lenkkari": "lenkkaria",

    # --- ABSTRACT & MASS NOUNS ---
    "vesi": "vettä", "rakkaus": "rakkautta", "onni": "onnea", "ilma": "ilmaa",
    "lumi": "lunta", "hiekka": "hiekkaa", "multa": "multaa", "ruoka": "ruokaa",
    "juoma": "juomaa", "maito": "maitoa", "kahvi": "kahvia", "tee": "teetä",
    "viini": "viiniä", "mehu": "mehua", "veri": "verta",
    "rauta": "rautaa", "kulta": "kultaa", "hopea": "hopeaa", "kupari": "kuparia",
    "öljy": "öljyä", "sokeri": "sokeria", "suola": "suolaa", "jauho": "jauhoa",
    "hunaja": "hunajaa", "liha": "lihaa", "apu": "apua", "voima": "voimaa",
    "valo": "valoa", "pimeys": "pimeyttä", "lämpö": "lämpöä", "kylmyys": "kylmyyttä",
    "aika": "aikaa", "elämä": "elämää", "kuolema": "kuolemaa", "toivo": "toivoa",
    "pelko": "pelkoa", "viha": "vihaa", "suru": "surua", "ilo": "iloa",
    "rauha": "rauhaa", "sota": "sotaa", "vapaus": "vapautta", "totuus": "totuutta",
    "valhe": "valhetta", "tieto": "tietoa", "taito": "taitoa", "usko": "uskoa",

    # --- ADJECTIVES ---
    "suuri": "suurta", "pieni": "pientä", "pitkä": "pitkää", "lyhyt": "lyhyttä",
    "paksu": "paksua", "ohut": "ohutta", "leveä": "leveää", "kapea": "kapeaa",
    "uusi": "uutta", "vanha": "vanhaa", "nuori": "nuorta", "rikas": "rikasta",
    "köyhä": "köyhää", "kaunis": "kaunista", "ruma": "rumaa", "hyvä": "hyvää",
    "paha": "pahaa", "iloinen": "iloista", "surullinen": "surullista", "viisas": "viisasta",
    "tyhmä": "tyhmää", "vahva": "vahvaa", "heikko": "heikkoa", "nopea": "nopeaa",
    "hidas": "hidasta", "kuuma": "kuumaa", "kylmä": "kylmää", "lämmin": "lämmintä",
    "viileä": "viileää", "kuiva": "kuivaa", "märkä": "märkää", "kova": "kovaa",
    "pehmeä": "pehmeää", "kallis": "kallista", "halpa": "halpaa", "painava": "painavaa",
    "kevyt": "kevyttä", "pimeä": "pimeää", "kirkas": "kirkasta", "puhdas": "puhdasta",
    "likainen": "likaista", "täysi": "täyttä", "tyhjä": "tyhjää", "terve": "tervettä",
    "sairas": "sairasta", "rehellinen": "rehellistä", "hauska": "hauskaa", "tylsä": "tylsää",
    "outo": "outoa", "tavallinen": "tavallista", "erilainen": "erilaista",
    "punainen": "punaista", "sininen": "sinistä", "vihreä": "vihreää", "keltainen": "keltaista",
    "musta": "mustaa", "valkoinen": "valkoista", "harmaa": "harmaata", "ruskea": "ruskeaa",
    "oranssi": "oranssia", "violetti": "violettia", "vaaleanpunainen": "vaaleanpunaista",

    # --- ANIMALS ---
    "orava": "oravaa", "siili": "siiliä", "hirvi": "hirveä", "peura": "peuraa", "karitsa": "karitsaa",
    "vuohi": "vuohta", "ankka": "ankkaa", "hanhi": "hanhea", "kana": "kanaa", "kukko": "kukkoa",
    "pöllö": "pöllöä", "kotka": "kotkaa", "varis": "varista", "harakka": "harakkaa", "pääskynen": "pääskystä",
    "muurahainen": "muurahaista", "mehiläinen": "mehiläistä", "hämähäkki": "hämähäkkiä", "itikka": "itikkaa",
    "perhonen": "perhosta", "valas": "valasta", "hylje": "hyljettä", "rapu": "rapua", "etana": "etanaa",
    "koira": "koiraa", "kissa": "kissaa", "hevonen": "hevosta", "lehmä": "lehmää", "lammas": "lammasta",
    "sika": "sikaa", "karhu": "karhua", "susi": "sutta", "kettu": "kettua", "jänis": "jänistä",
    "lintu": "lintua", "kala": "kalaa", "käärme": "käärmettä", "hyönteinen": "hyönteistä", "puu": "puuta",
    "kukka": "kukkaa", "metsä": "metsää", "järvi": "järveä", "meri": "merta", "joki": "jokea",
    "vuori": "vuorta", "mäki": "mäkeä", "saari": "saarta", "niemi": "niemeä", "ranta": "rantaa",
    "taivas": "taivasta", "aurinko": "aurinkoa", "kuu": "kuuta", "tähti": "tähteä", "pilvi": "pilveä",
    "ukkonen": "ukkosta", "kivi": "kiveä", "lehti": "lehteä", "oksa": "oksaa", "juuri": "juurta",
    "marja": "marjaa", "sieni": "sientä", "puro": "puroa", "lähde": "lähdettä", "tunturi": "tunturia",
    "ilves": "ilvestä", "poro": "poroa", "myyrä": "myyrää", "lepakko": "lepakkoa", "joutsen": "joutsenta",
    "sorsa": "sorsaa", "lokki": "lokkia", "tikka": "tikkaa", "kimalainen": "kimalaista",
    "kärpänen": "kärpästä", "mato": "matoa", "sammakko": "sammakkoa", "sisilisko": "sisiliskoa", "koivu": "koivua",
    "mänty": "mäntyä", "kuusi": "kuusta", "tammi": "tammea", "vaahtera": "vaahteraa", "pihlaja": "pihlajaa",
    "kanto": "kantoa", "neulanen": "neulasta", "käpy": "käpyä", "oja": "ojaa", "lampi": "lampea",
    "lahti": "lahtea", "salmi": "salmea", "koski": "koskea", "vesiputous": "vesiputousta",
    "jyrkänne": "jyrkännettä", "huippu": "huippua", "rinne": "rinnettä", "laakso": "laaksoa", "kyy": "kyytä",
    "ahven": "ahventa", "hauki": "haukea", "lohi": "lohta", "tiikeri": "tiikeriä", "leijona": "leijonaa",
    "norsu": "norsua", "kirahvi": "kirahvia", "apina": "apinaa", "seepra": "seepraa",
    "krokotiili": "krokotiilia", "kilpikonna": "kilpikonnaa", "pingviini": "pingviiniä", "kameli": "kamelia",

    # --- BODY PARTS ---
    "pää": "päätä", "silmä": "silmää", "korva": "korvaa", "nenä": "nenää", "suu": "suuta",
    "huuli": "huulta", "hammas": "hammasta", "kieli": "kieltä", "kaula": "kaulaa", "kurkku": "kurkkua",
    "olkapää": "olkapäätä", "käsivarsi": "käsivartta", "käsi": "kättä", "sormi": "sormea", "kynsi": "kynttä",
    "rinta": "rintaa", "vatsa": "vatsaa", "selkä": "selkää", "jalka": "jalkaa", "polvi": "polvea",
    "varvas": "varvasta", "iho": "ihoa", "luu": "luuta", "sydän": "sydäntä", "keuhko": "keuhkoa",
    "lihas": "lihasta", "naama": "naamaa", "maksa": "maksaa", "munuainen": "munuaista", "nivel": "niveltä",
    "verisuoni": "verisuonta", "hermo": "hermoa", "otsa": "otsaa", "leuka": "leukaa",
    "poski": "poskea", "kulmakarva": "kulmakarvaa", "ripsi": "ripseä", "napa": "napaa",
    "vyötärö": "vyötäröä", "kyynärpää": "kyynärpäätä", "ranne": "rannetta", "kämmen": "kämmentä",
    "lantio": "lantiota", "reisi": "reittä", "pohje": "pohjetta", "nilkka": "nilkkaa", "kantapää": "kantapäätä",

    # --- HOUSE & OBJECTS ---
    "talo": "taloa", "koti": "kotia", "asunto": "asuntoa", "huone": "huonetta", "keittiö": "keittiötä",
    "kylpyhuone": "kylpyhuonetta", "makuuhuone": "makuuhuonetta", "olohuone": "olohuonetta", "eteinen": "eteistä",
    "parveke": "parveketta", "piha": "pihaa", "ovi": "ovea", "ikkuna": "ikkunaa", "seinä": "seinää",
    "katto": "kattoa", "lattia": "lattiaa", "porras": "porrasta", "lukko": "lukkoa", "avain": "avainta",
    "pöytä": "pöytää", "tuoli": "tuolia", "sänky": "sänkyä", "sohva": "sohvaa", "kaappi": "kaappia",
    "hylly": "hyllyä", "lamppu": "lamppua", "matto": "mattoa", "verho": "verhoa", "peili": "peiliä",
    "taulu": "taulua", "kello": "kelloa", "radio": "radiota", "televisio": "televisiota",
    "tietokone": "tietokonetta", "puhelin": "puhelinta", "kone": "konetta", "uuni": "uunia",
    "hella": "hellaa", "allas": "allasta", "lautanen": "lautasta", "kulho": "kulhoa", "muki": "mukia",
    "kuppi": "kuppia", "veitsi": "veistä", "haarukka": "haarukkaa", "lusikka": "lusikkaa", "kattila": "kattilaa",
    "pannu": "pannua", "astianpesukone": "astianpesukonetta", "pyykinpesukone": "pyykinpesukonetta",
    "pakastin": "pakastinta", "mikroaaltouuni": "mikroaaltouunia", "leivänpaahdin": "leivänpaahdinta",
    "vedenkeitin": "vedenkeitintä", "tehosekoitin": "tehosekoitinta", "vatkain": "vatkainta", "kahvinkeitin": "kahvinkeitintä",
    "imuri": "imuria", "silitysrauta": "silitysrautaa", "laatikko": "laatikkoa", "tiskiallas": "tiskiallasta",
    "hana": "hanaa", "roskakori": "roskakoria", "tiskiharja": "tiskiharjaa", "sieni": "sientä",
    "liina": "liinaa", "tyyny": "tyynyä", "peitto": "peittoa", "lakana": "lakanaa", "pyyhe": "pyyhettä",
    "henkari": "henkaria", "kampa": "kampaa", "hammasharja": "hammasharjaa", "vasara": "vasaraa",
    "saha": "sahaa", "ruuvimeisseli": "ruuvimeisseliä", "naula": "naulaa", "ruuvi": "ruuvia",
    "ämpäri": "ämpäriä", "harja": "harjaa", "luuta": "luutaa", "lapio": "lapiota", "akku": "akkua",
    "johto": "johtoa", "pistorasia": "pistorasiaa", "sytytin": "sytytintä", "kynttilä": "kynttilää",
    "taskulamppu": "taskulamppua", "mutteri": "mutteria", "porakone": "porakonetta", "pultti": "pulttia",
    "jakkara": "jakkaraa", "nojatuoli": "nojatuolia", "kirjahylly": "kirjahyllyä", "lipasto": "lipastoa",

    # --- FOOD ---
    "makkara": "makkaraa", "peruna": "perunaa", "vihannes": "vihannesta", "hedelmä": "hedelmää",
    "omena": "omenaa", "banaani": "banaania", "sipuli": "sipulia", "valkosipuli": "valkosipulia",
    "porkkana": "porkkanaa", "kurkku": "kurkkua", "tomaatti": "tomaattia", "paprika": "paprikaa",
    "salaatti": "salaattia", "kaali": "kaalia", "herne": "hernettä", "papu": "papua", "maissi": "maissia",
    "päärynä": "päärynää", "luumu": "luumua", "viinirypäle": "viinirypälettä", "mansikka": "mansikkaa",
    "mustikka": "mustikkaa", "vadelma": "vadelmaa", "sitruuna": "sitruunaa", "appelsiini": "appelsiinia",
    "pähkinä": "pähkinää", "siemen": "siementä", "leivonnainen": "leivonnaista", "kakku": "kakkua", "keksi": "keksiä",
    "leipä": "leipää", "sämpylä": "sämpylää", "piirakka": "piirakkaa", "munkki": "munkkia", "pulla": "pullaa",

    # --- TRANSPORT & CITY ---
    "auto": "autoa", "bussi": "bussia", "juna": "junaa", "lentokone": "lentokonetta", "laiva": "laivaa",
    "vene": "venettä", "pyörä": "pyörää", "moottoripyörä": "moottoripyörää", "tie": "tietä",
    "katu": "katua", "polku": "polkua", "silta": "siltaa", "tunneli": "tunnelia", "asema": "asemaa",
    "satama": "satamaa", "tori": "toria", "puisto": "puistoa", "kaupunki": "kaupunkia", "kylä": "kylää",
    "kauppa": "kauppaa", "pankki": "pankkia", "sairaala": "sairaalaa", "koulu": "koulua",
    "kirkko": "kirkkoa", "tehdas": "tehdasta", "hotelli": "hotellia", "ravintola": "ravintolaa",
    "kahvila": "kahvilaa", "museo": "museota", "kirjasto": "kirjastoa", "teatteri": "teatteria",
    "apteekki": "apteekkia", "lentokenttä": "lentokenttää", "laituri": "laituria", "rekka": "rekkaa",

    # --- WORK & MEDIA ---
    "opiskelija": "opiskelijaa", "opettaja": "opettajaa", "rehtori": "rehtoria", "luokka": "luokkaa",
    "kurssi": "kurssia", "koe": "koetta", "arvosana": "arvosanaa", "kynä": "kynää",
    "lyijykynä": "lyijykynää", "pyyhekumi": "pyyhekumia", "viivatin": "viivatinta", "vihko": "vihkoa",
    "kirja": "kirjaa", "sanakirja": "sanakirjaa", "ammatti": "ammattia", "kokous": "kokousta",
    "sopimus": "sopimusta", "asiakas": "asiakasta", "pomo": "pomoa", "työpaikka": "työpaikkaa",
    "yritys": "yritystä", "sanomalehti": "sanomalehteä", "aikakauslehti": "aikakauslehteä",
    "mainos": "mainosta", "näyttö": "näyttöä", "näppäimistö": "näppäimistöä", "hiiri": "hiirtä",
    "tulostin": "tulostinta", "laturi": "laturia", "kaapeli": "kaapelia", "kaiutin": "kaiutinta",
    "sovellus": "sovellusta", "tiedosto": "tiedostoa", "kansio": "kansiota", "salasana": "salasanaa",
    "viesti": "viestiä", "lasku": "laskua", "kuitti": "kuittia", "allekirjoitus": "allekirjoitusta",

    # --- TIME ---
    "sekunti": "sekuntia", "minuutti": "minuuttia", "tunti": "tuntia", "päivä": "päivää", "viikko": "viikkoa",
    "kuukausi": "kuukautta", "vuosi": "vuotta", "vuosisata": "vuosisataa", "aamu": "aamua",
    "ilta": "iltaa", "yö": "yötä", "maanantai": "maanantaita", "tiistai": "tiistaita",
    "keskiviikko": "keskiviikkoa", "torstai": "torstaita", "perjantai": "perjantaita",
    "lauantai": "lauantaita", "sunnuntai": "sunnuntaita", "numero": "numeroa", "hetki": "hetkeä",

    # --- INSTRUMENTS ---
    "kitara": "kitaraa", "piano": "pianoa", "viulu": "viulua", "rumpu": "rumpua", "huilu": "huilua",
    "trumpetti": "trumpettia", "basso": "bassoa", "haitari": "haitaria",
    "saksofoni": "saksofonia", "kantele": "kanteletta",

    # --- PROFESSIONS ---
    "lääkäri": "lääkäriä", "hoitaja": "hoitajaa", "poliisi": "poliisia", "palomies": "palomiestä",
    "lentäjä": "lentäjää", "kokki": "kokkia", "tarjoilija": "tarjoilijaa", "myyjä": "myyjää",
    "insinööri": "insinööriä", "arkkitehti": "arkkitehtia", "taiteilija": "taiteilijaa",
    "muusikko": "muusikkoa", "kirjailija": "kirjailijaa", "lakimies": "lakimiestä", "tuomari": "tuomaria",
    "pappi": "pappia", "siivooja": "siivoojaa", "mekaanikko": "mekaanikkoa", "leipuri": "leipuria",

    # --- MISC ---
    "esine": "esinettä", "kappale": "kappaletta", "osa": "osaa", "ryhmä": "ryhmää",
    "joukko": "joukkoa", "pino": "pinoa", "kasa": "kasaa", "rivi": "riviä",
    "jono": "jonoa", "aukko": "aukkoa", "reikä": "reikää", "rako": "rakoa",
    "pinta": "pintaa", "reuna": "reunaa", "kulma": "kulmaa", "ympyrä": "ympyrää",
    "viiva": "viivaa", "piste": "pistettä", "merkki": "merkkiä", "kuva": "kuvaa",
    "ääni": "ääntä", "haju": "hajua", "maku": "makua", "tunne": "tunnetta", "veli":"veljeä","metsä": "metsää",
    "takki": "takkia",
    "hattu": "hattua",
    "pipo": "pipoa",
    "hansikas": "hansikasta",
    "laukku": "laukkua",
    "vyö": "vyötä",
    "kaulaliina": "kaulaliinaa",
    "sandaali": "sandaalia",
    "saapas": "saapasta",
    "purje": "purjetta",
    "vene": "venettä",
    "laituri": "laituria",
    "ankkuri": "ankkuria",
    "moottori": "moottoria",
    "polkupyörä": "polkupyörää",
    "autonrengas": "autonrengasta",
    "vaihde": "vaihdetta",
    "ohjauspyörä": "ohjauspyörää",
    "turvavyö": "turvavyötä",
    "kypärä": "kypärää",
    "selkälaukku": "selkälaukkua",
    "reppu": "reppua",
    "makuupussi": "makuupussia",
    "teltta": "telttaa",
    "retki": "retkeä",
    "vaellus": "vaellusta",
    "metsästys": "metsästystä",
    "kalastus": "kalastusta",
    "marjastus": "marjastusta",
    "sienestys": "sienestystä",
    "laavu": "laavua",
    "tuli": "tulta",
    "grilli": "grilliä",
    "nuotio": "nuotiota",
    "retkikeitin": "retkikeitintä",
    "termospullo": "termospulloa",
    "eväs": "evästä",
    "leipäpala": "leipäpalaa",
    "juustoviipale": "juustoviipaletta",
    "makkarapala": "makkarapalaa",
    "hedelmäviipale": "hedelmäviipaletta",
    "karkki": "karkkia",
    "keksipala": "keksipalaa",
    "pähkinä": "pähkinää",
    "siemen": "siementä",
    "lapio": "lapiota",
    "harava": "haravaa",
    "kottikärry": "kottikärryä",
    "kastelukannu": "kastelukannua",
    "ruukku": "ruukkua",
    "kukkaruukku": "kukkaruukkua",
    "kukkapenkki": "kukkapenkkiä",
    "nurmi": "nurmea",
    "pensasaita": "pensasaitaa",
    "puuvaja": "puuvajaa",
    "häkki": "häkkiä",
    "lintulaite": "lintulaitetta",
    "lintujenruoka": "lintujenruokaa",
    "mehiläispesä": "mehiläispesää",
    "maalaus": "maalausta",
    "veistos": "veistosta",
    "valokuvaus": "valokuvausta",
    "muotokuva": "muotokuvaa",
    "taide-esine": "taide-esinettä",
    "näyttelytila": "näyttelytilaa",
    "soitin": "soitinta",
    "kitara": "kitaraa",
    "piano": "pianoa",
    "rumpu": "rumpua",
    "viulu": "viulua",
    "sello": "selloa",
    "klarinetti": "klarinettia",
    "saksofoni": "saksofonia",
    "trumpetti": "trumpettia",
    "syntetisaattori": "syntetisaattoria",
    "mikrofoni": "mikrofonia",
    "kaiutin": "kaiutinta",
    "äänentoisto": "äänentoistoa",
    "kuuntelulaite": "kuuntelulaitetta",
    "soittotunti": "soittotuntia",
    "konsertti": "konserttia",
    "festivaali": "festivaalia",
    "elokuvanäytös": "elokuvanäytöstä",
    "teatterinäytös": "teatterinäytöstä",
    "kirjallisuus": "kirjallisuutta",
    "runoelma": "runoelmaa",
    "novelli": "novellia",
    "tarina": "tarinaa",
    "opas": "opasta",
    "kartta": "karttaa",
    "matkaopas": "matkaopasta",
    "kaupunkikartta": "kaupunkikarttaa",
    "maailmankartta": "maailmankarttaa",
    "aurinkolasi": "aurinkolasia",
    "t-paita": "t-paitaa",
    "sukka": "sukkaa",
    "nahkalaukku": "nahkalaukkua",
    "sormus": "sormusta",
    "kaulakoru": "kaulakorua",
    "rannekoru": "rannekorua",
    "tyyny": "tyynyä",
    "peitto": "peittoa",
    "makuuhuone": "makuuhuonetta",
    "olohuone": "olohuonetta",
    "keittiö": "keittiötä",
    "vessa": "vessaa",
    "sauna": "saunaa",
    "terassi": "terassia",
    "parveke": "parveketta",
    "piha": "pihaa",
    "joki": "jokea",
    "lammas": "lammasta",
    "vuori": "vuorta",
    "saari": "saarta",
    "kaupunki": "kaupunkia",
    "talo": "taloa",
    "koira": "koiraa",
    "kissa": "kissaa",
    "omena": "omenaa",
    "puu": "puuta",
    "lapsi": "lasta",
    "vesi": "vettä",
    "koulu": "koulua",
    "kala": "kalaa",
    "puhelin": "puhelinta",
    "tietokone": "tietokonetta",
    "kauppa": "kauppaa",
    "penkki": "penkkiä",
    "ikkuna": "ikkunaa",
    "ovi": "ovea",
    "kirjasto": "kirjastoa",
    "puisto": "puistoa",
    "tie": "tietä",
    "juna": "junaa",
    "laiva": "laivaa",
    "silta": "siltaa",
    "kukka": "kukkaa",
    "banaani": "banaania",
    "juusto": "juustoa",
    "leipä": "leipää",
    "liha": "lihaa",
    "suklaa": "suklaata",
    "maito": "maitoa",
    "kahvi": "kahvia",
    "tee": "teetä",
    "suola": "suolaa",
    "sokeri": "sokeria",
    "hattu": "hattua",
    "paita": "paitaa",
    "takki": "takkia",
    "sukka": "sukkaa",
    "lippu": "lippua",
    "raha": "rahaa",
    "pöytä": "pöytää",
    "tuoli": "tuolia",
    "lamppu": "lamppua",
    "kirje": "kirjettä",
    "lehti": "lehteä",
    "aika": "aikaa",
    "päivä": "päivää",
    "viikko": "viikkoa",
    "kuukausi": "kuukautta",
    "vuosi": "vuotta",
    "hetki": "hetkeä",
    "uni": "unta",
    "sana": "sanaa",
    "lause": "lausetta",
    "kirjain": "kirjainta",
    "numero": "numeroa",
    "symboli": "symbolia",
    "väri": "väriä",
    "musiikki": "musiikkia",
    "laulu": "laulua",
    "runous": "runoutta",
    "elokuva": "elokuvaa",
    "näytelmä": "näytelmää",
    "taulu": "taulua",
    "kuva": "kuvaa",
    "valokuva": "valokuvaa",
    "auto": "autoa",
    "pyörä": "pyörää",
    "vene": "venettä",
    "lumi": "lunta",
    "jää": "jäätä",
    "tuli": "tulta",
    "sade": "sadetta",
    "tuuli": "tuulta",
    "aurinko": "aurinkoa",
    "kuu": "kuuta",
    "tähti": "tähteä",
    "pilvi": "pilveä",
    "meri": "merta",
    "järvi": "järveä",
    "vuoristo": "vuoristoa",
    "kukka": "kukkaa",
    "marja": "marjaa",
    "hedelmä": "hedelmää",
    "juoma": "juomaa",
    "ruoka": "ruokaa",
    "lelu": "lelua",
    "kirja": "kirjaa",
    "taikina": "taikinaa",
    "kenguru": "kengurua",
    "siili": "siiliä",
    "orava": "oravaa",
    "karhu": "karhua",
    "peura": "peuraa",
    "jänis": "jänistä",
    "sieni": "sientä",
    "puu": "puuta",
    "kasvi": "kasvia",
    "puutarha": "puutarhaa",
    "metsästäjä": "metsästäjää",    "hiekka": "hiekkaa",
    "kivi": "kiveä",
    "sora": "soraa",
    "meri": "merta",
    "ranta": "rantaa",
    "saari": "saarta",
    "vuorijono": "vuorijonoa",
    "laakso": "laaksoa",
    "järvi": "järveä",
    "puro": "puroa",
    "koski": "koskea",
    "saaristo": "saaristoa",
    "pensas": "pensasta",
    "puutarha": "puutarhaa",
    "metsästäjä": "metsästäjää",
    "eläin": "eläintä",
    "lintu": "lintua",
    "hevonen": "hevosta",
    "lehmä": "lehmää",
    "sika": "sikaa",
    "lammas": "lammasta",
    "vuohi": "vuohta",
    "kana": "kanaa",
    "ankka": "ankkaa",
    "kalkkuna": "kalkkunaa",
    "kala": "kalaa",
    "rapu": "rapua",
    "simpukka": "simpukkaa",
    "äyriäinen": "äyriäistä",
    "omena": "omenaa",
    "banaani": "banaania",
    "appelsiini": "appelsiinia",
    "sitruuna": "sitruunaa",
    "mansikka": "mansikkaa",
    "vadelma": "vadelmaa",
    "herne": "hernettä",
    "peruna": "perunaa",
    "porkkana": "porkkanaa",
    "sipuli": "sipulia",
    "valkosipuli": "valkosipulia",
    "kurkku": "kurkkua",
    "tomaatti": "tomaattia",
    "paprika": "paprikaa",
    "kaali": "kaalia",
    "leipä": "leipää",
    "voileipä": "voileipää",
    "juusto": "juustoa",
    "makkara": "makkaraa",
    "liha": "lihaa",
    "kananmuna": "kananmunaa",
    "maito": "maitoa",
    "jogurtti": "jogurttia",
    "voi": "voita",
    "suklaa": "suklaata",
    "keksi": "keksiä",
    "kakku": "kakkua",
    "jäätelö": "jäätelöä",
    "kala": "kalaa",
    "keitto": "keittoa",
    "salaatti": "salaattia",
    "mehu": "mehua",
    "kahvi": "kahvia",
    "tee": "teetä",
    "limonadi": "limonadia",
    "vesi": "vettä",
    "sokeri": "sokeria",
    "suola": "suolaa",
    "pippuri": "pippuria",
    "mauste": "maustetta",
    "pöytä": "pöytää",
    "tuoli": "tuolia",
    "sohva": "sohvaa",
    "vuode": "vuodetta",
    "peitto": "peittoa",
    "tyyny": "tyynyä",
    "matto": "mattoa",
    "lamppu": "lamppua",
    "valaisin": "valaisinta",
    "ovi": "ovea",
    "ikkuna": "ikkunaa",
    "kaappi": "kaappia",
    "hylly": "hyllyä",
    "kirjahylly": "kirjahyllyä",
    "kirja": "kirjaa",
    "lehmä": "lehmää",
    "kirje": "kirjettä",
    "postimerkki": "postimerkkiä",
    "sanomalehti": "sanomalehteä",
    "lehti": "lehteä",
    "päivä": "päivää",
    "viikko": "viikkoa",
    "kuukausi": "kuukautta",
    "vuosi": "vuotta",
    "aika": "aikaa",
    "hetki": "hetkeä",
    "unelma": "unelmaa",
    "ajatus": "ajatusta",
    "tunne": "tunnetta",
    "ilo": "iloa",
    "suru": "surua",
    "rakkaus": "rakkautta",
    "viha": "vihaa",
    "pelko": "pelkoa",
    "toivo": "toivoa",
    "usko": "uskoa",
    "onnistuminen": "onnistumista",
    "epäonnistuminen": "epäonnistumista",
"metsä":"metsää",
"joki":"jokea",
"lammas":"lammasta",
"vuori":"vuorta",
"saari":"saarta",
"kaupunki":"kaupunkia",
"puutarha":"puutarhaa",
"opiskelija":"opiskelijaa",
"laulaja":"laulajaa",
"kirjasto":"kirjastoa",
"koulu":"koulua",
"ruoka":"ruokaa",
"juoma":"juomaa",
"kahvila":"kahvilaa",
"ravintola":"ravintolaa",
"hotelli":"hotellia",
"matkustaja":"matkustajaa",
"lento":"lentoa",
"asema":"asemaa",
"linja-auto":"linja-autoa",
"lentokenttä":"lentokenttää",
"tietokone":"tietokonetta",
"puhelin":"puhelinta",
"sähköposti":"sähköpostia",
"verkkosivu":"verkkosivua",
"kirje":"kirjettä",
"laite":"laitetta",
"huone":"huonetta",
"kone":"konetta",
"työhuone":"työhuonetta",
"perhe":"perhettä",
"lapsi":"lasta",
"ystävä":"ystävää",
"naapuri":"naapuria",
"opettaja":"opettajaa",
"johtaja":"johtajaa",
"pelaaja":"pelaajaa",
"kirjailija":"kirjailijaa",
"lukija":"lukijaa",
"kuuntelija":"kuuntelijaa",
"pankki":"pankkia",
"merkki":"merkkiä",
"hylly":"hyllyä",
"katto":"kattoa",
"tori":"toria",
"meri":"merta",
"veri":"verta",
"uni":"unta",
"onni":"onnea",
"peli":"peliä",
"laki":"lakia",
"sää":"säätä",
"tie":"tietä",
"yö":"yötä",
"historia":"historiaa",
"taide":"taidetta",
"musiikki":"musiikkia",
"fysiikka":"fysiikkaa",
"ajatus":"ajatusta",
"kysymys":"kysymystä",
"vastaus":"vastausta",
"kokemus":"kokemusta",
"elämys":"elämystä",
"päivä":"päivää",
"viikko":"viikkoa",
"kuukausi":"kuukautta",
"vuosi":"vuotta",
"hetki":"hetkeä",
"aika":"aikaa",
"tapahtuma":"tapahtumaa",
"projekti":"projektia",
"tehtävä":"tehtävää",
"harjoitus":"harjoitusta",
"kirjahylly":"kirjahyllyä",
"tietokoneohjelma":"tietokoneohjelmaa",
"ravintolaketju":"ravintolaketjua",
"kauppakeskus":"kauppakeskusta",
"linja-autoasema":"linja-autoasemaa",
"rautatieasema":"rautatieasemaa",
"kaupunki":"kaupunkia",
"maalaiskylä":"maalaiskylää",
"taimitarha":"taimitarhaa",
"museo":"museota",
"teatteri":"teatteria",
"elokuva":"elokuvaa",
"näyttely":"näyttelyä",
"kirjallinen":"kirjallista",
"yliopisto":"yliopistoa",
"ammattikoulu":"ammattikoulua",
"päiväkoti":"päiväkotia",
"kouluvierailu":"kouluvierailua",
"matkakohde":"matkakohdetta",
"lomamatka":"lomamatkaa",
"tehtaanrakennus":"tehtaanrakennusta",
"puutarhakaluste":"puutarhakalustetta",
"pöytäliina":"pöytäliinaa",
"ruokapöytä":"ruokapöytää",
"keittiö":"keittiötä",
"olohuone":"olohuonetta",
"makuuhuone":"makuuhuonetta",
"vaatekaappi":"vaatekaappia",
"kenkäkaappi":"kenkäkaappia",
"lastenhuone":"lastenhuonetta",
"vessa":"vessaa",
"sauna":"saunaa",
"terassi":"terassia",
"parveke":"parveketta",
"piha":"pihaa",
"puutarha":"puutarhaa",
"kasvihuone":"kasvihuonetta",
"laituri":"laituria",
"vene":"venettä",
"laiva":"laivaa",
"juna":"junaa",
"bussi":"bussia",
"auto":"autoa",
"pyörä":"pyörää",
"moottoripyörä":"moottoripyörää",
"lentokone":"lentokonetta",
"taksi":"taksia",
"hevonen":"hevosta",
"lehmä":"lehmää","sika":"sikaa","lammas":"lammasta","kana":"kanaa",
"koira":"koiraa","kissa":"kissaa","hamsteri":"hamsteria",
"papukaija":"papukaijaa","akvaario":"akvaariota",
"lämmitin":"lämmitintä","jäähdytin":"jäähdytintä",
    "talo":"taloa","kukka":"kukkaa","kenkä":"kenkää","leipä":"leipää","maa":"maata",
    "puu":"puuta","tie":"tietä","yö":"yötä","koulu":"koulua","omena":"omenaa",
    "kirja":"kirjaa","kala":"kalaa","tyttö":"tyttöä","lapsi":"lasta","mies":"miestä",
    "nainen":"naista","rikas":"rikasta","kaunis":"kaunista","järvi":"järveä","kivi":"kiveä",
    "käsi":"kättä","vesi":"vettä","kieli":"kieltä","ahven":"ahventa","perhe":"perhettä",
    "ystävä":"ystävää","opettaja":"opettajaa","opiskelija":"opiskelijaa","auto":"autoa",
    "juna":"junaa","lentokone":"lentokonetta","kauppa":"kauppaa","kaupunki":"kaupunkia",
    "kylä":"kylää","sydän":"sydäntä","pöytä":"pöytää","tuoli":"tuolia","ovi":"ovea",
    "ikkuna":"ikkunaa","koira":"koiraa","kissa":"kissaa","hevonen":"hevosta","lintu":"lintua",
    "puhelin":"puhelinta","numero":"numeroa","kirjasto":"kirjastoa","sairaala":"sairaalaa",
    "ravintola":"ravintolaa","hotelli":"hotellia","työhuone":"työhuonetta","sähköposti":"sähköpostia",

    # i-type + consonant gradation
    "lumi":"lunta","susi":"sutta","kansi":"kantta","hirsi":"hirttä","varsi":"vartta",
    "veitsi":"veistä","kurki":"kurkea","särki":"särkeä","järki":"järkeä","merkki":"merkkiä",

    # -nen
    "ihminen":"ihmistä","suomalainen":"suomalaista","punainen":"punaista","sininen":"sinistä",

    # -us / -ys
    "rakkaus":"rakkautta","kauneus":"kauneutta","kysymys":"kysymystä","vastaus":"vastausta",

    # more variety
    "kirjekuori":"kirjekuorta","tietokone":"tietokonetta","vesipullo":"vesipulloa",
    "autokauppa":"autokauppaa","kirjahylly":"kirjahyllyä","koulukirja":"koulukirjaa",
    "talonmies":"talonmiestä","yövuoro":"yövuoroa","kesäloma":"kesälomaa","talvitakki":"talvitakkia",
    "pääkaupunki":"pääkaupunkia","linja-auto":"linja-autoa","sähköjohto":"sähköjohtoa",
    "puutarha":"puutarhaa","lentokenttä":"lentokenttää","vesihana":"vesihanaa",
    "kirjoituspöytä":"kirjoituspöytää","tietoverkko":"tietoverkkoa","matkapuhelin":"matkapuhelinta",
    "työpäivä":"työpäivää","opintotuki":"opintotukea","sähkölasku":"sähkölaskua",
    "pankkitili":"pankkitiliä","postilaatikko":"postilaatikkoa","sanomalehti":"sanomalehteä",
    "elokuvateatteri":"elokuvateatteria","kahvikuppi":"kahvikuppia","vesilasi":"vesilasia",
"paperi":"paperia","banaani":"banaania","appelsiini":"appelsiinia","kahvi":"kahvia",
"tee":"teetä","juusto":"juustoa","voi":"voita","sokeri":"sokeria","maito":"maitoa",
"vesipullo":"vesipulloa","kahvikuppi":"kahvikuppia","ruokalista":"ruokalistaa",

"ovi":"ovea","sormi":"sormea","polvi":"polvea","silmä":"silmää","hammas":"hammasta",
"jalka":"jalkaa","kävely":"kävelyä","hyppy":"hyppyä","lento":"lentoa",

"ystävällinen":"ystävällistä","iloinen":"iloista","surullinen":"surullista",
"kaunis":"kaunista","ruma":"rumaa","nopea":"nopeaa","hidas":"hidasta",

"kirje":"kirjettä","laite":"laitetta","huone":"huonetta","kone":"konetta",
"perhe":"perhettä","vene":"venettä","lause":"lausetta","alue":"aluetta",

"päivä":"päivää","viikko":"viikkoa","kuukausi":"kuukautta","vuosi":"vuotta",
"hetki":"hetkeä","aika":"aikaa",

"musiikki":"musiikkia","taide":"taidetta","historia":"historiaa","fysiikka":"fysiikkaa","opettaja":"opettajaa","johtaja":"johtajaa","pelaaja":"pelaajaa",

"kirjailija":"kirjailijaa","lukija":"lukijaa","kuuntelija":"kuuntelijaa",

"pankki":"pankkia","merkki":"merkkiä","hylly":"hyllyä","katto":"kattoa",

"tori":"toria","meri":"merta","veri":"verta","uni":"unta","onni":"onnea",

"peli":"peliä","laki":"lakia","sää":"säätä","tie":"tietä","yö":"yötä",

"ruoka":"ruokaa","juoma":"juomaa","kahvila":"kahvilaa","ravintola":"ravintolaa",

"lentokenttä":"lentokenttää","rautatieasema":"rautatieasemaa",
"kauppakeskus":"kauppakeskusta","linja-autoasema":"linja-autoasemaa",

"työpaikka":"työpaikkaa","toimisto":"toimistoa","yritys":"yritystä",

"harjoitus":"harjoitusta","kysymys":"kysymystä","vastaus":"vastausta",

"tapahtuma":"tapahtumaa","kokemus":"kokemusta","elämys":"elämystä",

"pöytäliina":"pöytäliinaa","kirjahylly":"kirjahyllyä","tietokoneohjelma":"tietokoneohjelmaa"
    }

    tests_pl = {
    # --- Esimerkit ja testisanat ---
    "paperi": "papereita", "banaani": "banaaneja", "appelsiini": "appelsiineja",
    "kahvi": "kahveja", "tee": "teitä", "juusto": "juustoja", "voi": "voita",
    "sokeri": "sokereita", "maito": "maitoja",
    
    # --- CLOTHING & ACCESSORIES ---
    "vaate": "vaatteita", "paita": "paitoja", "hame": "hameita", "mekko": "mekkoja",
    "takki": "takkeja", "hattu": "hattuja", "pipo": "pipoja", "käsine": "käsineitä",
    "sukka": "sukkia", "kenkä": "kenkiä", "saapas": "saappaita", "vyö": "vöitä",
    "huivi": "huiveja", "solmio": "solmioita", "puku": "pukuja", "tasku": "taskuja",
    "nappi": "nappeja", "vetoketju": "vetoketjuja", "sateenvarjo": "sateenvarjoja",
    "laukku": "laukkuja", "reppu": "reppuja", "lompakko": "lompakoita", "sormus": "sormuksia",
    "kaulakoru": "kaulakoruja", "rannekello": "rannekelloja", "pusero": "puseroita",
    "huppari": "huppareita", "neule": "neuleita", "liivi": "liivejä", "yöpaita": "yöpaitoja",
    "kravatti": "kravatteja", "rusetti": "rusetteja", "kaulaliina": "kaulaliinoja",
    "lapanen": "lapasia", "sormikas": "sormikkaita", "sandaali": "sandaaleja",
    "tohveli": "tohveleita", "kumisaapas": "kumisaappaita", "solki": "solkia",
    "hihna": "hihnoja", "hiha": "hihoja", "lahje": "lahkeita", "kaulus": "kauluksia",
    "henkseli": "henkseleitä", "uimapuku": "uimapukuja", "bikinien yläosa": "bikinien yläosia",
    "viitta": "viittoja", "otsanauha": "otsanauhoja", "rintakoru": "rintakoruja",
    "kalvosinnappi": "kalvosinnappeja", "lippalakki": "lippalakkeja", "baretti": "baretteja",
    "turkki": "turkkeja", "lenkkari": "lenkkareita",

    # --- TECHNICAL & INDUSTRIAL ---
    "pumppu": "pumppuja", "moottori": "moottoreita", "turbiini": "turbiineja",
    "generaattori": "generaattoreita", "muuntaja": "muuntajia", "venttiili": "venttiilejä",
    "putki": "putkia", "johto": "johtoja", "kaapeli": "kaapeleita", "kytkin": "kytkimiä",
    "anturi": "antureita", "mittari": "mittareita", "robotti": "robotteja", "siru": "sirjuja",
    "prosessori": "prosessoreita", "kovalevy": "kovalevyjä", "virtalähde": "virtalähteitä",
    "jäähdytin": "jäähdyttimiä", "tuuletin": "tuulettimia", "suodatin": "suodattimia",
    "tiiviste": "tiivisteitä", "laakeri": "laakereita", "hammaspyörä": "hammaspyöriä",
    "ketju": "ketjuja", "vipu": "vipuja", "jousi": "jousia", "pultti": "pultteja",
    "mutteri": "muttereita", "prikka": "prikkoja", "niitti": "niittejä",
    "hitsaussauma": "hitsaussaumoja", "teline": "telineitä", "nosturi": "nostureita",
    "trukin": "trukkeja", "kontti": "kontteja", "lava": "lavoja", "mutteriavain": "mutteriavaimia",
    "ruuvitaltta": "ruuvitalttoja", "pora": "poria", "hiomakone": "hiomakoneita",
    "sirkkeli": "sirkkeleitä", "höylä": "höyliä", "taltta": "talttoja", "viila": "viiloja",
    "lekka": "lekoja", "sorkkarauta": "sorkkarautoja", "lapio": "lapioita", "hanko": "hankoja",
    "viikate": "viikatteita", "sirppi": "sirppejä", "kottikärry": "kottikärryjä",
    "kompressori": "kompressoreita", "hitsikone": "hitsikoneita", "sorvi": "sorveja",
    "jyrsin": "jyrsimiä", "painepesuri": "painepesureita", "ruohonleikkuri": "ruohonleikkureita",
    "lehtipuhallin": "lehtipuhaltimia", "lumilinko": "lumilinkoja", "aggregaatti": "aggregaatteja",
    "rele": "releitä", "vastus": "vastuksia", "kondensaattori": "kondensaattoreita",
    "diodi": "diodeja", "transistori": "transistoreita", "piirilevy": "piirilevyjä",
    "antenni": "antenneja", "satelliitti": "satelliitteja", "kaukoputki": "kaukoputkia",
    "mikroskooppi": "mikroskooppeja", "laboratoriotakki": "laboratoriotakkeja",
    "koeputki": "koeputkia", "pipetti": "pipettejä", "vaaka": "vaakoja",
    "lämpömittari": "lämpömittareita", "verenpainemittari": "verenpainemittareita",
    "stetoskooppi": "stetoskooppeja", "ruisku": "ruiskuja", "laastari": "laastareita",
    "sideharsorulla": "sideharsorullia", "pyörätuoli": "pyörätuoleja", "kipsi": "kipsejä",
    "tekohammas": "tekohampaita", "kuulolaite": "kuulolaitteita",
    "silmälasinsanka": "silmälasinsankoja", "piilolinssi": "piilolinssejä",
    "hammasrauta": "hammasrautoja", "tutti": "tutteja", "vaippa": "vaippoja",
    "vaunu": "vaunuja", "ratas": "rattaita", "keinu": "keinuja", "liukumäki": "liukumäkiä",
    "hiekkalaatikko": "hiekkalaatikoita", "kiipeilyteline": "kiipeilytelineitä",
    "lippu": "lippuja", "viiri": "viirejä", "kilpi": "kilpiä", "miekka": "miekkoja",
    "jousi": "jousia", "nuoli": "nuolia", "keihäs": "keihäitä", "kanuuna": "kanuunoita",
    "panssarivaunu": "panssarivaunuja", "sukellusvene": "sukellusveneitä",
    "laskuvarjo": "laskuvarjoja", "kuumailmapallo": "kuumailmapalloja",
    "avaruusalus": "avaruusaluksia", "raketti": "raketteja", "komeetta": "komeettoja",
    "asteroidi": "asteroideja", "musta aukko": "mustia aukkoja", "galaksi": "galakseja",
    "sumu": "sumuja", "tähdenlento": "tähdenlentoja",

    # --- BODY PARTS ---
    "pää": "päitä", "silmä": "silmiä", "korva": "korvia", "nenä": "neniä", "suu": "suita",
    "huuli": "huulia", "hammas": "hampaita", "kieli": "kieliä", "kaula": "kauloja",
    "kurkku": "kurkkuja", "olkapää": "olkapäitä", "käsivarsi": "käsivarsia", "käsi": "käsiä",
    "sormi": "sormia", "kynsi": "kynsiä", "rinta": "rintoja", "vatsa": "vatsoja", "selkä": "selkiä",
    "jalka": "jalkoja", "polvi": "polvia", "varvas": "varpaita", "iho": "ihoja", "luu": "luita",
    "sydän": "sydämiä", "keuhko": "keuhkoja", "lihas": "lihaksia", "naama": "naamoja",
    "maksa": "maksoja", "munuainen": "munuaisia", "nivel": "niveliä", "verisuoni": "verisuonia",
    "hermo": "hermoja", "otsa": "otsia", "leuka": "leukoja", "poski": "poskia",
    "kulmakarva": "kulmakarvoja", "ripsi": "ripsiä", "napa": "napoja", "vyötärö": "vyötäröitä",
    "kyynärpää": "kyynärpäitä", "ranne": "ranteita", "kämmen": "kämmeniä", "lantio": "lantioita",
    "reisi": "reisiä", "pohje": "pohkeita", "nilkka": "nilkkoja", "kantapää": "kantapäitä",
    "pikkurilli": "pikkurillejä", "nimetön": "nimettömiä", "keskisormi": "keskisormia",
    "etusormi": "etusormia", "peukalo": "peukaloita", "isoavarvas": "isovarpaita",
    "kantaluu": "kantaluita", "nikama": "nikamia", "kylkiluu": "kylkiluita",
    "leukaluu": "leukaluita", "aivonystyrä": "aivonystyröitä", "karva": "karvoja",
    "pisama": "pisamia", "luomi": "luomia", "arpi": "arpia",

    # --- ABSTRACT & MASS NOUNS ---
    "vesi": "vesiä", "rakkaus": "rakkauksia", "onni": "onnia", "ilma": "ilmoja",
    "lumi": "lumia", "hiekka": "hiekkoja", "multa": "multia", "ruoka": "ruokia",
    "juoma": "juomia", "viini": "viinejä", "mehu": "mehuja", "veri": "veriä",
    "rauta": "rautoja", "kulta": "kultia", "hopea": "hopeita", "kupari": "kupareita",
    "öljy": "öljyjä", "suola": "suoloja", "jauho": "jauhoja", "hunaja": "hunajia",
    "liha": "lihoja", "apu": "apuja", "voima": "voimia", "valo": "valoja",
    "pimeys": "pimeyksiä", "lämpö": "lämpöjä", "kylmyys": "kylmyyksiä", "aika": "aikoja",
    "elämä": "elämiä", "kuolema": "kuolemia", "toivo": "toivoja", "pelko": "pelkoja",
    "viha": "vihoja", "suru": "suruja", "ilo": "iloja", "rauha": "rauhoja", "sota": "sotia",
    "vapaus": "vapauksia", "totuus": "totuuksia", "valhe": "valheita", "tieto": "tietoja",
    "taito": "taitoja", "usko": "uskoja",

    # --- ADJECTIVES ---
    "suuri": "suuria", "pieni": "pieniä", "pitkä": "pitkiä", "lyhyt": "lyhyitä",
    "paksu": "paksuja", "ohut": "ohuita", "leveä": "leveitä", "kapea": "kapeita",
    "uusi": "uusia", "vanha": "vanhoja", "nuori": "nuoria", "rikas": "rikkaita",
    "köyhä": "köyhiä", "kaunis": "kauniita", "ruma": "rumia", "hyvä": "hyviä",
    "paha": "pahoja", "iloinen": "iloisia", "surullinen": "surullisia", "viisas": "viisaita",
    "tyhmä": "tyhmiä", "vahva": "vahvoja", "heikko": "heikkoja", "nopea": "nopeita",
    "hidas": "hitaita", "kuuma": "kuumia", "kylmä": "kylmiä", "lämmin": "lämpimiä",
    "viileä": "viileitä", "kuiva": "kuivia", "märkä": "märkiä", "kova": "kovia",
    "pehmeä": "pehmeitä", "kallis": "kalliita", "halpa": "halpoja", "painava": "painavia",
    "kevyt": "kevyitä", "pimeä": "pimeitä", "kirkas": "kirkkaita", "puhdas": "puhtaita",
    "likainen": "likaisia", "täysi": "täysiä", "tyhjä": "tyhjiä", "terve": "terveitä",
    "sairas": "sairaita", "rehellinen": "rehellisiä", "hauska": "hauskoja", "tylsä": "tylsiä",
    "outo": "outoja", "tavallinen": "tavallisia", "erilainen": "erilaisia",
    "punainen": "punaisia", "sininen": "sinisiä", "vihreä": "vihreitä", "keltainen": "keltaisia",
    "musta": "mustia", "valkoinen": "valkoisia", "harmaa": "harmaita", "ruskea": "ruskeita",
    "oranssi": "oransseja", "violetti": "violetteja", "vaaleanpunainen": "vaaleanpunaisia",

    # --- ANIMALS & BIOLOGY ---
    "orava": "oravia", "siili": "siilejä", "hirvi": "hirviä", "peura": "peuroja",
    "karitsa": "karitsoita", "vuohi": "vuohia", "ankka": "ankkoja", "hanhi": "hanhia",
    "kana": "kanoja", "kukko": "kukkoja", "pöllö": "pöllöjä", "kotka": "kotkia",
    "varis": "variksia", "harakka": "harakoita", "pääskynen": "pääskysiä",
    "muurahainen": "muurahaisia", "mehiläinen": "mehiläisiä", "hämähäkki": "hämähäkkejä",
    "itikka": "itikoita", "perhonen": "perhosia", "valas": "valaita", "hylje": "hylkeitä",
    "rapu": "rapuja", "etana": "etanoita", "koira": "koiria", "kissa": "kissoja",
    "hevonen": "hevosia", "lehmä": "lehmiä", "lammas": "lampaita", "sika": "sikoja",
    "karhu": "karhuja", "susi": "susia", "kettu": "kettuja", "jänis": "jäniksiä",
    "lintu": "lintuja", "kala": "kaloja", "käärme": "käärmeitä", "hyönteinen": "hyönteisiä",
    "puu": "puita", "kukka": "kukkia", "metsä": "metsiä", "järvi": "järviä", "meri": "meriä",
    "joki": "jokia", "vuori": "vuoria", "mäki": "mäkiä", "saari": "saaria", "niemi": "niemiä",
    "ranta": "rantoja", "taivas": "taivaita", "aurinko": "aurinkoja", "kuu": "kuita",
    "tähti": "tähtiä", "pilvi": "pilviä", "ukkonen": "ukkosia", "kivi": "kiviä",
    "lehti": "lehtiä", "oksa": "oksia", "juuri": "juuria", "marja": "marjoja",
    "sieni": "sieniä", "puro": "puroja", "lähde": "lähteitä", "tunturi": "tuntureita",
    "ilves": "ilveksiä", "poro": "poroja", "myyrä": "myyriä", "lepakko": "lepakoita",
    "joutsen": "joutsenia", "sorsa": "sorsia", "lokki": "lokkeja", "tikka": "tikkoja",
    "kimalainen": "kimalaisia", "kärpänen": "kärpäsiä", "mato": "matoja",
    "sammakko": "sammakoita", "sisilisko": "sisiliskoja", "koivu": "koivuja",
    "mänty": "mäntyjä", "kuusi": "kuusia", "tammi": "tammia", "vaahtera": "vaahteroita",
    "pihlaja": "pihlajoita", "kanto": "kantoja", "neulanen": "neulasia", "käpy": "käpyjä",
    "oja": "ojia", "lampi": "lampia", "lahti": "lahtia", "salmi": "salmia", "koski": "koskia",
    "vesiputous": "vesiputouksia", "jyrkänne": "jyrkänteitä", "huippu": "huippuja",
    "rinne": "rinteitä", "laakso": "laaksoja", "kyy": "kyitä", "rantakäärme": "rantakäärmeitä",
    "ahven": "ahvenia", "hauki": "haukia", "lohi": "lohia", "siika": "siikoja",
    "muikku": "muikkuja", "simpukka": "simpukoita", "mustekala": "mustekaloja",
    "meduusa": "meduusoja", "pulu": "puluja", "tiikeri": "tiikereitä", "leijona": "leijonia",
    "norsu": "norsuja", "kirahvi": "kirahveja", "apina": "apinoita", "seepra": "seeproja",
    "krokotiili": "krokotiileja", "kilpikonna": "kilpikonnia", "pingviini": "pingviinejä",
    "kameli": "kameleita", "papukaija": "papukaijoja", "päästäinen": "päästäisiä",
    "majava": "majavia", "vesikko": "vesikkoja", "nääpikkä": "nääpikköjä", "kärppä": "kärppiä",
    "ahma": "ahmoja", "mursu": "mursuja",

    # --- HOUSE & EVERYDAY OBJECTS ---
    "talo": "taloja", "koti": "koteja", "asunto": "asuntoja", "huone": "huoneita",
    "keittiö": "keittiöitä", "kylpyhuone": "kylpyhuoneita", "makuuhuone": "makuuhuoneita",
    "olohuone": "olohuoneita", "eteinen": "eteisiä", "parveke": "parvekkeita",
    "piha": "pihoja", "ovi": "ovia", "ikkuna": "ikkunoita", "seinä": "seiniä",
    "katto": "kattoja", "lattia": "lattioita", "porras": "portaita", "lukko": "lukkoja",
    "avain": "avaimia", "pöytä": "pöytiä", "tuoli": "tuoleja", "sänky": "sänkyjä",
    "sohva": "sohvia", "kaappi": "kaappeja", "hylly": "hyllyjä", "lamppu": "lamppuja",
    "matto": "mattoja", "verho": "verhoja", "peili": "peilejä", "taulu": "tauluja",
    "kello": "kelloja", "radio": "radioita", "televisio": "televisioita",
    "tietokone": "tietokoneita", "puhelin": "puhelimia", "kone": "koneita", "uuni": "uuneja",
    "hella": "helloja", "allas": "altaita", "lautanen": "lautasia", "kulho": "kulhoja",
    "muki": "mukeja", "kuppi": "kuppeja", "veitsi": "veitsiä", "haarukka": "haarukoita",
    "lusikka": "lusikoita", "kattila": "kattiloita", "pannu": "pannuja",
    "astianpesukone": "astianpesukoneita", "pyykinpesukone": "pyykinpesukoneita",
    "pakastin": "pakastimia", "mikroaaltouuni": "mikroaaltouuneja",
    "leivänpaahdin": "leivänpaahtimia", "vedenkeitin": "vedenkeittimiä",
    "tehosekoitin": "tehosekoittimia", "vatkain": "vatkaimia", "kahvinkeitin": "kahvinkeittimiä",
    "imuri": "imureita", "silitysrauta": "silitysrautoja", "laatikko": "laatikoita",
    "tiskiallas": "tiskialtaita", "hana": "hanoja", "roskakori": "roskakoreja",
    "tiskiharja": "tiskiharjoja", "sieni": "sieniä", "liina": "liinoja", "tyyny": "tyynyjä",
    "peitto": "peittoja", "lakana": "lakanoita", "pyyhe": "pyyhkeitä", "henkari": "henkareita",
    "kampa": "kampoja", "hammasharja": "hammasharjoja", "vasara": "vasaroita", "saha": "sahoja",
    "ruuvimeisseli": "ruuvimeisseleitä", "naula": "nauloja", "ruuvi": "ruuveja",
    "ämpäri": "ämpäreitä", "harja": "harjoja", "luuta": "luutia", "lapio": "lapioita",
    "akku": "akkuja", "sytytin": "sytyttimiä", "kynttilä": "kynttilöitä",
    "taskulamppu": "taskulamppuja", "porakone": "porakoneita", "jakkara": "jakkaroita",
    "nojatuoli": "nojatuoleja", "kirjahylly": "kirjahyllyjä", "lipasto": "lipastoja",
    "yöpöytä": "yöpöytiä", "vaatekaappi": "vaatekaappeja", "kynnys": "kynnyksiä",
    "kahva": "kahvoja", "sarana": "saranoita", "patteri": "pattereita",
    "pistorasia": "pistorasioita", "jatkojohto": "jatkojohtoja", "sulake": "sulakkeita",
    "hehkulamppu": "hehkulamppuja", "varjostin": "varjostimia", "vaasi": "vaaseja",
    "ruukku": "ruukkuja", "tarjotin": "tarjottimia", "pannunalunen": "pannunalusia",
    "patakinnas": "patakintaita", "esiliina": "esiliinoja", "leikkuulauta": "leikkuulautoja",
    "raastin": "raastimia", "siivilä": "siivilöitä", "kuorimaveitsi": "kuorimaveitsiä",
    "perunasurvin": "perunasurvimia", "vispilä": "vispilöitä", "kaulun": "kaulimia",

    # --- FOOD & INGREDIENTS ---
    "makkara": "makkaroita", "peruna": "perunoita", "vihannes": "vihanneksia",
    "hedelmä": "hedelmiä", "sipuli": "sipuleita", "valkosipuli": "valkosipuleita",
    "porkkana": "porkkanoita", "kurkku": "kurkkuja", "tomaatti": "tomaatteja",
    "paprika": "paprikoita", "salaatti": "salaatteja", "kaali": "kaaleja",
    "herne": "herneitä", "papu": "papuja", "maissi": "maisseja", "päärynä": "päärynöitä",
    "luumu": "luumuja", "viinirypäle": "viinirypäleitä", "mansikka": "mansikoita",
    "mustikka": "mustikoita", "vadelma": "vadelmia", "sitruuna": "sitruunoita",
    "pähkinä": "pähkinöitä", "siemen": "siemeniä", "leivonnainen": "leivonnaisia",
    "kakku": "kakkuja", "keksi": "keksejä", "leipä": "leipiä", "sämpylä": "sämpylöitä",
    "piirakka": "piirakoita", "munkki": "munkkeja", "pulla": "pullia",
    "voileipä": "voileipiä", "hampurilainen": "hampurilaisia", "pizza": "pizzoja",
    "kananmuna": "kananmunia", "lihapulla": "lihapullia", "nakki": "nakkeja",
    "pihvi": "pihvejä", "kyljys": "kyljyksiä", "koipi": "koipia", "filee": "fileitä",
    "katkarapu": "katkarapuja", "simpukka": "simpukoita", "oliivi": "oliiveja",
    "kapris": "kapriksia", "retiisi": "retiisejä", "parsa": "parsoja",
    "kukkakaali": "kukkakaaleja", "parsakaali": "parsakaaleja", "munakoiso": "munakoisoja",
    "kesäkurpitsa": "kesäkurpitsoja",

    # --- TRANSPORT & CITY ---
    "auto": "autoja", "bussi": "busseja", "juna": "junia", "lentokone": "lentokoneita",
    "laiva": "laivoja", "vene": "veneitä", "pyörä": "pyöriä", "moottoripyörä": "moottoripyöriä",
    "tie": "teitä", "katu": "katuja", "polku": "polkuja", "silta": "siltoja",
    "tunneli": "tunneleita", "asema": "asemia", "satama": "satamia", "tori": "toreja",
    "puisto": "puistoja", "kaupunki": "kaupunkeja", "kylä": "kyliä", "keskusta": "keskustoja",
    "kauppa": "kauppoja", "pankki": "pankkeja", "sairaala": "sairaaloita", "koulu": "kouluja",
    "kirkko": "kirkkoja", "tehdas": "tehtaita", "hotelli": "hotelleja",
    "ravintola": "ravintoloita", "kahvila": "kahviloita", "museo": "museoita",
    "kirjasto": "kirjastoja", "teatteri": "teattereita", "apteekki": "apteekkeja",
    "lentokenttä": "lentokenttiä", "laituri": "laitureita", "kiitotie": "kiitoteitä",
    "opas": "oppaita", "kartta": "karttoja", "suunta": "suuntia", "rekka": "rekkoja",
    "paku": "pakuja", "traktori": "traktoreita", "mopo": "mopoja", "ratikka": "ratikoita",
    "metro": "metroja", "helikopteri": "helikoptereita", "purjevene": "purjeveneitä",
    "soutuvene": "soutuveneitä", "liikennemerkki": "liikennemerkkejä",
    "liikennevalo": "liikennevaloja", "suojatie": "suojateitä", "pysäkki": "pysäkkejä",
    "parkkipaikka": "parkkipaikkoja", "autotalli": "autotalleja", "pilvenpiirtäjä": "pilvenpiirtäjiä",
    "mökki": "mökkejä", "talli": "talleja", "navetta": "navettoja", "lato": "latoja",
    "aita": "aitoja", "portti": "portteja", "penkki": "penkkejä", "patsas": "patsaita",
    "suihkulähde": "suihkulähteitä",

    # --- WORK, MEDIA, EDUCATION ---
    "opiskelija": "opiskelijoita", "opettaja": "opettajia", "rehtori": "rehtoreita",
    "luokka": "luokkia", "kurssi": "kursseja", "koe": "kokeita", "arvosana": "arvosanoja",
    "kynä": "kyniä", "lyijykynä": "lyijykyniä", "pyyhekumi": "pyyhekumeja",
    "viivatin": "viivaimia", "vihko": "vihkoja", "kirja": "kirjoja", "sanakirja": "sanakirjoja",
    "tussi": "tusseja", "liitu": "liituja", "ammatti": "ammatteja", "kokous": "kokouksia",
    "sopimus": "sopimuksia", "asiakas": "asiakkaita", "pomo": "pomoja",
    "työpaikka": "työpaikkoja", "yritys": "yrityksiä", "sanomalehti": "sanomalehtiä",
    "aikakauslehti": "aikakauslehtiä", "mainos": "mainoksia", "näyttö": "näyttöjä",
    "näppäimistö": "näppäimistöjä", "hiiri": "hiiriä", "tulostin": "tulostimia",
    "laturi": "latureita", "kaiutin": "kaiuttimia", "kaukosäädin": "kaukosäätimiä",
    "sovellus": "sovelluksia", "tiedosto": "tiedostoja", "kansio": "kansioita",
    "salasana": "salasanoja", "viesti": "viestejä", "lasku": "laskuja", "kuitti": "kuitteja",
    "allekirjoitus": "allekirjoituksia", "vankila": "vankiloita", "mittanauha": "mittanauhoja",
    "todistus": "todistuksia", "tutkinto": "tutkintoja", "yliopisto": "yliopistoja",
    "nitoja": "nitojia", "klemmari": "klemmareita", "teippirulla": "teippirullia",
    "kirjekuori": "kirjekuoria", "postimerkki": "postimerkkejä", "kortti": "kortteja",
    "kalenteri": "kalentereita", "muistilehtiö": "muistilehtiöitä", "piirustus": "piirustuksia",
    "valokuva": "valokuvia", "maalaus": "maalauksia", "veistos": "veistoksia",
    "kamera": "kameroita", "objektiivi": "objektiiveja", "jalusta": "jalustoja",
    "mikrofoni": "mikrofoneja", "kuuloke": "kuulokkeita", "levy": "levyjä",
    "muistitikku": "muistitikkuja", "reititin": "reitittimiä",

    # --- TIME & NUMBERS ---
    "sekunti": "sekunteja", "minuutti": "minuutteja", "tunti": "tunteja", "päivä": "päiviä",
    "viikko": "viikkoja", "kuukausi": "kuukausia", "vuosi": "vuosia", "vuosisata": "vuosisatoja",
    "aamu": "aamuja", "ilta": "iltoja", "yö": "öitä", "maanantai": "maanantaita",
    "tiistai": "tiistaita", "keskiviikko": "keskiviikkoja", "torstai": "torstaita",
    "perjantai": "perjantaita", "lauantai": "lauantaita", "sunnuntai": "sunnuntaita",
    "numero": "numeroita", "hetki": "hetkiä",

    # --- SPORTS, HOBBIES, MUSIC ---
    "pallo": "palloja", "maila": "mailoja", "verkko": "verkkoja", "maali": "maaleja",
    "kypärä": "kypäriä", "suksi": "suksia", "sauva": "sauvoja", "luistin": "luistimia",
    "potkulauta": "potkulautoja", "rullalauta": "rullalautoja", "mitali": "mitaleja",
    "pokaali": "pokaaleja", "rata": "ratoja", "kenttä": "kenttiä", "hyppylauta": "hyppylautoja",
    "trampoliini": "trampoliineja", "keila": "keiloja", "noppa": "noppia",
    "nappula": "nappuloita", "korttipakka": "korttipakkoja", "pelilauta": "pelilautoja",
    "palapeli": "palapelejä", "nukke": "nukkeja", "pehmolelu": "pehmoleluja",
    "pienoismalli": "pienoismalleja", "soitin": "soittimia", "kitara": "kitaroita",
    "piano": "pianoja", "viulu": "viuluja", "rumpu": "rumpuja", "huilu": "huiluja",
    "trumpetti": "trumpetteja", "sähkökitara": "sähkökitaroita", "basso": "bassoja",
    "syntetisaattori": "syntetisaattoreita", "vahvistin": "vahvistimia",
    "nuottiteline": "nuottitelineitä", "haitari": "haitareita", "saksofoni": "saksofoneja",
    "kantele": "kanteleita",

    # --- PROFESSIONS ---
    "lääkäri": "lääkäreitä", "hoitaja": "hoitajia", "poliisi": "poliiseja",
    "palomies": "palomiehiä", "sotilas": "sotilaita", "lentäjä": "lentäjiä",
    "kapteeni": "kapteeneja", "kuljettaja": "kuljettajia", "kokki": "kokkeja",
    "tarjoilija": "tarjoilijoita", "myyjä": "myyjiä", "siivooja": "siivoojia",
    "insinööri": "insinöörejä", "arkkitehti": "arkkitehteja", "ohjelmoija": "ohjelmoijia",
    "taitaja": "taitajia", "taiteilija": "taiteilijoita", "muusikko": "muusikoita",
    "näyttelijä": "näyttelijöitä", "ohjaaja": "ohjaajia", "toimittaja": "toimittajia",
    "kirjailija": "kirjailijoita", "runoilija": "runoilijoita", "tutkija": "tutkijoita",
    "tiedemies": "tiedemiehiä", "lakimies": "lakimiehiä", "tuomari": "tuomareita",
    "pappi": "pappeja", "piispa": "piispoja", "kuningas": "kuninkaita",
    "kuningatar": "kuningattaria", "presidentti": "presidenttejä", "ministeri": "ministereitä",
     "edustaja": "edustajia", "johtaja": "johtajia",
    "työntekijä": "työntekijöitä", "harjoittelija": "harjoittelijoita",
    "asiantuntija": "asiantuntijoita", "neuvonantaja": "neuvonantajia",
     "sähköasentaja": "sähköasentajia",
    "putkiasentaja": "putkiasentajia", "muurari": "muurareita", "puuseppä": "puuseppiä",
    "leipuri": "leipureita", "parturi": "partureita", "kampaaja": "kampaajia",
    "kosmetologi": "kosmetologeja", "valokuvaaja": "valokuvaajia",

    # --- MISCELLANEOUS COUNTABLE NOUNS ---
    "esine": "esineitä", "kappale": "kappaleita", "osa": "osia", "ryhmä": "ryhmiä",
    "joukko": "joukkoja", "pino": "pinoja", "kasa": "kasoja", "rivi": "rivejä",
    "jono": "jonoja", "aukko": "aukkoja", "reikä": "reikiä", "rako": "rakoja",
    "pinta": "pintoja", "reuna": "reunoja", "kulma": "kulmia", "keskipiste": "keskipisteitä",
    "ympyrä": "ympyröitä", "viiva": "viivoja", "piste": "pisteitä", "merkki": "merkkejä",
    "symboli": "symboleja", "kuva": "kuvia", "varjo": "varjoja", "heijastus": "heijastuksia",
    "ääni": "ääniä", "melu": "meluja", "kaiku": "kaikuja", "haju": "hajuja",
    "tuoksu": "tuoksuja", "maku": "makuja", "tunne": "tunteita", "aisti": "aisteja",

    # --- PLANTS & GARDEN ---
    "ruusu": "ruusuja", "tulppaani": "tulppaaneja", "voikukka": "voikukkia",
    "lilja": "liljoja", "apila": "apiloita", "sammal": "sammalia", "jäkälä": "jäkäliä",
    "varpu": "varpuja", "pensas": "pensaita", "heinä": "heiniä", "olki": "olkia",
    "sipulikasvi": "sipulikasveja", "taimi": "taimia", "pistokas": "pistokkaita",
    "hedelmäpuu": "hedelmäpuita", "lauta": "lautoja", "purje": "purjeita", "mela": "meloja",
    "vapa": "vapoja", "koukku": "koukkuja", "uistin": "uistimia", "teltta": "telttoja", "paperi":"papereita","banaani":"banaaneja","appelsiini":"appelsiineja","kahvi":"kahveja",
    # --- HOBBIES & SPORTS ---
    "pallo": "palloja", "maila": "mailoja", "verkko": "verkkoja", "maali": "maaleja",
    "rata": "ratoja", "kenttä": "kenttiä", "kypärä": "kypäriä", "suksi": "suksia",
    "luistin": "luistimia", "lauta": "lautoja", "purje": "purjeita", "mela": "meloja",
    "vapa": "vapoja", "koukku": "koukkuja", "uistin": "uistimia", "teltta": "telttoja",
    "reppu": "reppuja", "sauva": "sauvoja", "potkulauta": "potkulautoja", 
    "rullalauta": "rullalautoja", "mitali": "mitaleja", "pokaali": "pokaaleja", 
    "allas": "altaita", "hyppylauta": "hyppylautoja", "trampoliini": "trampoliineja", 
    "keila": "keiloja", "noppa": "noppia", "nappula": "nappuloita", 
    "korttipakka": "korttipakkoja", "pelilauta": "pelilautoja", "palapeli": "palapelejä", 
    "nukke": "nukkeja", "pehmolelu": "pehmoleluja", "pienoismalli": "pienoismalleja", 
    "soitin": "soittimia", "kitara": "kitaroita", "piano": "pianoja", "viulu": "viuluja", 
    "rumpu": "rumpuja", "huilu": "huiluja", "trumpetti": "trumpetteja", 
    "sähkökitara": "sähkökitaroita", "basso": "bassoja", "syntetisaattori": "syntetisaattoreita", 
    "vahvistin": "vahvistimia", "nuottiteline": "nuottitelineitä",

    # --- MISC COUNTABLE NOUNS ---
    "esine": "esineitä", "kappale": "kappaleita", "osa": "osia", "ryhmä": "ryhmiä",
    "joukko": "joukkoja", "pino": "pinoja", "kasa": "kasoja", "rivi": "rivejä",
    "jono": "jonoja", "aukko": "aukkoja", "reikä": "reikiä", "rako": "rakoja",
    "pinta": "pintoja", "reuna": "reunoja", "kulma": "kulmia", "keskipiste": "keskipisteitä",
    "ympyrä": "ympyröitä", "viiva": "viivoja", "piste": "pisteitä", "merkki": "merkkejä",
    "symboli": "symboleja", "kuva": "kuvia", "varjo": "varjoja", "heijastus": "heijastuksia",
    "ääni": "ääniä", "melu": "meluja", "kaiku": "kaikuja", "haju": "hajuja",
    "tuoksu": "tuoksuja", "maku": "makuja", "tunne": "tunteita", "aisti": "aisteja",
    "hihna": "hihnoja", "hiha": "hihoja", "lahje": "lahkeita", "kaulus": "kauluksia", 
    "henkseli": "henkseleitä", "uimapuku": "uimapukuja", "bikinien yläosa": "bikinien yläosia", 
    "viitta": "viittoja", "otsanauha": "otsanauhoja", "rintakoru": "rintakoruja", 
    "kalvosinnappi": "kalvosinnappeja", "lippalakki": "lippalakkeja", "baretti": "baretteja",
    "maailma": "maailmoja", "planeetta": "planeettoja", "salama": "salamoita", "myrsky": "myrskyjä",
    "tulva": "tulvia", "maanjäristys": "maanjäristyksiä", "tulivuori": "tulivuoria", "aavikko": "aavikoita",
    "viidakko": "viidakkoja", "luola": "luolia", "hiekkaranta": "hiekkarantoja", "valtameri": "valtameriä",
    "aalto": "aaltoja", "rannikko": "rannikoita",

    # --- ANIMALS & NATURE ---
    "orava": "oravia", "siili": "siilejä", "hirvi": "hirviä", "peura": "peuroja",
    "karitsa": "karitsoita", "vuohi": "vuohia", "ankka": "ankkoja", "hanhi": "hanhia",
    "kana": "kanoja", "kukko": "kukkoja", "pöllö": "pöllöjä", "kotka": "kotkia",
    "varis": "variksia", "harakka": "harakoita", "pääskynen": "pääskysiä",
    "muurahainen": "muurahaisia", "mehiläinen": "mehiläisiä", "hämähäkki": "hämähäkkejä",
    "itikka": "itikoita", "perhonen": "perhosia", "valas": "valaita", "hylje": "hylkeitä",
    "rapu": "rapuja", "etana": "etanoita", "koira": "koiria", "kissa": "kissoja",
    "hevonen": "hevosia", "lehmä": "lehmiä", "lammas": "lampaita", "sika": "sikoja",
    "karhu": "karhuja", "susi": "susia", "kettu": "kettuja", "jänis": "jäniksiä",
    "lintu": "lintuja", "kala": "kaloja", "käärme": "käärmeitä", "hyönteinen": "hyönteisiä",
    "puu": "puita", "kukka": "kukkia", "metsä": "metsiä", "järvi": "järviä", "meri": "meriä",
    "joki": "jokia", "vuori": "vuoria", "mäki": "mäkiä", "saari": "saaria", "niemi": "niemiä",
    "ranta": "rantoja", "taivas": "taivaita", "aurinko": "aurinkoja", "kuu": "kuita",
    "tähti": "tähtiä", "pilvi": "pilviä", "ukkonen": "ukkosia", "kivi": "kiviä",
    "lehti": "lehtiä", "oksa": "oksia", "juuri": "juuria", "marja": "marjoja", "sieni": "sieniä",
    "puro": "puroja", "lähde": "lähteitä", "tunturi": "tuntureita", "ilves": "ilveksiä",
    "poro": "poroja", "myyrä": "myyriä", "lepakko": "lepakoita", "joutsen": "joutsenia",
    "sorsa": "sorsia", "lokki": "lokkeja", "tikka": "tikkoja", "kimalainen": "kimalaisia",
    "kärpänen": "kärpäsiä", "mato": "matoja", "sammakko": "sammakoita", "sisilisko": "sisiliskoja",
    "koivu": "koivuja", "mänty": "mäntyjä", "kuusi": "kuusia", "tammi": "tammia",
    "vaahtera": "vaahteroita", "pihlaja": "pihlajoita", "kanto": "kantoja", "neulanen": "neulasia",
    "käpy": "käpyjä", "oja": "ojia", "lampi": "lampia", "lahti": "lahtia", "salmi": "salmia",
    "koski": "koskia", "vesiputous": "vesiputouksia", "jyrkänne": "jyrkänteitä", "huippu": "huippuja",
    "rinne": "rinteitä", "laakso": "laaksoja", "kyy": "kyitä", "rantakäärme": "rantakäärmeitä",
    "ahven": "ahvenia", "hauki": "haukia", "lohi": "lohia", "siika": "siikoja",
    "muikku": "muikkuja", "simpukka": "simpukoita", "mustekala": "mustekaloja",
    "meduusa": "meduusoja", "pulu": "puluja", "tiikeri": "tiikereitä", "leijona": "leijonia",
    "norsu": "norsuja", "kirahvi": "kirahveja", "apina": "apinoita", "seepra": "seeproja",
    "krokotiili": "krokotiileja", "kilpikonna": "kilpikonnia", "pingviini": "pingviinejä",
    "kameli": "kameleita", "papukaija": "papukaijoja", "päästäinen": "päästäisiä",
    "majava": "majavia", "nääpikkä": "nääpikköjä", "kärppä": "kärppiä",
    "ahma": "ahmoja", "mursu": "mursuja",

    # --- BODY PARTS ---
    "pää": "päitä", "silmä": "silmiä", "korva": "korvia", "nenä": "neniä", "suu": "suita",
    "huuli": "huulia", "hammas": "hampaita", "kieli": "kieliä", "kaula": "kauloja",
    "kurkku": "kurkkuja", "olkapää": "olkapäitä", "käsivarsi": "käsivarsia", "käsi": "käsiä",
    "sormi": "sormia", "rinta": "rintoja", "vatsa": "vatsoja", "selkä": "selkiä",
    "jalka": "jalkoja", "polvi": "polvia", "varvas": "varpaita", "iho": "ihoja",
    "luu": "luita", "sydän": "sydämiä", "keuhko": "keuhkoja", "lihas": "lihaksia",
    "naama": "naamoja", "maksa": "maksoja", "munuainen": "munuaisia", "nivel": "niveliä",
    "verisuoni": "verisuonia", "hermo": "hermoja", "otsa": "otsia", "leuka": "leukoja",
    "poski": "poskia", "kulmakarva": "kulmakarvoja", "ripsi": "ripsiä", "napa": "napoja",
    "vyötärö": "vyötäröitä", "kyynärpää": "kyynärpäitä", "ranne": "ranteita",
    "kämmen": "kämmeniä", "lantio": "lantioita", "reisi": "reisiä", "pohje": "pohkeita",
    "nilkka": "nilkkoja", "kantapää": "kantapäitä", "pikkurilli": "pikkurillejä",
    "nimetön": "nimettömiä", "keskisormi": "keskisormia", "etusormi": "etusormia",
    "peukalo": "peukaloita", "isoavarvas": "isovarpaita", "kantaluu": "kantaluita",
    "nikama": "nikamia", "kylkiluu": "kylkiluita", "leukaluu": "leukaluita",
    "aivonystyrä": "aivonystyröitä", "karva": "karvoja", "pisama": "pisamia",
    "luomi": "luomia", "arpi": "arpia",

    # --- HOUSE & OBJECTS ---
    "talo": "taloja", "koti": "koteja", "asunto": "asuntoja", "huone": "huoneita",
    "keittiö": "keittiöitä", "kylpyhuone": "kylpyhuoneita", "makuuhuone": "makuuhuoneita",
    "olohuone": "olohuoneita", "eteinen": "eteisiä", "parveke": "parvekkeita",
    "piha": "pihoja", "ovi": "ovia", "ikkuna": "ikkunoita", "seinä": "seiniä",
    "katto": "kattoja", "lattia": "lattioita", "porras": "portaita", "lukko": "lukkoja",
    "avain": "avaimia", "pöytä": "pöytiä", "tuoli": "tuoleja", "sänky": "sänkyjä",
    "sohva": "sohvia", "kaappi": "kaappeja", "hylly": "hyllyjä", "lamppu": "lamppuja",
    "matto": "mattoja", "verho": "verhoja", "peili": "peilejä", "taulu": "tauluja",
    "kello": "kelloja", "radio": "radioita", "televisio": "televisioita",
    "tietokone": "tietokoneita", "puhelin": "puhelimia", "kone": "koneita", "uuni": "uuneja",
    "hella": "helloja", "allas": "altaita", "lautanen": "lautasia", "kulho": "kulhoja",
    "muki": "mukeja", "kuppi": "kuppeja", "veitsi": "veitsiä", "haarukka": "haarukoita",
    "lusikka": "lusikka", "pannu": "pannuja", "astianpesukone": "astianpesukoneita",
    "pyykinpesukone": "pyykinpesukoneita", "pakastin": "pakastimia", "mikroaaltouuni": "mikroaaltouuneja",
    "leivänpaahdin": "leivänpaahtimia", "vedenkeitin": "vedenkeittimiä",
    "tehosekoitin": "tehosekoittimia", "vatkain": "vatkaimia", "kahvinkeitin": "kahvinkeittimiä",
    "imuri": "imureita", "laatikko": "laatikoita", "tiskiallas": "tiskialtaita",
    "hana": "hanoja", "roskakori": "roskakoreja", "tiskiharja": "tiskiharjoja",
    "sieni": "sieniä", "liina": "liinoja", "tyyny": "tyynyjä", "peitto": "peittoja",
    "lakana": "lakanoita", "pyyhe": "pyyhkeitä", "henkari": "henkareita", "kampa": "kampoja",
    "hammasharja": "hammasharjoja", "vasara": "vasaroita", "saha": "sahoja",
    "ruuvimeisseli": "ruuvimeisseleitä", "naula": "nauloja", "ruuvi": "ruuveja",
    "ämpäri": "ämpäreitä", "harja": "harjoja", "luuta": "luutia", "lapio": "lapioita",
    "akku": "akkuja", "pistorasia": "pistorasioita", "sytytin": "sytyttimiä",
    "kynttilä": "kynttilöitä", "taskulamppu": "taskulamppuja", "porakone": "porakoneita",
    "jakkara": "jakkaroita", "nojatuoli": "nojatuoleja", "kirjahylly": "kirjahyllyjä",
    "lipasto": "lipastoja", "yöpöytä": "yöpöytiä", "vaatekaappi": "vaatekaappeja",
    "kynnys": "kynnyksiä", "kahva": "kahvoja", "sarana": "saranoita", "patteri": "pattereita",
    "jatkojohto": "jatkojohtoja", "sulake": "sulakkeita", "hehkulamppu": "hehkulamppuja",
    "varjostin": "varjostimia", "vaasi": "vaaseja", "ruukku": "ruukkuja", "tarjotin": "tarjottimia",
    "pannunalunen": "pannunalusia", "patakinnas": "patakintaita", "esiliina": "esiliinoja",
    "leikkuulauta": "leikkuulautoja", "raastin": "raastimia", "siivilä": "siivilöitä",
    "kuorimaveitsi": "kuorimaveitsiä", "perunasurvin": "perunasurvimia", "vispilä": "vispilöitä",
    "kaulin": "kaulimia",

    # --- TRANSPORT & CITY ---
    "auto": "autoja", "bussi": "busseja", "juna": "junia", "lentokone": "lentokoneita",
    "laiva": "laivoja", "vene": "veneitä", "pyörä": "pyöriä", "moottoripyörä": "moottoripyöriä",
    "tie": "teitä", "katu": "katuja", "polku": "polkuja", "silta": "siltoja",
    "tunneli": "tunneleita", "asema": "asemia", "satama": "satamia", "tori": "toreja",
    "puisto": "puistoja", "kaupunki": "kaupunkeja", "kylä": "kyliä", "keskusta": "keskustoja",
    "kauppa": "kauppoja", "pankki": "pankkeja", "sairaala": "sairaaloita", "koulu": "kouluja",
    "kirkko": "kirkkoja", "tehdas": "tehtaita", "hotelli": "hotelleja",
    "ravintola": "ravintoloita", "kahvila": "kahviloita", "museo": "museoita",
    "kirjasto": "kirjastoja", "teatteri": "teattereita", "apteekki": "apteekkeja",
    "lentokenttä": "lentokenttiä", "laituri": "laitureita", "kiitotie": "kiitoteitä",
    "opas": "oppaita", "kartta": "karttoja", "suunta": "suuntia", "rekka": "rekkoja",
    "paku": "pakuja", "traktori": "traktoreita", "mopo": "mopoja", "ratikka": "ratikoita",
    "metro": "metroja", "helikopteri": "helikoptereita", "purjevene": "purjeveneitä",
    "soutuvene": "soutuveneitä", "liikennemerkki": "liikennemerkkejä",
    "liikennevalo": "liikennevaloja", "suojatie": "suojateitä", "pysäkki": "pysäkkejä",
    "parkkipaikka": "parkkipaikkoja", "autotalli": "autotalleja", "pilvenpiirtäjä": "pilvenpiirtäjiä",
    "mökki": "mökkejä", "talli": "talleja", "navetta": "navettoja", "lato": "latoja",
    "aita": "aitoja", "portti": "portteja", "penkki": "penkkejä", "patsas": "patsaita",
    "suihkulähde": "suihkulähteitä",

    # --- FOOD & INGREDIENTS ---
    "makkara": "makkaroita", "peruna": "perunoita", "vihannes": "vihanneksia",
    "hedelmä": "hedelmiä", "omena": "omenoita", "banaani": "banaaneja", "sipuli": "sipuleita",
    "valkosipuli": "valkosipuleita", "porkkana": "porkkanoita", "kurkku": "kurkkuja",
    "tomaatti": "tomaatteja", "paprika": "paprikoita", "salaatti": "salaatteja",
    "kaali": "kaaleja", "herne": "herneitä", "papu": "papuja", "maissi": "maisseja",
    "päärynä": "päärynöitä", "luumu": "luumuja", "viinirypäle": "viinirypäleitä",
    "mansikka": "mansikoita", "mustikka": "mustikka", "vadelma": "vadelmia",
    "sitruuna": "sitruunoita", "pähkinä": "pähkinöitä", "siemen": "siemeniä",
    "leivonnainen": "leivonnaisia", "kakku": "kakkuja", "keksi": "keksejä",
    "leipä": "leipiä", "sämpylä": "sämpylöitä", "piirakka": "piirakoita",
    "munkki": "munkkeja", "pulla": "pullia", "voileipä": "voileipiä",
    "hampurilainen": "hampurilaisia", "pizza": "pizzoja", "kananmuna": "kananmunia",
    "lihapulla": "lihapullia", "nakki": "nakkeja", "pihvi": "pihvejä",
    "kyljys": "kyljyksiä", "koipi": "koipia", "filee": "fileitä", "katkarapu": "katkarapuja",
    "oliivi": "oliiveja", "kapris": "kapriksia", "retiisi": "retiisejä", "parsa": "parsoja",
    "kukkakaali": "kukkakaaleja", "parsakaali": "parsakaaleja", "munakoiso": "munakoisoja",
    "kesäkurpitsa": "kesäkurpitsoja",

    # --- MEDIA, OFFICE & TOOLS ---
    "opiskelija": "opiskelijoita", "opettaja": "opettajia", "rehtori": "rehtoreita",
    "luokka": "luokkia", "kurssi": "kursseja", "koe": "kokeita", "arvosana": "arvosanoja",
    "kynä": "kyniä", "lyijykynä": "lyijykyniä", "pyyhekumi": "pyyhekumeja",
    "viivatin": "viivaimia", "vihko": "vihkoja", "kirja": "kirjoja", "sanakirja": "sanakirjoja",
    "tussi": "tusseja", "liitu": "liituja", "ammatti": "ammatteja", "kokous": "kokouksia",
    "sopimus": "sopimuksia", "asiakas": "asiakkaita", "pomo": "pomoja",
    "työpaikka": "työpaikkoja", "yritys": "yrityksiä", "sanomalehti": "sanomalehtiä",
    "aikakauslehti": "aikakauslehtiä", "mainos": "mainoksia", "näyttö": "näyttöjä",
    "näppäimistö": "näppäimistöjä", "hiiri": "hiiriä", "tulostin": "tulostimia",
    "laturi": "latureita", "kaapeli": "kaapeleita", "kaiutin": "kaiuttimia",
    "kaukosäädin": "kaukosäätimiä", "sovellus": "sovelluksia", "tiedosto": "tiedostoja",
    "kansio": "kansioita", "salasana": "salasanoja", "viesti": "viestejä",
    "mittanauha": "mittanauhoja", "todistus": "todistuksia", "tutkinto": "tutkintoja",
    "yliopisto": "yliopistoja", "lasku": "laskuja", "kuitti": "kuitteja",
    "allekirjoitus": "allekirjoituksia", "vankila": "vankiloita", "nitoja": "nitojia",
    "klemmari": "klemmareita", "teippirulla": "teippirullia", "kirjekuori": "kirjekuoria",
    "postimerkki": "postimerkkejä", "kalenteri": "kalentereita",
    "muistilehtiö": "muistilehtiöitä", "piirustus": "piirustuksia", "valokuva": "valokuvia",
    "maalaus": "maalauksia", "veistos": "veistoksia", "kamera": "kameroita",
    "objektiivi": "objektiiveja", "jalusta": "jalustoja", "mikrofoni": "mikrofoneja",
    "kuuloke": "kuulokkeita", "levy": "levyjä", "muistitikku": "muistitikkuja",
    "reititin": "reitittimiä",

    # --- TIME & ABSTRACT ---
    "sekunti": "sekunteja", "minuutti": "minuutteja", "tunti": "tunteja", "päivä": "päiviä",
    "viikko": "viikkoja", "kuukausi": "kuukausia", "vuosi": "vuosia", "vuosisata": "vuosisatoja",
    "aamu": "aamuja", "ilta": "iltoja", "yö": "öitä", "maanantai": "maanantaita",
    "tiistai": "tiistaita", "keskiviikko": "keskiviikkoja", "torstai": "torstaita",
    "perjantai": "perjantaita", "lauantai": "lauantaita", "sunnuntai": "sunnuntaita",
    "asia": "asioita", "sana": "sanoja", "nimi": "nimiä", "numero": "numeroita",
    "ongelma": "ongelmia", "vastaus": "vastauksia", "kysymys": "kysymyksiä", "muisto": "muistoja",
    "uni": "unia", "ajatus": "ajatuksia", "liike": "liikkeitä", "matka": "matkoja",
    "peli": "pelejä", "voitto": "voittoja", "häviö": "häviöitä", "muoto": "muotoja",
    "tauko": "taukoja", "hetki": "hetkiä", "tapahtuma": "tapahtumia", "juhla": "juhlia",
    "esitys": "esityksiä", "näyttely": "näyttelyitä", "konsertti": "konsertteja",
    "elokuva": "elokuvia", "sarja": "sarjoja", "jakso": "jaksoja", "luku": "lukuja",
    "sivu": "sivuja", "virhe": "virheitä", "sääntö": "sääntöjä", "laki": "lakeja",
    "oikeus": "oikeuksia", "velvollisuus": "velvollisuuksia", "tehtävä": "tehtäviä",
    "projekti": "projekteja", "suunnitelma": "suunnitelmia", "idea": "ideoita",
    "unelma": "unelmia", "toive": "toiveita", "pelko": "pelkoja", "salaisuus": "salaisuuksia",
    "vitsi": "vitsejä", "tarina": "tarinoita", "runo": "runoja", "laulu": "lauluja",
    "nuotti": "nuotteja", "sointu": "sointuja", "rytmi": "rytmejä",

    # --- PROFESSIONS ---
    "lääkäri": "lääkäreitä", "hoitaja": "hoitajia", "poliisi": "poliiseja",
    "palomies": "palomiehiä", "sotilas": "sotilaita", "lentäjä": "lentäjiä",
    "kapteeni": "kapteeneja", "kuljettaja": "kuljettajia", "kokki": "kokkeja",
    "tarjoilija": "tarjoilijoita", "myyjä": "myyjiä", "siivooja": "siivoojia",
    "insinööri": "insinöörejä", "arkkitehti": "arkkitehteja", "ohjelmoija": "ohjelmoijia",
    "taitaja": "taitajia", "taiteilija": "taiteilijoita", "muusikko": "muusikoita",
    "näyttelijä": "näyttelijöitä", "ohjaaja": "ohjaajia", "toimittaja": "toimittajia",
    "kirjailija": "kirjailijoita", "runoilija": "runoilijoita", "tutkija": "tutkijoita",
    "tiedemies": "tiedemiehiä", "lakimies": "lakimiehiä", "tuomari": "tuomareita",
    "pappi": "pappeja", "piispa": "piispoja", "kuningas": "kuninkaita",
    "kuningatar": "kuningattaria", "presidentti": "presidenttejä", "ministeri": "ministereitä",
   "edustaja": "edustajia", "johtaja": "johtajia",
    "työntekijä": "työntekijöitä", "harjoittelija": "harjoittelijoita",
    "asiantuntija": "asiantuntijoita", "neuvonantaja": "neuvonantajia",
   "sähköasentaja": "sähköasentajia",
    "putkiasentaja": "putkiasentajia", "muurari": "muurareita", "puuseppä": "puuseppiä",
    "leipuri": "leipureita", "parturi": "partureita", "kampaaja": "kampaajia",
    "kosmetologi": "kosmetologeja", "valokuvaaja": "valokuvaajia",

    # --- TECHNICAL & INDUSTRIAL ---
    "pumppu": "pumppuja", "moottori": "moottoreita", "turbiini": "turbiineja",
    "generaattori": "generaattoreita", "muuntaja": "muuntajia", "venttiili": "venttiilejä",
    "putki": "putkia", "johto": "johtoja", "kaapeli": "kaapeleita", "kytkin": "kytkimiä",
    "anturi": "antureita", "mittari": "mittareita", "robotti": "robotteja", "siru": "siruja",
    "prosessori": "prosessoreita", "kovalevy": "kovalevyjä", "virtalähde": "virtalähteitä",
    "jäähdytin": "jäähdyttimiä", "tuuletin": "tuulettimia", "suodatin": "suodattimia",
    "tiiviste": "tiivisteitä", "laakeri": "laakereita", "hammaspyörä": "hammaspyöriä",
    "ketju": "ketjuja", "vipu": "vipuja", "jousi": "jousia", "pultti": "pultteja",
    "mutteri": "muttereita", "prikka": "prikkoja", "niitti": "niittejä",
    "hitsaussauma": "hitsaussaumoja", "teline": "telineitä", "nosturi": "nostureita",
    "trukki": "trukkeja", "kontti": "kontteja", "lava": "lavoja", "mutteriavain": "mutteriavaimia",
    "ruuvitaltta": "ruuvitalttoja", "pora": "poria", "hiomakone": "hiomakoneita",
    "sirkkeli": "sirkkeleitä", "höylä": "höyliä", "taltta": "talttoja", "viila": "viiloja",
    "leka": "lekoja", "sorkkarauta": "sorkkarautoja", "lapio": "lapioita", "hanko": "hankoja",
    "viikate": "viikatteita", "sirppi": "sirppejä", "kottikärry": "kottikärryjä",
    "kompressori": "kompressoreita", "hitsikone": "hitsikoneita", "sorvi": "sorveja",
    "jyrsin": "jyrsimiä", "painepesuri": "painepesureita", "ruohonleikkuri": "ruohonleikkureita",
    "lehtipuhallin": "lehtipuhaltimia", "lumilinko": "lumilinkoja", "aggregaatti": "aggregaatteja",
    "rele": "releitä", "vastus": "vastuksia", "kondensaattori": "kondensaattoreita",
    "diodi": "diodeja", "transistori": "transistoreita", "piirilevy": "piirilevyjä",
    "antenni": "antenneja", "satelliitti": "satelliitteja", "kaukoputki": "kaukoputkia",
    "mikroskooppi": "mikroskooppeja", "laboratoriotakki": "laboratoriotakkeja",
    "koeputki": "koeputkia", "pipetti": "pipettejä", "vaaka": "vaakoja",
    "lämpömittari": "lämpömittareita", "verenpainemittari": "verenpainemittareita",
    "stetoskooppi": "stetoskooppeja", "ruisku": "ruiskuja", "laastari": "laastareita",
    "sideharsorulla": "sideharsorullia", "pyörätuoli": "pyörätuoleja", "kipsi": "kipsejä",
    "tekohammas": "tekohampaita", "kuulolaite": "kuulolaitteita",
    "silmälasinsanka": "silmälasinsankoja", "piilolinssi": "piilolinssejä",
    "hammasrauta": "hammasrautoja", "tutti": "tutteja", "vaippa": "vaippoja",
    "vaunu": "vaunuja", "ratas": "rattaita", "keinu": "keinuja", "liukumäki": "liukumäkiä",
    "hiekkalaatikko": "hiekkalaatikoita", "kiipeilyteline": "kiipeilytelineitä",
    "lippu": "lippuja", "viiri": "viirejä", "kilpi": "kilpiä", "miekka": "miekkoja",
    "nuoli": "nuolia", "keihäs": "keihäitä", "kanuuna": "kanuunoita",
    "panssarivaunu": "panssarivaunuja", "sukellusvene": "sukellusveneitä",
    "laskuvarjo": "laskuvarjoja", "kuumailmapallo": "kuumailmapalloja",
    "avaruusalus": "avaruusaluksia", "raketti": "raketteja", "komeetta": "komeettoja",
    "asteroidi": "asteroideja", "galaksi": "galakseja",
    "sumu": "sumuja", "tähdenlento": "tähdenlentoja", "tee":"teitä","juusto":"juustoja","voi":"voita","sokeri":"sokereita","maito":"maitoja",

"ovi":"ovia","sormi":"sormia","polvi":"polvia","silmä":"silmiä","hammas":"hampaita",
"jalka":"jalkoja","kävely":"kävelyjä","hyppy":"hyppyjä","lento":"lentoja",

"ystävällinen":"ystävällisiä","iloinen":"iloisia","surullinen":"surullisia",
"kaunis":"kauniita","ruma":"rumia","nopea":"nopeita","hidas":"hitaita",

"kirje":"kirjeitä","laite":"laitteita","huone":"huoneita","kone":"koneita",
"perhe":"perheitä","vene":"veneitä","lause":"lauseita","alue":"alueita",

"päivä":"päiviä","viikko":"viikkoja","kuukausi":"kuukausia","vuosi":"vuosia",
"hetki":"hetkiä","aika":"aikoja",

"musiikki":"musiikkeja","taide":"taiteita","historia":"historioita","fysiikka":"fysiikkoja",

"opettaja":"opettajia","johtaja":"johtajia","pelaaja":"pelaajia",
"kirjailija":"kirjailijoita","lukija":"lukijoita","kuuntelija":"kuuntelijoita",

"pankki":"pankkeja","merkki":"merkkejä","hylly":"hyllyjä","katto":"kattoja",

"tori":"toreja","meri":"meriä","veri":"veriä","uni":"unia","onni":"onnia",

"peli":"pelejä","laki":"lakeja","sää":"säitä","tie":"teitä","yö":"öitä",

"ruoka":"ruokia","juoma":"juomia","kahvila":"kahviloita","ravintola":"ravintoloita",

"lentokenttä":"lentokenttiä","rautatieasema":"rautatieasemia",
"kauppakeskus":"kauppakeskuksia","linja-autoasema":"linja-autoasemia",

"työpaikka":"työpaikkoja","toimisto":"toimistoja","yritys":"yrityksiä",

"harjoitus":"harjoituksia","kysymys":"kysymyksiä","vastaus":"vastauksia",

"tapahtuma":"tapahtumia","kokemus":"kokemuksia","elämys":"elämyksiä",

"pöytäliina":"pöytäliinoja","kirjahylly":"kirjahyllyjä","tietokoneohjelma":"tietokoneohjelmia",
    "talo":"taloja","kukka":"kukkia","kenkä":"kenkiä","leipä":"leipiä","maa":"maita",
    "puu":"puita","tie":"teitä","yö":"öitä","koulu":"kouluja","omena":"omenoita",
    "kirja":"kirjoja","kala":"kaloja","tyttö":"tyttöjä","lapsi":"lapsia","mies":"miehiä",
    "nainen":"naisia","rikas":"rikkaita","kaunis":"kauniita","järvi":"järviä","kivi":"kiviä",
    "käsi":"käsiä","vesi":"vesiä","kieli":"kieliä","ahven":"ahvenia","perhe":"perheitä",
    "ystävä":"ystäviä","opettaja":"opettajia","opiskelija":"opiskelijoita","auto":"autoja",
    "juna":"junia","lentokone":"lentokoneita","kauppa":"kauppoja","kaupunki":"kaupunkeja",
    "kylä":"kyliä","sydän":"sydämiä","pöytä":"pöytiä","tuoli":"tuoleja","ovi":"ovia",
    "ikkuna":"ikkunoita","koira":"koiria","kissa":"kissoja","hevonen":"hevosia","lintu":"lintuja",
    "puhelin":"puhelimia","numero":"numeroita","kirjasto":"kirjastoja","sairaala":"sairaaloita",
    "ravintola":"ravintoloita","hotelli":"hotelleja","työhuone":"työhuoneita","sähköposti":"sähköposteja",

    # i-type
    "lumi":"lumia","susi":"susia","kansi":"kansia","hirsi":"hirsiä","varsi":"varsia",
    "veitsi":"veitsiä","kurki":"kurkia","särki":"särkiä","järki":"järkiä","merkki":"merkkejä",

    # -nen
    "ihminen":"ihmisiä","suomalainen":"suomalaisia","punainen":"punaisia","sininen":"sinisiä",

    # -us / -ys
    "rakkaus":"rakkauksia","kauneus":"kauneuksia","kysymys":"kysymyksiä","vastaus":"vastauksia",

    # compounds
    "kirjekuori":"kirjekuoria","tietokone":"tietokoneita","vesipullo":"vesipulloja",
    "autokauppa":"autokauppoja","kirjahylly":"kirjahyllyjä","koulukirja":"koulukirjoja",
    "talonmies":"talonmiehiä","yövuoro":"yövuoroja","kesäloma":"kesälomia","talvitakki":"talvitakkeja",
    "pääkaupunki":"pääkaupunkeja","linja-auto":"linja-autoja","sähköjohto":"sähköjohtoja",
    "puutarha":"puutarhoja","lentokenttä":"lentokenttiä","vesihana":"vesihanoja",
    "kirjoituspöytä":"kirjoituspöytiä","tietoverkko":"tietoverkkoja","matkapuhelin":"matkapuhelimia",
    "työpäivä":"työpäiviä","opintotuki":"opintotukia","sähkölasku":"sähkölaskuja",
    "pankkitili":"pankkitilejä","postilaatikko":"postilaatikoita","sanomalehti":"sanomalehtiä",
    "elokuvateatteri":"elokuvateattereita","kahvikuppi":"kahvikuppeja","vesilasi":"vesilaseja",
  "aamu": "aamuja", "aamupäivä": "aamupäiviä", "aavikko": "aavikoita", "aihe": "aiheita", "aika": "aikoja", "aita": "aitoja", "aitous": "aitouksia", "ajatus": "ajatuksia", "ala": "aloja", "alku": "alkuja", "allas": "altaita", "alusvaate": "alusvaatteita", "amme": "ammeita", "ammatti": "ammatteja", "angervo": "angervoja", "ankka": "ankkoja", "annos": "annoksia", "ansio": "ansioita", "apu": "apuja", "apteekki": "apteekkeja", "arabia": "arabioita", "arvosana": "arvosanoja", "asema": "asemia", "asia": "asioita", "asiakas": "asiakkaita", "asunto": "asuntoja", "atomi": "atomeja", "aukio": "aukioita", "aurinko": "aurinkoja", "auto": "autoja", "avain": "avaimia", "avanto": "avantoja", "avaruus": "avaruuksia", "banaani": "banaaneja", "betoni": "betoneja", "bussi": "busseja", "elokuva": "elokuvia", "elokuvateatteri": "elokuvateattereita", "elämä": "elämiä", "emäntä": "emäntiä", "eno": "enoja", "erä": "eriä", "eteinen": "eteisiä", "etelä": "eteliä", "etu": "etuja", "filmi": "filmejä", "hame": "hameita", "hammas": "hampaita", "hana": "hanoja", "harja": "harjoja", "hattu": "hattuja", "hedelmä": "hedelmiä", "hella": "helloja", "henkilö": "henkilöitä", "hetki": "hetkiä", "hevonen": "hevosia", "hiili": "hiiliä", "hiekka": "hiekkoja", "hinta": "hintoja", "hopea": "hopeita", "hotelli": "hotelleja", "huivi": "huiveja", "huone": "huoneita", "huuli": "huulia", "huuhtelu": "huuhteluja", "hyvyys": "hyvyyksiä", "hyvänlaatuinen": "hyvänlaatuisia", "hyödyke": "hyödykkeitä", "hyönteinen": "hyönteisiä", "hölkkä": "hölkkiä", "hylly": "hyllyjä", "ihminen": "ihmisiä", "iho": "ihoja", "ikkuna": "ikkunoita", "ilta": "iltoja", "iltapäivä": "iltapäiviä", "ilo": "iloja", "isoisä": "isoisiä", "isoisä": "isoisiä", "isoäiti": "isoäitejä", "isäntä": "isäntiä", "isä": "isiä", "itä": "itiä", "jalka": "jalkoja", "jauho": "jauhoja", "johtaja": "johtajia", "joki": "jokia", "joukko": "joukkoja", "joulu": "jouluja", "juoma": "juomia", "juuri": "juuria", "juusto": "juustoja", "jäätelö": "jäätelöitä", "jää": "jäitä", "jänis": "jäniksiä", "järvi": "järviä", "kaappi": "kaappeja", "kaapu": "kaapuja", "kaava": "kaavoja", "kahvi": "kahveja", "kahvila": "kahviloita", "kaivo": "kaivoja", "kala": "kaloja", "kalastus": "kalastuksia", "kalleus": "kalleuksia", "kallio": "kallioita", "kana": "kanoja", "kanava": "kanavia", "kangas": "kankaita", "kansi": "kansia", "kansa": "kansoja", "kappale": "kappaleita", "karhu": "karhuja", "kartano": "kartanoja", "kassi": "kasseja", "kastike": "kastikkeita", "katto": "kattoja", "katu": "katuja", "kaula": "kauloja", "kauneus": "kauneuksia", "kauppa": "kauppoja", "kaupunki": "kaupunkeja", "keikka": "keikkoja", "keittiö": "keittiöitä", "kello": "kelloja", "kenkä": "kenkiä", "keskiviikko": "keskiviikkoja", "keskiyö": "keskiöitä", "keskusta": "keskustoja", "kesä": "kesiä", "kesäkuu": "kesäkuita", "ketju": "ketjuja", "kettu": "kettuja", "keuhko": "keuhkoja", "kevät": "keväitä", "kievari": "kievareita", "kiitos": "kiitoksia", "kipu": "kipuja", "kirja": "kirjoja", "kirjasto": "kirjastoja", "kirkko": "kirkkoja", "kissa": "kissoja", "kitara": "kitaroita", "kiuas": "kiukaita", "kivi": "kiviä", "koe": "kokeita", "koira": "koiria", "koivu": "koivuja", "kokous": "kokouksia", "kolikko": "kolikoita", "kone": "koneita", "korkeus": "korkeuksia", "korva": "korvia", "kosketus": "kosketuksia", "koski": "koskia", "koti": "koteja", "koulu": "kouluja", "kuitu": "kuituja", "kukka": "kukkia", "kukkula": "kukkuloita", "kulho": "kulhoja", "kulta": "kultia", "kulma": "kulmia", "kuningatar": "kuningattaria", "kunnia": "kunnioita", "kuukausi": "kuukausia", "kuulo": "kuuloja", "kuunloiste": "kuunloisteita", "kuuppa": "kuuppia", "kuppi": "kuppeja", "kurkku": "kurkkuja", "kurssi": "kursseja", "kuva": "kuvia", "kylpylä": "kylpylöitä", "kylpyhuone": "kylpyhuoneita", "kylä": "kyliä", "kynä": "kyniä", "kyse": "kyseitä", "kysymys": "kysymyksiä", "käsine": "käsineitä", "käsivarsi": "käsivarsia", "käsi": "käsiä", "käärme": "käärmeitä", "laakso": "laaksoja", "laatikko": "laatikoita", "lahja": "lahjoja", "lahti": "lahtia", "laiva": "laivoja", "laki": "lakeja", "lammas": "lampaita", "lamppu": "lamppuja", "lampi": "lampia", "lanka": "lankoja", "lapsi": "lapsia", "lasi": "laseja", "lattia": "lattioita", "laukku": "laukkuja", "laulu": "lauluja", "lautanen": "lautasia", "lehmä": "lehmiä", "lehti": "lehtiä", "leikki": "leikkejä", "leipä": "leipiä", "lelu": "leluja", "lentokenttä": "lentokenttiä", "lentokone": "lentokoneita", "leveys": "leveyksiä", "lihas": "lihaksia", "liike": "liikkeitä", "liitos": "liitoksia", "liittyvä": "liittyviä", "linna": "linnoja", "lintu": "lintuja", "loma": "lomia", "lompakko": "lompakoita", "loppu": "loppuja", "lukio": "lukioita", "lukko": "lukkoja", "luku": "lukuja", "lumi": "lumia", "luokka": "luokkia", "luola": "luolia", "luomu": "luomuja", "luonto": "luontoja", "luoto": "luotoja", "lusikka": "lusikoita", "luu": "luita", "läheinen": "läheisiä", "lähde": "lähteitä", "lääke": "lääkkeitä", "länsi": "länsiä", "maa": "maita", "maailma": "maailmoja", "maaliskuu": "maaliskuita", "maito": "maitoja", "makkara": "makkaroita", "maku": "makuja", "makuuhuone": "makuuhuoneita", "marja": "marjoja", "matka": "matkoja", "matkalaukku": "matkalaukkuja", "matto": "mattoja", "mehu": "mehuja", "mekko": "mekkoja", "melu": "meluja", "meri": "meriä", "metsä": "metsiä", "metsästys": "metsästyksiä", "mies": "miehiä", "mieli": "mieliä", "minuutti": "minuutteja", "moottoripyörä": "moottoripyöriä", "muisto": "muistoja", "muna": "munia", "muoto": "muotoja", "musiikki": "musiikkeja", "mustikka": "mustikoita", "mutka": "mutkia", "muovi": "muoveja", "myymälä": "myymälöitä", "mäki": "mäkiä", "määrä": "määriä", "naama": "naamoja", "nainen": "naisia", "nappi": "nappeja", "naula": "nauloja", "neula": "neuloja", "niemi": "niemiä", "niitty": "niittyjä", "nimi": "nimiä", "nopeus": "nopeuksia", "nukke": "nukkeja", "numero": "numeroita", "näkymä": "näkymiä", "näkö": "näköjä", "ohje": "ohjeita", "oikea": "oikeita", "oikeus": "oikeuksia", "oja": "ojia", "oksa": "oksia", "olkapää": "olkapäitä", "olohuone": "olohuoneita", "olut": "oluita", "omena": "omenoita", "ongelma": "ongelmia", "onni": "onnia", "opettaja": "opettajia", "opisto": "opistoja", "oppilas": "oppilaita", "osa": "osia", "ovi": "ovia", "paikka": "paikkoja", "paita": "paitoja", "pallo": "palloja", "palkka": "palkkoja", "pankki": "pankkeja", "pannu": "pannuja", "paperi": "papereita", "pari": "pareja", "parveke": "parvekkeita", "patsas": "patsaita", "peili": "peilejä", "pelto": "peltoja", "perhe": "perheitä", "peruna": "perunoita", "piha": "pihoja", "pilvi": "pilviä", "pimento": "pimentoja", "pinta": "pintoja", "pipo": "pipoja", "piste": "pisteitä", "pituus": "pituuksia", "poika": "poikia", "poliisi": "poliiseja", "polvi": "polvia", "porras": "portaita", "posti": "posteja", "projekti": "projekteja", "puhelin": "puhelimia", "puro": "puroja", "pussi": "pusseja", "puu": "puita", "puutarha": "puutarhoja", "pyörä": "pyöriä", "pää": "päitä", "pääsiäinen": "pääsiäisiä", "pöly": "pölyjä", "pöytä": "pöytiä", "raha": "rahoja", "raja": "rajoja", "rakkaus": "rakkauksia", "ranta": "rantoja", "ratkaisu": "ratkaisuja", "rauta": "rautoja", "ravintola": "ravintoloita", "reppu": "reppuja", "reuna": "reunoja", "riisi": "riisejä", "rinta": "rintoja", "roska": "roskia", "ruoka": "ruokia", "rumpu": "rumpuja", "runo": "runoja", "ruoho": "ruohoja", "ruuvi": "ruuveja", "ryhmä": "ryhmiä", "saari": "saaria", "saapas": "saappaita", "sade": "sateita", "saha": "sahoja", "sairaala": "sairaaloita", "salkku": "salkkuja", "salmi": "salmia", "sana": "sanoja", "sateenvarjo": "sateenvarjoja", "satama": "satamia", "sauna": "saunoja", "savu": "savuja", "seinä": "seiniä", "sekunti": "sekunteja", "selkä": "selkiä", "serkku": "serkkuja", "seteli": "setelejä", "sieni": "sieniä", "sika": "sikoja", "silta": "siltoja", "silmä": "silmiä", "sisar": "sisaria", "sisältö": "sisältöjä", "sisko": "siskoja", "sohva": "sohvia", "soitin": "soittimia", "sokeri": "sokereita", "solu": "soluja", "sormi": "sormia", "sormus": "sormuksia", "suku": "sukuja", "summa": "summia", "suo": "soita", "suola": "suoloja", "suunta": "suuntia", "suru": "suruja", "susi": "susia", "suu": "suita", "sydän": "sydämiä", "syksy": "syksyjä", "syntymäpäivä": "syntymäpäiviä", "syvyys": "syvyyksiä", "sänky": "sänkyjä", "taide": "taiteita", "taivas": "taivaita", "takka": "takkoja", "takki": "takkeja", "talo": "taloja", "talvi": "talvia", "tapa": "tapoja", "tarina": "tarinoita", "tasku": "taskuja", "taulu": "tauluja", "tauti": "tauteja", "tehdas": "tehtaita", "tehtävä": "tehtäviä", "televisio": "televisioita", "tie": "teitä", "tieto": "tietoja", "tietokone": "tietokoneita", "tiili": "tiiliä", "tiimi": "tiimejä", "tila": "tiloja", "toimisto": "toimistoja", "tori": "toreja", "torvi": "torvia", "totuus": "totuuksia", "tuli": "tulia", "tunneli": "tunneleja", "tunne": "tunteita", "tunti": "tunteja", "tunturi": "tuntureita", "tuoli": "tuoleja", "tuuli": "tuulia", "tyttö": "tyttöjä", "tytär": "tyttäriä", "työ": "töitä", "työkalu": "työkaluja", "tähti": "tähtiä", "täti": "tätejä", "ukkonen": "ukkosia", "uni": "unia", "unelma": "unelmia", "uuni": "uuneja", "vaara": "vaaroja", "vaate": "vaatteita", "vaippa": "vaippoja", "vaimo": "vaimoja", "valo": "valoja", "valtameri": "valtameriä", "valta": "valtoja", "valtio": "valtioita", "varasto": "varastoja", "varvas": "varpaita", "vasara": "vasaroita", "vastaus": "vastauksia", "vatsa": "vatsoja", "vauva": "vauvoja", "veitsi": "veitsiä", "veli": "veljiä", "vene": "veneitä", "veri": "veriä", "verho": "verhoja", "vesi": "vesiä", "viikko": "viikkoja", "viini": "viinejä", "viiva": "viivoja", "vihannes": "vihanneksia", "vihko": "vihkoja", "viina": "viinoja", "virasto": "virastoja", "virhe": "virheitä", "viulu": "viuluja", "voima": "voimia", "vuori": "vuoria", "vuosi": "vuosia", "vyö": "vöitä", "ympyrä": "ympyröitä", "ystävä": "ystäviä", "yö": "öitä", "ääni": "ääniä"

}

    print("---- Singular tests ----")
    total_sg = 0
    correct_sg = 0
    
    for word, expected in tests_sg.items():
        result = partitive_sg(word)
        total_sg += 1
        if result == expected:
            correct_sg += 1
        else:
            print(f"❌ {word} → {result} (should be {expected})")

    print("\n---- Plural tests ----")
    total_pl = 0
    correct_pl = 0
    
    for word, expected in tests_pl.items():
        result = partitive_pl(word)
        total_pl += 1
        if result == expected:
            correct_pl += 1
        else:
            print(f"❌ {word} → {result} (should be {expected})")

    total = total_sg + total_pl
    correct = correct_sg + correct_pl
    
    print("\n--- Summary ---")
    if correct == total:
        print("✅ Everything looks perfect!")
    
    print(f"Result: {correct}/{total} correct ({(correct/total)*100:.2f}%)")

if False:
    main()
else:
    run_tests()


#Change To git hub