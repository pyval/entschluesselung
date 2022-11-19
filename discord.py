# häufigkeitsanalyse
def getFreq(text):
    # finale buchstabenzuweisung
    german_freq = [" ", "E", "N", "I", "S", "A", "R",
     "D", "T", "H", "U", "L", "C", ",", "O", 
     "M", "G", "W", "F", "B", "P", "S", "Z", 
     ".", "\"", "K", "K", "T", 
     # zweiter teil nochmal
     "V", "W", "A", "D", "E", "F",
     ":", "M", "J", "J", "I", "U", "G", "R", 
     "O", "B", "H", "-", "K", "Z", "P", "E", 
     "ß", "H", "Y", "X", "Q",] 
    # hier ist die normale buchstabenhäufigkeit
    # doppelt angewandt
    german_freq_begin = [" ", "E", "N", "I", "S", "R", "A",
     "T", "D", "H", "U", "L", "C", "G", "M", 
     "O", "B", "W", "F", "K", "Z", "P", "V", 
     "ß", "J", "Y", "X", "Q",
     # zweiter Teil nochmal
     " ", "E", "N", "I", "S", "R", "A",
     "T", "D", "H", "U", "L", "C", "G", "M", 
     "O", "B", "W", "F", "K", "Z", "P", "V", 
     "ß", "J", "Y", "X", "Q",]
    # alle großen buchstaben A-Z
    up_letters = {chr(i+65): 0 for i in range(26)}
    # alle kleinen buchstaben a-z
    lower_letters = {chr(i+97): 0 for i in range(26)}
    # spezielle symbole, welche im verschlüsselten text vorkommen und
    # gezählt werden müssen
    symbols = {",": 0, "\"": 0, "!": 0, ".": 0, "'": 0, ";": 0}
    
    # es werden alle zeichen (buchstaben groß/klein, symbole) gezählt
    for char in text:
        if char in up_letters:
            up_letters[char] += 1

        elif char in lower_letters:
            lower_letters[char] += 1
        elif char in symbols:
            symbols[char] += 1
    
    # wörterbuch als liste in der form [(key_i, value_i)] von i=0 bis n
    # key = jeweiliger buchstabe, value = jeweilige häufigkeit
    up_items = list(up_letters.items())
    low_items = list(lower_letters.items())
    sym_items = list(symbols.items())
    # alle häufigkeiten zusammengefasst
    lCountArr = up_items + low_items + sym_items
    # alle tupel umdrehen (aus (key, value) wird (value, key))
    lCountArr = [(i[1], i[0]) for i in lCountArr ]
    # häufigkeiten werden von min bis max sortiert und dann wird das feld umgedreht
    # sodass max als erstes und min als letztes ist
    lCountArr.sort()
    lCountArr.reverse()
    # feld wird in wörterbuch umgewandelt der form (key, value)
    lDict = {i[1]:i[0]  for i in lCountArr if i[0] != 0}
    possibleCase = lDict.copy()
    print(possibleCase, len(possibleCase))
    #  Den häufigsten vorkommenden buchstaben wird durch
    # häufigsten buchstaben der angegeben buchstabenhäufigkeit ersetzt
    # Wörterbuch[i] = Buchstabenhäufigkeit[i] von i=0 bis n
    i = 0
    for key in possibleCase:
        possibleCase[key] = german_freq[i]
        i += 1
    print(possibleCase)
    return possibleCase
def decode(text: str, keys: dict):
    print("\nEntschlüsselt:\n")
    cleanString = ""
    for i in text:
        if i in keys:
            cleanString += str(keys[i])
        else:
            cleanString += i
    print(cleanString)
    return cleanString

