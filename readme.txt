0) Required files:
-Database.py: Code. Given a range of xpg card IDs, extracts pairs of "xpg card IDs;card name" into database.txt
-Decks.txt: Text file. Contains xpg urls. Lines starting with "#" are ignored, but old urls need to be deleted before a new batch is processed. Otherwise old decks will show up again.
-Xpg3.py: Code. Given a decks.txt file and a database.txt file, it parses the source code of the xpg urls (from decks.txt) into just the card amounts and card names (by mapping the card IDs to the ones in database.txt)
Generated files:
-Database.txt: Contains pairs of xpg "card IDs;card name". Names are inserted in Japanese and need to be translated manually.
-Decklists.txt: Contains the translated Decklists, separated by spoiler tags and dashes (-----). New decklists are appended to existing ones. Therefore, it's good practice to keep this file empty.


1) How to create a card database:
-Open database.py with a python editor.
-There are three variables at the start of the code: "url", "cardnumber" and "endnumber".
-The card ID number at the end of "url" and the value of "card number" always must match.
-This number is the first card of the range of cards that will be added to the database. (Minimum == 1)
-"endnumber" is the last card that will be added to the database. This number can be found manually by visiting http://vg.xpg.jp/c/[...]/ until the website returns an error, meaning there are no cards with that card ID. "endnumber" must match the last valid card ID on xpg.
-Run database.py.
-The file database.txt will be appended with the new "card ID;card name" pairs.

2) How to parse decklists:
-Open decks.txt
-Browse the xpg website and copy the url links in separate lines inside decks.txt.
-Save the file.
-Run xpg3.py.
-After xpg3.py finishes, open decklists.txt to find the decklists.

Common errors:
-Database.py
1) Might crash if it tries to write a very odd character into database.txt. Write the card ID;card name manually.

-Xpg3.py:
1) Might crash if it tries to read a very odd character from database.txt. Replace the offending character with a more common one in database.txt. Invisible spacing characters may cause this issue as well.
2) Might crash due to connection errors to xpg. In that case, the program needs to be restarted. If some decklists have already been processed, you can remove them from decks.txt and the remaining ones will be appended to decklists.txt.
3) Might crash if the card does not exist in database.txt. This is likely due to decks using new cards that haven't been added to database.txt. This can be fixed by adding the cardID;cardname pair to database.txt
