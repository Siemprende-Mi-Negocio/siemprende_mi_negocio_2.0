# Guía de Colaboración para Agentes de IA (Codex)

Este documento proporciona contexto y directrices exhaustivas para los agentes de IA (como Codex) que interactúan con el repositorio de "Siemprende Mi Negocio". Su propósito es asegurar que todas las tareas se realicen de manera consistente, eficiente, y en estricta adherencia a nuestros estándares de desarrollo, arquitectura y seguridad.

## 1. Contexto Profundo del Proyecto

"Siemprende Mi Negocio" es una plataforma integral de gestión empresarial modular, diseñada específicamente para digitalizar y escalar los procesos operativos de pequeñas y medianas empresas (PYMES). Nuestro objetivo primordial es proporcionar una Experiencia de Usuario (UX) excepcional a través de un sistema que no solo sea robusto y eficiente, sino también inherentemente seguro y fácilmente mantenible.

* **Arquitectura:** Implementamos una arquitectura de microservicios. El backend se desarrolla en Python (utilizando Flask para servicios ligeros y FastAPI de forma opcional para alto rendimiento y validación de datos) y el frontend en React.js. La plataforma se despliega de manera serverless en Google Cloud Run, utilizando MongoDB Atlas como nuestra base de datos NoSQL principal.
* **Modularidad Fundamental:**
    * **Backend:** Cada microservicio es una unidad de desarrollo y despliegue completamente independiente, comunicándose exclusivamente a través de APIs RESTful bien definidas.
    * **Frontend:** La aplicación web está diseñada con un enfoque de "páginas independientes" (o módulos de UI lógicos) para cada microservicio. Esto no solo facilita el desarrollo y despliegue incremental del frontend, sino que también permite la activación o desactivación granular de módulos según los roles de usuario.
* **Principios de Diseño:** Nos adherimos estrictamente a los principios de microservicios, desacoplamiento de capas, despliegue independiente y Responsabilidad Única por Servicio (SRP).
* **Filosofía Cloud-Native:** La arquitectura está intrínsecamente diseñada para aprovechar al máximo los servicios gestionados de GCP, garantizando escalabilidad, resiliencia y eficiencia operativa.
* **Objetivos Estratégicos:** Todas las decisiones y desarrollos deben contribuir a la escalabilidad (crecimiento de 10x en 2 años), seguridad (cumplimiento OWASP Top 10), alta disponibilidad (99.9% de uptime), modularidad, capacidad de análisis predictivo, y automatización de procesos, siempre priorizando la UX.

## 2. Estructura Detallada del Repositorio

El repositorio raíz `siemprende/` refleja directamente nuestra arquitectura modular, separando lógicamente el backend del frontend.

* `backend/`: Este directorio contiene todos los microservicios Python.
    * Cada microservicio reside en su propio subdirectorio, siguiendo un patrón consistente (ej. `backend/crm_service/`, `backend/inventory_service/`, etc.).
    * Dentro de cada subdirectorio de servicio, se espera la siguiente estructura estándar:
        * `app.py`: El punto de entrada principal del microservicio (aplicación Flask/FastAPI).
        * `models/`: Definiciones de esquemas de datos (usando MongoEngine/Pydantic).
        * `controllers/`: Contiene la lógica de negocio específica del microservicio.
        * `routes/`: Define los endpoints API del microservicio.
        * `Dockerfile`: Configuración específica de Docker para construir la imagen de este servicio.
        * `requirements.txt`: Dependencias de Python únicas para este microservicio.
        * `tests/`: Pruebas unitarias y de integración para el servicio.
    * `shared/`: Este es un módulo crucial para código transversal y reutilizable entre microservicios, asegurando consistencia.
        * `auth_middleware.py`: Middleware centralizado para autenticación (JWT) y autorización (RBAC).
        * `error_handlers.py`: Manejo de errores común para respuestas HTTP estandarizadas.
        * `utils.py`: Funciones de utilidad comunes (ej. helpers para logging estructurado).
