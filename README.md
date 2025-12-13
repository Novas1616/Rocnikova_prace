
#Ročníková práce#

Autor: Michal Novák

Školní rok: 2025/2026

Tvorba vlastní macro klávesnice / Button boxu pro hry

Úvod

Tématem mé ročníkové práce je návrh a tvorba vlastní macro klávesnice — často označované jako button box — která bude sloužit pro ovládání závodních her a dalších aplikací. Cílem je vytvořit zařízení, které umožní odesílání klávesových zkratek nebo sekvencí kláves jediným stiskem fyzického tlačítka.

Rozhodl jsem se pro tento projekt proto, že mě dlouhodobě zajímá elektronika, programování mikrokontrolérů a využití 3D tisku v praxi. Komerční macro panely jsou často drahé nebo nenabízejí takové možnosti přizpůsobení, jaké potřebuji při hraní závodních simulátorů. Vytvořením vlastního řešení získám praktické zkušenosti v několika technických oblastech.

1. Cíle ročníkové práce
   
1.1 Hardwarová část

vybrat vhodný mikrokontrolér

navrhnout rozmístění tlačítek

připravit 3D model pouzdra

vytisknout pouzdro a provést montáž

zajistit kvalitní a přehledné zapojení vodičů

1.2 Softwarová část

naučit se pracovat s USB HID protokolem

naprogramovat mikrokontrolér tak, aby se choval jako klávesnice

vytvořit jednoduchou správu makro funkcí

implementovat debounce a případné zpoždění mezi stisky

otestovat fungování na Windows

1.3 Testování a ladění

ověřit funkčnost v závodních hrách

provést dlouhodobé testy spolehlivosti

analyzovat případné problémy a optimalizovat kód

2. Teoretické pozadí
   
2.1 Makra a jejich využití

Makro je sekvence stisků kláves nebo příkazů, která se vykoná automaticky při stisku tlačítka. Ve hrách se používá například k přepínání kamer, resetu vozidla, zapnutí světel nebo aktivaci funkcí bez nutnosti mačkat více kláves najednou.

2.2 HID protokol

Aby se button box choval jako klávesnice, je potřeba implementovat USB HID standard. Ten definuje:

jakým způsobem zařízení komunikuje

jak vypadají datové struktury (HID reporty)

jak OS reaguje na stisk a uvolnění kláves

Výhodou HID je, že není nutná instalace ovladačů.

2.3 Mikrokontrolér RP2040

Zvolil jsem Raspberry Pi Pico W z důvodů:

nativní USB

nízká cena

dostupná dokumentace

výborná podpora MicroPythonu, CircuitPythonu i C/C++

možnost připojení až desítek vstupů

Tento mikrokontrolér je ideální pro malé HID projekty jako moje makro klávesnice.

2.4 CircuitPython

Pro programování mikrokontroléru Pico W používám CircuitPython, což je verze programovacího jazyka Python optimalizovaná pro mikrokontroléry. CircuitPython umožňuje rychlý a přehledný vývoj programu přímo na zařízení, bez nutnosti složitého nízkoúrovňového programování. Díky tomu je možné snadno ovládat vstupy a výstupy, číst stisky tlačítek a odesílat je do počítače jako klávesové zkratky.

Použití CircuitPython mi umožňuje:

rychle implementovat funkce pro ovládání tlačítek a makra,

využít připravené knihovny, například adafruit_hid, pro emulaci klávesnice a myši,

jednoduše řešit problémy se zákmity tlačítek (debounce) a správné odesílání sekvencí kláves,

testovat a upravovat program během vývoje, což urychluje ladění a ověřování funkčnosti.

Díky CircuitPythonu jsem mohl provést první praktické testy tlačítka ještě před samotným sestavením celé krabičky, a ověřit tak základní fungování softwaru a komunikaci přes USB HID.

3. Návrh zařízení

3.1 Rozmístění tlačítek

Zařízení bude mít celkem 6 tlačítek, každé přiřazené k jiné funkci. Rozmístění je navrženo tak, aby bylo pohodlné při používání jednou rukou.

3.2 Zapojení

Každé tlačítko bude:

jednou stranou připojené na GND

