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
        if content:
            innerHTML += f'<p>{content}</p>\n'
        if subtitle:
            innerHTML += f'<h2>{subtitle}</h2>\n'
        if context:
            innerHTML += f'<p>{context}</p>\n'

    slides_html += f'<div class="{classes}">\n{innerHTML}\n</div>\n'

html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Presentación Bitácora</title>
    <link rel="stylesheet" href="../src/styles/deck.css">
</head>
<body>
    <div id="deck">
        {slides_html}
    </div>
    
    <script>
        let currentSlide = 0;
        window.addEventListener('keydown', (e) => {{
            const slides = document.querySelectorAll('.slide');
            if(e.key === 'ArrowRight' && currentSlide < slides.length - 1) {{
                slides[currentSlide].classList.remove('active');
                currentSlide++;
                slides[currentSlide].classList.add('active');
            }} else if (e.key === 'ArrowLeft' && currentSlide > 0) {{
                slides[currentSlide].classList.remove('active');
                currentSlide--;
                slides[currentSlide].classList.add('active');
            }}
        }});
    </script>
</body>
</html>"""

with open(dist_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print("deck_full.html generado exitosamente.")