* `frontend/`: Este directorio contiene la aplicación web desarrollada con React.
    * `src/App.tsx`: Componente principal que gestiona el ruteo global y las rutas protegidas.
    * `src/index.tsx`: Punto de entrada de la aplicación React.
    * `src/i18n.ts`: Configuración para la internacionalización (`react-i18next`).
    * `src/auth/`: Encapsula toda la lógica relacionada con la autenticación (login, logout, manejo de JWT) y la autorización (RBAC en el frontend).
        * `AuthProvider.tsx`: Contexto de autenticación de React.
        * `ProtectedRoute.tsx`: Componente para proteger rutas basado en autenticación y roles/privilegios.
        * `AuthUtils.ts`: Funciones auxiliares para JWT y roles.
        * `hooks.ts`: Custom hooks relacionados con autenticación.
    * `src/common/`: Componentes, hooks y utilidades reutilizables globalmente (botones, modales, layouts generales).
    * `src/pages/`: **CONTENEDORES DE PÁGINA POR CADA MICROSERVICIO/MÓDULO**. Cada subdirectorio aquí representa una "página independiente" o un módulo lógico de UI (ej. `pages/DashboardPage/`, `pages/CrmPage/`, `pages/InventoryPage/`, `pages/MarketingPage/`, etc.). Cada uno de estos subdirectorios sigue una estructura interna consistente (`index.tsx`, `components/`, `hooks.ts`, `styles.ts`).
    * `src/locales/`: Archivos de traducción JSON (`en.json`, `es.json`).
    * `src/services/`: Clientes HTTP (Axios) para interactuar con las APIs de cada microservicio backend.
    * `src/styles/`: Estilos globales, variables CSS.
* `docker-compose.yml`: Archivo de configuración central para levantar un entorno de desarrollo local completo que incluye todos los microservicios backend, el frontend y una instancia de MongoDB.
* `.env.example`: Un archivo de ejemplo con las variables de entorno necesarias para el proyecto, incluyendo las credenciales para servicios externos en un contexto de desarrollo local. Este archivo debe ser copiado a `.env` y editado localmente, y `.env` **DEBE** estar en `.gitignore`.
* `README.md`: Documentación general del proyecto.

## 3. Directrices Estrictas de Calidad de Código

Es imperativo que todo el código fuente generado o modificado cumpla con los más altos estándares de calidad, asegurando la mantenibilidad, escalabilidad y robustez de la plataforma.

