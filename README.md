## Descriere proiect pentru certificare
          Cristina Bodea


Ce face proiectul meu:

Acesta este un joc clasic Snake implementat in Python folosind modulul Turtle pentru grafica. Jocul ofera o interfata grafica in care jucatorul controleaza un sarpe care se misca in jurul ecranului.
Obiectul jocului este de a manca mancare si de a creste lungimea sarpelui fara a se ciocni cu peretii sau cu propriul corp.
Codul este format din trei clase: Snake, Food și Scoreboard.
Clasa Snake reprezintă sarpele din joc. Are metode pentru crearea sarpelui, adaugarea de segmente la sarpe, extinderea sarpelui, mutarea sarpelui si schimbarea directiei acestuia. Sarpele este compus din segmente individuale.
Clasa Food reprezinta hrana pe care sarpele trebuie sa o manance. Este o subclasa de Turtle si are o metoda de a-si reimprospata pozitia în mod aleatoriu pe ecran.
Clasa Scoreboard gestioneaza scorul jocului si îl afisează pe ecran. Are metode de actualizare a tabelului de marcaj, de afisare a mesajului game over si de crestere a scorului.



Caracteristici:
- Jocul permite jucatorului sa controleze miscarea sarpelui folosind tastele sageti: Sus, Jos, Stanga, Dreapta.
- Sarpele creste in lungime de fiecare data cand mananca mancare.
- Jocul se termina daca sarpele se ciocneste de pereti sau de propriul sau corp.
- Scorul jucatorului este afisat pe ecran, crescand de fiecare data cand sarpele mananca mancare.
- Ecraul game over arata scorul final.

Instalare:
1. Clonati repositorul  https://github.com/Cristinaa90/Snake_game.git
2. Pentru a rula acest cod, trebuie să aveți instalat modulul Turtle. Puteti executa codul într-un mediu Python care accepta modulul Turtle, cum ar fi IDLE sau PyCharm.
3. Rulati scriptul main.py
4. Se va deschide fereastra de joc si puteti incepe sa jucati jocul Snake.

Cum se joaca:
- Folositi tastele sageti (Sus, Jos, Stanga, Dreapta) pentru a controla miscarea sarpelui.
- Sarpele se va misca continuu in directie in care a fost ghidat.
- De fiecare data cand sarpele mananca acesta va creste in lungime.
- Evitati ciocnirea cu peretii sau cu propiul corp al sarpelui.
- Jocul se termina cand sarpele se ciocneste de un perete sau de propiul corp.
- Scorul final va fi afisat pe ecran impreuna cu mesajul 'Game over'.