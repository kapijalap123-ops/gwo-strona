import os
from flask import Flask, send_from_directory

app = Flask(__name__)


# Serwowanie statycznych plików (np. logo)
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

# Strona główna
@app.route("/")
def home():
    return """
    <body style="
        margin: 0;
        min-height: 100vh;
        background-color: white;
        font-family: Verdana;
        color: black;
        position: relative;
    ">
        <!-- Czerwone pasy po bokach -->
        <div style='position: absolute; left: 300px; top: 0; width: 150px; height: 100%; background-color: red;'></div>
        <div style='position: absolute; right: 300px; top: 0; width: 150px; height: 100%; background-color: red;'></div>

        <!-- Nagłówek w czerwonym boxiku z ramką -->
        <div style="
            position: absolute; top: 20px; left: 50%; transform: translateX(-50%);
            padding: 15px 30px; border-radius: 10px; border: 3px solid red;
        ">
            <h1 style="color: red; font-family: Arial Black; margin: 0;">
                🧰 Strona o GWO i o pierwszej pomocy 🧰
            </h1>
        </div>

<!-- BLOK GWO + strzałki + obrazek -->
<div style="
    position: absolute;
    top: 200px;
    left: 45%;  /* 👈 było 50%, przesunąłem w lewo */
    transform: translateX(-50%);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 40px;
">
    <!-- Blok tekstowy -->
    <div style="
        max-width: 500px;
        padding: 20px;
        border: 2px solid black;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        background-color: #f9f9f9;
        line-height: 1.4;
    ">
        <a href="/gwo" 
           style="text-decoration: none; color: black; font-weight: 900; font-size: 25px; transition: color 0.3s;"
           onmouseover="this.style.color='red'"
           onmouseout="this.style.color='black'">
           GWO
        </a> 
        <span style="display: block; font-size: 20px; font-weight: normal; text-align: justify; margin-top: 10px;">
            Celem GWO (Global Wind Organisation) jest zapewnienie maksymalnego bezpieczeństwa pracy w branży energetyki wiatrowej poprzez stworzenie i utrzymanie jednolitych, międzynarodowych standardów szkoleniowych. Organizacja dąży do tego, aby każda osoba pracująca przy turbinach wiatrowych była odpowiednio przeszkolona i przygotowana do reagowania w sytuacjach zagrożenia, zmniejszając liczbę wypadków i kontuzji, podnosząc świadomość bezpieczeństwa wśród pracowników i firm, ujednolicając szkolenia na całym świecie oraz tworząc kulturę bezpieczeństwa.
        </span>
    </div>

    <!-- Strzałki -->
    <div style="font-size: 60px; color: red; font-weight: bold;">➡️➡️➡️</div>

    <!-- Obrazek -->
    <img src="/static/gwo.png" 
         alt="Logo GWO" 
         style="
            width: 400px;
            height: auto;
            border: 4px solid black;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.3);
         ">
</div>



        <!-- BLOK PIERWSZA POMOC GWO + strzałki + obrazek -->
<div style="
    position: absolute;
    top: 750px;   /* 👈 niżej niż pierwszy blok */
    left: 45%;
    transform: translateX(-50%);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 40px;
">
    <!-- Blok tekstowy -->
    <div style="
        max-width: 500px;
        padding: 20px;
        border: 2px solid black;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        background-color: #f9f9f9;
        line-height: 1.4;
    ">
        <a href="/first_aid" 
           style="text-decoration: none; color: black; font-weight: 900; font-size: 25px; transition: color 0.3s;"
           onmouseover="this.style.color='red'"
           onmouseout="this.style.color='black'">
           Pierwsza Pomoc GWO
        </a> 
        <span style="display: block; font-size: 20px; font-weight: normal; text-align: justify; margin-top: 10px;">
            Celem pierwszej pomocy w ramach GWO jest zapewnienie, że każda osoba pracująca przy turbinach wiatrowych wie, jak reagować w nagłych sytuacjach. Szkolenia obejmują podstawy resuscytacji, opatrunki, postępowanie przy urazach i innych zagrożeniach zdrowotnych.
        </span>
    </div>

    <!-- Strzałki -->
    <div style="font-size: 60px; color: red; font-weight: bold;">➡️➡️➡️</div>

    <!-- Obrazek -->
    <img src="/static/gwo2.png" 
         alt="Pierwsza pomoc GWO" 
         style="
            width: 400px;
            height: auto;
            border: 4px solid black;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.3);
         ">
</div>
 </body>
    """


