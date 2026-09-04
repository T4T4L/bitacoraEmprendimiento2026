import os
import json

base_dir = r'c:\Users\marci\OneDrive - Universidad Adolfo Ibanez\UAI\Sem 12\Emprendimiento\Bitácora\en_desarrollo\presentacion'
manifest_path = os.path.join(base_dir, 'content', 'manifest.json')
slides_dir = os.path.join(base_dir, 'content', 'slides')
dist_path = os.path.join(base_dir, 'dist', 'deck_full.html')

with open(manifest_path, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

slides_html = ""

for index, slide_id in enumerate(manifest['slides']):
    with open(os.path.join(slides_dir, f"{slide_id}.json"), 'r', encoding='utf-8') as f:
        slideData = json.load(f)
    
    classes = "slide"
    if slideData.get('type') == 'key_problem':
        classes += " dark-green layout-key-problem"
    if slideData.get('type') == 'cover':
        classes += " dark"
    if slideData.get('type') == 'interview':
        classes += " layout-interview"
    
    if index == 0:
        classes += " active"
        
    innerHTML = f'<div class="slide-chapter">{slideData.get("chapter", "")}</div>\n'
    
    if slideData.get('type') == 'interview':
        innerHTML += f'''
            <h2>{slideData.get("title", "")}</h2>
            <div class="role">{slideData.get("role", "")}</div>
            <div class="insight">Concepto: {slideData.get("concept", "")}</div>
            <div class="findings">{slideData.get("findings", "")}</div>
        '''
    elif slideData.get('type') == 'key_problem':
        innerHTML += f'''
            <div style="font-size:24px; color:var(--amber); margin-bottom: 30px;">PROBLEMA DEFINIDO</div>
            <h1>{slideData.get("content", "")}</h1>
        '''
    else:
        title = slideData.get("title", "")
        content = slideData.get("content", "")
        subtitle = slideData.get("subtitle", "")
        context = slideData.get("context", "")
        
        innerHTML += f'<h1>{title}</h1>\n'
        if subtitle:
            innerHTML += f'<h2>{subtitle}</h2>\n'
            
        # Inyectar SVG basado en el ID de la lámina
        svg_img = ""
        if slide_id == "012":
            svg_img = '<img src="../assets/illustrations/fenologia.svg" style="width:1000px; margin-top:20px;">'
        elif slide_id == "015":
            svg_img = '<img src="../assets/illustrations/agua.svg" style="width:800px; margin-top:20px;">'
        elif slide_id == "017":
            svg_img = '<img src="../assets/illustrations/rendimiento.svg" style="width:1000px; margin-top:20px;">'
        elif slide_id == "021" or slide_id == "033":
            svg_img = '<img src="../assets/illustrations/variabilidad.svg" style="width:1000px; margin-top:20px;">'
        elif slide_id == "034" or slide_id == "035":
            svg_img = '<img src="../assets/illustrations/arbol_problema.svg" style="width:900px; margin-top:20px;">'
            
        if content:
            innerHTML += f'<p>{content}</p>\n'
        
        if svg_img:
            innerHTML += f'<div style="text-align:center;">{svg_img}</div>\n'
            
        if context:
            innerHTML += f'<p>{context}</p>\n'

    slides_html += f'<div class="{classes}">\n{innerHTML}\n</div>\n'

html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Presentación Bitácora</title>
    <link rel="stylesheet" href="../src/styles/deck.css">
    <style>
        .nav-controls {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            display: flex;
            gap: 10px;
            z-index: 1000;
        }}
        .nav-btn {{
            background: var(--wine, #6E293B);
            color: var(--paper, #F6F3EC);
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
            opacity: 0.5;
            transition: opacity 0.2s;
        }}
        .nav-btn:hover {{ opacity: 1; }}
        .slide-counter {{
            position: fixed;
            bottom: 25px;
            left: 20px;
            color: var(--olive, #7D8B62);
            font-size: 20px;
            font-family: sans-serif;
            z-index: 1000;
        }}
    </style>
</head>
<body>
    <div id="deck">
        {slides_html}
    </div>
    
    <div class="nav-controls">
        <button class="nav-btn" onclick="prevSlide()">Anterior</button>
        <button class="nav-btn" onclick="nextSlide()">Siguiente</button>
    </div>
    <div class="slide-counter" id="counter">1 / 46</div>
    
    <script>
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const counter = document.getElementById('counter');
        
        function updateCounter() {{
            counter.innerText = (currentSlide + 1) + " / " + slides.length;
        }}

        function nextSlide() {{
            if (currentSlide < slides.length - 1) {{
                slides[currentSlide].classList.remove('active');
                currentSlide++;
                slides[currentSlide].classList.add('active');
                updateCounter();
            }}
        }}
        
        function prevSlide() {{
            if (currentSlide > 0) {{
                slides[currentSlide].classList.remove('active');
                currentSlide--;
                slides[currentSlide].classList.add('active');
                updateCounter();
            }}
        }}

        window.addEventListener('keydown', (e) => {{
            if(e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
                nextSlide();
            }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
                prevSlide();
            }}
        }});

        document.getElementById('deck').addEventListener('click', (e) => {{
            nextSlide();
        }});

        function resizeDeck() {{
            const deck = document.getElementById('deck');
            const scale = Math.min(window.innerWidth / 1920, window.innerHeight / 1080);
            deck.style.transform = `scale(${{scale}})`;
            deck.style.transformOrigin = 'center center';
        }}
        
        window.addEventListener('resize', resizeDeck);
        resizeDeck();
        updateCounter();
    </script>
</body>
</html>"""

with open(dist_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print("deck_full.html generado exitosamente.")