* **Principios de Diseño de Software:** Se exige la aplicación rigurosa de principios como SOLID (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion), DRY (Don't Repeat Yourself) y KISS (Keep It Simple, Stupid). El código debe ser intrínsecamente limpio, legible y fácilmente mantenible por cualquier miembro del equipo.
* **Análisis Estático (Linting):**
    * **Python (Backend):** Antes de cualquier push o despliegue, el código Python debe pasar satisfactoriamente los linters configurados. Se ejecutarán comandos como `flake8 .` y `pylint .` para verificar el estilo y la calidad del código, y `mypy .` para asegurar la verificación de tipado estático, mejorando la robustez y la detección temprana de errores.
    * **JavaScript/TypeScript (React - Frontend):** Similarmente, el código del frontend debe adherirse a los estándares de estilo. Se ejecutará `npm run lint` o `eslint .` para análisis estático, identificando problemas de estilo y posibles errores lógicos.
* **Formateo Automático Consistente:**
    * **Python:** La herramienta `Black` se utilizará para el formateo automático del código Python, garantizando una consistencia de estilo absoluto en todo el codebase.
    * **JavaScript/TypeScript:** `Prettier` será la herramienta para el formateo automático del código JavaScript/TypeScript, complementando a ESLint para un estilo unificado.
* **Documentación de Código:** Es obligatorio escribir `docstrings` completos y comentarios relevantes en el código, especialmente para funciones, clases y módulos complejos. Los archivos `README.md` de cada microservicio y del proyecto deben ser actualizados proactivamente para reflejar los cambios en la funcionalidad o la arquitectura.

## 4. Pruebas y Estrategias de Verificación Rigurosas

Todo cambio de código, sin excepción, debe ir acompañado de las pruebas adecuadas y verificaciones para garantizar la integridad y el correcto funcionamiento de la plataforma.

* **Cobertura de Pruebas:** Establecemos un objetivo mínimo del 80% de cobertura de código para las pruebas unitarias y de integración. Este es un indicador clave de la calidad del código y su resistencia a las regresiones.
* **Ejecución de Pruebas Automatizadas:**
    * **Python (Backend):** Para cada microservicio, las pruebas unitarias y de integración se ejecutarán utilizando `pytest` desde el directorio raíz del servicio (ej. `cd backend/crm_service && pytest`).
    * **React (Frontend):** Las pruebas del frontend se ejecutarán con `npm test` desde el directorio `frontend/`.
* **Pruebas de Integración y API:** Cuando sea relevante y la tarea lo amerite, se deben considerar pruebas de integración entre microservicios o pruebas de API completas. Esto puede implicar la ejecución de colecciones de Postman/Newman para validar los endpoints del backend contra los contratos de API definidos.
* **Pasos de Verificación Finales:** Antes de que el agente considere una tarea completa y presente un `diff`, debe realizar una serie de verificaciones críticas:
    * Confirmar que **todas las pruebas automatizadas** (unitarias y de integración, tanto en Python con `pytest` como en React con `npm test`) han pasado exitosamente.
    * Verificar que **no hay errores de linting** (usando `flake8`, `mypy` para Python, y `eslint` para JavaScript/TypeScript).
    * Asegurarse de que el código ha sido **formateado automáticamente** (`black` para Python, `prettier` para JavaScript/TypeScript) para mantener la consistencia de estilo.

## 5. Directrices Inquebrantables de Seguridad

La seguridad no es una característica, sino un pilar fundamental de "Siemprende Mi Negocio". El agente debe integrar la mentalidad de seguridad en cada línea de código y decisión de diseño.

* **Cumplimiento OWASP Top 10:** Todas las implementaciones y revisiones de código deben realizarse teniendo en cuenta las vulnerabilidades más críticas identificadas por OWASP Top 10. Se deben aplicar contramedidas proactivas.
* **Validación de Entradas Rigurosa:** Es absolutamente crítico que todas las entradas de datos, tanto a nivel de API como en cualquier punto de interacción, sean validadas rigurosamente. Esto previene ataques como inyección SQL (o su equivalente en MongoDB), Cross-Site Scripting (XSS) y otros tipos de manipulación de datos.
* **Gestión Segura de Secretos:** Bajo ninguna circunstancia se deben incrustar credenciales, claves API, tokens de autenticación o cualquier otra información sensible directamente en el código fuente (hardcoding). Todas estas configuraciones deben ser leídas de variables de entorno, las cuales en producción provienen de Google Secret Manager, y en entornos de desarrollo/pruebas deben ser inyectadas de forma segura.
* **Control de Acceso Basado en Roles (RBAC):** Cualquier funcionalidad nueva o modificada debe integrarse perfectamente con nuestro sistema RBAC. El agente debe verificar que los endpoints API y los elementos de la UI (páginas, botones) aplican los permisos adecuados basados en los roles y privilegios del usuario autenticado (extraídos del JWT).
* **Cifrado de Datos:** Se debe asegurar que los datos sensibles estén cifrados tanto en tránsito (mediante HTTPS obligatorio para todas las comunicaciones) como en reposo (cifrado de bases de datos MongoDB).
* **Auditoría de Acciones Críticas:** Implementar logs de auditoría detallados para todas las acciones críticas realizadas por los usuarios o por el sistema.
* **Protección de Integraciones Externas:** Cuando se realicen integraciones con servicios de terceros (ej. Stripe, Shopify, APIs de anuncios), se debe implementar un manejo seguro de sus tokens OAuth, claves API y credenciales.

## 6. Comportamiento Esperado y Metodología de Trabajo del Agente

El agente no es solo un codificador, sino un colaborador técnico proactivo y analítico.

* **Análisis Inicial Profundo:** Antes de cualquier intervención, el agente debe realizar un análisis exhaustivo de la tarea, comprendiendo su propósito, su impacto en la arquitectura de microservicios, y cómo se alinea con la estructura de archivos existente y los principios de diseño.
* **Planificación Detallada:** Para tareas significativas, el agente debe esbozar un plan de acción claro. Esto incluye identificar los archivos exactos a modificar, las nuevas pruebas a escribir, los componentes a crear y cualquier consideración arquitectónica.
* **Proactividad y Optimización:** El agente está mandatado a ir más allá de la solicitud explícita. Si durante el análisis o la implementación se identifican oportunidades de mejora (en rendimiento, seguridad, mantenibilidad, costos de GCP, o adherencia a patrones arquitectónicos como Saga o Circuit Breaker) o posibles problemas (cuellos de botella, riesgos de seguridad), el agente debe señalarlo activamente y proponer soluciones.
* **Enfoque de Microservicio (Responsabilidad Única):** Cuando se trabaje en un microservicio específico, los cambios deben limitarse estrictamente a su directorio (`backend/[nombre_servicio]/`) y sus dependencias directas. Las modificaciones al módulo `shared/` solo deben realizarse si son transversalmente beneficiosas y con la debida justificación.
* **Comunicación Clara y Justificada:** Al completar una tarea, el agente debe presentar un `diff` limpio y fácil de entender. La explicación debe ser concisa, pero debe justificar las decisiones clave, los resultados de las pruebas (pasando, linting limpio) y cualquier consideración adicional o proactiva.
* **Limitación de Acceso a Internet:** Es fundamental que el agente recuerde que el acceso a internet está deshabilitado durante la fase de ejecución de la tarea (cuando el código se está probando o ejecutando). Todas las dependencias de los proyectos (Python y Node.js) deben ser instaladas previamente en los `setup scripts` del entorno de Codex.

## 7. Ejemplo de Prompt Altamente Detallado para Codex

Para una tarea típica en "Siemprende Mi Negocio", se espera un prompt que brinde suficiente contexto y especifique claramente las expectativas, permitiendo al agente trabajar de manera autónoma y efectiva:

```text
(Al usar el modo 'Code' en Codex)

**Tarea:** Implementar la funcionalidad de gestión de "Órdenes de Compra" (CRUD) en el nuevo microservicio `procurement_service`.

**Contexto:**
El `procurement_service` es uno de los nuevos módulos clave, enfocado en la gestión de compras y proveedores. Necesitamos una API robusta para manejar el ciclo de vida de las órdenes de compra.

**Requisitos Específicos:**

1.  **Esquema de Datos (Modelo MongoDB):**
    * Definir un esquema de datos detallado para "Orden de Compra" en `backend/procurement_service/models/order_model.py`.
    * Campos mínimos requeridos:
        * `order_id` (String, UUID o ObjectId si MongoDB lo genera, clave principal)
        * `supplier_id` (String, referencia al servicio de proveedores)
        * `items_ordered` (Array de objetos, cada uno con `product_id`, `quantity`, `unit_price`, `subtotal`)
        * `total_amount` (Decimal o Float)
        * `status` (String, Enum: 'draft', 'pending_approval', 'approved', 'rejected', 'completed', 'cancelled')
        * `order_date` (DateTime)
        * `delivery_date` (DateTime, opcional)
        * `notes` (String, opcional)
        * `created_by` (String, User ID, para auditoría)
        * `created_at` (DateTime, timestamp de creación)
        * `updated_at` (DateTime, timestamp de última actualización)
    * Utilizar `MongoEngine` para la definición del esquema y su mapeo.

2.  **Lógica de Negocio (Controladores):**
    * Crear un archivo `backend/procurement_service/controllers/order_controller.py`.
    * Implementar las funciones de lógica de negocio para:
        * `create_order(data)`: Validar datos, guardar nueva orden, generar ID único.
        * `get_all_orders()`: Recuperar todas las órdenes de compra (posiblemente con paginación/filtros).
        * `get_order_by_id(order_id)`: Recuperar una orden específica.
        * `update_order(order_id, data)`: Actualizar campos específicos de una orden (parcialmente).
        * `delete_order(order_id)`: Eliminar una orden (considerar borrado lógico).
        * `approve_order(order_id, approver_id)`: Lógica para cambiar el estado a 'approved', registrando quién aprobó.

3.  **Definición de Endpoints API (Rutas):**
    * Crear un archivo `backend/procurement_service/routes/order_routes.py`.
    * Definir los siguientes endpoints RESTful usando Flask (o FastAPI si se opta por él para este servicio):
        * `POST /api/v1/procurement/orders`: Crear una nueva orden.
        * `GET /api/v1/procurement/orders`: Obtener todas las órdenes.
        * `GET /api/v1/procurement/orders/{order_id}`: Obtener una orden por ID.
        * `PUT /api/v1/procurement/orders/{order_id}`: Actualizar una orden existente.
        * `DELETE /api/v1/procurement/orders/{order_id}`: Eliminar una orden.
        * `POST /api/v1/procurement/orders/{order_id}/approve`: Aprobar una orden.

4.  **Seguridad y RBAC (Control de Acceso Basado en Roles):**
    * Todos los endpoints deben ser protegidos con autenticación JWT, utilizando el middleware centralizado en `shared/auth_middleware.py`.
    * Asignar los siguientes privilegios específicos para cada endpoint (utilizar decoradores o lógica en el controlador):
        * `POST /api/v1/procurement/orders`: Requiere `procurement:create_order`
        * `GET /api/v1/procurement/orders`: Requiere `procurement:read_orders`
        * `GET /api/v1/procurement/orders/{order_id}`: Requiere `procurement:read_orders`
        * `PUT /api/v1/procurement/orders/{order_id}`: Requiere `procurement:update_orders`
        * `DELETE /api/v1/procurement/orders/{order_id}`: Requiere `procurement:delete_orders`
        * `POST /api/v1/procurement/orders/{order_id}/approve`: Requiere `procurement:approve_orders`
    * El JWT (JSON Web Token) contendrá los roles y/o privilegios del usuario, que el middleware debe verificar.

5.  **Validación de Entradas:**
    * Implementar una validación robusta para todas las solicitudes entrantes a los endpoints del `procurement_service`.
    * Asegurarse de que los tipos de datos sean correctos, los campos obligatorios estén presentes, y los rangos/valores sean válidos.

6.  **Pruebas Exhaustivas:**
    * Escribir pruebas unitarias e de integración en `backend/procurement_service/tests/` para cubrir la funcionalidad CRUD completa y la lógica de aprobación.
    * Asegurar que las pruebas cubran casos de éxito, errores de validación, errores de autenticación/autorización, y manejo de casos límite.
    * El objetivo es alcanzar una cobertura de código superior al 80% para este nuevo módulo.

7.  **Calidad de Código y Formateo:**
    * Asegurarse de que todo el código generado pase el linting (`flake8`, `mypy`) y se formatee automáticamente con `black`.

8.  **Actualización de Dependencias:**
    * Actualizar el archivo `backend/procurement_service/requirements.txt` con cualquier nueva librería Python que se utilice (ej. `MongoEngine`).

9.  **Consideraciones de Integración Futuras (No Implementar Ahora):**
    * Notar cómo las órdenes de compra podrían afectar el `inventory_service` (entradas de stock) o el `accounting_service` (cuentas por pagar) en flujos de negocio futuros. Esto servirá para futuras tareas.

**Verificación Final:**
El `diff` debe incluir:
* Los nuevos archivos (`order_model.py`, `order_controller.py`, `order_routes.py`) y sus respectivos contenidos.
* Actualizaciones en `requirements.txt`.
* Nuevos archivos de prueba en `tests/`.
* Confirmación de que `pytest`, `flake8`, `mypy`, y `black` se ejecutaron exitosamente.
```
