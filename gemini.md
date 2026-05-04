
## Pravila za pisanje vsebine in za razvijalce (Slog za začetnike)
Da bo učbenik maksimalno razumljiv, se je pri vsaki nalogi potrebno držati naslednjih pravil:
1. **Brez izgube informacij in enačb:** Ohani 100% vseh matematičnih enačb in izpeljav iz PDF-jev. Vsako vrstico prikaži v MathJax `\[ ... \]` in razloži vse pretvorbe in logične preskoke (ne preskakuj korakov).
2. **Analogoije:** Uporabljaj analogije z električnimi krogi (magnetna napetost = električna napetost, reluktanca = upor, pretok = tok).
3. **Pretvorbe enot:** Jasno razloži, kako pretvarjamo enote (npr. zakaj je $1 \text{ cm}^2 = 10^{-4} \text{ m}^2$, zakaj mm v m).
4. **Pomen predpostavk:** Kadar je v nalogi podano $\mu \to \infty$ ali "zanemarite stresanje", točno razloži, kaj to pomeni v fizikalnem in matematičnem smislu.
5. **Real World Use:** Pri vsaki nalogi in konceptu obvezno vključi okvirček z opisom rabe v resničnem svetu.
6. **Kvizi in Interaktivnost:** Vsaka naloga mora imeti delujoč kviz (z JavaScript preverjanjem) ter interaktivni SVG z gumbi/sliderji in sprotnim preračunavanjem podatkov.
7. **SVG Opozorilo:** Za risanje linij, krivulj in tuljav v SVG vedno uporabljaj element `<path>`. Ne uporabljaj `<g>` z atributom `d=`, saj to brskalniki ignorirajo!

# Zemljevid interaktivnega učbenika (Električni stroji)

To je glavno kazalo in seznam vseh PDF gradiv, ki jih je potrebno pretvoriti v interaktivni učbenik, da se zagotovi, da ni izgubljena nobena informacija.
Zaradi kompleksnosti in obsežnosti so PDF-ji razdeljeni na manjše, obvladljive korake, kar omogoča vključitev vseh enačb, kvizov, "Real World Uses" in interaktivnih SVG elementov.

## Pretvornik po korakih

- [x] **Korak 1:** Priprava strukture in pregled repozitorija
- [x] **Korak 2:** Priprava moderne vizualne podobe in navigacije
- [x] **Korak 3:** Obnova 1. dela - Naloge 1.1 do 1.3 (1_magnetni_krogi.html)
- [x] **Korak 4:** POPRAVEK: Prave naloge 1.4, 1.5 in 1.6 z vsemi skicami, grafi in razlagami
- [x] **Korak 5:** Obdelava PDF strani 12 do 15 (Naloga 1.7 in 1.8 z vsemi detajli in grafi)
- [x] **Korak 6:** Obdelava PDF strani 16 do 18 (Naloga 1.9, Histerezna zanka in vpeljava trdomagnetnih materialov)
- [x] **Korak 7:** Obdelava PDF strani 19 do 21 (Naloge 1.10 - 1.11, Sila magnetnega polja)
- [x] **Korak 8:** Obdelava PDF strani 22 do konca poglavja (Naloge 1.12 - 1.13 in zaključek 1. poglavja)

**2. POGLAVJE: TRANSFORMATORJI (`2-Transformatorji 2021.pdf` in `2_transformatorji.html`)**
- [x] **Korak 9:** Naloge 2.1, 2.2 in 2.3 (Osnovne enačbe transformatorja, harmonske komponente, izračun mase bakra) - *Strani 1-3 v PDF-ju*.
- [x] **Korak 10:** Naloge 2.4 in 2.5 (Trifazni transformatorji, vezave Yz5, preračuni izgub in izkoristek pri spremembi frekvence in napetosti) - *Strani 4-8 v PDF-ju*.
- [x] **Korak 11:** Naloge 2.6, 2.7 in 2.8 (Fazorski diagrami, nadomestno vezje, paralelno obratovanje transformatorjev) - *Strani 9-13 v PDF-ju*.
- [x] **Korak 12:** Naloge 2.9, 2.10 in 2.11 (Segrevanje stroja, časovna konstanta in dopustna preobremenitev) - *Strani 14-16 v PDF-ju*.
- [x] **Korak 13:** Naloge 2.12 in 2.13 (Prevezave navitij, urni koti, asimetrične in napačne vezave - vektorski diagrami) - *Strani 17-21 v PDF-ju*.

