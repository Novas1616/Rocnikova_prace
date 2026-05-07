# Ročníková práce: 
# Tvorba vlastní macro klávesnice (Button boxu pro hry)

**Autor:** Michal Novák  
**Školní rok:** 2025/2026  

---

## Úvod

Tématem mé ročníkové práce byl návrh a tvorba vlastní macro klávesnice — často označované jako button box — která slouží pro ovládání závodních her a dalších aplikací. Cílem bylo vytvořit zařízení, které umožní odesílání klávesových zkratek nebo sekvencí kláves jediným stiskem fyzického tlačítka.

Rozhodl jsem se pro tento projekt proto, že mě dlouhodobě zajímá elektronika a programování mikrokontrolérů v praxi. Komerční macro panely jsou často drahé nebo nenabízejí takové možnosti přizpůsobení, jaké potřebuji při hraní závodních simulátorů. Vytvořením vlastního řešení jsem získal praktické zkušenosti v několika technických oblastech, od návrhu obvodu až po psaní firmwaru.

## 1. Cíle ročníkové práce

### 1.1 Hardwarová část
* Vybrat vhodný mikrokontrolér s podporou USB HID.
* Navrhnout ergonomické rozmístění tlačítek.
* Připravit a mechanicky upravit pouzdro pro zařízení.
* Zajistit kvalitní a přehledné zapojení vodičů a provést finální montáž.

### 1.2 Softwarová část
* Naučit se pracovat s USB HID protokolem.
* Naprogramovat mikrokontrolér tak, aby se choval jako běžná klávesnice.
* Vytvořit efektivní správu makro funkcí a optimalizovat kód.
* Implementovat ošetření zákmitů (debounce) a zpoždění mezi stisky.

### 1.3 Testování a ladění
* Ověřit funkčnost v reálném provozu a v závodních hrách.
* Analyzovat případné problémy a doladit latenci stisků.

## 2. Teoretické pozadí

### 2.1 Makra a jejich využití
Makro je sekvence stisků kláves nebo příkazů, která se vykoná automaticky při stisku tlačítka. Ve hrách se používá například k přepínání kamer, resetu vozidla, zapnutí světel nebo aktivaci funkcí bez nutnosti mačkat více kláves najednou na standardní klávesnici.

### 2.2 HID protokol
Aby se button box choval jako klávesnice, bylo potřeba implementovat **USB HID** (Human Interface Device) standard. Ten definuje, jakým způsobem zařízení komunikuje, jak vypadají datové struktury (tzv. HID reporty) a jak operační systém reaguje na stisk a uvolnění kláves. Zásadní výhodou HID je, že nevyžaduje instalaci žádných externích ovladačů.

### 2.3 Mikrokontrolér RP2040
Zvolil jsem mikrokontrolér **Raspberry Pi Pico W** z těchto důvodů:
* Nativní podpora USB komunikace přímo na čipu.
* Nízká pořizovací cena a dostupná dokumentace.
* Výborná podpora MicroPythonu, CircuitPythonu i C/C++.
* Dostatek GPIO vstupů pro připojení tlačítek.

### 2.4 CircuitPython
Pro programování jsem využil **CircuitPython**, což je verze programovacího jazyka Python optimalizovaná pro mikrokontroléry. Umožňuje rychlý vývoj přímo na zařízení bez nutnosti složitého kompilování. Díky připravené knihovně `adafruit_hid` pro emulaci klávesnice bylo možné snadno řešit odesílání sekvencí kláves a testovat chování programu v reálném čase.

## 3. Návrh a konstrukce zařízení

### 3.1 Rozmístění a zapojení tlačítek
Zařízení je osazeno celkem **7 tlačítky**, každé je přiřazeno k jiné funkci nebo makru. Rozmístění bylo navrženo tak, aby bylo pohodlné při používání jednou rukou. 

Každé tlačítko je jednou stranou připojeno na digitální vstup (GPIO) Pico W a druhou stranou na společnou zem (GND). V softwaru jsou aktivovány **interní PULL-UP rezistory**, takže nebylo potřeba osazovat žádnou externí elektroniku. Pro minimalizaci kabeláže uvnitř šasi byla použita metoda **"Common Ground" (společná zem)**, kdy jsou zemnící kontakty všech tlačítek propojeny mezi sebou a do mikrokontroléru vede pouze jeden společný zemnící vodič.

Pro připojení tlačítek k desce Raspberry Pi Pico W byly využity připájené pinové lišty a dupont vodiče, což usnadnilo testování a případné úpravy zapojení během montáže.

### 3.2 Konstrukce pouzdra (Šasi)
Ačkoliv původní plán počítal s 3D tiskem pouzdra, v průběhu realizace došlo k optimalizaci návrhu. Pro finální prototyp jsem se rozhodl využít **hotovou plastovou přístrojovou krabičku** vhodných rozměrů. Toto řešení se ukázalo jako praktičtější z hlediska mechanické odolnosti a rychlosti konstrukce. Do čelního panelu krabičky jsem přesně rozměřil a vyvrtal otvory pro tlačítka a do boční stěny byl vyříznut otvor pro protažení USB kabelu.

## 4. Softwarová realizace

### 4.1 Základní struktura a knihovny
Kód využívá knihovny `adafruit_hid.keyboard` a `adafruit_hid.keycode`. Software úspěšně inicializuje 7 fyzických tlačítek, neustále ve smyčce čte jejich stav a ošetřuje mechanické zákmity (debounce) pomocí časových prodlev, aby nedocházelo k nechtěným dvojstiskům.

