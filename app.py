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
        "enlace_recurso": "https://pdfobject.com/pdf/sample.pdf"
    },
    {
        "id": "pdf_02",  # Su ID único para la categoría PDF
        "categoria": "pdf",
        "badge": "📖 GUÍA TEXTO",
        "titulo": "COMO_VENDER_CUANDO_NADIE_ESTA_COMPRANDO_2",
        "descripcion": "Si últimamente lo único que escuchas es que la gente no está comprando porque no hay forma de hacerlo cuando el mundo está parado entonces debes replantearte inmediatamente la situación. Como emprendedores o líderes de proyectos debemos tomar estos retos con pasión para tratar de generar nuevos ángulos de negocios. Esta guía te servirá como un primer paso para redireccionar los pasos que deberás dar y justamente es lo que necesitamos en este momento, un modelo que ayude a nuestra mente a entender cómo abordar la situación.",
        "icono": "https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?w=400&auto=format&fit=crop&q=80",
        
        # 🎯 NOTA LA DIFERENCIA: Este enlace termina en /preview para activar el modo lectura
        "enlace_recurso": "https://docs.google.com/gview?embedded=true&url=https://drive.google.com/uc?export=download&id=16TB1Z4UyxhYUeAAkJ0UCh4THHLPYzkOI"
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
        
        .media-container {
            display: none;
            margin-top: 8px;
            width: 100%;
        }
        .video-element {
            width: 100%; border-radius: 4px; border: 1px solid #cbd5e1; background: #000000; outline: none;
        }

        /* 🔍 INTERFAZ MODAL DE MODO LECTURA PANTALLA COMPLETA */
        .pdf-modal {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background-color: rgba(15, 23, 42, 0.95); /* Fondo oscuro elegante */
            z-index: 1000;
            box-sizing: border-box;
            padding: 10px;
        }
        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 5px 10px 12px 10px;
        }
        .modal-title {
            color: #ffffff; font-size: 14px; font-weight: 600;
        }
        .close-btn {
            background: #ef4444; color: white; border: none;
            padding: 6px 14px; border-radius: 4px; font-weight: bold;
            font-size: 12px; cursor: pointer;
        }
        .pdf-fullscreen-view {
            width: 100%;
            height: calc(100% - 45px);
            border: none;
            border-radius: 6px;
            background: #ffffff;
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
                    <a href="#" class="btn-action" onclick="procesarAccion('{{ item.id }}', '{{ item.categoria }}', '{{ item.enlace_recurso }}', '{{ item.titulo }}'); return false;">
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

<div id="global-pdf-modal" class="pdf-modal">
    <div class="modal-header">
        <div id="modal-pdf-title" class="modal-title">Documento de Estudio</div>
        <button class="close-btn" onclick="cerrarModoLectura()">✕ CERRAR</button>
    </div>
    <iframe id="modal-pdf-frame" class="pdf-fullscreen-view" src=""></iframe>
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

    // PROCESADOR MULTIMEDIA ACTUALIZADO
    function procesarAccion(id, tipo, url, titulo) {
        console.log("Procesando recurso id: " + id + " de tipo: " + tipo);
        
        var containerAudio = document.getElementById('audio-player-container-' + id);
        var containerVideo = document.getElementById('video-player-container-' + id);
        
        // 🎧 COMPORTAMIENTO AUDIO
        if (tipo === 'audio') {
            if (containerAudio.style.display === 'block') {
                containerAudio.innerHTML = ''; containerAudio.style.display = 'none'; return;
            }
            containerAudio.innerHTML = `<audio controls controlsList="nodownload" style="width: 100%; height: 32px; outline: none;"><source src="${url}" type="audio/mpeg"></audio>`;
            containerAudio.style.display = 'block';
            
        // 🎬 COMPORTAMIENTO VIDEO
        } else if (tipo === 'video') {
            if (containerVideo.style.display === 'block') {
                containerVideo.innerHTML = ''; containerVideo.style.display = 'none'; return;
            }
            containerVideo.innerHTML = `<video controls controlsList="nodownload" class="video-element"><source src="${url}" type="video/mp4"></video>`;
            containerVideo.style.display = 'block';
            
        // 📖 COMPORTAMIENTO PDF: MODO LECTURA PANTALLA COMPLETA SMART
        } else if (tipo === 'pdf') {
            
            // 💰 AQUÍ ENTRARÁ TU DISPARADOR DE ANUNCIOS DE MONETAG EN EL FUTURO
            
            // Cargamos dinámicamente los datos en el modal global
            document.getElementById('modal-pdf-title').innerText = "📖 " + titulo;
            document.getElementById('modal-pdf-frame').src = url;
            
            // Desplegamos el modal cubriendo la pantalla
            document.getElementById('global-pdf-modal').style.display = 'block';
            
        // 📊 COMPORTAMIENTO EXCEL
        } else if (tipo === 'excel') {
            window.open(url, '_blank');
        }
    }

    // FUNCIÓN PARA SALIR DEL MODO LECTURA
    function cerrarModoLectura() {
        document.getElementById('global-pdf-modal').style.display = 'none';
        document.getElementById('modal-pdf-frame').src = ''; // Limpia la memoria del navegador
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
