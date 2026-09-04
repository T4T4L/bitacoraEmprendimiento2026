import os

svg_dir = r'c:\Users\marci\OneDrive - Universidad Adolfo Ibanez\UAI\Sem 12\Emprendimiento\Bitácora\en_desarrollo\presentacion\assets\illustrations'
os.makedirs(svg_dir, exist_ok=True)

# 1. Fenologia (Timeline botánico)
fenologia_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 200">
    <rect width="1000" height="200" fill="#F6F3EC" />
    <line x1="50" y1="100" x2="950" y2="100" stroke="#7D8B62" stroke-width="4" />
    <g fill="#284638" font-family="sans-serif" font-size="12" text-anchor="middle">
        <circle cx="100" cy="100" r="10" fill="#202420" />
        <text x="100" y="130">Dormancia</text>
        <circle cx="200" cy="100" r="10" fill="#7D8B62" />
        <text x="200" y="80">Brotación</text>
        <circle cx="300" cy="100" r="10" fill="#7D8B62" />
        <text x="300" y="130">Crecimiento</text>
        <circle cx="400" cy="100" r="10" fill="#C68A38" />
        <text x="400" y="80">Floración</text>
        <circle cx="500" cy="100" r="10" fill="#7D8B62" />
        <text x="500" y="130">Cuaja</text>
        <circle cx="600" cy="100" r="10" fill="#7D8B62" />
        <text x="600" y="80">Desarrollo Baya</text>
        <circle cx="700" cy="100" r="10" fill="#6E293B" />
        <text x="700" y="130">Envero</text>
        <circle cx="800" cy="100" r="10" fill="#6E293B" />
        <text x="800" y="80">Maduración</text>
        <circle cx="900" cy="100" r="10" fill="#202420" />
        <text x="900" y="130">Cosecha</text>
    </g>
</svg>"""

with open(os.path.join(svg_dir, 'fenologia.svg'), 'w', encoding='utf-8') as f:
    f.write(fenologia_svg)

# 2. Árbol del Problema
arbol_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600">
    <rect width="1000" height="600" fill="#F6F3EC" />
    <g font-family="sans-serif" text-anchor="middle">
        <!-- CAUSAS (Abajo) -->
        <rect x="50" y="450" width="200" height="60" rx="10" fill="#D8CEB8" />
        <text x="150" y="485" fill="#202420" font-size="14">Escala del viñedo</text>
        
        <rect x="300" y="450" width="200" height="60" rx="10" fill="#D8CEB8" />
        <text x="400" y="485" fill="#202420" font-size="14">Variabilidad espacial</text>
        
        <rect x="550" y="450" width="200" height="60" rx="10" fill="#D8CEB8" />
        <text x="650" y="485" fill="#202420" font-size="14">Presión económica</text>
        
        <rect x="800" y="450" width="150" height="60" rx="10" fill="#D8CEB8" />
        <text x="875" y="485" fill="#202420" font-size="14">Menos personal</text>
        
        <!-- Líneas a problema -->
        <path d="M150,450 L500,340 M400,450 L500,340 M650,450 L500,340 M875,450 L500,340" stroke="#7D8B62" stroke-width="3" />
        
        <!-- PROBLEMA (Centro) -->
        <rect x="200" y="240" width="600" height="100" rx="10" fill="#173126" />
        <text x="500" y="280" fill="#F6F3EC" font-size="16" font-weight="bold">BRECHA ENTRE OBSERVACIÓN REQUERIDA Y</text>
        <text x="500" y="310" fill="#F6F3EC" font-size="16" font-weight="bold">CAPACIDAD DISPONIBLE PARA MANTENERLA</text>
        
        <!-- Líneas a efectos -->
        <path d="M500,240 L300,120 M500,240 L500,120 M500,240 L700,120" stroke="#7D8B62" stroke-width="3" />
        
        <!-- EFECTOS (Arriba) -->
        <rect x="150" y="60" width="300" height="60" rx="10" fill="#6E293B" />
        <text x="300" y="95" fill="#F6F3EC" font-size="14">Anomalías locales sin observar</text>
        
        <rect x="500" y="60" width="350" height="60" rx="10" fill="#6E293B" />
        <text x="675" y="95" fill="#F6F3EC" font-size="14">Dificultad para priorizar y reacción tardía</text>
    </g>
</svg>"""

with open(os.path.join(svg_dir, 'arbol_problema.svg'), 'w', encoding='utf-8') as f:
    f.write(arbol_svg)

