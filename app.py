import os
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# BANCO DE DATOS MULTIMEDIA (Estructura Limpia y Modular)
RECURSOS_BASE = [
    # 1. CATEGORÍA: EXCEL
    {
        "id": "ex_01",
        "categoria": "excel",
        "badge": "📊 PLANTILLA",
        "titulo": "Control Financiero Pro",
        "descripcion": "Gestión de ingresos, egresos y balances con cuadros dinámicos automatizados.",
        "icono": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400&auto=format&fit=crop&q=80",
        "archivos": [
            {"titulo": "Plantilla Control Financiero Pro", "tipo": "excel", "url": "https://docs.google.com/spreadsheets/d/1u6Vb2S3XbEEX87RjX647b0H_M8X4X_X8/copy"}
        ]
    },
    # 2. CATEGORÍA: AUDIO
        {
        "id": "au_01",
        "categoria": "audio",
        "badge": "🎧 AUDIOLIBRO",
        "titulo": "Consejos para superar depresion",
        "descripcion": "Audiolibro completo metodo para estimular el cerebro asi mejorar el aprendizaje salud y alcanzar el éxito.",
        "icono": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400&auto=format&fit=crop&q=80",
        "archivos": 
            [
            {"titulo": "Consejos para superar depresion", "tipo": "audio", "url": "https://f005.backblazeb2.com/file/Material-recursos/Material-AudioLibros/Consejos+para+superar+depresion.mp3"}
            ]
    },
            {
        "id": "au_02",
        "categoria": "audio",
        "badge": "🎧 AUDIOLIBRO",
        "titulo": "Los Hombres son de Marte y las Mujeres de Venus",
        "descripcion": "«Los hombres son de Marte, las mujeres de Venus» de John Gray es un clásico de autoayuda que explica cómo las diferencias fundamentales en la comunicación, necesidades emocionales y formas de lidiar con el estrés generan malentendidos en la pareja, ofreciendo herramientas para construir relaciones más sanas y comprensivas.",
        "icono": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400&auto=format&fit=crop&q=80",
        "archivos": 
            [
            {"titulo": "Los Hombres son de Marte y las Mujeres de Venus", "tipo": "audio", "url": "https://f005.backblazeb2.com/file/Material-recursos/Material-AudioLibros/Los_Hombres_son_de_Marte_y_las_Mujeres_de_Venus_John_Gray_phD.mp3"}
            ]
    },
     {
        "id": "au_03",
        "categoria": "audio",
        "badge": "🎧 AUDIOLIBRO",
        "titulo": "Millonario inteligentes",
        "descripcion": "« es una guía práctica de educación financiera y desarrollo personal. Su enfoque principal es enseñarte cómo cambiar tu mentalidad hacia el dinero, eliminar creencias limitantes y aplicar estrategias para alcanzar la libertad financiera.",
        "icono": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400&auto=format&fit=crop&q=80",
        "archivos": 
            [
            {"titulo": "Millonario inteligentes", "tipo": "audio", "url": "https://f005.backblazeb2.com/file/Material-recursos/Material-AudioLibros/Millonario+inteligente.mp3"}
            ]
    },
         {
        "id": "au_04",
        "categoria": "audio",
        "badge": "🎧 AUDIOLIBRO",
        "titulo": "Cómo construir la autodisciplina",
        "descripcion": "¿Cómo construir la autodisciplina en tu vida? ¿Cómo resistir a las recompensas a corto plazo con el fin de alcanzar tus metas a largo plazo? Este libro es la respuesta a esas preguntas. ",
        "icono": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400&auto=format&fit=crop&q=80",
        "archivos": 
            [
            {"titulo": "Cómo construir la autodisciplina", "tipo": "audio", "url": "https://f005.backblazeb2.com/file/Material-recursos/Material-AudioLibros/C%C3%B3mo+Construir+la+Autodisciplina.mp3"}
            ]
    },
#    {
#        "id": "au_02",
#        "categoria": "audio",
#        "badge": "🎧 AUDIOLIBRO",
#        "titulo": "El Hombre Más Rico de Babilonia",
#        "descripcion": "Audiolibro completo organizado por capítulos para dominar las leyes del oro y la riqueza.",
#        "icono": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400&auto=format&fit=crop&q=80",
#        "archivos": [
#            {"titulo": "Capítulo 1: El hombre que deseaba oro", "tipo": "audio", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"},
#            {"titulo": "Capítulo 2: El hombre más rico de Babilonia", "tipo": "audio", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"},
#            {"titulo": "Capítulo 3: Las siete maneras de llenar una bolsa vacía", "tipo": "audio", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"}
#     ]
 
    
    # 3. CATEGORÍA: VIDEO
    {
        "id": "vi_01",
        "categoria": "video",
        "badge": "🎬 VIDEO CLASE",
        "titulo": "Estrategia de Ventas Hotmart",
        "descripcion": "Masterclass ejecutiva para ajustar embudos de venta orgánica de alta conversión.",
        "icono": "https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?w=400&auto=format&fit=crop&q=80",
        "archivos": [
            {"titulo": "Clase Única: Embudo Orgánico Pro", "tipo": "video", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"}
        ]
    },
    # 4. CATEGORÍA: PDF
    {
        "id": "pdf_01",
        "categoria": "pdf",
        "badge": "📖 GUÍA TEXTO",
        "titulo": "Como Vender Cuando Nadie esta Comprando",
        "descripcion": "Esta guía te servirá como un primer paso para redireccionar los pasos que deberás dar y justamente es lo que necesitamos en este momento, un modelo que ayude a nuestra mente a entender cómo abordar la situación.",
        "icono": "https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?w=400&auto=format&fit=crop&q=80",
        "archivos": [
            {"titulo": "Como Vender Cuando Nadie esta Comprando", "tipo": "pdf", "url": "https://f005.backblazeb2.com/file/Material-recursos/Material-PDF/EBOOK_COMO_VENDER_CUANDO_NADIE_ESTA_COMPRANDO_2_.pdf"}
        ]
    },
    {
        "id": "pdf_02",
        "categoria": "pdf",
        "badge": "🎓 Curso Aprende Ingles",
        "titulo": "Ingles Sin Barreras Manual",
        "descripcion": "Accede a los módulos oficiales y guías estratégicas de este entrenamiento, El que sabe dos idiomas vale por dos personas",
        "icono": "https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?w=400&auto=format&fit=crop&q=80",
        "archivos": [
            {
                "titulo": "Módulo 1", 
                "tipo": "pdf", 
                "url": "https://f005.backblazeb2.com/file/Material-recursos/Material-PDF/Curso+aprende+Ingles/Ingles+Sin+Barreras+Manual+01-By.Priale+(1).pdf"
            },
                        {
                "titulo": "Módulo 2", 
                "tipo": "pdf", 
                "url": "https://f005.backblazeb2.com/file/Material-recursos/Material-PDF/Curso+aprende+Ingles/Ingles+Sin+Barreras+Manual+02-By.Priale.pdf"
            },
                        {
                "titulo": "Módulo 3", 
                "tipo": "pdf", 
                "url": "https://f005.backblazeb2.com/file/Material-recursos/Material-PDF/Curso+aprende+Ingles/Ingles+Sin+Barreras+Manual+03-By.Priale+(1).pdf"
            },
                        {
                "titulo": "Módulo 4", 
                "tipo": "pdf", 
                "url": "https://f005.backblazeb2.com/file/Material-recursos/Material-PDF/Curso+aprende+Ingles/Ingles+Sin+Barreras+Manual+04-By.Priale.pdf"
            },
                        {
                "titulo": "Módulo 5", 
                "tipo": "pdf", 
                "url": "https://f005.backblazeb2.com/file/Material-recursos/Material-PDF/Curso+aprende+Ingles/Ingles+Sin+Barreras+Manual+05-By.Priale.pdf"
            },
                        {
                "titulo": "Módulo 6", 
                "tipo": "pdf", 
                "url": "https://f005.backblazeb2.com/file/Material-recursos/Material-PDF/Curso+aprende+Ingles/Ingles+Sin+Barreras+Manual+06-By.Priale.pdf"
            },
                        {
                "titulo": "Módulo 7", 
                "tipo": "pdf", 
                "url": "https://f005.backblazeb2.com/file/Material-recursos/Material-PDF/Curso+aprende+Ingles/Ingles+Sin+Barreras+Manual+07-By.Priale.pdf"
            },
        ]
    }
]

HTML_FRONTEND = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta name="monetag" content="b6437955edabbcb46ba78e6a83c5819b">
    <script>(function(s){s.dataset.zone='11062026',s.src='https://al5sm.com/tag.min.js'})([document.documentElement, document.body].filter(Boolean).pop().appendChild(document.createElement('script')))</script>
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
        .card-title { font-size: 13.5px; font-weight: 600; color: #0f172a; margin: 4px 0 4px 0; }
        .card-text { 
            font-size: 11px; color: #627185; line-height: 1.4; margin-bottom: 10px; 
            overflow: visible; white-space: normal; 
        }
        
        .btn-action {
            display: block; text-align: center; background: #1e293b;
            color: #ffffff; text-decoration: none; padding: 7px 0;
            border-radius: 4px; font-weight: 600; font-size: 11px; margin-bottom: 2px;
            cursor: pointer;
        }

        /* MODAL MULTIMEDIA UNIFICADO */
        .global-modal {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background-color: rgba(15, 23, 42, 0.98);
            z-index: 1000;
            box-sizing: border-box;
            padding: 12px;
        }
        .modal-header {
            display: flex; justify-content: space-between; align-items: center; padding: 5px 10px 12px 10px;
        }
        .modal-header-left {
            display: flex; gap: 8px; align-items: center; max-width: 70%;
        }
        .modal-title {
            color: #ffffff; font-size: 14px; font-weight: 600;
            white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
        }
        .btn-back-menu {
            display: none; background: #475569; color: white; border: none;
            padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 11px; cursor: pointer;
        }
        .close-btn {
            background: #ef4444; color: white; border: none;
            padding: 6px 14px; border-radius: 4px; font-weight: bold;
            font-size: 12px; cursor: pointer;
        }
        .modal-body-content {
            width: 100%; height: calc(100% - 50px);
            display: flex; flex-direction: column; justify-content: center; align-items: center; box-sizing: border-box;
        }
        
        /* DISEÑO MENÚ DE MÓDULOS */
        .modules-menu-container {
            width: 100%; max-width: 380px; height: 95%;
            display: flex; flex-direction: column; gap: 10px; overflow-y: auto; padding: 10px 0;
        }
        .module-list-btn {
            background: #1e293b; border: 1px solid #334155; border-radius: 6px;
            color: #ffffff; padding: 14px 16px; text-align: left; font-size: 12.5px;
            font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center;
        }
        .module-list-btn:hover { background: #27374d; }
        .module-list-btn .icon-format { font-size: 10px; background: #334155; padding: 3px 6px; border-radius: 4px; font-weight: bold; }

        /* REPRODUCTORES */
        .fullscreen-frame { width: 100%; height: 100%; border: none; border-radius: 6px; background: #ffffff; }
        .fullscreen-video { width: 100%; max-height: 85%; border-radius: 6px; outline: none; background: #000000; }
        
        .audio-modal-card {
            background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 30px 20px;
            width: 90%; max-width: 360px; text-align: center;
        }
        .audio-modal-card .audio-icon { font-size: 45px; margin-bottom: 15px; }
        .audio-modal-card .audio-title { color: #ffffff; font-size: 15px; font-weight: bold; margin-bottom: 20px; }
        
        .excel-modal-card {
            background: #ffffff; border-radius: 12px; padding: 35px 25px;
            width: 90%; max-width: 360px; text-align: center;
        }
        .excel-modal-card .excel-icon { font-size: 50px; margin-bottom: 15px; }
        .excel-modal-card .excel-title { color: #1e293b; font-size: 16px; font-weight: 700; margin-bottom: 8px; }
        .excel-modal-card .excel-desc { color: #64748b; font-size: 12px; margin-bottom: 25px; line-height: 1.4; }
        .btn-excel-download {
            display: inline-block; background: #10b981; color: white; text-decoration: none;
            padding: 12px 24px; border-radius: 6px; font-weight: bold; font-size: 13px;
        }
    </style>
</head>
<body>

<div id="welcome-overlay" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(15, 23, 42, 0.96); z-index: 99999; display: flex; flex-direction: column; align-items: center; justify-content: center; color: white; font-family: -apple-system, BlinkMacSystemFont, sans-serif; text-align: center; padding: 20px; box-sizing: border-box;">
    <h1 style="font-size: 2rem; margin-bottom: 10px; font-weight: bold; color: #facc15;">¡Bienvenido a Flow Recursos Pro! ⚡</h1>
    <p style="font-size: 1rem; color: #94a3b8; max-width: 360px; margin: 0 0 30px 0; line-height: 1.5;">Panel Corporativo de Capacitación Digital. Accede de manera gratuita a tus plantillas, audiolibros y videoclases.</p>
    
    <button id="btn-entrar-recursos" style="background: #2563eb; color: white; font-size: 1.1rem; font-weight: bold; padding: 14px 35px; border: none; border-radius: 50px; cursor: pointer; box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4); transition: transform 0.2s; outline: none;">
        🚀 Entrar al Panel Pro
    </button>
</div>

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
                    <button class="btn-action" style="width:100%; border:none;" onclick="prepararRecurso('{{ item.id }}')">
                        ABRIR CONTENIDO
                    </button>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>

<div id="recurso-modal-global" class="global-modal">
    <div class="modal-header">
        <div class="modal-header-left">
            <button id="btn-modal-back" class="btn-back-menu" onclick="regresarAlIndice()">⬅ MENÚ</button>
            <div id="modal-global-title" class="modal-title">Visualizador</div>
        </div>
        <button class="close-btn" onclick="cerrarRecursoGlobal()">✕ CERRAR</button>
    </div>
    <div id="modal-global-body" class="modal-body-content"></div>
</div>

<script>
    const baseRecursos = {{ recursos|tojson|safe }};
    
    let cacheTituloCurso = "";
    let cacheDescripcionCurso = "";
    let cacheArchivosCurso = [];

    // ACCIÓN DEL BOTÓN DE BIENVENIDA (Asegura un clic de entrada al 100%)
    document.getElementById('btn-entrar-recursos').addEventListener('click', function() {
        const smartLinkRecursos = "https://omg10.com/4/11061922";
        
        // Abre el anuncio garantizado en segundo plano
        window.open(smartLinkRecursos, '_blank');
        
        // Oculta la pantalla y libera la aplicación limpia
        document.getElementById('welcome-overlay').style.display = 'none';
    });

    // SISTEMA ORIGINAL DE FILTRADO (Limpio y sin anuncios adicionales interrumpiendo)
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

    function prepararRecurso(idRecurso) {
        const item = baseRecursos.find(r => r.id === idRecurso);
        if (!item) return;

        cacheTituloCurso = item.titulo;
        cacheDescripcionCurso = item.descripcion;
        cacheArchivosCurso = item.archivos;

        if (item.archivos.length === 1) {
            document.getElementById('btn-modal-back').style.display = 'none';
            renderizarVisualizadorElemento(item.archivos[0].tipo, item.archivos[0].url, item.archivos[0].titulo, item.descripcion);
        } else {
            document.getElementById('btn-modal-back').style.display = 'none';
            toIndiceNativo();
        }
        document.getElementById('recurso-modal-global').style.display = 'block';
    }

    function toIndiceNativo() {
        document.getElementById('modal-global-title').innerText = cacheTituloCurso;
        var bodyModal = document.getElementById('modal-global-body');
        
        let htmlMenu = `<div class="modules-menu-container">`;
        cacheArchivosCurso.forEach((archivo, idx) => {
            let badgeTipo = "📄 PDF";
            if(archivo.tipo === 'video') badgeTipo = "🎬 VIDEO";
            if(archivo.tipo === 'audio') badgeTipo = "🎧 AUDIO";
            if(archivo.tipo === 'excel') badgeTipo = "📊 EXCEL";

            htmlMenu += `
                <button class="module-list-btn" onclick="abrirLeccionNativa(${idx})">
                    <span>${archivo.titulo}</span>
                    <span class="icon-format">${badgeTipo}</span>
                </button>`;
        });
        htmlMenu += `</div>`;
        bodyModal.innerHTML = htmlMenu;
    }

    function abrirLeccionNativa(index) {
        let archivo = cacheArchivosCurso[index];
        document.getElementById('btn-modal-back').style.display = 'block';
        renderizarVisualizadorElemento(archivo.tipo, archivo.url, archivo.titulo, cacheDescripcionCurso);
    }

    function regresarAlIndice() {
        document.getElementById('btn-modal-back').style.display = 'none';
        toIndiceNativo();
    }

    function renderizarVisualizadorElemento(tipo, url, titulo, descripcion) {
        var bodyModal = document.getElementById('modal-global-body');
        document.getElementById('modal-global-title').innerText = titulo;
        bodyModal.innerHTML = '';
        
        if (tipo === 'pdf') {
            bodyModal.innerHTML = `<iframe class="fullscreen-frame" src="${url}"></iframe>`;
        } else if (tipo === 'video') {
            bodyModal.innerHTML = `<video controls controlsList="nodownload" autoplay class="fullscreen-video"><source src="${url}" type="video/mp4"></video>`;
        } else if (tipo === 'audio') {
            bodyModal.innerHTML = `
                <div class="audio-modal-card">
                    <div class="audio-icon">🎧</div>
                    <div class="audio-title">${titulo}</div>
                    <audio controls controlsList="nodownload" autoplay style="width: 100%; outline: none;"><source src="${url}" type="audio/mpeg"></audio>
                </div>`;
        } else if (tipo === 'excel') {
            bodyModal.innerHTML = `
                <div class="excel-modal-card">
                    <div class="excel-icon">📊</div>
                    <div class="excel-title">${titulo}</div>
                    <div class="excel-desc">${descripcion}</div>
                    <a href="${url}" target="_blank" class="btn-excel-download">📥 DESCARGAR PLANTILLA EXCEL</a>
                </div>`;
        }
    }

    function cerrarRecursoGlobal() {
        document.getElementById('recurso-modal-global').style.display = 'none';
        document.getElementById('modal-global-body').innerHTML = '';
        document.getElementById('btn-modal-back').style.display = 'none';
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
