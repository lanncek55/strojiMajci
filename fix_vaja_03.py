import re

with open('vaja_03.html', 'r') as f:
    content = f.read()

# Replace missing mathematical parts
missing_math = r"""
                <p><strong>Fizikalno ozadje izgub v železu:</strong></p>
                <p>Izgube v železu se delijo na histerezne in vrtinčne izgube.</p>
                <div class="formula-box">
                    \[ P_h = k_h \cdot \left(\frac{f}{50}\right) \cdot B^x \cdot m_{Fe}, \quad x = (1.5 \div 3) \quad \text{(histerezne izgube)} \]
                    \[ P_v = k_v \cdot \left(\frac{f}{50}\right)^2 \cdot B^2 \cdot m_{Fe} \quad \text{(vrtinčne izgube)} \]
                </div>
                <p>Za izračun večinoma uporabljamo specifične izgube (\(p_{Fe}\)), ki jih poda proizvajalec feromagnetne pločevine. To so izgube na 1 kg materiala pri točno določeni frekvenci (največkrat 50 Hz) in izbrani maksimalni gostoti magnetnega pretoka (npr. 1 T ali 1.5 T). Splošna enačba za celotne izgube je podana kot poenostavljen združen izraz:</p>
                <div class="formula-box">
                    \[ P_{Fe} = k_{Fe} \cdot \left(\frac{f}{50}\right)^2 \cdot B^2 \cdot m_{Fe} \]
                </div>
                <p>Za izračun vpliva frekvence pri konstantni napetosti se vrnemo k osnovni definiciji inducirane napetosti iz prejšnje vaje (\(E \approx U = 4.44 \cdot f \cdot N_1 \cdot B \cdot S_{Fe}\)).</p>
                <div class="formula-box">
                    \[ U = \text{konst} \cdot f \cdot B \quad \rightarrow \quad B \propto \frac{U}{f} \]
                </div>
                <p>Ker iz podatkov izhaja \(U_1' = U_{1n}\), sledi tudi \(E' = E\). Z deljenjem enačb za inducirano napetost v nazivnem in spremenjenem stanju dobimo:</p>
                <div class="formula-box">
                    \[ 1 = \frac{f' \cdot B'}{f \cdot B} \quad \rightarrow \quad B' = B \cdot \frac{f}{f'} \]
                </div>
                <p>Tako kot pri relaciji za napetost, sedaj to novo obratovalno stanje primerjamo (delimo enačbi) z enačbo za celotne izgube železa (\(P_{Fe}\)), s čimer se eliminirajo konstante (masa, preseki, koeficienti materiala):</p>
                <div class="formula-box">
                    \[ \frac{P'_{Fe}}{P_{Fe}} = \frac{k_{Fe} \cdot \left(\frac{f'}{50}\right)^2 \cdot B'^2 \cdot m_{Fe}}{k_{Fe} \cdot \left(\frac{f}{50}\right)^2 \cdot B^2 \cdot m_{Fe}} \]
                    \[ \frac{P'_{Fe}}{P_{Fe}} = \left(\frac{f'}{f}\right)^2 \cdot \left( \frac{B'}{B} \right)^2 = \left(\frac{f'}{f}\right)^2 \cdot \left(\frac{f}{f'}\right)^2 = \frac{f'^2}{f^2} \cdot \frac{f^2}{f'^2} = 1 \quad \text{...ČAKAJ, originalno besedilo poenostavi z } P \propto f \cdot B^2 \text{!} \]
                </div>
                <p>Opomba: v originalnem PDF izrazu je uporabljena linearna aproksimacija \(P_{Fe} \propto f \cdot B^2\). Preverimo uradno PDF rešitev za deljenje izgub:</p>
                <div class="formula-box">
                    \[ \frac{P'_{Fe}}{P_{Fe}} = \frac{f' \cdot B'^2}{f \cdot B^2} = \left(\frac{f'}{f}\right) \cdot \left(\frac{f}{f'}\right)^2 = \frac{f}{f'} \]
                    \[ \frac{P'_{Fe}}{P_{Fe}} = \frac{42}{50} = 0.84 \]
                </div>
                <p>Sedaj izračunamo nove izgube v železu:</p>
                <div class="formula-box">
                    \[ P'_{Fe} = P_{Fe} \cdot 0.84 = 300 \cdot 0.84 = 252 \text{ W} \]
                </div>
"""

start_str = '<p>Izgube v železu pa so močno odvisne'
end_str = '\\[ P\'_{Fe} = 300 \\cdot 0.84 = \\underline{\\underline{252 \\text{ W}}} \\]\n                </div>'

start_idx = content.find(start_str)
end_idx = content.find(end_str) + len(end_str)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + missing_math + content[end_idx:]

with open('vaja_03.html', 'w') as f:
    f.write(content)