### 4.2 Optimalizace kódu
Během vývoje byl program optimalizován. Namísto psaní samostatných podmínek pro každé tlačítko zvlášť jsem kód přepsal s využitím **polí (seznamů) a cyklů**. Tlačítka i jim přiřazené klávesové zkratky (např. CTRL + F13 až F19) jsou uloženy v seznamech. Program tak ve smyčce prochází jednotlivé piny a v případě detekce stisku odešle příslušný HID report. Tento přístup výrazně zkrátil délku kódu a zjednodušil případné budoucí přidávání dalších tlačítek.

### 4.3 Rozšíření funkcionality pro produktivitu (Stream Deck)
Kromě primárního využití v herních simulátorech lze toto zařízení díky emulaci USB HID využít také jako efektivní nástroj pro zvýšení produktivity v prostředí Windows (tzv. Stream Deck). V aktuální verzi firmwaru je každému ze sedmi tlačítek přiřazena specifická kombinace kláves CTRL + F13 až F19. Volba těchto funkčních kláves je záměrná, protože se běžně na standardních klávesnicích nevyskytují, což eliminuje riziko nechtěných konfliktů s ovládáním jiných programů. V systému Windows lze tyto signály snadno využít pro spouštění libovolných aplikací, webových prohlížečů nebo systémových příkazů. Toho lze docílit buď přiřazením dané kombinace přímo ve vlastnostech zástupce aplikace na ploše, nebo pomocí skriptovacího softwaru AutoHotkey, který na pozadí zachytí stisknutí tlačítka a provede nadefinovanou akci, jako je například otevření komunikačního nástroje nebo správa oken.

Pro maximální efektivitu využívám k obsluze button boxu program AutoHotkey (AHK). Tento software slouží jako prostředník, který zachytává specifické klávesové zkratky vysílané mikrokontrolérem (CTRL + F13 až F19) a převádí je na konkrétní systémové akce. V mém projektu je těchto 7 tlačítek nadefinováno pro okamžité spouštění klíčových pracovních i multimediálních aplikací, jako jsou Spotify, VS Code nebo DaVinci Resolve.

Hlavní výhodou tohoto řešení je, že pro změnu funkce tlačítek není nutné fyzicky zasahovat do zařízení ani přepisovat firmware v CircuitPythonu. Kompletní a připravený skript button_box.ahk se všemi nadefinovanými cestami k aplikacím přikládám jako samostatný soubor v tomto repozitáři. Uživatel si jej tak může snadno stáhnout a upravit podle vlastních potřeb.

## 5. Testování a uvedení do provozu

Po fyzické montáži tlačítek do krabičky a propojení s Raspberry Pi Pico W proběhlo finální testování na PC s operačním systémem Windows 11. 
* Zařízení je po připojení okamžitě automaticky detekováno jako běžná klávesnice.
* Úspěšně bylo otestováno odesílání jednoduchých kláves, složitějších klávesových zkratek i delších sekvencí kláves (maker).
* Dlouhodobý test v závodních hrách potvrdil, že zařízení funguje stabilně, latence je neznatelná a mechanické provedení krabičky bez problémů odolává běžnému používání.

## 6. Závěr

Ročníková práce byla úspěšně dokončena a všechny stanovené cíle byly splněny. Podařilo se mi navrhnout, naprogramovat a fyzicky sestavit plně funkční macro klávesnici. Změna plánu z 3D tisku na úpravu hotové plastové krabičky se ukázala jako efektivní krok, který urychlil montáž a zajistil prototypu profesionální a robustní vzhled. Zařízení nyní aktivně využívám při hraní simulátorů, čímž projekt splnil svůj původní praktický účel. Práce mi přinesla cenné zkušenosti s jazykem CircuitPython, USB komunikací a praktickou elektronikou.

## 7. Použité nástroje a zdroje

Při tvorbě projektu byly využity následující nástroje:
* **Hardware:** Raspberry Pi Pico W, mechanická tlačítka, plastová přístrojová krabička.
* **Software:** CircuitPython, AutoHotkey v2, Visual Studio Code.
* **AI Asistence:** Konzultace textové část dokumentace a schéma zapojení tlačítek byly vytvořeny s využitím modelu **Gemini AI** (Google).
  
## Citace:
How to Build a Pico Macro Pad. Online. 2021. Dostupné z: https://www.hackster.io/1NextPCB/how-to-build-a-pico-macro-pad-3638e6. [cit. 2025-12-01].

A made a Raspberry Pi Pico Macro Board!. Online. 2020. Dostupné z: https://www.reddit.com/r/raspberry_pi/comments/n2s3i8/a_made_a_raspberry_pi_pico_macro_board/. [cit. 2025-12-01].

Raspberry Pi Pico - DIY Macro Keyboard. Online. Novaspirit Tech. 2021. Dostupné z: https://www.youtube.com/watch?v=aEWptdD32iA. [cit. 2025-12-01].

GOOGLE. Gemini [software]. Verze z 17. prosince 2025. Mountain View: Google, 2025 [cit. 2025-12-17]. Dostupné z: https://gemini.google.com

Wired USB keyboard, mouse, controller to Bluetooth w/ $6 Raspberry Pi Pico W. Online. Kenjinerd. 2025. Dostupné z: https://www.youtube.com/watch?v=YuHbTrccshw. [cit. 2025-12-01].

Raspberry Pi. Online. Dostupné z: https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#pico-1-family. [cit. 2025-12-13].
