from tkinter import *
from tkinter.scrolledtext import *
from tkinter.messagebox import *

mainw = Tk()
#===
text_lf = LabelFrame(mainw, text="Text ...")
text_lf.pack(fill="both", expand="no")
#===
to_translate_lf = LabelFrame(text_lf, text="Text to translate")
to_translate_lf.pack(fill="both", expand="yes", side=LEFT)
#---
translated_lf = LabelFrame(text_lf, text="Translated text")
translated_lf.pack(fill="both", expand="yes", side=RIGHT)
#===
to_translate = ScrolledText(to_translate_lf, wrap="word")
translated = ScrolledText(translated_lf, wrap="word")
#---
infos1 = Label(to_translate_lf, text="Type your text to translate here :")
infos2 = Label(translated_lf, text="See the translated text :")
infos1.pack()
infos2.pack()
to_translate.pack()
translated.pack()
def translate_t():
    firstl = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Â", "À", "É", "Ë", "Ç", "Œ", "Æ", "Á","Ã", "Ō", "Ñ","Ą", "Ä", "Č", "Ĉ", "Ù", "È", "Ê"]
    secondl = ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "N", "R", "R", "P", "BR", "NR", "N", "N", "B", "A", "N", "N", "P", "P", "H", "R", "R"]
    translated.configure(state='normal')
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
    translated.configure(state='disabled')
translate=Button(mainw, text="Traduire", command=translate_t)
translate.pack(side=TOP)

    
#translate_t()
mainw.mainloop()