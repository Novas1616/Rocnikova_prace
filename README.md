# Ročníková práce: Tvorba vlastní macro klávesnice (Button boxu pro hry)

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

## 5. Testování a uvedení do provozu

Po fyzické montáži tlačítek do krabičky a propojení s Raspberry Pi Pico W proběhlo finální testování na PC s operačním systémem Windows. 
* Zařízení je po připojení okamžitě automaticky detekováno jako běžná klávesnice.
* Úspěšně bylo otestováno odesílání jednoduchých kláves, složitějších klávesových zkratek i delších sekvencí kláves (maker).
* Dlouhodobý test v závodních hrách potvrdil, že zařízení funguje stabilně, latence je neznatelná a mechanické provedení krabičky bez problémů odolává běžnému používání.

## 6. Závěr

Ročníková práce byla úspěšně dokončena a všechny stanovené cíle byly splněny. Podařilo se mi navrhnout, naprogramovat a fyzicky sestavit plně funkční macro klávesnici. Změna plánu z 3D tisku na úpravu hotové plastové krabičky se ukázala jako efektivní krok, který urychlil montáž a zajistil prototypu profesionální a robustní vzhled. Zařízení nyní aktivně využívám při hraní simulátorů, čímž projekt splnil svůj původní praktický účel. Práce mi přinesla cenné zkušenosti s jazykem CircuitPython, USB komunikací a praktickou elektronikou.
