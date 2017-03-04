import urllib.request
import time

#FUNCTIONS:
def create_database():
   cards = open("database.txt", encoding = "utf8")
   for line in cards:
      (number, name) = line.split(";", 1)
      data[number] = name
   cards.close()

def decktotal (text):
   pos_start = text.find("（")
   pos_end = text.find("枚／")
   return text[pos_start+1:pos_end]

def towikia(text):
   url = "<a href=\"http://yugioh.wikia.com/wiki/"
   url = url + text.replace(" ", "_").rstrip("\n")
   url = url + "\">" + text.rstrip("\n").replace(" (card)", "" ) + "</a> \n"
   return url

def number_to_card(number):
   return data[number]


#OPEN FILES
fo = open("decklists.txt", "a", encoding='utf8')
decks = open("decks.txt")

data = {}
decknumber = 0
print ("Creating Database...")
create_database()
print ("DATABASE CREATED!" + "\n")

#BIG FUNCTION

def process_deck(deckid):
   global data
   global decknumber
   
   page = urllib.request.urlopen("https://vg.xpg.jp/deck/deck.fcgi?ListNo=" + deckid)
   text = page.read().decode("s_jis", "ignore")


   deck_table_start = "<table class=\"jHover c2 f9 nw dd\">"
   deck_table_end = "</table>"

   decknumber +=1
   print ("Writing Deck #" + str(decknumber) + "...")
   
   
   start_pos = text.find(deck_table_start)
   end_pos = text.find(deck_table_end, start_pos)
   decklist = text[start_pos:end_pos]


   rows = []
   rows.extend( decklist.split("</tr>"))
   fo.write("----------------------------------------------------------------")
   fo.write("\n[spoiler]")
   amount_pos = 8


   for line in rows:


      card_link = line.find("<a")
      is_deck = line.find("<th class=\"w6\">")
      if is_deck != -1:
        if line.find("グレード3") != -1 :
          fo.write("\n" +"Grade 3 (" + decktotal(line) + "): "+ "\n")
        elif line.find("グレード2") != -1:
          fo.write("\n" +"Grade 2 (" + decktotal(line) + "): "+ "\n")
        elif line.find("グレード1") != -1:
          fo.write("\n" +"Grade 1 (" + decktotal(line) + "): "+ "\n")
        elif line.find("グレード0") != -1:
          fo.write("\n" +"Grade 0 (" + decktotal(line) + "): "+ "\n")
        elif line.find("Gゾーン") != -1:
          fo.write("\n" +"G Zone (" + decktotal(line) + "): "+ "\n")


      if card_link != -1:
          card_start = (line[card_link: ].find("/c/"))
          card_link += card_start+3
          card_end = line[card_start:].find ("/\">")
          card_end += card_start
          amount_pos = line.find("<tr><td>")
          amount_pos = amount_pos + 8
          fo.write(line[amount_pos] + " " + number_to_card(line[card_link:card_end]))


   fo.write("[/spoiler] \n")

#ACTUAL PROGRAM
for line in decks:
   if not line.strip():
      continue
   else:
      if not line.startswith("#"):
         idpos = line.find("No=")
         process_deck(line[idpos+3:])
         time.sleep(1)

fo.close()
decks.close()
print ("FINISHED")
