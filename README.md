# Siemprende Mi Negocio

## 🚀 Plataforma Integral de Gestión Empresarial Modular para PYMES

"Siemprende Mi Negocio" es una plataforma web integral, orientada a microservicios, diseñada para digitalizar y escalar los procesos operativos de pequeñas y medianas empresas (PYMES)[cite: 3]. Nuestro objetivo principal es lograr una Experiencia de Usuario (UX) excepcional a través de un sistema robusto, eficiente, seguro y de fácil mantenimiento[cite: 4].

Esta plataforma se concibe como un "Operating System Empresarial Modular" con KPIs propios, automatización y flujos inteligentes, paneles de control independientes y un tablero general consolidado, todo con una interfaz UI/UX amigable y coherente[cite: 6].

## ✨ Características Destacadas

* **Arquitectura de Microservicios:** Cada módulo funcional es una unidad de negocio y software autocontenida, desplegada y desarrollada de forma independiente[cite: 30, 31].
* **Despliegue Cloud-Native:** Construida intrínsecamente para Google Cloud Platform (GCP), aprovechando al máximo servicios serverless como Cloud Run para escalabilidad automática y alta disponibilidad[cite: 39, 105].
* **Backend Robusto:** Desarrollado en **Python (Flask/FastAPI)**, utilizando MongoDB Atlas como base de datos[cite: 61, 62, 63, 64].
* **Frontend Intuitivo:** Construido con **React.js**, diseñado con un enfoque "Mobile-First" y "páginas independientes" para cada microservicio/módulo, facilitando el desarrollo incremental y el despliegue desacoplado[cite: 34, 35, 96, 97].
* **Gestión de Acceso Basada en Roles (RBAC):** Sistema granular para usuarios, roles y privilegios, controlando el acceso tanto al backend como a las funcionalidades del frontend[cite: 36, 37].
* **IA Integrada:** Incorporación de funciones de Inteligencia Artificial para diagnóstico, sugerencias de mejora y resúmenes ejecutivos[cite: 25, 206].
* **Automatización Completa (CI/CD):** Pipelines automatizados con GitHub Actions y Google Cloud Build para pruebas, construcción de imágenes Docker y despliegue continuo en Cloud Run[cite: 107, 115].
* **Seguridad Integral:** Implementación de JWT para autenticación, gestión de secretos con Google Secret Manager, HTTPS obligatorio, y cumplimiento con OWASP Top 10[cite: 111, 168, 170, 265, 267].
* **Observabilidad Avanzada:** Centralización de logs con Google Cloud Logging, métricas con Cloud Monitoring y trazabilidad distribuida con OpenTelemetry[cite: 108, 109, 176, 177, 178].

## 📚 Módulos de la Plataforma

La plataforma cubre una amplia gama de dominios funcionales, organizados como microservicios independientes:

* **CRM** (Customer Relationship Management) [cite: 7]
* **Inventario** [cite: 8]
* **Recursos Humanos (RRHH)** [cite: 8]
* **Facturación Electrónica** [cite: 9]
* **Chatbot** [cite: 9]
* **Logística** [cite: 10]
* **Dashboard Predictivo** [cite: 10]
* **Seguridad y Autenticación** (Gestión de Usuarios, Roles y Privilegios) [cite: 11]
* **Notificaciones** (Email, WhatsApp, Messenger) [cite: 12]
* **Marketing y Campañas** (NUEVO) [cite: 13]
* **Compras / Proveedores (Abastecimiento)** (NUEVO) [cite: 14]
* **Contabilidad y Finanzas** (NUEVO) [cite: 15]
* **Calidad / ISO** (NUEVO) [cite: 16]
* **Legal / Contratos** (NUEVO) [cite: 17]
* **Conocimiento y Documentación** (NUEVO) [cite: 18]
* **Capacitación y Evaluación (LMS)** (NUEVO) [cite: 19]
* **Atención a Clientes / Postventa (Soporte)** (NUEVO) [cite: 20]
* **Cobranza** (NUEVO) [cite: 21]
* **Planeación Estratégica y OKRs** (NUEVO) [cite: 22]
* **Integración con E-commerce y Tiendas en Línea** (NUEVO) [cite: 23]

## 🛠️ Tecnologías Utilizadas