#txt2 = f',IctZMIzGokIxMUHpMtCDMtIZTMIzMTUMtI.oG,MtIZGUIFTtZIlTDITpoMtI!,tZModGxMtmIZTMIMTtMIlTDIR,dMtZkIZTMIGtZMoMIlTDIPHp"MtpMTDkIZTMIZoTDDMIlTDIwMTHpD,lkI,tZIU"IlTDIGEEMlkIzGUIG,WIZMoI!MEDIv,Iz,MtUHpMtITUDSIsEUIMEWMITpoMIPno,MHpMIMxMtIdMDGtIpGDDMtkIDoGDInE"MDvETHpIZTMIZoMTvMptDMIpMoMTtSIPTMIz"EEDMIUTHpIZGW,MoIoGMHpMtkIZGUUIUTMItTHpDIMTtdMEGZMtIzGokI,tZI"ptMI;MlGtZIv,Ido,MUUMtI"ZMoIt,oIGtv,UMpMtkIoTMWIUTMIlTDIEG,DMoIPDTllMmIJiTMIF"MtTdUD"HpDMoIU"EEIUTHpITtITpoMlIW,MtWvMptDMtIfGpoIGtIMTtMoIPnTtZMEIUDMHpMtI,tZID"DIpTtWGEEMtSJINtZI"ptMIMTtI!"oDIzMTDMoIv,IUnoMHpMtkICMpoDMIUTMIUTHpI,lI,tZIqMoETMUUIZMtIPGGESIsEEMIzGoMtIMoUHpo"HCMtkIZGIDoGDIZTMIvz"MEWDMIpMoq"okIZTMITpoMtI!,tUHpIt"HpI,MxoTdIpGDDMkI,tZIzMTEIUTMIZMtIx"MUMtIPno,HpItTHpDIG,WpMxMtkIU"tZMotIt,oITptIlTEZMotIC"ttDMkIU"IUGdDMIUTMmIJcUIU"EEIGxMoICMTtIR"ZIUMTtkIU"tZMotIMTtIp,tZMoD;GMpoTdMoIDTMWMoIPHpEGWkITtIzMEHpMtIZTMIF"MtTdUD"HpDMoIWGMEEDSJIiMoIF"MtTdkIZMoIUMTtIETMxMUIFTtZIq"oIZMlINtdE,MHCIdMotIxMzGpoMtIz"EEDMkIETMUUIZMtIbMWMpEIG,UdMpMtkIZGUUIGEEMIPnTtZMEtITlIdGtvMtIF"MtTdoMTHpMIqMoxoGttDIzMoZMtSIstIZMlIhGMZHpMtIGxMoIz,oZMtIZTMI\'GxMtIZMoIzMTUMtI.oG,MtIUGMlDETHpIMoW,MEEDkIZMttIMUIzGoIU"IUHp"MtkIUTDDUGlkIWoM,tZETHpI,tZIqMoUDGMtZTdkIZGUUIMUI;MZMolGttkIMoIMUIGtUGpkIETMxIpGxMtIl,UUDMSIcUIdMUHpGpkIZGUUIGtIZMlIRGdMkIz"IMUIdMoGZMIW,MtWvMptIfGpoIGEDIzGoZkIZMoIF"MtTdI,tZIZTMIF"MtTdTtItTHpDIv,IVG,UIzGoMtkI,tZIZGUIhGMZHpMtIdGtvIGEEMTtITlIPHpE"UUIv,o,MHCxETMxSIiGIdTtdIMUIGEEMo"oDMtIpMo,lkIxMUGpIPD,xMtI,tZIFGllMotkIzTMIMUIu,UDIpGDDMkI,tZICGlIMtZETHpIG,HpIGtIMTtMtIGEDMtIR,olSIcUIUDTMdIZTMIMtdMI!MtZMEDoMnnMIpTtG,WkI,tZIdMEGtdDMIv,IMTtMoICEMTtMtIR,MoMSIetIZMlIPHpE"UUIUDMHCDMIMTtIqMoo"UDMDMoIPHpE,MUUMEkI,tZIGEUIMUI,lZoMpDMkIUnoGtdIZTMIR,MoMIG,WkI,tZIUGUUIZGITtIMTtMlICEMTtMtIPD,MxHpMtIMTtMIGEDMI.oG,IlTDIMTtMoIPnTtZMEI,tZIUnGttIMlUTdITpoMtI.EGHpUSIJ\',DMtIRGdkIZ,IGEDMUIh,MDDMoHpMtkJIUnoGHpIZTMIF"MtTdUD"HpDMokIJzGUIlGHpUDIZ,IZG JIKIJeHpIUnTttMkJIUGdDMIZTMIsEDMI,tZItTHCDMIlTDIZMlIF"nWISJ!GUITUDIZGUIW,MoIMTtIiTtdkIZGUIU"IE,UDTdIpMo,lUnoTtdD JIUn'
txt2 = f'Füge hier den Text ein'
freq = getFreq(txt2)
decode(txt2, freq)