html_content = r"""<!DOCTYPE html>
<html lang="sl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>1. Magnetni krogi - Interaktivni učbenik</title>
    <link rel="stylesheet" href="style.css">
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        .task { background-color: #fcfcfc; border: 1px solid #e0e0e0; padding: 20px; border-radius: 8px; margin-bottom: 30px; }
        .solution-step { margin-top: 15px; border-left: 3px solid var(--primary-color); padding-left: 15px; background: #f4f7f6; }
        .formula-box { background-color: #f8f9fa; border-left: 4px solid var(--primary-color); padding: 1rem; margin: 1rem 0; font-family: monospace; font-size: 1.1rem; overflow-x: auto;}
    </style>
</head>
<body>
    <header>
        <h1>1. Magnetni krogi</h1>
        <p>Popoln pregled in zbirka nalog iz področja magnetnih krogov z interaktivnimi razlagami in skicami.</p>
    </header>

    <main class="container">
        <a href="index.html" style="display:inline-block; margin-bottom: 20px; color: var(--primary-color); text-decoration: none;">&larr; Nazaj na zemljevid</a>

        <!-- ... Enačbe ... -->
        <section class="content-section">
            <h2>Uvodne Enačbe in Koncepti</h2>
            <p>Osnova za izračunavanje magnetnih krogov so naslednje enačbe:</p>
            <ul>
                <li><strong>Magnetna napetost:</strong> \( V_m = N \cdot i \)</li>
                <li><strong>Ohmov zakon za magnetne kroge:</strong> \( V_m = \Phi \cdot R_m \)</li>
                <li><strong>Reluktanca (magnetna upornost):</strong> \( R_m = \frac{l}{\mu \cdot A} \), pri čemer je \( \mu = \mu_r \cdot \mu_0 \)</li>
                <li><strong>Gostota magnetnega pretoka:</strong> \( B = \frac{\Phi}{A} \) in \( B = \mu \cdot H \)</li>
            </ul>
        </section>

        <!-- Naloga 1.1 -->
        <section class="task">
            <h3>NALOGA 1.1: Magnetni krog – transformatorsko jedro z zračno režo</h3>
            <p><strong>Podatki:</strong> \( A_{Fe} = A_\delta = 9 \cdot 10^{-4} \text{ m}^2 \), \( l_{Fe} = 0.3 \text{ m} \), \( N = 500 \), \( \mu_r = 70000 \).</p>

            <div class="real-world-box">
                <div class="real-world-title">
                    <svg width="24" height="24" viewBox="0 0 24 24"><path d="M9 21c0 .55.45 1 1 1h4c.55 0 1-.45 1-1v-1H9v1zm3-19C8.14 2 5 5.14 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.86-3.14-7-7-7zm2.85 11.1l-.85.6V16h-4v-2.3l-.85-.6A4.997 4.997 0 0 1 7 9c0-2.76 2.24-5 5-5s5 2.24 5 5c0 1.63-.8 3.16-2.15 4.1z"/></svg>
                    Uporaba v praksi
                </div>
                <p><strong>Zakaj imajo nekateri transformatorji zračno režo?</strong> Zračna reža močno poveča skupno reluktanco magnetnega kroga, kar preprečuje, da bi se železno jedro prehitro magnetno nasitilo ob visokih enosmernih tokovih (npr. pri dušilkah v stikalnih napajalnikih - "flyback" transformatorjih). Zrak služi kot hranilnik magnetne energije.</p>
            </div>

            <p><strong>Interaktivni preizkus:</strong> Opazuj, kako dolžina zračne reže \( \delta \) (v mm) vpliva na skupno reluktanco in potreben magnetilni tok za vzpostavitev polja \( B = 1 \text{ T} \).</p>

            <div class="interactive-container">
                <div class="interactive-controls">
                    <div class="control-group">
                        <label for="slider-delta-1">Dolžina reže \( \delta \) [mm]: <span id="val-delta-1">0.50</span></label>
                        <input type="range" id="slider-delta-1" min="0" max="5" step="0.05" value="0.5" oninput="updateTask1()">
                    </div>
                    <div class="interactive-results">
                        <div>R_m_Fe: 3789 A/Vs (nespremenjeno)</div>
                        <div>R_m_δ: <span id="res-rmg-1">4.42e5</span> A/Vs</div>
                        <div>Skupni R_m: <span id="res-rmt-1">4.46e5</span> A/Vs</div>
                        <div style="margin-top:10px; font-weight:bold;">Potreben tok (i_μ): <span id="res-i-1">0.80</span> A</div>
                    </div>
                </div>
                <div class="interactive-svg-wrapper">
                    <svg id="svg-core-1" width="200" height="200" viewBox="0 0 200 200">
                        <path d="M 40,40 L 160,40 L 160,160 L 40,160 Z" fill="none" stroke="#ccc" stroke-width="40"/>
                        <!-- Zračna reža (bel pravokotnik, ki ga bomo širili) -->
                        <rect id="svg-gap-1" x="140" y="90" width="40" height="5" fill="#fafafa" stroke="#333" stroke-width="1"/>
                        <text x="175" y="100" font-size="12" fill="#333" font-family="sans-serif">δ</text>
                        <!-- Tuljava -->
                        <path d="M 20,70 Q 10,80 30,90 Q 50,100 30,110 Q 10,120 30,130" fill="none" stroke="#e67e22" stroke-width="5"/>
                        <text x="15" y="65" font-size="14" fill="#e67e22" font-family="sans-serif">N=500</text>
                    </svg>
                </div>
            </div>

            <details>
                <summary>Prikaži uradno rešitev in postopek z enačbami (iz izhodišča δ = 0.5 mm)</summary>
                <div class="solution-step">
                    <h4>a) Izračun reluktanc:</h4>
                    <p>Reluktanca železa:</p>
                    <div class="formula-box">\[ R_{mFe} = \frac{l_{Fe}}{\mu_r \cdot \mu_0 \cdot A_{Fe}} = 3789 \text{ A/Vs} \]</div>
                    <p>Reluktanca zračne reže:</p>
                    <div class="formula-box">\[ R_{m\delta} = \frac{\delta}{\mu_0 \cdot A_\delta} = \frac{0.0005}{4\pi \cdot 10^{-7} \cdot 9 \cdot 10^{-4}} = 4.42 \cdot 10^5 \text{ A/Vs} \]</div>
                </div>
                <div class="solution-step">
                    <h4>b) Magnetni pretok:</h4>
                    <div class="formula-box">\[ \Phi = B_{Fe} \cdot A_{Fe} = 1 \cdot 0.0009 = 9 \cdot 10^{-4} \text{ Vs} \]</div>
                </div>
                <div class="solution-step">
                    <h4>c) Magnetilni tok:</h4>
                    <div class="formula-box">\[ i_\mu = \frac{\Phi \cdot (R_{mFe} + R_{m\delta})}{N} = 0.8 \text{ A} \]</div>
                </div>
            </details>
        </section>

        <!-- Naloga 1.2 -->
        <section class="task">
            <h3>NALOGA 1.2: Magnetni krog sinhronskega stroja</h3>
            <p>Predpostavimo \( \mu \to \infty \) (kar pomeni \( R_{mFe} = 0 \)). Podatki: \( N = 1000 \), \( A_\delta = 0.2 \text{ m}^2 \).</p>

            <div class="real-world-box">
                <div class="real-world-title">
                    <svg width="24" height="24" viewBox="0 0 24 24"><path d="M9 21c0 .55.45 1 1 1h4c.55 0 1-.45 1-1v-1H9v1zm3-19C8.14 2 5 5.14 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.86-3.14-7-7-7zm2.85 11.1l-.85.6V16h-4v-2.3l-.85-.6A4.997 4.997 0 0 1 7 9c0-2.76 2.24-5 5-5s5 2.24 5 5c0 1.63-.8 3.16-2.15 4.1z"/></svg>
                    Uporaba v praksi
                </div>
                <p><strong>Sinhronski stroji in rotacijska polja:</strong> V generatorjih (elektrarne) ali velikih motorjih se rotor vrti znotraj statorja. Med njima *mora* biti fizičen razmik, da ne trčita - to je zračna reža. Magnetni pretok mora preskočiti iz rotorja skozi zračno režo v stator in potem spet nazaj. Zato sta tu **dve zaporedni zračni reži** v poti silnic.</p>
            </div>

            <p><strong>Interaktivni preizkus:</strong> Spreminjaj vzbujalni tok rotorskega magneta in opazuj, kakšno gostoto magnetnega polja v zračni reži (\( B_\delta \)) dobimo. Zračna reža je fiksna pri 1 cm (\( 2 \cdot 1\text{cm} = 0.02\text{m} \)).</p>

            <div class="interactive-container">
                <div class="interactive-controls">
                    <div class="control-group">
                        <label for="slider-tok-2">Vzbujalni tok \( i \) [A]: <span id="val-tok-2">10</span></label>
                        <input type="range" id="slider-tok-2" min="1" max="50" step="1" value="10" oninput="updateTask2()">
                    </div>
                    <div class="interactive-results">
                        <div>Magnetna nap. (\( V_m \)): <span id="res-vm-2">10000</span> A</div>
                        <div>Magnetni pretok (\( \Phi \)): <span id="res-phi-2">0.126</span> Wb</div>
                        <div style="margin-top:10px; font-weight:bold; color:var(--primary-color);">Gostota B_δ: <span id="res-b-2">0.63</span> T</div>
                    </div>
                </div>
                <div class="interactive-svg-wrapper">
                    <svg width="250" height="200" viewBox="0 0 250 200">
                        <!-- Stator zunaj -->
                        <path d="M 20,20 L 230,20 L 230,180 L 20,180 Z" fill="none" stroke="#bdc3c7" stroke-width="20"/>
                        <!-- Rotor notri -->
                        <rect x="70" y="50" width="110" height="100" fill="#7f8c8d" />
                        <!-- Zračna reža -->
                        <!-- Prikaz B vektorjev -->
                        <g id="svg-b-arrows-2" stroke="#e74c3c" stroke-width="2" marker-end="url(#arrowhead)">
                             <!-- Zgoraj -->
                             <line x1="125" y1="50" x2="125" y2="30"/>
                             <!-- Spodaj -->
                             <line x1="125" y1="180" x2="125" y2="150"/>
                        </g>
                        <defs>
                            <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                                <polygon points="0 0, 10 3.5, 0 7" fill="#e74c3c" />
                            </marker>
                        </defs>
                        <text x="135" y="45" font-size="12" fill="#e74c3c">δ</text>
                    </svg>
                </div>
            </div>

            <details>
                <summary>Prikaži uradno rešitev in postopek</summary>
                <div class="solution-step">
                    <div class="formula-box">
                        \[ \Phi \approx \frac{V_m}{R_\delta} = \frac{N \cdot i}{\frac{2\delta}{\mu_0 A_\delta}} = 1000 \cdot 10 \cdot \frac{4\pi \cdot 10^{-7} \cdot 0.2}{2 \cdot 10^{-2}} = 0.126 \text{ Wb} \]
                        \[ B_\delta = \frac{\Phi}{A_\delta} = \frac{0.126}{0.2} = 0.63 \text{ T} \]
                    </div>
                </div>
            </details>
        </section>

        <!-- Naloga 1.7 / 1.8 -->
        <section class="task">
            <h3>NALOGA 1.7 in 1.8: Dve sklopljeni navitji in vpliv zračne reže</h3>
            <p><strong>Naloga 1.7:</strong> Izračunajte samoinduktivnosti \( L_{11} \) in \( L_{22} \) <strong>brez zračne reže</strong>.<br>
            <strong>Naloga 1.8:</strong> Ponovite izračun za primer <strong>z zračno režo</strong> \( \delta = 2.0 \text{ mm} \).</p>
            <p>Podatki: \( N_1 = 50 \), \( N_2 = 100 \), \( \mu_r = 4000 \), \( l = 1 \text{ m} \), \( A_{Fe} = 25 \cdot 10^{-4} \text{ m}^2 \).</p>

            <div class="real-world-box">
                <div class="real-world-title">
                    <svg width="24" height="24" viewBox="0 0 24 24"><path d="M9 21c0 .55.45 1 1 1h4c.55 0 1-.45 1-1v-1H9v1zm3-19C8.14 2 5 5.14 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.86-3.14-7-7-7zm2.85 11.1l-.85.6V16h-4v-2.3l-.85-.6A4.997 4.997 0 0 1 7 9c0-2.76 2.24-5 5-5s5 2.24 5 5c0 1.63-.8 3.16-2.15 4.1z"/></svg>
                    Uporaba v praksi
                </div>
                <p><strong>Zakaj uporabljamo sklopljena navitja?</strong> To je osnova vsakega transformatorja. Zveza med primarno in sekundarno stranjo omogoča pretvorbo visoke napetosti iz omrežja na npr. 5V za polnjenje telefona. Dodana zračna reža drastično zniža induktivnost navitja in povzroči slabo sklopljenost, zato transformatorji v omrežju NIMAJO zračne reže. Imajo pa jih dušilke, kjer rabimo linearnejšo karakteristiko in preprečitev nasičenja (saturation).</p>
            </div>

            <p><strong>Interaktivni preizkus:</strong> Vklapljaj in izklapljaj zračno režo ali zmanjšaj njeno širino, da vidiš, kako drastično reža "ubije" induktivnost jedra z visoko permeabilnostjo.</p>

            <div class="interactive-container">
                <div class="interactive-controls">
                    <div class="control-group">
                        <label for="slider-delta-8">Dolžina reže \( \delta \) [mm]: <span id="val-delta-8">2.0</span></label>
                        <input type="range" id="slider-delta-8" min="0" max="10" step="0.1" value="2" oninput="updateTask8()">
                        <small style="color:#777">Nastavi na 0 mm, da dobiš rezultat naloge 1.7!</small>
                    </div>
                    <div class="interactive-results">
                        <div>Skupni \( R_m \): <span id="res-rm-8">716020</span> A/Vs</div>
                        <div style="margin-top:10px; font-weight:bold;">Induktivnost L_11: <span id="res-l11-8">3.5</span> mH</div>
                        <div style="font-weight:bold;">Induktivnost L_22: <span id="res-l22-8">14.0</span> mH</div>
                    </div>
                </div>
                <div class="interactive-svg-wrapper">
                    <svg width="250" height="200" viewBox="0 0 250 200">
                        <path d="M 50,40 L 200,40 L 200,160 L 50,160 Z" fill="none" stroke="#2c3e50" stroke-width="30"/>
                        <!-- Zračna reža -->
                        <rect id="svg-gap-8" x="115" y="25" width="20" height="30" fill="#fafafa" stroke="#333" stroke-width="1"/>
                        <!-- N1 in N2 tuljave -->
                        <rect x="30" y="70" width="40" height="60" fill="#e67e22" rx="5"/>
                        <text x="40" y="105" font-size="16" fill="white">N1</text>
                        <rect x="180" y="70" width="40" height="60" fill="#3498db" rx="5"/>
                        <text x="190" y="105" font-size="16" fill="white">N2</text>
                    </svg>
                </div>
            </div>

            <details>
                <summary>Prikaži uradno rešitev in postopek za 1.7 (brez reže) in 1.8 (z režo 2mm)</summary>
                <div class="solution-step">
                    <h4>Rešitev 1.7 (Brez zračne reže, δ = 0):</h4>
                    <div class="formula-box">
                        \[ L_{11} = \frac{N_1^2 \cdot \mu_r \cdot \mu_0 \cdot A_{Fe}}{l} = 31.4 \text{ mH} \]
                        \[ L_{22} = \frac{N_2^2 \cdot \mu_r \cdot \mu_0 \cdot A_{Fe}}{l} = 125.7 \text{ mH} \]
                    </div>
                </div>
                <div class="solution-step">
                    <h4>Rešitev 1.8 (Z zračno režo δ = 2 mm):</h4>
                    <div class="formula-box">
                        \[ R_{mc} = R_{mFe} + R_{m\delta} = 79.4 \cdot 10^3 + 636.6 \cdot 10^3 = 716.02 \cdot 10^3 \text{ A/Vs} \]
                        \[ L_{11} = \frac{N_1^2}{R_{mc}} = \frac{50^2}{716.02 \cdot 10^3} = 3.5 \text{ mH} \]
                        \[ L_{22} = \frac{N_2^2}{R_{mc}} = 14 \text{ mH} \]
                    </div>
                </div>
            </details>
        </section>


        <!-- Trdomagnetni materiali in preostale naloge izvirno oblikovane -->
        <section class="content-section">
            <h2>Magnetni krogi s trdomagnetnimi materiali</h2>

            <div class="real-world-box">
                <div class="real-world-title">
                    <svg width="24" height="24" viewBox="0 0 24 24"><path d="M9 21c0 .55.45 1 1 1h4c.55 0 1-.45 1-1v-1H9v1zm3-19C8.14 2 5 5.14 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.86-3.14-7-7-7zm2.85 11.1l-.85.6V16h-4v-2.3l-.85-.6A4.997 4.997 0 0 1 7 9c0-2.76 2.24-5 5-5s5 2.24 5 5c0 1.63-.8 3.16-2.15 4.1z"/></svg>
                    Uporaba v praksi
                </div>
                <p><strong>Alnico 5 in stalni magneti:</strong> Trdomagnetni materiali ohranijo močno magnetno polje (velika remanenca \( B_r \)) tudi po tem, ko odstranimo zunanje vzbujanje. Uporabljajo se v BLDC motorjih (motorji brez ščetk v dronih, skuterjih, električnih avtomobilih), zvočnikih, senzorjih (Hall senzorji) in zadrževalnih magnetih. Alnico zlitine posebej so zelo stabilne pri visokih temperaturah.</p>
            </div>

            <p>Trdomagnetne materiale (npr. Alnico 5) karakterizira velika remanenčna gostota magnetnega pretoka \( B_r \) in velika koercitivna jakost magnetnega polja \( H_c \). Delovna točka se določi s presečiščem <strong>obremenilne karakteristike</strong> (odvisne od dimenzij magnetnega kroga in zračne reže) in materialove B-H krivulje (2. kvadrant histerezne zanke).</p>
        </section>

        <!-- Naloga 1.12 & 1.13 -->
        <section class="task">
            <h3>NALOGA 1.12 in 1.13: Trdomagnetni materiali v zračni reži</h3>
            <p><strong>1.12:</strong> Magnetni krog tvori jedro iz mehkomagnetnega materiala (\( \mu \to \infty \)), zračna reža \( \delta = 0.2 \text{ cm} \) in odsek iz trdomagnetnega materiala dolžine \( l_m = 1 \text{ cm} \). Prerezi \( A_m = A_\delta = 4 \text{ cm}^2 \). Izračunajte gostoto v reži.</p>
            <p><strong>1.13:</strong> Reža je pomanjšana na \( 2 \text{ cm}^2 \). Določi volumen magneta za \( B_\delta = 0.8 \text{ T} \) pri optimalni točki (energijski produkt 40 kJ/m³ pri B=1T in H=-40kA/m).</p>

            <details>
                <summary>Prikaži rešitev in postopek</summary>
                <div class="solution-step">
                    <h4>Rešitev 1.12:</h4>
                    <p>Obremenilna karakteristika:</p>
                    <div class="formula-box">
                        \[ B_m = -\mu_0 \cdot \frac{A_\delta}{A_m} \cdot \frac{l_m}{\delta} \cdot H_m = -6.28 \cdot 10^{-6} \cdot H_m \]
                    </div>
                    <p>Iz grafa histerezne zanke v pdf-ju za Alnico 5: \( B_m = 0.3 \text{ T} \). Ker je \( A_m = A_\delta \), je tudi \( B_\delta = 0.3 \text{ T} \).</p>
                </div>
                <div class="solution-step">
                    <h4>Rešitev 1.13:</h4>
                    <div class="formula-box">
                        \[ A_m = A_\delta \cdot \frac{B_\delta}{B_m} = 2 \cdot 10^{-4} \cdot \frac{0.8}{1.0} = 1.6 \cdot 10^{-4} \text{ m}^2 \]
                        \[ l_m = -\delta \cdot \frac{B_\delta}{\mu_0 \cdot H_m} = -0.002 \cdot \frac{0.8}{4\pi \cdot 10^{-7} \cdot (-40000)} = 0.0318 \text{ m} \]
                        \[ V_m = l_m \cdot A_m = 5.09 \cdot 10^{-6} \text{ m}^3 \]
                    </div>
                </div>
            </details>
        </section>

        <!-- Kviz -->
        <section class="quiz-section">
            <h3>Kviz: Utrjevanje celotne prve teme</h3>
            <p>S pomočjo drsnika zgoraj (pri Nalogi 1.8) odgovori na naslednje vprašanje:</p>
            <p>Če v vezju z dvema sklopljenima navitjema (N1=50, N2=100) nastavimo zračno režo natanko na <strong>5 mm (\( \delta = 5.0 \text{ mm} \))</strong>, kolikšna bo induktivnost prvega navitja \( L_{11} \) v mH?</p>
            <div class="input-group">
                <input type="number" id="quiz-final-input" placeholder="Vnesi mH" step="0.1">
                <button onclick="checkFinalQuiz()">Preveri odgovor</button>
            </div>
            <div id="quiz-final-feedback" class="feedback"></div>
        </section>

    </main>

    <footer>
        <p>Ustvarjeno za učenje in utrjevanje znanja.</p>
    </footer>

    <script>
        // JS logika za interaktivne drsnike
        const PI4e7 = 4 * Math.PI * 1e-7;

        function updateTask1() {
            let delta_mm = parseFloat(document.getElementById('slider-delta-1').value);
            document.getElementById('val-delta-1').innerText = delta_mm.toFixed(2);

            let delta_m = delta_mm / 1000.0;
            let rm_fe = 3789;
            let A_delta = 9e-4;

            let rm_g = delta_m / (PI4e7 * A_delta);
            let rm_tot = rm_fe + rm_g;

            let phi = 9e-4; // B=1T, A=9e-4
            let n = 500;
            let i = (phi * rm_tot) / n;

            document.getElementById('res-rmg-1').innerText = rm_g.toExponential(2);
            document.getElementById('res-rmt-1').innerText = rm_tot.toExponential(2);
            document.getElementById('res-i-1').innerText = i.toFixed(2);

            // Vizualni update SVG (širina gap elementa je sorazmerna)
            // Osnovna širina je bila 40 za gap, reža je debela 'height'.
            let gapHeight = Math.max(1, delta_mm * 10);
            document.getElementById('svg-gap-1').setAttribute('height', gapHeight);
            // premaknemo, da ostane sredinsko
            document.getElementById('svg-gap-1').setAttribute('y', 100 - gapHeight/2);
        }

        function updateTask2() {
            let i = parseFloat(document.getElementById('slider-tok-2').value);
            document.getElementById('val-tok-2').innerText = i;

            let N = 1000;
            let A = 0.2;
            let delta = 0.01; // 1 cm

            let Vm = N * i;
            let phi = (N * i * PI4e7 * A) / (2 * delta);
            let B = phi / A;

            document.getElementById('res-vm-2').innerText = Vm;
            document.getElementById('res-phi-2').innerText = phi.toFixed(3);
            document.getElementById('res-b-2').innerText = B.toFixed(3);

            // Vizualni update puščic: deblje puščice pomenijo večje polje
            let strokeW = Math.max(1, B * 4);
            document.getElementById('svg-b-arrows-2').setAttribute('stroke-width', strokeW);
        }

        function updateTask8() {
            let delta_mm = parseFloat(document.getElementById('slider-delta-8').value);
            document.getElementById('val-delta-8').innerText = delta_mm.toFixed(1);

            let delta_m = delta_mm / 1000.0;
            let l_fe = 1.0 - delta_m;
            let A = 25e-4;
            let mu_r = 4000;

            let rm_fe = l_fe / (mu_r * PI4e7 * A);
            let rm_g = delta_m / (PI4e7 * A);
            let rm_tot = rm_fe + rm_g;

            let N1 = 50;
            let N2 = 100;

            let l11 = (N1 * N1) / rm_tot * 1000; // v mH
            let l22 = (N2 * N2) / rm_tot * 1000; // v mH

            document.getElementById('res-rm-8').innerText = Math.round(rm_tot);
            document.getElementById('res-l11-8').innerText = l11.toFixed(1);
            document.getElementById('res-l22-8').innerText = l22.toFixed(1);

            // Vizualni update SVG gap (če delta=0, ga skrijemo)
            let gapWidth = delta_mm * 4;
            let gap = document.getElementById('svg-gap-8');
            if (delta_mm === 0) {
                gap.style.display = 'none';
            } else {
                gap.style.display = 'block';
                gap.setAttribute('width', gapWidth);
                gap.setAttribute('x', 125 - gapWidth/2);
            }
        }

        // Initialize sliders on load
        window.onload = function() {
            updateTask1();
            updateTask2();
            updateTask8();
        };

        function checkFinalQuiz() {
            let input = parseFloat(document.getElementById('quiz-final-input').value);
            let fb = document.getElementById('quiz-final-feedback');

            if (isNaN(input)) {
                fb.className = "feedback error"; fb.innerText = "Prosim vnesi številko."; return;
            }
            // Pri 5 mm reluktanca zraste na okoli 1.67e6, L11 = 50^2 / 1.67e6 = 1.5 mH
            if (input >= 1.4 && input <= 1.6) {
                fb.className = "feedback success"; fb.innerText = "Odlično! Pravilen odgovor je 1.5 mH. Zračna reža drastično zmanjša induktivnost.";
            } else {
                fb.className = "feedback error"; fb.innerText = "Ni povsem prav. Uporabi drsnik pri Nalogi 1.8 in nastavi dolžino na 5.0 mm, nato preberi L_11!";
            }
        }
    </script>
</body>
</html>
"""
with open('1_magnetni_krogi.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
