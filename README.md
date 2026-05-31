# 📚 Readers

> Una red social para amantes de los libros. Descubrí lecturas, escribí reseñas y conectá con otros lectores.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=flat&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=flat&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/Licencia-MIT-green?style=flat)

---

## Características

- 🔐 Registro e inicio de sesión de usuarios
- 👤 Perfil personal con biblioteca, reseñas y lista de lectura
- 📖 Catálogo de libros con portadas
- 🎨 Diseño inspirado en Instagram, adaptado al mundo lector
- 🔒 Rutas protegidas con autenticación

---

## 🚀 Instalación local

### Requisitos

- Python 3.12+
- pipenv

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/readers.git
cd readers

# 2. Crear entorno virtual e instalar dependencias
pipenv install
pipenv shell

# 3. Aplicar migraciones
python manage.py migrate

# 4. Crear superusuario
python manage.py createsuperuser

# 5. Correr el servidor
python manage.py runserver
```

Abrí [http://localhost:8000](http://localhost:8000) en tu navegador.

---

## 📁 Estructura

```
readers/
├── config/          # Configuración del proyecto (settings, urls)
├── core/            # Home y landing page
├── users/           # Autenticación, registro y perfiles
├── books/           # Catálogo de libros
├── static/
│   └── css/
│       └── main.css
├── media/           # Portadas de libros subidas
├── manage.py
└── README.md
```

---

## ⚙️ Variables de entorno

Para producción, creá un archivo `.env` en la raíz con estas variables:

```env
SECRET_KEY=tu-clave-secreta
DEBUG=False
ALLOWED_HOSTS=tudominio.com
```

> En desarrollo, los valores por defecto en `settings.py` son suficientes.

---

## 🗺️ Roadmap

- [ ] Modelo de reseñas vinculado a usuario y libro
- [ ] Lista de lectura personalizada
- [ ] Sistema de seguidores
- [ ] Búsqueda de libros y usuarios
- [ ] Avatar de perfil con subida de imagen
- [ ] Clubes de lectura virtuales

---

## 🛠️ Stack

| Tecnología | Uso |
|------------|-----|
| Django 6 | Backend y ORM |
| SQLite | Base de datos (desarrollo) |
| Bootstrap 5 | Componentes UI base |
| CSS custom | Estilos propios del diseño |
| Tabler Icons | Iconografía |
| Google Fonts | Tipografías (Playfair Display + Lato) |
