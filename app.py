import os
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# CONFIGURACIÓN ESTRUCTURAL DE PRUEBA
# Usamos IDs reales de IMDb para verificar que el reproductor externo conecte a la primera
PELICULAS_BASE = [
    {
        "id": "tt1877830", 
        "titulo": "The Batman", 
        "anio": "2022", 
        "poster": "https://images.unsplash.com/photo-1626814026160-2237a95fc5a0?w=600&auto=format&fit=crop&q=80", 
        "sinopsis": "En su segundo año luchando contra el crimen, Batman explora la corrupción existente en la ciudad de Gotham y el vínculo de esta con su propia familia."
    },
    {
        "id": "tt0133096", 
        "titulo": "The Matrix", 
        "anio": "1999", 
        "poster": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=80", 
        "sinopsis": "Un programador de computación descubre que el mundo en el que vive es una simulación virtual controlada por máquinas superiores."
    },
    {
        "id": "tt0816692", 
        "titulo": "Interstellar", 
        "anio": "2014", 
        "poster": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&auto=format&fit=crop&q=80", 
        "sinopsis": "Un grupo de científicos y exploradores espaciales se embarcan en un viaje desafiante para encontrar un nuevo hogar para la humanidad."
    }
]

# DISEÑO VISUAL LIMPIO OPTIMIZADO PARA TELEGRAM (Formato Vertical Largo)
HTML_FRONTEND = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>MundoFlow Cinema</title>
    <style>
        body {
            background-color: #0b0c10;
            color: #c5c6c7;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            margin: 0;
            padding: 12px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .app-container {
            width: 100%;
            max-width: 440px; /* Ancho exacto para simular la vista dentro de Telegram */
            background: #1f2833;
            border-radius: 12px;
            padding: 16px;
            box-sizing: border-box;
            box-shadow: 0 4px 15px rgba(0,0,0,0.6);
        }
        h1 {
            font-size: 20px;
            text-align: center;
            color: #66fcf1;
            margin-top: 0;
            margin-bottom: 16px;
        }
        .search-area {
            display: flex;
            gap: 8px;
            margin-bottom: 16px;
        }
        input {
            flex: 1;
            padding: 10px;
            border-radius: 6px;
            border: 1px solid #45a29e;
            background: #0b0c10;
            color: #ffffff;
            font-size: 14px;
        }
        button {
            padding: 10px 16px;
            border-radius: 6px;
            border: none;
            background: #66fcf1;
            color: #0b0c10;
            font-weight: bold;
            cursor: pointer;
        }
        .movie-card {
            background: #0b0c10;
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 16px;
            border: 1px solid #1f2833;
        }
        .movie-poster {
            width: 100%;
            height: 220px;
            object-fit: cover;
        }
        .movie-details {
            padding: 12px;
        }
        .movie-title {
            font-size: 16px;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 4px;
        }
        .movie-meta {
            font-size: 11px;
            color: #45a29e;
            margin-bottom: 8px;
        }
        .movie-synopsis {
            font-size: 13px;
            line-height: 1.4;
            margin-bottom: 12px;
        }
        .btn-stream {
            display: block;
            text-align: center;
            background: #45a29e;
            color: #ffffff;
            text-decoration: none;
            padding: 10px;
            border-radius: 6px;
            font-weight: bold;
            font-size: 14px;
        }
        .player-box {
            position: relative;
            width: 100%;
            padding-top: 56.25%; /* Mantiene proporción 16:9 de video */
            margin-top: 12px;
            display: none;
            border-radius: 6px;
            overflow: hidden;
            background: #000000;
        }
        iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }
    </style>
</head>
<body>

<div class="app-container">
    <h1>🎬 MundoFlow Cinema</h1>
    
    <div class="search-area">
        <input type="text" id="input-search" placeholder="Buscar película de prueba...">
        <button onclick="ejecutarBusqueda()">Buscar</button>
    </div>

    <div id="content-list">
        {% for film in movies %}
        <div class="movie-card">
            <img class="movie-poster" src="{{ film.poster }}" alt="Poster">
            <div class="movie-details">
                <div class="movie-title">{{ film.titulo }}</div>
                <div class="movie-meta">Año: {{ film.anio }} | Servidor: Vidsrc CDN</div>
                <div class="movie-synopsis">{{ film.sinopsis }}</div>
                
                <a href="#" class="btn-stream" onclick="cargarReproductor('{{ film.id }}', this); return false;">▶️ REPRODUCIR CONTENIDO</a>
                
                <div class="player-box" id="box-{{ film.id }}">
                    </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>

<script>
    function cargarReproductor(id, elemento) {
        var contenedor = document.getElementById('box-' + id);
        
        // Endpoint oficial gratuito que no requiere tokens para cargar los streams
        var urlEmbed = "https://vidsrc.to/embed/movie/" + id;
        
        // Inyectamos el reproductor nativo directamente sin recargar la página web
        contenedor.innerHTML = '<iframe src="' + urlEmbed + '" allowfullscreen></iframe>';
        contenedor.style.display = 'block';
        elemento.style.display = 'none'; // Oculta el botón para centrar la atención en el video
    }

    function ejecutarBusqueda() {
        alert("Estructura de búsqueda lista. En el siguiente paso la conectaremos al inventario global.");
    }
</script>

</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_FRONTEND, movies=PELICULAS_BASE)

if __name__ == '__main__':
    # Configuración estricta para que Railway asigne el puerto de producción dinámico
    puerto = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=puerto)
