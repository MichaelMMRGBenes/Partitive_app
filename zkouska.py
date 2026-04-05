WORDS = [
    # --- Příroda a zvířata ---
    "koira", "kissa", "hevonen", "lehmä", "lammas", "sika", "karhu", "susi", "kettu", "jänis",
    "lintu", "kala", "käärme", "hyönteinen", "puu", "kukka", "metsä", "järvi", "meri", "joki",
    "vuori", "mäki", "saari", "niemi", "ranta", "taivas", "aurinko", "kuu", "tähti", "pilvi",
    "sade", "lumi", "jää", "tuuli", "ukkonen", "kivi", "hiekka", "multa", "ruoho",
    "lehti", "oksa", "juuri", "marja", "sieni", "puro", "lähde", "suo", "tunturi", "luonto",
    
    # --- Lidé a rodina ---
    "mies", "nainen", "lapsi", "poika", "tyttö", "vauva", "isä", "äiti", "veli", "sisko",
    "poika", "tytär", "isoäiti", "isoisä", "serkku", "täti", "setä", "eno", "perhe", "suku",
    "ystävä", "naapuri", "ihminen", "henkilö", "vieras", "isäntä", "emäntä", "vaimo", "mies", "pari",
    
    # --- Tělo ---
    "pää", "silmä", "korva", "nenä", "suu", "huuli", "hammas", "kieli", "kaula",
    "kurkku", "olkapää", "käsivarsi", "käsi", "sormi", "kynsi", "rinta", "vatsa", "selkä", "jalka",
    "polvi", "varvas", "iho", "luu", "veri", "sydän", "keuhko", "lihas", "naama",
    
    # --- Dům a domácnost ---
    "talo", "koti", "asunto", "huone", "keittiö", "kylpyhuone", "makuuhuone", "olohuone", "eteinen", "parveke",
    "piha", "ovi", "ikkuna", "seinä", "katto", "lattia", "porras", "lukko", "avain", "pöytä",
    "tuoli", "sänky", "sohva", "kaappi", "hylly", "lamppu", "matto", "verho", "peili", "taulu",
    "kello", "radio", "televisio", "tietokone", "puhelin", "kone", "uuni", "hella", "kaappi", "allas",
    
    # --- Kuchyně a jídlo ---
    "ruoka", "juoma", "vesi", "maito", "kahvi", "tee", "mehu", "olut", "viini", "leipä",
    "voi", "juusto", "liha", "kala", "kana", "muna", "makkara", "peruna", "riisi", "pasta",
    "vihannes", "hedelmä", "omena", "banaani", "marja", "suola", "sokeri", "jauho", "öljy", "kastike",
    "lautanen", "kulho", "lasi", "muki", "kuppi", "veitsi", "haarukka", "lusikka", "kattila", "pannu",
    
    # --- Oblečení ---
    "vaate", "paita",  "hame", "mekko", "takki", "pipo", "hattu", "huivi", "käsine",
    "sukka", "kenkä", "saapas", "alusvaate", "vyö", "solmio", "nappi", "tasku", "vetoketju", "sateenvarjo",
    
    # --- Doprava a město ---
    "auto", "bussi", "juna", "lentokone", "laiva", "vene", "pyörä", "moottoripyörä", "tie", "katu",
    "polku", "silta", "tunneli", "asema", "satama", "lentoke", "tori", "puisto", "kaupunki", "kylä",
    "maa", "valtio", "raja", "keskusta", "kauppa", "pankki", "sairaala", "koulu", "kirkko", "tehdas",
    "hotelli", "ravintola", "kahvila", "elokuvateatteri", "museo", "kirjasto", "teatteri", "poliisi", "posti", "apteekki",
    
    # --- Čas a kalendář ---
    "aika", "hetki", "sekunti", "minuutti", "tunti", "päivä", "viikko", "kuukausi", "vuosi", "vuosisata",
    "aamu", "päivä", "ilta", "yö", "aamupäivä", "iltapäivä", "keskiyö", "maanantai", "tiistai", "keskiviikko",
    "torstai", "perjantai", "lauantai", "sunnuntai", "tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu",
    "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu", "kevät", "kesä", "syys", "talvi",
    
    # --- Abstraktní a ostatní ---
    "asia", "sana", "nimi", "luku", "numero", "väri", "muoto", "ääni", "valo", "pimeys",
    "elämä", "kuolema", "onni", "rakkaus", "viha", "pelko", "ilo", "suru", "työ", "leikki",
    "peli", "urheilu", "musiikki", "taide", "kirja", "lehti", "kuva", "elokuva", "uutinen", "tieto",
    "ajatus", "mieli", "sielu", "voima", "valta", "laki", "oikeus", "raha", "hinta", "palkka",
    "lahja", "ongelma", "vastaus", "kysymys", "syy", "seuraus", "tapa", "mahdollisuus", "virhe", "totuus",
    
    # --- Škola a práce ---
    "opettaja", "oppilas", "luokka", "kynä", "paperi", "vihko", "laukku", "tehtävä", "koe", "arvosana",
    "yliopisto", "kurssi", "ammatti", "johtaja", "työntekijä", "toimisto", "kokous", "asiakas", "projekti", "suunnitelma",
    
    # --- Materiály a předměty ---
    "metalli", "rauta", "kulta", "hopea", "lasi", "muovi", "puu", "paperi", "kangas", "nahka",
    "kivi", "tiili", "betoni", "roska", "jäte", "pöly", "savu", "tuli", "liekki", "hiili",
    
    # --- Další podstatná jména ---
    "kone", "laite", "työkalu", "vasara", "saha", "naula", "ruuvi", "neula", "lanka",
    "pallo", "lelu", "kortti", "raha", "kolikko", "seteli", "lompakko", "kassi", "pussi", "laatikko",
    "pullo", "tölkki", "kansi", "pohja", "reuna", "pinta", "sisältö", "osa", "kappale", "ryhmä",
    "joukko", "kansa", "kieli", "maa", "maailma", "avaruus", "planeetta", "tähti", "aurinko", "kuu",
    "metsästys", "kalastus", "matka", "loma", "juhla", "joulu", "pääsiäinen", "syntymäpäivä",
    "terveys", "tauti", "kipu", "lääke", "uni", "unelma", "muisto", "kokemus", "seikkailu", "tarina",
    "runo", "laulu", "soitin", "kitara", "piano", "rumpu", "viulu", "huilu", "torvi", "ääni",
    "melu", "hiljaisuus", "haju", "maku", "tunne", "kosketus", "näkö", "kuulo", "liike", "vauhti",
    "suunta", "pohjoinen", "etelä", "itä", "länsi", "vasen", "oikea", "ylä", "ala",
    "sisä", "ulko", "etu", "taka", "alku", "loppu", "reuna", "keskusta", "piste", "viiva",
    "kulma", "ympyrä", "neliö", "pinta-ala", "pituus", "leveys", "korkeus", "paino", "määrä", "summa",
    
    # --- Přídavná jména (použitá jako podstatná jména nebo vlastnosti) ---
    "hyvyys", "pahuus", "kauneus", "kalleus", "nopeus", "pituus", "leveys", "syvyys", "korkeus",
    "viisaus", "tyhmyys", "rehellisyys", "rohkeus", "pelkuruus", "ystävyys", "vapaus", "rauha", "sota", "voitto",
    "tappio", "vaara", "turva", "apu", "kiitos", "anteeksi", "tervehdys", "hyvästi", "onni", "menestys",
    
    # --- Různé ---
    "paita", "hame", "takki", "hattu", "sukka", "kenkä", "saapas", "huivi", "vyö",
    "sormus", "ketju", "kello",  "laukku", "reppu", "salkku", "matkalaukku", "sateenvarjo", "avain",
    "lukko", "ovi", "ikkuna", "portti", "aita", "seinä", "katto", "lattia", "katto", "uuni",
    "liesi", "allas", "hana", "suihku", "amme", "sauna", "kiuas", "löyly", "vihta", "vasta",
    "mökki", "huvila", "kartano", "linna", "torni", "kirkko", "pappila", "koulu", "opisto", "lukio",
    "yliopisto", "virasto", "tehdas", "paja", "halli", "varasto", "kauppa", "myymälä", "tori", "aukio",
    "puisto", "puutarha", "pelto", "niitty", "laidun", "metsä", "viidakko", "aavikko", "saari", "luoto",
    "vuori", "vaara", "kukkula", "laakso", "solu", "puro", "oja", "kanava", "koski", "putous",
    "lähde", "kaivo", "lampi", "järvi", "selkä", "lahti", "salmi", "meri", "valtameri", "ranta",
    "hiekka", "kivi", "kallio", "muta", "savu", "tuli", "hiili", "tuhka", "pöly", "ilma"
]

print(len(WORDS))