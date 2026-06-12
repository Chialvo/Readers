# 📚 Readers

> Una red social para amantes de los libros. Buscá cualquier libro, llevá registro de tus lecturas y conectá con otros lectores.

🌐 **Demo en vivo:** [readers-production.up.railway.app](https://readers-production.up.railway.app/)

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0.3-092E20?style=flat&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=flat&logo=sqlite&logoColor=white)
![Railway](https://img.shields.io/badge/Railway-deployed-0B0D0E?style=flat&logo=railway&logoColor=white)

---

## Características

- 🔐 Registro e inicio de sesión de usuarios
- 👤 Perfil con foto, bio, estadísticas y biblioteca personal
- 📖 Búsqueda de libros en tiempo real via Google Books API
- 📚 Sistema de estados: Quiero leer / Leyendo / Leído
- ⭐ Puntuación de 1 a 5 estrellas al marcar un libro como leído
- 📊 Mi Biblioteca: estadísticas, géneros favoritos y mejor puntuado
- 👥 Sistema de seguidores entre usuarios
- 🔍 Búsqueda de lectores por nombre de usuario
- 🎨 Sidebar de navegación colapsable con iconos
- 🔒 Rutas protegidas con autenticación

---

## Instalación local

### Requisitos

- Python 3.14+
- pipenv

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/readers.git
cd readers/Readers

# 2. Crear entorno virtual e instalar dependencias
pipenv install
pipenv shell

# 3. Configurar variables de entorno
cp .env.example .env
# Editá el .env con tus valores

# 4. Aplicar migraciones
python manage.py migrate

# 5. Crear superusuario
python manage.py createsuperuser

# 6. Correr el servidor
python manage.py runserver
```

Abrí [http://localhost:8000](http://localhost:8000) en tu navegador.

---

## Variables de entorno

Creá un archivo `.env` en la raíz del proyecto:

```env
SECRET_KEY=tu-clave-secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
GOOGLE_BOOKS_API_KEY=tu-api-key-de-google-books
```

Para producción en Railway:

```env
DEBUG=False
ALLOWED_HOSTS=readers-production.up.railway.app
CSRF_TRUSTED_ORIGINS=https://readers-production.up.railway.app
GOOGLE_BOOKS_API_KEY=tu-api-key-de-google-books
```

> La API key de Google Books es gratuita. Podés obtenerla en [Google Cloud Console](https://console.cloud.google.com) habilitando la Books API.

---

## 📁 Estructura

```
Readers/
├── config/          # Configuración del proyecto (settings, urls, wsgi)
├── core/            # Home y vistas base
├── users/           # Autenticación, registro, perfiles y seguidores
├── books/           # Búsqueda, detalle, estados y biblioteca personal
├── static/
│   └── css/
│       └── main.css # Estilos centralizados
├── media/           # Avatares de usuarios subidos
├── manage.py
└── README.md
```

---

## Stack

| Tecnología | Uso |
|------------|-----|
| Django 6.0.3 | Backend y ORM |
| SQLite | Base de datos |
| Google Books API | Catálogo de libros |
| Bootstrap 5 | Componentes UI base |
| CSS custom | Diseño editorial propio |
| Tabler Icons | Iconografía |
| Google Fonts | Playfair Display + Lato + DM Sans |
| WhiteNoise | Archivos estáticos en producción |
| Gunicorn | Servidor WSGI en producción |
| Railway | Hosting y deployment |

---

## Modelos principales

```
User          → AbstractUser con bio, avatar y sistema de seguidores (M2M)
Book          → Identificado por google_books_id, con géneros (M2M)
Genre         → Géneros extraídos de la API
UserBook      → Relación usuario-libro con status, rating y read_date
```

---

## Roadmap

- [x] Autenticación y registro
- [x] Perfiles de usuario con avatar y bio
- [x] Integración con Google Books API
- [x] Estados de lectura con puntuación
- [x] Sistema de seguidores
- [x] Búsqueda de usuarios
- [x] Mi Biblioteca con estadísticas y géneros favoritos
- [x] Sidebar de navegación colapsable
- [x] Deploy en Railway
- [ ] Feed social con actividad de seguidos
- [ ] Reseñas con texto
- [ ] Clubes de lectura virtuales
- [ ] Notificaciones
