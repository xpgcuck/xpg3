import urllib.request
import time
import codecs


url = "http://vg.xpg.jp/c/4017/" #set to first new card url
cardnumber= "4017" #set to the same number as the line above
endnumber= 4693 #set to the last new card number (not url)


def next_card(): #function to move to the next card
   global cardnumber
   global url
   url = url.replace(cardnumber, str(int(cardnumber)+1))
   cardnumber = str(int(cardnumber)+1)

fo = open("database.txt", "a", encoding='utf8') 
while int(cardnumber) <= endnumber:
    page = urllib.request.urlopen(url)
    text = page.read().decode("s_jis", "ignore") #get page
    name_start = text.find("<h1>") #get where the first name is
    if name_start == -1:
        break
    name_start += 4 #skip font tag
    name_end = text.find("</h1>")

    names = text[name_start: name_end] #here you have all the names, Kanji and Furigana
    names_amount = names.count ("<br>") #count if there is Kanji + Furigana or just Hiragana/Katakana
 
    if names_amount == 2: #leftover code in case they include Kanji + Furigana + English name
       break
##      
##        first_pos = 0
##        
##        first_end = names.find("<br>")
##        second_pos = names.find("<br><span ")
##        second_end = names[second_pos:].find("</span>")
##        second_end += second_pos
##        third_pos = names[second_end].find("<span>")
##        third_pos += second_end
##        third_pos_end = names[third_pos:].find("]</span>")
##        third_pos_end += third_pos
##        stripped_text = ((names[third_pos+18:third_pos_end]).lstrip("[").rstrip("]").lstrip("（").rstrip("）"))
##        fo.write(cardnumber + ";" + stripped_text  + "\n")
##        print (cardnumber + ";" + stripped_text)
        
    elif names_amount == 1: #If there is Kanji + Furigana

        first_pos = 0
        first_end = names.find("<br>") #end of Kanji name
        second_pos = names.find("<br><span") #start of Furigana
        second_pos += 20 #skip font tag
        stripped_text = (names[first_pos:first_end] + names[second_pos:]).lstrip("[").rstrip("</span>").rstrip("]").lstrip("(").rstrip(")")
    
        fo.write(cardnumber + ";" + stripped_text + "\n")
        print (cardnumber + ";" + stripped_text)

    else: #If it is just Hiragana/Katakana

        stripped_text = names
        
        fo.write(cardnumber + ";" + stripped_text + "\n")
        print(cardnumber + ";" + stripped_text)
    next_card() #Proceed

fo.close()
