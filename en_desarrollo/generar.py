import os
import json

base_dir = r'c:\Users\marci\OneDrive - Universidad Adolfo Ibanez\UAI\Sem 12\Emprendimiento\Bitácora\en_desarrollo\presentacion'

dirs = [
    'content/slides',
    'assets/images',
    'assets/illustrations',
    'assets/icons',
    'src/styles',
    'dist',
    'scripts'
]

for d in dirs:
    os.makedirs(os.path.join(base_dir, d), exist_ok=True)

# CSS
css_content = '''
:root {
 --paper: #F6F3EC;
 --ink: #202420;
 --vine: #284638;
 --wine: #6E293B;
 --olive: #7D8B62;
 --sand: #D8CEB8;
 --amber: #C68A38;
}

body {
    background-color: var(--ink);
    color: var(--paper);
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

.slide {
    width: 1920px;
    height: 1080px;
    background-color: var(--paper);
    color: var(--ink);
    position: relative;
    overflow: hidden;
    box-sizing: border-box;
    padding: 80px;
    display: none;
}

.slide.active {
    display: block;
}

.slide.dark {
    background-color: var(--vine);
    color: var(--paper);
}

.slide.dark-green {
    background-color: #173126;
    color: var(--paper);
}

.slide h1 {
    font-size: 80px;
    margin-bottom: 20px;
    font-weight: 700;
}

.slide h2 {
    font-size: 50px;
    font-weight: 600;
    margin-bottom: 40px;
}

.slide p {
    font-size: 35px;
    line-height: 1.5;
    max-width: 70%;
}

.slide-chapter {
    font-weight: 600;
    text-transform: uppercase;
    position: absolute;
    top: 50px;
    left: 80px;
    font-size: 24px;
    color: var(--olive);
}

/* Specific layouts */
.layout-interview .role {
    font-size: 30px;
    color: var(--wine);
    margin-bottom: 50px;
}
.layout-interview .insight {
    font-size: 45px;
    font-weight: bold;
    color: var(--vine);
    margin-top: 50px;
}
.layout-interview .findings {
    margin-top: 30px;
    font-size: 30px;
}

.layout-key-problem {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    height: 100%;
}
.layout-key-problem h1 {
    font-size: 60px;
    font-weight: 400;
    max-width: 1400px;
    line-height: 1.4;
}
'''
with open(os.path.join(base_dir, 'src/styles/deck.css'), 'w', encoding='utf-8') as f:
    f.write(css_content)

