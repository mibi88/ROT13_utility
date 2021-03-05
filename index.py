from tkinter import *
from tkinter.scrolledtext import *
from tkinter.messagebox import *

mainw = Tk()

to_translate = ScrolledText(mainw)
translated = ScrolledText(mainw)
infos1 = Label(mainw, text="Type your text to translate here :")
translated.pack(side = RIGHT)
infos1.pack(side = LEFT)
to_translate.pack(side = LEFT)
def translate_t():
    firstl = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Â", "À", "É", "Ë", "Ç", "Œ", "Æ", "Á","Ã", "Ō", "Ñ","Ą", "Ä", "Č", "Ĉ", "Ù", "È", "Ê"]
    secondl = ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "N", "R", "R", "P", "BR", "NR", "N", "N", "B", "A", "N", "N", "P", "P", "H", "R", "R"]
    translated.delete("1.0","end")
    #translated.insert("1.0", "text")
    #===test===
    #firstl = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    #secondl = ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
    #blabla = "blabla"
    #nbletters = len(blabla)
    #scrollletters = 0
    #while scrollletters != nbletters:
    #    secnb = scrollletters + 1
    #    testvar = blabla[scrollletters:secnb]
    #    print(testvar)
    #    scrollletters = scrollletters + 1
    #==========
    text = to_translate.get("1.0","end")
    text = str(text)
    text = text.upper()
    nbletters = len(text)
    scrollletters = 0
    while scrollletters != nbletters:
        secnb = scrollletters + 1
        testvar = text[scrollletters:secnb]
        testvar = str(testvar)
        try:
            result = firstl.index(testvar)
            result = int(result)
            resvar = secondl[result]
            translated.insert("end", resvar)
        except ValueError:
            translated.insert("end", testvar)
        scrollletters = scrollletters + 1
translate=Button(mainw, text="Traduire", command=translate_t)
translate.pack()

    
#translate_t()
mainw.mainloop()