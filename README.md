# Siemprende Mi Negocio

## 🚀 Plataforma Integral de Gestión Empresarial Modular para PYMES

"Siemprende Mi Negocio" es una plataforma web integral, orientada a microservicios, diseñada para digitalizar y escalar los procesos operativos de pequeñas y medianas empresas (PYMES). Nuestro objetivo principal es lograr una Experiencia de Usuario (UX) excepcional a través de un sistema robusto, eficiente, seguro y de fácil mantenimiento.

Esta plataforma se concibe como un "Operating System Empresarial Modular" con KPIs propios, automatización y flujos inteligentes, paneles de control independientes y un tablero general consolidado, todo con una interfaz UI/UX amigable y coherente.

## ✨ Características Destacadas

* **Arquitectura de Microservicios:** Cada módulo funcional es una unidad de negocio y software autocontenida, desplegada y desarrollada de forma independiente.
* **Despliegue Cloud-Native:** Construida intrínsecamente para Google Cloud Platform (GCP), aprovechando al máximo servicios serverless como Cloud Run para escalabilidad automática y alta disponibilidad.
* **Backend Robusto:** Desarrollado en **Python (Flask/FastAPI)**, utilizando MongoDB Atlas como base de datos.
* **Frontend Intuitivo:** Construido con **React.js**, diseñado con un enfoque "Mobile-First" y "páginas independientes" para cada microservicio/módulo, facilitando el desarrollo incremental y el despliegue desacoplado.
* **Gestión de Acceso Basada en Roles (RBAC):** Sistema granular para usuarios, roles y privilegios, controlando el acceso tanto al backend como a las funcionalidades del frontend.
* **IA Integrada:** Incorporación de funciones de Inteligencia Artificial para diagnóstico, sugerencias de mejora y resúmenes ejecutivos.
* **Automatización Completa (CI/CD):** Pipelines automatizados con GitHub Actions y Google Cloud Build para pruebas, construcción de imágenes Docker y despliegue continuo en Cloud Run.
* **Seguridad Integral:** Implementación de JWT para autenticación, gestión de secretos con Google Secret Manager, HTTPS obligatorio, y cumplimiento con OWASP Top 10.
* **Observabilidad Avanzada:** Centralización de logs con Google Cloud Logging, métricas con Cloud Monitoring y trazabilidad distribuida con OpenTelemetry.

## 📚 Módulos de la Plataforma

La plataforma cubre una amplia gama de dominios funcionales, organizados como microservicios independientes:

* **CRM** (Customer Relationship Management)
* **Inventario** 
* **Recursos Humanos (RRHH)** 
* **Facturación Electrónica** 
* **Chatbot** 
* **Logística**
* **Dashboard Predictivo**
* **Seguridad y Autenticación** (Gestión de Usuarios, Roles y Privilegios)
* **Notificaciones** (Email, WhatsApp, Messenger) 
* **Marketing y Campañas**  
* **Compras / Proveedores (Abastecimiento)** 
* **Contabilidad y Finanzas** 
* **Calidad / ISO** 
* **Legal / Contratos** 
* **Conocimiento y Documentación** 
* **Capacitación y Evaluación (LMS)** 
* **Atención a Clientes / Postventa (Soporte)**
* **Cobranza**
* **Planeación Estratégica y OKRs**
* **Integración con E-commerce y Tiendas en Línea**

## 🛠️ Tecnologías Utilizadas

### Backend
* **Lenguaje:** Python 3.10+ 
* **Frameworks:** Flask, FastAPI (opcional) 
* **Base de Datos:** MongoDB Atlas 
* **ODMs/Drivers:** Pymongo, MongoEngine, Motor 
* **Autenticación:** PyJWT 
* **ML/Optimización:** Scikit-learn, Pandas, NumPy, Google OR-Tools 
* **LLMs:** OpenAI API, Google Gemini API (u otros) 
* **Calidad de Código:** Flake8, Pylint, Black, Mypy 

### Frontend
* **Framework:** React.js 18+ 
* **Ruteo:** `react-router-dom` 
* **HTTP Client:** Axios 
* **Estado:** React Context API, Redux Toolkit (opcional) 
* **Internacionalización:** `react-i18next` 
* **Calidad de Código:** ESLint, Prettier 

### Infraestructura y DevOps
* **Contenerización:** Docker 
* **Orquestación Local:** `docker-compose` 
* **Plataforma Cloud:** Google Cloud Platform (GCP) 
* **Servicios GCP:** Cloud Run, Artifact Registry, Cloud Build, Secret Manager, Logging, Monitoring, IAM, Load Balancing, VPC Access Connector 
* **CI/CD:** GitHub Actions 

## 🚀 Guía de Inicio Rápido (Desarrollo Local)

Para levantar la plataforma en tu entorno local:

1.  **Clonar el Repositorio:**
    ```bash
    git clone [https://github.com/Siemprende-Mi-Negocio/siemprende_mi_negocio_2.0.git] (https://github.com/Siemprende-Mi-Negocio/siemprende_mi_negocio_2.0.git)
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

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---
