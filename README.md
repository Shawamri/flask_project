# Anleitung
Die webseite ist noch in noch nicht Reif. Ein Teil ist schon fertig und kann man mit ''app.py'' ausprobieren und enthält die Hauptfunktion des Projekts.
<br>Der zweite Teil enthält eine Registrierung- und Loginseite,die mit einer DatenBank verbunden ist,der noch in Bearbeitung ist ''my_app_in_working.py''
<br>Die Webseite wird mit **Flask python**  und **sqlite** entwickelt

## Ziel der Webseite
Posts mit Name,Inhalt und Datum zu erstellen mit der Möglichkeit sie jederzeit aktualisieren bzw. löschen zu können.
<br>Durch die Registrierung werden jedem user ein konto und dadurch ein Zugriff zugeordnet.
<br>Die Webseite wird so weiterentwickelt, dass jede post ein user besitzt.
<br>Ziel ist es,eine Plattform wie Twitter zu erstellen.
### Ausführung in Terminal
python3 init_db.py <br>
export FLASK_APP=app<br>
export FLASSK_ENV=development<br>
flask run -p (portnumber z.B 5000)