druhou na digitální vstup Pico W
Použiji interní PULL-UP rezistory, takže není potřeba externí elektronika.

3.3 3D tištěné pouzdro

Pouzdro mám navržené ve Fusion 360, ale tisk ještě neproběhl. Návrh aktuálně obsahuje:

přední panel s otvory pro tlačítka

vnitřní držáky na desku Pico W

prostor pro vedení kabeláže

zadní víko na šroubky

V dalším období budu pouzdro dolaďovat a poté vytisknu finální verzi.

4. Softwarová část — hotová k pololetí

K pololetí mám hotovou prakticky kompletní softwarovou část projektu, což byla jedna z hlavních priorit první části roku.

4.1 Použité knihovny

Používám CircuitPython a knihovny:

adafruit_hid.keyboard

adafruit_hid.keycode

Debouncer pro filtraci stisku tlačítek

4.2 Základní funkce programu

Můj software umí:

inicializovat 6 fyzických tlačítek

sledovat jejich stav (stisk/pustění)

odesílat zvolené HID příkazy při stisku

ošetřit zákmity (debounce)

správně odeslat kombinaci více kláves (např. CTRL + SHIFT)

Software jsem již testoval pomocí náhradních tlačítek na breadboardu — chování je stabilní a funkční.

4.3 Ověření funkčnosti na PC

Pico W funguje jako běžná klávesnice, počítač ho detekuje automaticky bez ovladačů. Úspěšně jsem otestoval:

odesílání jednoduchých kláves

klávesové zkratky

sekvence kláves

makra pro hry

Chová se přesně podle očekávání.

5. Současný stav projektu k pololetí

V této fázi mám:

Z větší části připravený software

firmware umí odesílat makra

funguje 6 vstupů

hotové ošetření zákmity i správné odesílání reportů

připraveno pro rozšíření funkcí

Navržené hardware řešení (teoreticky)

rozvržené piny

určený typ tlačítek

proběhl první test odesílání macra do hry s testovacím kódem

připravený CAD model pouzdra (zatím bez tisku)

Zatím chybí fyzická realizace

3D tisk pouzdra

pájení kabeláže

montáž celku

Toto bude hlavní náplní druhého pololetí.

6. Další postup (druhé pololetí)

V druhé části školního roku plánuji:

Dokončit finální CAD model pouzdra.

Vytisknout pouzdro na 3D tiskárně.

Zakoupit nebo připravit vodiče a konektory.

Připájet vodiče k tlačítkům i mikrokontroléru.

Provést finální montáž button boxu.

Otestovat funkčnost při běžném používání.

Optimalizovat software podle reálného testování.

Vypracovat dokumentaci a vložit ji na GitHub.

7. Závěr

K prvnímu pololetí jsem splnil všechny plánované softwarové cíle a mám funkční základ celého zařízení. Button box zatím není fyzicky sestavený, ale hardwarová část je navržená a připravená k realizaci.

Druhé pololetí bude zaměřené hlavně na praktickou konstrukci krabičky, 3D tisk a fyzické zapojení celého systému. Po dokončení očekávám, že zařízení bude plně funkční a použitelné v závodních hrách i běžném použití.

8. Citace:

How to Build a Pico Macro Pad. Online. 2021. Dostupné z: https://www.hackster.io/1NextPCB/how-to-build-a-pico-macro-pad-3638e6. [cit. 2025-12-01].

A made a Raspberry Pi Pico Macro Board!. Online. 2020. Dostupné z: https://www.reddit.com/r/raspberry_pi/comments/n2s3i8/a_made_a_raspberry_pi_pico_macro_board/. [cit. 2025-12-01].

Raspberry Pi Pico - DIY Macro Keyboard. Online. Novaspirit Tech. 2021. Dostupné z: https://www.youtube.com/watch?v=aEWptdD32iA. [cit. 2025-12-01].

Wired USB keyboard, mouse, controller to Bluetooth w/ $6 Raspberry Pi Pico W. Online. Kenjinerd. 2025. Dostupné z: https://www.youtube.com/watch?v=YuHbTrccshw. [cit. 2025-12-01].

Raspberry Pi Pico W and Pico WH. Online. Raspberrypi.com. 2024. Dostupné z: https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#pico-1-family. [cit. 2025-12-06].