**3. POGLAVJE: SINHRONSKI STROJI (`3-Sinhronski_stroji 2021_Brez navitij.pdf` in `3_sinhronski_stroji.html`)**
- [x] **Korak 14:** Naloge 3.2, 3.3 in 3.4 (Sinhronski generator s cilindričnim rotorjem, kratek stik in V-krivulje) - *Osnove obratovanja turbo generatorjev in kompenzacija*.
- [ ] **Korak 15:** Implementacija preostalih nalog 3. poglavja (Naloge 3.5 dalje) - razdelitev bo narejena naknadno.

### 1. Magnetni krogi (Datoteka: `1_magnetni_krogi.html`)
Trenutno implementirano:
* **Uvodne enačbe in koncepti** (Ohmov zakon za mag. kroge, reluktanca).
* **Naloga 1.1:** Transformatorsko jedro z zračno režo (interaktivni drsnik, Real World uporaba v dušilkah, Kviz o razmerju reluktanc).
* **Naloga 1.2:** Magnetni krog sinhronskega stroja (interaktivni drsnik za tok, Real World uporaba strojev, Kviz o vplivu permeabilnosti).
* **Naloga 1.3:** Dve paralelni zračni reži (podroben postopek nadomestnih reluktanc, Kviz o paralelni vezavi).

* **Naloga 1.4:** Toroidni magnetni krog z zračno režo (interaktivni SVG drsnik toroida, izračun poti iz polmera, kviz o stresanju).
* **Naloga 1.5:** Uporaba magnetilnice (nelinearna analiza, branje B-H grafa, kviz o nasičenju in padcu permeabilnosti).
* **Naloga 1.6:** Navitje s časovno spremenljivo napetostjo (Faradayev zakon, drsnik za frekvenco in izračun E_max, kviz o primerjavi 50Hz in 60Hz).

## AVDITORNE VAJE (`ES_AV - Vaja XX.pdf`)
Dopolnitev gradiv z dodatnimi zunanjimi vajami. Za vsako vajo je potrebno narediti pripadajočo `.html` datoteko, dodati vsa matematična izvajanja, ustvariti interaktivne SVG skice, kvize in "Real World Uses".

- [x] **Korak 16:** Vaja 00 (Uvodne informacije o tematiki in področju električnih strojev) - `vaja_00.html`
- [x] **Korak 17:** Vaja 01 (Magnetilni tok dušilke navite na toroidno jedro iz feromagnetnega materiala) - `vaja_01.html`
- [x] **Korak 18:** Vaja 02 (Enofazni transformator brez zračne reže, jedro v obliki kvadratnega okvirja) - `vaja_02.html`
- [ ] **Korak 19:** Vaja 03 (Transformator podatki Sn=50kVA, p=6, reševanje napetosti/izgub) - `vaja_03.html`
- [ ] **Korak 20:** Vaja 04 (Enofazni transformator Sn=50kVA, U1n=2400V, nadomestno vezje in tokovi) - `vaja_04.html`
- [ ] **Korak 21:** Vaja 05 (Razvoj kazalčnega diagrama transformatorja) - `vaja_05.html`
- [ ] **Korak 22:** Vaja 06 (Transformator Sn=100kVA z določenim izkoristkom in uK) - `vaja_06.html`
- [ ] **Korak 23:** Vaja 07 (Trifazni transformator splošne lastnosti in naloge) - `vaja_07.html`
- [ ] **Korak 24:** Vaja 08 (Trifazni transformator Yzn5, kratki stiki ali nesimetrije) - `vaja_08.html`
- [ ] **Korak 25:** Vaja 09 (Paralelno obratovanje transformatorjev) - `vaja_09.html`
- [ ] **Korak 26:** Vaja 10 (Segrevanje transformatorja, razmerje izgub ξ=3) - `vaja_10.html`
- [ ] **Korak 27:** Vaja 11 (Načrtovanje max nadtemperature transformatorja) - `vaja_11.html`
- [ ] **Korak 28:** Vaja 12 (Časovna konstanta segrevanja T=1h, ciklično obratovanje) - `vaja_12.html`
- [ ] **Korak 29:** Vaja 13 (Sinhronski generator uvodne naloge) - `vaja_13.html`
- [ ] **Korak 30:** Vaja 14 (Sinhronski generator 6.3MVA, 10kV, cosφ=0.7) - `vaja_14.html`
- [ ] **Korak 31:** Vaja 15 (Nadaljevanje vaj SG 6.3MVA s spremenjenimi pogoji) - `vaja_15.html`
- [ ] **Korak 32:** Vaja 16 (Trifazni SG 25MVA, 10kV, cosφ=0.8) - `vaja_16.html`
- [ ] **Korak 33:** Vaja 17 (Asinhronski stroj uvod in lastnosti) - `vaja_17.html`
- [ ] **Korak 34:** Vaja 18 (Energijska bilanca trifaznega, 4-polnega AM s kratkostično kletko) - `vaja_18.html`
