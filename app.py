import os
from flask import Flask, render_template_string

app = Flask(__name__)

# BANCO DE DATOS MULTIMEDIA (Clasificado por Categorías de Oficina)
RECURSOS_BASE = [
    # 1. CATEGORÍA: EXCEL
    {
        "id": "ex_01",
        "categoria": "excel",
        "badge": "📊 PLANTILLA",
        "titulo": "Control Financiero Pro",
        "descripcion": "Gestión de ingresos, egresos y balances con cuadros dinámicos automatizados.",
        "icono": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400&auto=format&fit=crop&q=80",
        "enlace_recurso": "https://docs.google.com/spreadsheets/d/1u6Vb2S3XbEEX87RjX647b0H_M8X4X_X8/copy"
    },
    # 2. CATEGORÍA: AUDIO
    {
        "id": "au_01",
        "categoria": "audio",
        "badge": "🎧 AUDIOLIBRO",
        "titulo": "El Hombre Más Rico de Babilonia",
        "descripcion": "Lección de audio sobre las leyes del oro. Escucha directa desde la aplicación.",
        "icono": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400&auto=format&fit=crop&q=80",
        "enlace_recurso": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    },
    # 3. CATEGORÍA: VIDEO
    {
        "id": "vi_01",
        "categoria": "video",
        "badge": "🎬 VIDEO CLASE",
        "titulo": "Estrategia de Ventas Hotmart",
        "descripcion": "Masterclass ejecutiva para estructurar embudos de venta orgánica de alta conversión.",
        "icono": "https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?w=400&auto=format&fit=crop&q=80",
        "enlace_recurso": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"
    },
    # 4. CATEGORÍA: PDF
    {
        "id": "pdf_01",
        "categoria": "pdf",
        "badge": "📖 GUÍA TEXTO",
        "titulo": "50 Ganchos Virales TikTok",
        "descripcion": "Manual en PDF con copys persuasivos listos para enganchar tráfico en 3 segundos.",
        "icono": "https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?w=400&auto=format&fit=crop&q=80",
        "enlace_recurso": "https://arxiv.org/pdf/quant-ph/0410100.pdf"
    }
]