# 🔹 Podstrona GWO
@app.route("/gwo")
def gwo():
    return """
    <body style="font-family: Verdana; text-align: center; margin: 50px;">
        <h1 style="color: black; transition: color 0.3s;"
            onmouseover="this.innerHTML='🌍 Wszytko o GWO 🌍';"
            onmouseout="this.innerHTML='🌍 Strona GWO 🌍';">
            🌍 Strona GWO 🌍
        </h1>
        
        <div style="width: 80%; max-width: 800px; height: 400px; margin: 20px auto; padding: 20px; 
                    border: 2px solid black; border-radius: 10px; overflow-y: scroll; text-align: left; background-color: #f9f9f9;">
            <h2 style="color: black;">Co to jest GWO?</h2>
            <p><b>GWO</b> to skrót od <b>Global Wind Organisation</b>, czyli Światowej Organizacji Energetyki Wiatrowej.</p>
            <p>Organizacja została stworzona, aby poprawić <b>bezpieczeństwo i jakość szkoleń</b> w branży energetyki wiatrowej na całym świecie.</p>
            
            <h3>Dlaczego taki skrót?</h3>
            <ul>
                <li><b>G</b> – Global (Światowa)</li>
                <li><b>W</b> – Wind (Wiatrowa / energetyka wiatrowa)</li>
                <li><b>O</b> – Organisation (Organizacja)</li>
            </ul>
            
            <h3>Co robi GWO?</h3>
            <ul>
                <li>Tworzy <b>międzynarodowe standardy szkoleń</b> dla osób pracujących przy turbinach wiatrowych.</li>
                <li>Szkolenia obejmują m.in.:
                    <ul>
                        <li>Pracę na wysokości</li>
                        <li>Pierwszą pomoc</li>
                        <li>Gaszenie pożarów</li>
                        <li>Ewakuację i bezpieczeństwo</li>
                    </ul>
                </li>
                <li>Certyfikaty GWO są uznawane na całym świecie, co pozwala pracownikom pracować w różnych krajach.</li>
            </ul>
            
            <p>Dzięki GWO branża wiatrowa staje się <b>bezpieczniejsza i bardziej profesjonalna</b>, a pracownicy mogą zdobywać kompetencje według tych samych, wysokich standardów.</p>
        </div>
        
        <a href="/" style="
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            border: 2px solid black;
            border-radius: 8px;
            background-color: #f9f9f9;
            font-weight: bold;
            color: black;
            text-decoration: none;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
            transition: all 0.2s;
        "
        onmouseover="this.style.backgroundColor='#ffe6e6'; this.style.transform='scale(1.05)';"
        onmouseout="this.style.backgroundColor='#f9f9f9'; this.style.transform='scale(1)';">
            ← Wróć
        </a>
    </body>
    """

# 🔹 Podstrona Pierwsza Pomoc GWO
@app.route("/first_aid")
def first_aid():
    return """
    <body style="font-family: Verdana; text-align: center; margin: 50px;">
        <h1 style="color: black; transition: color 0.3s;"
            onmouseover="this.innerHTML='🆘 Pomoc GWO 🆘';"
            onmouseout="this.innerHTML='🩺 Pierwsza Pomoc GWO 🩺';">
            🩺 Pierwsza Pomoc GWO 🩺
        </h1>
        
        <div style="width: 80%; max-width: 800px; height: 400px; margin: 20px auto; padding: 20px; 
                    border: 2px solid black; border-radius: 10px; overflow-y: scroll; text-align: left; background-color: #f9f9f9;">
            <h2 style="color: black;">Co to jest Pierwsza Pomoc GWO?</h2>
            <p>Pierwsza pomoc w ramach GWO to szkolenia przygotowujące pracowników do reagowania w sytuacjach zagrożenia życia lub zdrowia na turbinach wiatrowych.</p>
            
            <h3>Zakres szkoleń:</h3>
            <ul>
                <li>Podstawy resuscytacji (RKO)</li>
                <li>Opatrunki i opatrywanie ran</li>
                <li>Postępowanie przy urazach i złamaniach</li>
                <li>Zabezpieczenie miejsca zdarzenia i wezwanie pomocy</li>
            </ul>
            
            <p>Dzięki temu każda osoba pracująca w branży wiatrowej jest przygotowana do szybkiej i skutecznej reakcji w nagłych sytuacjach, co znacząco zwiększa bezpieczeństwo w miejscu pracy.</p>
        </div>
        
        <a href="/" style="
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            border: 2px solid black;
            border-radius: 8px;
            background-color: #f9f9f9;
            font-weight: bold;
            color: black;
            text-decoration: none;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
            transition: all 0.2s;
        "
        onmouseover="this.style.backgroundColor='#ffe6e6'; this.style.transform='scale(1.05)';"
        onmouseout="this.style.backgroundColor='#f9f9f9'; this.style.transform='scale(1)';">
            ← Wróć
        </a>
    </body>
    """

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
