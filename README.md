# Rocnikova_prace

Autor: Michal Novák

Školní Rok: 2025/2026

Macro klávesnice / button box pro hry


Jako svůj cíl pro letošní ročníkovou práci jsem si vybral tvorbu vlasní macro klávesnice. Vzhledem k cenám takových klávesnic a modulů jsem se rozhodl pro vytvoření vlastní s možností přizpůsobení pro moje konkrétní potřeby. Cílem této práce je navrhnout a zpracovat klávesnici, která urychlí a usnadní ovládání závodních her a zároveň nabídne využití pro konkrétní aplikace.


Cíle Práce:
Hardwarová realizace: Vyrobit funkční modulární klávesnici založenou na mikrokontroléru s podporou USB HID.
Softwarová implementace: Naprogramovat mikrokontrolér tak, aby při stisku fyzického tlačítka odeslal předdefinovanou sekvenci kláves operačnímu systému.
Funkčnost: Ověřit spolehlivost makra při použití ve hře a při spouštění standardních Windows Hotkeys.


Teoretické znalosti:

Makra a Vstupní Emulace
Makro je z pohledu operačního systému sekvence stisků kláves, které jsou odeslány v krátkém, přesně definovaném čase. Kritickým prvkem je schopnost mikrokontroléru odesílat data s takovou přesností, aby aplikace (simulátor) všechny po sobě jdoucí stisky správně zaregistrovala.

Protokol Human Interface Device (HID)
Základním předpokladem pro realizaci projektu je schopnost zařízení komunikovat s hostitelským počítačem jako standardní klávesnice. To je zajištěno implementací protokolu USB HID. Mikrokontrolér se tak pro operační systém tváří jako standardní periferie. Při stisku makro tlačítka odešle čip tzv. HID Report, který obsahuje data o stavu kláves, čímž simuluje stisk jedné či více kláves.


Volba Mikrokontroléru
Pro projekt byl vybrán čip RP2040, který je standardně osazován na vývojové desky typu Raspberry Pi Pico W.


Klíčová vlastnost: Na rozdíl od běžných mikrokontrolérů (např. ATmega328P) má nativní podporu USB. Tato vlastnost je zásadní pro přímou implementaci USB HID protokolu bez nutnosti použití externích převodníků.


Hardware Design:
Button Box je navržen se šesti spínači pro primární ovládání. Namísto standardních klávesových spínačů jsem použil větší, barevně odlišená momentová tlačítka (push buttons).


Tiskové Pouzdro (Šasi):
Pouzdro bylo navrženo s důrazem na ergonomii a snadné využití u běžného stolu.
Pro návrh 3d modelu jsem využil CAD software (Fusion 360). Klíčové bylo vytvořit otvory, které přesně odpovídají průměru a fixačním mechanismům zvolených tlačítek.
Použitá technologie: 3D tisk FDM z materiálu PLA.
Volba Tlačítek: Momentové spínače s jasnou hmatovou odezvou, které jsou robustnější a lépe ovladatelné za jízdy než miniaturní klávesové spínače.
Zapojení: Každé tlačítko je připojeno na digitální I/O pin a na zemnící pin (GND), s využitím interních PULL-UP rezistorů na desce Raspberry Pi Pico W.

Konstrukce a Finální Montáž


Po dokončení tisku a očištění pouzdra proběhla finální montáž:
Usazení Tlačítek: Tlačítka byla zacvaknuta nebo zašroubována do připravených otvorů v 3D tištěném pouzdře.
Kabeláž: Připájení propojovacích vodičů k tlačítkům a následné připojení k určeným pinům na desce Raspberry Pi Pico W.
Uložení Elektroniky: Deska mikrokontroléru byla bezpečně uložena uvnitř pouzdra a fixována, aby nedocházelo k pohybu a riziku zkratu.
Uzavření Pouzdra: Pouzdro bylo uzavřeno pomocí tištěného spodního víka.
Výhoda 3D Tisku: Umožnil mi přesně definovat rozestupy tlačítek, úhel sklonu panelu, což by bylo při použití univerzální krabičky nebylo ožné dosáhnout.



Citace:
How to Build a Pico Macro Pad. Online. 2021. Dostupné z: https://www.hackster.io/1NextPCB/how-to-build-a-pico-macro-pad-3638e6. [cit. 2025-12-01].
A made a Raspberry Pi Pico Macro Board!. Online. 2020. Dostupné z: https://www.reddit.com/r/raspberry_pi/comments/n2s3i8/a_made_a_raspberry_pi_pico_macro_board/. [cit. 2025-12-01].
Raspberry Pi Pico - DIY Macro Keyboard. Online. Novaspirit Tech. 2021. Dostupné z: https://www.youtube.com/watch?v=aEWptdD32iA. [cit. 2025-12-01].
Wired USB keyboard, mouse, controller to Bluetooth w/ $6 Raspberry Pi Pico W. Online. Kenjinerd. 2025. Dostupné z: https://www.youtube.com/watch?v=YuHbTrccshw. [cit. 2025-12-01].
