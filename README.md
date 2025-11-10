# Network Scanner

## Group Members
- [Philip]
- [Edvin]
- [Mahdi]

Network Scanner — Enkel portscanner

Beskrivning Denna enkla Python-skript försöker ansluta till en angiven värd (domännamn eller IP) över ett intervall av TCP-portar och rapporterar vilka portar som är öppna. Den sparar också resultatet i filen result.txt.

Hur man kör

Se till att du har Python 3 installerat (rekommenderat: Python 3.8).

Spara skriptet i en fil, t.ex. portscanner.py.

Kör skriptet i terminalen: python3 portscanner.py
Följ de interaktiva frågorna:

vilken sida vill du scanna?: — skriv domännamn eller IP (t.ex. example.com eller 93.184.216.34).

Välj intervallets start tal: — startport (t.ex. 1).

välj intervallets slut tal: — slutport (t.ex. 1024).

Hur länge tills timeout?(sec): — timeout i sekunder för varje anslutningsförsök (t.ex. 1 eller 2).

Resultat skrivs både ut i terminalen och sparas i result.txt i samma mapp.

Bannermottagning: Skriptet försöker läsa en "banner" med recv(1024) efter att anslutningen upprättats. Många tjänster skickar ingen data förrän klienten skickar något — därför kan recv returnera tomt.

Timeouts och fel: Om du anger en mycket kort timeout kan du få falska stängda portar (tidsutslag innan servern svarar). Ange en rimlig timeout (t.ex. 1–3 sekunder beroende på nätverk).

Prestanda: Skriptet skannar portar sekventiellt (en i taget). Detta är enkelt men långsamt för stora intervall. Om du behöver snabbare skanning bör du överväga parallellisering (trådar/asyncio) men var försiktig — hög hastighet ökar risken att trigga säkerhetssystem.