# 3. Rendimiento Ecuación
rendimiento_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 200">
    <rect width="1000" height="200" fill="#F6F3EC" />
    <g font-family="sans-serif" text-anchor="middle" font-size="18" fill="#202420">
        <rect x="50" y="60" width="120" height="80" rx="10" fill="#D8CEB8" />
        <text x="110" y="105">Plantas/ha</text>
        
        <text x="200" y="105" font-weight="bold" fill="#7D8B62">×</text>
        
        <rect x="230" y="60" width="120" height="80" rx="10" fill="#D8CEB8" />
        <text x="290" y="105">Brotes/pl</text>
        
        <text x="380" y="105" font-weight="bold" fill="#7D8B62">×</text>
        
        <rect x="410" y="60" width="120" height="80" rx="10" fill="#D8CEB8" />
        <text x="470" y="105">Racimos/br</text>
        
        <text x="560" y="105" font-weight="bold" fill="#7D8B62">×</text>
        
        <rect x="590" y="60" width="120" height="80" rx="10" fill="#D8CEB8" />
        <text x="650" y="105">Bayas/rac</text>
        
        <text x="740" y="105" font-weight="bold" fill="#7D8B62">×</text>
        
        <rect x="770" y="60" width="120" height="80" rx="10" fill="#D8CEB8" />
        <text x="830" y="105">Peso/baya</text>
        
        <text x="500" y="30" font-size="24" font-weight="bold" fill="#284638">RENDIMIENTO (Kg/ha)</text>
    </g>
</svg>"""

with open(os.path.join(svg_dir, 'rendimiento.svg'), 'w', encoding='utf-8') as f:
    f.write(rendimiento_svg)

# 4. Agua
agua_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 400">
    <rect width="1000" height="400" fill="#F6F3EC" />
    <g font-family="sans-serif" text-anchor="middle" font-size="16">
        <circle cx="500" cy="100" r="50" fill="#C68A38" opacity="0.8" />
        <text x="500" y="105" fill="#202420" font-weight="bold">CLIMA</text>
        <text x="500" y="170" fill="#6E293B">Demanda atmosférica</text>
        
        <path d="M500,180 L500,240" stroke="#7D8B62" stroke-width="4" marker-end="url(#arrow)" />
        
        <rect x="400" y="250" width="200" height="80" fill="#D8CEB8" rx="10" />
        <text x="500" y="295" fill="#202420" font-weight="bold">PLANTA</text>
        
        <path d="M500,330 L500,370" stroke="#7D8B62" stroke-width="4" />
        <rect x="0" y="370" width="1000" height="30" fill="#7D8B62" opacity="0.5" />
        <text x="500" y="390" fill="#202420" font-weight="bold">SUELO (Disponibilidad) + RIEGO</text>
    </g>
</svg>"""

with open(os.path.join(svg_dir, 'agua.svg'), 'w', encoding='utf-8') as f:
    f.write(agua_svg)

# 5. Variabilidad / Hilera
hilera_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300">
    <rect width="1000" height="300" fill="#F6F3EC" />
    <g stroke="#7D8B62" stroke-width="4">
        <line x1="50" y1="200" x2="950" y2="200" /> <!-- Suelo -->
        <line x1="50" y1="120" x2="950" y2="120" /> <!-- Alambre -->
    </g>
    <g font-family="sans-serif" text-anchor="middle">
        <!-- Vides con variabilidad -->
        <!-- Planta normal -->
        <rect x="150" y="80" width="60" height="120" fill="#284638" rx="30" opacity="0.9" />
        <line x1="180" y1="200" x2="180" y2="150" stroke="#202420" stroke-width="8" />
        
        <!-- Planta pequeña/estresada -->
        <rect x="350" y="100" width="40" height="100" fill="#7D8B62" rx="20" opacity="0.8" />
        <line x1="370" y1="200" x2="370" y2="170" stroke="#202420" stroke-width="6" />
        <text x="370" y="70" fill="#6E293B" font-size="14" font-weight="bold">Estrés local</text>
        
        <!-- Planta muy vigorosa -->
        <rect x="520" y="50" width="100" height="150" fill="#173126" rx="50" opacity="0.95" />
        <line x1="570" y1="200" x2="570" y2="130" stroke="#202420" stroke-width="12" />
        
        <!-- Planta faltante / dañada -->
        <line x1="770" y1="200" x2="770" y2="180" stroke="#202420" stroke-width="8" />
        <text x="770" y="170" fill="#6E293B" font-size="14" font-weight="bold">Falla</text>
        
        <text x="500" y="270" fill="#202420" font-size="20">La variabilidad requiere resolución espacial a nivel de planta</text>
    </g>
</svg>"""

with open(os.path.join(svg_dir, 'variabilidad.svg'), 'w', encoding='utf-8') as f:
    f.write(hilera_svg)

print("SVGs generados correctamente en assets/illustrations")