slides_data = [
    {'id': '001', 'type': 'cover', 'title': '¿Qué ocurre realmente en un viñedo?', 'subtitle': 'Investigación sobre monitoreo y toma de decisiones en viticultura vinífera.', 'context': 'Caso: Viña TerraMater · Valle del Maipo.', 'chapter': ''},
    {'id': '002', 'type': 'text', 'title': 'Nos interesa la robótica y su impacto en la agricultura.', 'content': 'Como equipo nos interesa la robótica y entender dónde puede generar un impacto real en agricultura.', 'chapter': 'ORIGEN'},
    {'id': '003', 'type': 'text', 'title': '¿Dónde puede generar valor la tecnología en el campo?', 'content': 'Antes de decidir qué automatizar, exploramos dónde la tecnología podría generar valor.', 'chapter': 'ORIGEN'},
    {'id': '004', 'type': 'text', 'title': 'Antes de actuar sobre una planta, hay que saber qué ocurre.', 'content': 'observar → detectar → interpretar → decidir → actuar → volver a observar', 'chapter': 'ORIGEN'},
    {'id': '005', 'type': 'text', 'title': 'Encontramos un cultivo particularmente interesante.', 'content': 'La exploración nos llevó a la vid vinífera.', 'chapter': 'ORIGEN'},
    {'id': '006', 'type': 'text', 'title': '¿Por qué la vid es especialmente interesante para monitorear?', 'content': 'Es perenne, estacional, variable, exigente agronómicamente, y acumula historial.', 'chapter': 'ORIGEN'},
    {'id': '007', 'type': 'text', 'title': 'La industria mundial del vino se está ajustando.', 'content': 'Consumo mundial 2025 ≈ 208 M hl (-2,7%). Caída del sector.', 'chapter': 'CONTEXTO'},
    {'id': '008', 'type': 'text', 'title': '¿Qué está pasando con el vino chileno?', 'content': 'Datos enero–julio 2026: -13,3% volumen exportado, -10,6% valor.', 'chapter': 'CONTEXTO'},
    {'id': '009', 'type': 'text', 'title': 'El campo sigue requiriendo decisiones aunque existan menos recursos.', 'content': 'Menores márgenes y presión por eficiencia.', 'chapter': 'CONTEXTO'},
    {'id': '010', 'type': 'text', 'title': 'Para entender el problema necesitábamos trabajar con una viña real.', 'content': 'Viña TerraMater nos abrió el viñedo.', 'chapter': 'CONTEXTO'},
    {'id': '011', 'type': 'text', 'title': 'Una vid no comienza de cero cada temporada.', 'content': 'La longevidad permite construir un historial productivo, sanitario e hídrico.', 'chapter': 'COMPRENDER LA VID'},
    {'id': '012', 'type': 'text', 'title': '¿Cuántas “vides distintas” vemos en una temporada?', 'content': 'Fenología: Dormancia → Brotación → Crecimiento → Floración → Cuaja → Desarrollo de baya → Envero → Maduración → Cosecha', 'chapter': 'COMPRENDER LA VID'},
    {'id': '013', 'type': 'text', 'title': 'Lo importante observar cambia con ella.', 'content': 'Cada etapa requiere un tipo de monitoreo distinto.', 'chapter': 'COMPRENDER LA VID'},
    {'id': '014', 'type': 'text', 'title': 'Una vid funciona como un sistema.', 'content': 'genética × ambiente × manejo', 'chapter': 'COMPRENDER LA VID'},
    {'id': '015', 'type': 'text', 'title': '¿Cuánta agua hay… y cómo está respondiendo la planta?', 'content': 'Humedad del suelo ≠ estado hídrico de la planta.', 'chapter': 'COMPRENDER LA VID'},
    {'id': '016', 'type': 'text', 'title': '¿Por qué mirar la canopia?', 'content': 'Conecta fotosíntesis, exposición, microclima, sanidad y maduración.', 'chapter': 'COMPRENDER LA VID'},
    {'id': '017', 'type': 'text', 'title': 'Los kg/ha son el resultado, no la explicación.', 'content': 'Rendimiento = plantas/ha × brotes/planta × racimos/brote × bayas/racimo × peso medio', 'chapter': 'COMPRENDER LA VID'},
    {'id': '018', 'type': 'text', 'title': 'Un problema sanitario puede comenzar localizado.', 'content': 'La escala del problema puede ser mucho menor que la escala del cuartel.', 'chapter': 'COMPRENDER LA VID'},
    {'id': '019', 'type': 'text', 'title': 'Observar no es diagnosticar.', 'content': 'Observación → Indicador → Interpretación → Diagnóstico', 'chapter': 'COMPRENDER LA VID'},
    {'id': '020', 'type': 'text', 'title': 'Entender la vid en papel no era suficiente.', 'content': 'Necesitábamos entender cómo fluye la información en un campo real.', 'chapter': 'ENTRAR AL CAMPO'},
    {'id': '021', 'type': 'text', 'title': 'El viñedo como entorno de observación.', 'content': 'Escalas: punto → planta → segmento → hilera → zona → cuartel', 'chapter': 'ENTRAR AL CAMPO'},
    {'id': '022', 'type': 'text', 'title': 'AEIOU — Activities.', 'content': 'Inspeccionar, podar, observar sanidad, supervisar agua.', 'chapter': 'ENTRAR AL CAMPO'},
    {'id': '023', 'type': 'text', 'title': 'El estado del viñedo conecta a muchos actores.', 'content': 'Operario → Viticultor → Administración', 'chapter': 'ENTRAR AL CAMPO'},
    {'id': '024', 'type': 'interview', 'title': 'Carlos Bendek', 'role': 'Agrónomo', 'concept': 'SIMPLICIDAD', 'findings': 'La fricción operacional puede destruir el valor de una buena tecnología.', 'chapter': 'PERSONAS'},
    {'id': '025', 'type': 'interview', 'title': 'Rodrigo Moraga', 'role': 'Experiencia en viñedos', 'concept': 'TEMPORADA', 'findings': 'No existe un único monitoreo del viñedo: las preguntas cambian con la planta.', 'chapter': 'PERSONAS'},
    {'id': '026', 'type': 'interview', 'title': 'Marcelo Prado', 'role': 'Administrador de viña', 'concept': 'COSTO', 'findings': 'Aumentar información sin demostrar retorno no resuelve el problema.', 'chapter': 'PERSONAS'},
    {'id': '027', 'type': 'interview', 'title': 'Sergio Hormazábal', 'role': 'Viticultor y enólogo', 'concept': 'ESCALA', 'findings': 'En grandes superficies es difícil mantener una visión precisa y frecuente de lo que ocurre.', 'chapter': 'PERSONAS'},
    {'id': '028', 'type': 'interview', 'title': 'Karim Reuse', 'role': 'TerraMater', 'concept': 'EXIGENCIA', 'findings': 'Los casos más exigentes ayudan a revelar los límites del sistema actual.', 'chapter': 'PERSONAS'},
    {'id': '029', 'type': 'interview', 'title': 'Don Cloro', 'role': 'Operario de campo TerraMater', 'concept': 'EXPERIENCIA', 'findings': 'Parte del conocimiento del viñedo vive en las personas.', 'chapter': 'PERSONAS'},
    {'id': '030', 'type': 'interview', 'title': 'Manuel Fuentes', 'role': 'Viticultor TerraMater', 'concept': 'COBERTURA', 'findings': 'El muestreo hace posible manejar la escala, pero sacrifica cobertura.', 'chapter': 'PERSONAS'},
    {'id': '031', 'type': 'interview', 'title': 'Nicolás Lea-Plaza', 'role': 'Ingeniero agrónomo', 'concept': 'VALOR', 'findings': 'La calidad del sistema no se mide por cuántos datos captura, sino por cuáles justifican ser capturados.', 'chapter': 'PERSONAS'},
    {'id': '032', 'type': 'interview', 'title': 'Manuel Cisterna', 'role': 'Gerente General TerraMater', 'concept': 'INFORMACIÓN', 'findings': 'La reducción de estructura organizacional genera una brecha de información.', 'chapter': 'PERSONAS'},
    {'id': '033', 'type': 'text', 'title': 'Las conversaciones convergen. ¿Qué se repite?', 'content': 'Limitación de cobertura y frecuencia, variabilidad espacial.', 'chapter': 'PERSONAS'},
    {'id': '034', 'type': 'text', 'title': 'El viñedo necesita ser observado justo cuando existe menos capacidad.', 'content': 'Presión por costos limita la mano de obra disponible para observar.', 'chapter': 'DEFINICIÓN'},
    {'id': '035', 'type': 'text', 'title': '¿Dónde aparecen las fricciones?', 'content': 'Customer Journey: Aparece una pregunta → Recorrido → Interpretación → Decisión.', 'chapter': 'DEFINICIÓN'},
    {'id': '036', 'type': 'text', 'title': 'Punto de Vista (POV)', 'content': 'Un responsable agronómico necesita mantener una visión frecuente porque los muestreos no permiten continuidad.', 'chapter': 'DEFINICIÓN'},
    {'id': '037', 'type': 'key_problem', 'title': 'PROBLEMA DEFINIDO', 'content': 'En viñedos de gran extensión existe una brecha entre el nivel de observación que requiere la variabilidad del cultivo y la capacidad disponible para mantener esa observación de forma frecuente, sistemática y trazable.', 'chapter': 'DEFINICIÓN'},
    {'id': '038', 'type': 'text', 'title': 'No existe una única forma de mirar un viñedo.', 'content': 'Scouting, sensores fijos, satélite, dron, robótica.', 'chapter': 'ALTERNATIVAS'},
    {'id': '039', 'type': 'text', 'title': 'Cobertura, detalle y frecuencia obligan a compromisos.', 'content': 'Benchmark de alternativas actuales.', 'chapter': 'ALTERNATIVAS'},
    {'id': '040', 'type': 'text', 'title': 'La frontera tecnológica existe...', 'content': 'Scout AMP, VineScout, PhytoPatholoBot.', 'chapter': 'ALTERNATIVAS'},
    {'id': '041', 'type': 'text', 'title': '...pero ¿es accesible desde Chile?', 'content': '¿Se comercializa localmente? ¿Hay soporte? ¿Cuál es el costo?', 'chapter': 'ALTERNATIVAS'},
    {'id': '042', 'type': 'text', 'title': '¿Dónde ocurre este problema?', 'content': 'Chile: 116.962 ha. Región Metropolitana: 8.898 ha.', 'chapter': 'OPORTUNIDAD'},
    {'id': '043', 'type': 'text', 'title': 'Nuestro punto de partida ya existe', 'content': 'TERRAMATER. Acceso real, interés, problemas observables.', 'chapter': 'OPORTUNIDAD'},
    {'id': '044', 'type': 'text', 'title': 'El problema ya entrega criterios para idear.', 'content': 'La próxima etapa será idear distintas formas de abordarlo.', 'chapter': 'CIERRE'},
    {'id': '045', 'type': 'text', 'title': 'Próximos pasos', 'content': 'Completar entrevista con Gerente de Operaciones de TerraMater, pospuesta. Precisar frecuencia de actividades.', 'chapter': 'CIERRE'},
    {'id': '046', 'type': 'text', 'title': 'Referencias', 'content': 'Abbatantuono et al. (2024), OIV (2025), SAG (2024)...', 'chapter': 'REFERENCIAS'}
]