HTML_FRONTEND = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Flow Recursos Pro</title>
    <style>
        body {
            background-color: #f8fafc;
            color: #334155;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            margin: 0; padding: 15px;
            display: flex; flex-direction: column; align-items: center;
        }
        .app-container {
            width: 100%; max-width: 440px;
            background: #ffffff; border-radius: 8px; padding: 20px;
            box-sizing: border-box; box-shadow: 0 1px 4px rgba(0,0,0,0.05);
            border: 1px solid #e2e8f0;
        }
        .header {
            text-align: center; margin-bottom: 20px;
            border-bottom: 2px solid #f1f5f9; padding-bottom: 12px;
        }
        h1 { font-size: 19px; color: #1e293b; margin: 0; font-weight: 700; }
        .subtitle { font-size: 11px; color: #64748b; margin: 4px 0 0 0; }
        
        .tabs-menu {
            display: flex; justify-content: space-between;
            background: #f1f5f9; border-radius: 6px;
            padding: 4px; margin-bottom: 20px; gap: 4px;
        }
        .tab-btn {
            flex: 1; border: none; background: transparent;
            color: #64748b; font-size: 11px; font-weight: 600;
            padding: 8px 0; border-radius: 4px; cursor: pointer;
            text-align: center; transition: all 0.2s;
        }
        .tab-btn.active {
            background: #ffffff; color: #1e293b;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }
        
        .resources-grid { display: flex; flex-direction: column; gap: 12px; }
        
        .card {
            background: #ffffff; border-radius: 6px; border: 1px solid #e2e8f0;
            display: flex; flex-direction: row; overflow: hidden; min-height: 110px; height: auto;
        }
        .card-img { width: 95px; min-height: 110px; object-fit: cover; border-right: 1px solid #e2e8f0; }
        .card-body { padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; flex: 1; min-width: 0; }
        .badge {
            font-size: 9px; font-weight: bold; color: #475569;
            background: #f1f5f9; padding: 2px 6px; border-radius: 3px; align-self: flex-start;
        }
        .card-title { font-size: 13.5px; font-weight: 600; color: #0f172a; margin: 4px 0 2px 0; }
        .card-text { font-size: 11px; color: #627185; line-height: 1.3; margin-bottom: 8px; text-overflow: ellipsis; overflow: hidden; white-space: nowrap; }
        
        .btn-action {
            display: block; text-align: center; background: #1e293b;
            color: #ffffff; text-decoration: none; padding: 7px 0;
            border-radius: 4px; font-weight: 600; font-size: 11px; margin-bottom: 2px;
        }
        
        /* Contenedores para reproductores internos */
        .media-container {
            display: none;
            margin-top: 8px;
            width: 100%;
        }
        .video-element {
            width: 100%;
            border-radius: 4px;
            border: 1px solid #cbd5e1;
            background: #000000;
            outline: none;
        }
    </style>
</head>
<body>

<div class="app-container">
    <div class="header">
        <h1>Flow Recursos Pro</h1>
        <p class="subtitle">Panel Corporativo de Capacitación Digital</p>
    </div>

    <div class="tabs-menu">
        <button class="tab-btn active" onclick="filtrarCategoria('excel', this)">Excel</button>
        <button class="tab-btn" onclick="filtrarCategoria('audio', this)">Audios</button>
        <button class="tab-btn" onclick="filtrarCategoria('video', this)">Videos</button>
        <button class="tab-btn" onclick="filtrarCategoria('pdf', this)">PDFs</button>
    </div>

    <div class="resources-grid" id="resources-list">
        {% for item in recursos %}
        <div class="card resource-item" data-category="{{ item.categoria }}">
            <img class="card-img" src="{{ item.icono }}" alt="Recurso">
            <div class="card-body">
                <div>
                    <span class="badge">{{ item.badge }}</span>
                    <div class="card-title">{{ item.titulo }}</div>
                    <div class="card-text">{{ item.descripcion }}</div>
                </div>
                
                <div>
                    <a href="#" class="btn-action" onclick="procesarAccion('{{ item.id }}', '{{ item.categoria }}', '{{ item.enlace_recurso }}'); return false;">
                        ABRIR CONTENIDO
                    </a>
                    
                    <div id="audio-player-container-{{ item.id }}" class="media-container"></div>
                    <div id="video-player-container-{{ item.id }}" class="media-container"></div>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>

<script>
    function filtrarCategoria(categoria, botonActivo) {
        let botones = document.querySelectorAll('.tab-btn');
        botones.forEach(btn => btn.classList.remove('active'));
        botonActivo.classList.add('active');

        let tarjetas = document.querySelectorAll('.resource-item');
        tarjetas.forEach(tarjeta => {
            if (tarjeta.getAttribute('data-category') === categoria) {
                tarjeta.style.display = 'flex';
            } else {
                tarjeta.style.display = 'none';
            }
        });
    }

    function procesarAccion(id, tipo, url) {
        console.log("Procesando recurso id: " + id + " de tipo: " + tipo);
        
        // 🎧 COMPORTAMIENTO DE AUDIO
        if (tipo === 'audio') {
            var contenedor = document.getElementById('audio-player-container-' + id);
            if (contenedor.style.display === 'block') {
                contenedor.innerHTML = '';
                contenedor.style.display = 'none';
                return;
            }
            contenedor.innerHTML = `
                <audio controls controlsList="nodownload" style="width: 100%; height: 32px; outline: none;">
                    <source src="${url}" type="audio/mpeg">
                </audio>
            `;
            contenedor.style.display = 'block';
            
        // 🎬 COMPORTAMIENTO DE VIDEO
        } else if (tipo === 'video') {
            var contenedorVideo = document.getElementById('video-player-container-' + id);
            if (contenedorVideo.style.display === 'block') {
                contenedorVideo.innerHTML = '';
                contenedorVideo.style.display = 'none';
                return;
            }
            
            // 💰 PASO PUBLICITARIO MONETAG (PREPARADO AQUÍ PARA EL FUTURO)
            
            // Inyectamos un reproductor de video nativo que bloquea la descarga directa
            contenedorVideo.innerHTML = `
                <video controls controlsList="nodownload" class="video-element">
                    <source src="${url}" type="video/mp4">
                    Tu navegador no soporta videos.
                </video>
            `;
            contenedorVideo.style.display = 'block';
            
        } else {
            alert("Pestañas operativas. En el próximo paso programaremos el formato: " + tipo.toUpperCase());
        }
    }

    document.addEventListener("DOMContentLoaded", function() {
        let primerBoton = document.querySelector('.tab-btn');
        filtrarCategoria('excel', primerBoton);
    });
</script>

</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_FRONTEND, recursos=RECURSOS_BASE)

if __name__ == '__main__':
    puerto = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=puerto)
