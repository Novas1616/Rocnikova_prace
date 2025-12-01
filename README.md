# Rocnikova_prace

Autor: Michal Novák
Školní Rok: 2025/2026

Macro klávesnice / button box pro hry

Jako svůj cíl pro letošní ročníkovou práci jsem si vybral tvorbu vlasní macro klávesnice. Vzhledem k cenám takových klávesnic a modulů jsem se rozhodl pro vytvoření vlastní s možností přizpůsobení pro moje konkrétní potřeby. Cílem této práce je navrhnout a zpracovat klávesnici, která urychlí a usnadní ovládání závodních her a zároveň nabídne využití pro konkrétní aplikace.

Cíle Práce:
Hardwarová realizace: Vyrobit funkční modulární klávesnici založenou na mikrokontroléru s podporou USB HID.

Softwarová implementace: Naprogramovat mikrokontrolér tak, aby při stisku fyzického tlačítka odeslal předdefinovanou sekvenci kláves operačnímu systému.

Funkčnost: Ověřit spolehlivost makra při použití ve hře a při spouštění standardních Windows Hotkeys.


Teoretické Zázemí

Protokol Human Interface Device (HID)
Základním předpokladem pro realizaci projektu je schopnost zařízení komunikovat s hostitelským počítačem jako standardní klávesnice. To je zajištěno implementací protokolu USB HID. Mikrokontrolér se tak pro operační systém tváří jako standardní periferie. Při stisku makro tlačítka odešle čip tzv. HID Report, který obsahuje data o stavu kláves, čímž simuluje stisk jedné či více kláves.

Volba Mikrokontroléru
Pro projekt byl vybrán čip ATmega32U4, který je standardně osazován na vývojové desky typu Arduino Pro Micro.

Klíčová vlastnost: Na rozdíl od běžných mikrokontrolérů (např. ATmega328P) má nativní podporu USB. Tato vlastnost je zásadní pro přímou implementaci USB HID protokolu bez nutnosti použití externích převodníků nebo softwarových hacků.


Citace:
How to Build a Pico Macro Pad. Online. 2021. Dostupné z: https://www.hackster.io/1NextPCB/how-to-build-a-pico-macro-pad-3638e6. [cit. 2025-12-01].
A made a Raspberry Pi Pico Macro Board!. Online. 2020. Dostupné z: https://www.reddit.com/r/raspberry_pi/comments/n2s3i8/a_made_a_raspberry_pi_pico_macro_board/. [cit. 2025-12-01].
Raspberry Pi Pico - DIY Macro Keyboard. Online. Novaspirit Tech. 2021. Dostupné z: https://www.youtube.com/watch?v=aEWptdD32iA. [cit. 2025-12-01].
Wired USB keyboard, mouse, controller to Bluetooth w/ $6 Raspberry Pi Pico W. Online. Kenjinerd. 2025. Dostupné z: https://www.youtube.com/watch?v=YuHbTrccshw. [cit. 2025-12-01].