manifest = {'title': 'Bitácora - Entregable 1', 'slides': []}
for slide in slides_data:
    filename = f"{slide['id']}.json"
    with open(os.path.join(base_dir, 'content/slides', filename), 'w', encoding='utf-8') as f:
        json.dump(slide, f, ensure_ascii=False, indent=2)
    manifest['slides'].append(slide['id'])

with open(os.path.join(base_dir, 'content/manifest.json'), 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

html_template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Presentación Bitácora</title>
    <link rel="stylesheet" href="../src/styles/deck.css">
</head>
<body>
    <div id="deck"></div>
    
    <script>
        async function loadDeck() {
            const manifestRes = await fetch('../content/manifest.json');
            const manifest = await manifestRes.json();
            const deck = document.getElementById('deck');
            
            for (let id of manifest.slides) {
                const slideRes = await fetch(`../content/slides/${id}.json`);
                const slideData = await slideRes.json();
                
                const slideEl = document.createElement('div');
                slideEl.className = 'slide';
                if (slideData.type === 'key_problem') slideEl.classList.add('dark-green', 'layout-key-problem');
                if (slideData.type === 'cover') slideEl.classList.add('dark');
                
                let innerHTML = `<div class="slide-chapter">${slideData.chapter}</div>`;
                
                if (slideData.type === 'interview') {
                    slideEl.classList.add('layout-interview');
                    innerHTML += `
                        <h2>${slideData.title}</h2>
                        <div class="role">${slideData.role}</div>
                        <div class="insight">Concepto: ${slideData.concept}</div>
                        <div class="findings">${slideData.findings}</div>
                    `;
                } else if (slideData.type === 'key_problem') {
                    innerHTML += `
                        <div style="font-size:24px; color:var(--amber); margin-bottom: 30px;">PROBLEMA DEFINIDO</div>
                        <h1>${slideData.content}</h1>
                    `;
                } else {
                    innerHTML += `
                        <h1>${slideData.title}</h1>
                        <p>${slideData.content || ''}</p>
                        ${slideData.subtitle ? `<h2>${slideData.subtitle}</h2>` : ''}
                        ${slideData.context ? `<p>${slideData.context}</p>` : ''}
                    `;
                }
                
                slideEl.innerHTML = innerHTML;
                deck.appendChild(slideEl);
            }
            
            if(deck.children.length > 0) deck.children[0].classList.add('active');
        }
        
        loadDeck();
        
        let currentSlide = 0;
        window.addEventListener('keydown', (e) => {
            const slides = document.querySelectorAll('.slide');
            if(e.key === 'ArrowRight' && currentSlide < slides.length - 1) {
                slides[currentSlide].classList.remove('active');
                currentSlide++;
                slides[currentSlide].classList.add('active');
            } else if (e.key === 'ArrowLeft' && currentSlide > 0) {
                slides[currentSlide].classList.remove('active');
                currentSlide--;
                slides[currentSlide].classList.add('active');
            }
        });
    </script>
</body>
</html>"""

with open(os.path.join(base_dir, 'dist/deck.html'), 'w', encoding='utf-8') as f:
    f.write(html_template)

print('Presentacion generada exitosamente en en_desarrollo/presentacion')