### Backend
* **Lenguaje:** Python 3.10+ [cite: 62]
* **Frameworks:** Flask, FastAPI (opcional) [cite: 63, 64]
* **Base de Datos:** MongoDB Atlas [cite: 61]
* **ODMs/Drivers:** Pymongo, MongoEngine, Motor [cite: 65, 66]
* **Autenticación:** PyJWT [cite: 67]
* **ML/Optimización:** Scikit-learn, Pandas, NumPy, Google OR-Tools [cite: 71, 72]
* **LLMs:** OpenAI API, Google Gemini API (u otros) [cite: 73]
* **Calidad de Código:** Flake8, Pylint, Black, Mypy [cite: 77, 78, 79]

### Frontend
* **Framework:** React.js 18+ [cite: 87]
* **Ruteo:** `react-router-dom` [cite: 88]
* **HTTP Client:** Axios [cite: 90]
* **Estado:** React Context API, Redux Toolkit (opcional) [cite: 91, 92]
* **Internacionalización:** `react-i18next` [cite: 89]
* **Calidad de Código:** ESLint, Prettier [cite: 95]

### Infraestructura y DevOps
* **Contenerización:** Docker [cite: 102]
* **Orquestación Local:** `docker-compose` [cite: 103]
* **Plataforma Cloud:** Google Cloud Platform (GCP) [cite: 104]
* **Servicios GCP:** Cloud Run, Artifact Registry, Cloud Build, Secret Manager, Logging, Monitoring, IAM, Load Balancing, VPC Access Connector [cite: 105, 106, 107, 108, 109, 110, 111, 112, 113]
* **CI/CD:** GitHub Actions [cite: 115]

## 🚀 Guía de Inicio Rápido (Desarrollo Local)

Para levantar la plataforma en tu entorno local:

1.  **Clonar el Repositorio:**
    ```bash
    git clone [https://github.com/tu-organizacion/siemprende.git](https://github.com/tu-organizacion/siemprende.git)
    cd siemprende
    ```
2.  **Configurar Variables de Entorno:**
    Copia el archivo de ejemplo y edita las variables necesarias para tu entorno local.
    ```bash
    cp .env.example .env
    # Abre .env y edita MONGO_URI, JWT_SECRET, REACT_APP_API_URL, y las API Keys locales.
    ```
    *Asegúrate de que `.env` esté en tu `.gitignore` para no subir secretos.*
3.  **Levantar Servicios con Docker Compose:**
    Este comando construirá las imágenes de Docker para todos los microservicios backend y el frontend, y los levantará junto con una instancia local de MongoDB.
    ```bash
    docker-compose up --build
    ```
4.  **Acceder a la Aplicación:**
    * **Frontend:** `http://localhost:3000`
    * **Backend (ej. User Management):** `http://localhost:8080/api/v1/users` (los puertos pueden variar por servicio, consulta `docker-compose.yml`)
    * **MongoDB:** `mongodb://localhost:27017`

## ⚙️ Despliegue en Google Cloud Platform

El despliegue en producción se realiza de manera automatizada a través de pipelines de CI/CD configurados en GitHub Actions (integrado con Google Cloud Build). Los pasos clave incluyen:

1.  **Requisitos Previos en GCP:** Configuración de `gcloud CLI`, proyecto GCP, habilitación de servicios como Artifact Registry, Cloud Run, Secret Manager, etc.
2.  **Gestión Segura de Secretos:** Todas las credenciales sensibles se almacenan en Google Secret Manager y se inyectan como variables de entorno en los contenedores de Cloud Run durante el despliegue.
3.  **Construcción y Publicación de Imágenes:** Las imágenes Docker de cada microservicio y del frontend son construidas y publicadas en Google Artifact Registry.
4.  **Despliegue Automatizado:** Los workflows de GitHub Actions (`.github/workflows/ci-cd.yml`) orquestan la ejecución de pruebas, linting, construcción de imágenes y despliegue de los servicios en Cloud Run en las ramas `dev`, `staging` y `main`.

Para más detalles sobre el despliegue y la configuración en GCP, consulta la sección **6. Procedimientos de Desarrollo y Despliegue** en el [Documento Técnico de Diseño Detallado](link-a-tu-documento-final.pdf).

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Consulta nuestro [Documento Técnico de Diseño Detallado](link-a-tu-documento-final.pdf) para entender la arquitectura, los estándares de código y las buenas prácticas. Antes de enviar un Pull Request, asegúrate de que tu código cumpla con los estándares de calidad y que todas las pruebas pasen.

## 📄 Licencia

Este proyecto está bajo la licencia [Nombre de la Licencia, ej. MIT]. Consulta el archivo `LICENSE` para más detalles.

---

**Nota:** Reemplaza `https://github.com/tu-organizacion/siemprende.git` y `link-a-tu-documento-final.pdf` con los URLs reales de tu repositorio y el documento final.
