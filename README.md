## Descriere proiect penru certificare
          Cristina Bodea


Ce face proiectul meu:

Acesta este un joc clasic Snake implementat in Python folosind modulul Turtle pentru grafica. Jocul ofera o interfata grafica in care jucatorul controleaza un sarpe care se misca in jurul ecranului.
Obiectul jocului este de a manca mancare si de a creste lungimea sarpelui fara a se ciocni cu peretii sau cu propriul corp.
Codul este format din trei clase: Snake, Food și Scoreboard.
Clasa Snake reprezintă șarpele din joc. Are metode pentru crearea șarpelui, adăugarea de segmente la șarpe, extinderea șarpelui, mutarea șarpelui și schimbarea direcției acestuia. Șarpele este compus din segmente individuale de țestoasă.
Clasa Food reprezintă hrana pe care șarpele trebuie să o mănânce. Este o subclasă de Turtle și are o metodă de a-și reîmprospăta poziția în mod aleatoriu pe ecran.
Clasa Scoreboard gestionează scorul jocului și îl afișează pe ecran. Are metode de actualizare a tabelului de marcaj, de afișare a mesajului game over și de creștere a scorului.



Caracteristici:
- Jocul permite jucatorului sa controleze miscarea sarpelui folosind tastele sageti: Sus, Jos, Stanga, Dreapta.
- Sarpele creste in lungime de fiecare data cand mananca mancare.
- Jocul se termina daca sarpele se ciocneste de pereti sau de propriul sau corp.
- Scorul jucatorului este afisat pe ecran, crescand de fiecare data cand sarpele mananca mancare.
- Ecraul game over arata scorul final.

Instalare:
1. Clonati repositorul  https://github.com/Cristinaa90/Snake_game.git
2. Pentru a rula acest cod, trebuie să aveți instalat modulul Turtle. Puteți executa codul într-un mediu Python care acceptă modulul Turtle, cum ar fi IDLE sau PyCharm.
3. Rulati scriptul main.py
4. Se va deschide fereastra de joc si puteti incepe sa jucati jocul Snake.

Cum se joaca:
- Folositi tastele sageti (Sus, Jos, Stanga, Dreapta) pentru a controla miscarea sarpelui.
- Sarpele se va misca continuu in directie in care a fost ghidat.
- De fiecare data cand sarpele mananca acesta va creste in lungime.
- Evitati ciocnirea cu peretii sau cu propiul corp al sarpelui.
- Jocul se termina cand sarpele se ciocneste de un perete sau de propiul corp.
- Scorul final va fi afisat pe ecran impreuna cu mesajul 'Game over'.