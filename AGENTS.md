Siemprende Mi Negocio — Configuración de Agentes Codex (GPT)

Documento maestro de especialización, activación y uso de agentes GPT para apoyar el desarrollo profesional del sistema "Siemprende Mi Negocio".

Versión: 1.0Fecha: 2025-05-24Autor: Kevin Javier García Pérez

📊 Propósito

Este documento define una arquitectura de agentes GPT especializados alineados al ecosistema modular de "Siemprende Mi Negocio". Cada agente tiene un ámbito de acción, criterios de calidad, reglas de seguridad y formato de salida específico.

Para estándares operativos, filosofía de calidad y ejemplos detallados de prompts, consulta el documento complementario: AGENTS_GUIDE.md

🧑‍💻 Agentes Definidos

🔹 Codex.DevArchitectAgent

Especialidad: Arquitectura de microservicios Python, MongoDB, patrones SOLID/KISS/DRY.

Entradas esperadas: nombre del servicio, funcionalidades, restricciones, sección del documento técnico.

Salidas:

Estructura de carpetas.

Dockerfile, requirements.txt, app.py, modelos, rutas, controladores, tests con pytest.

README con instrucciones de ejecución local y despliegue a GCP.

OpenAPI 3.1, docstrings, RBAC, validaciones estrictas.

🔹 Codex.FrontendPageAgent

Especialidad: Módulos React modulares (pages/XPage), internacionalización, UI accesible.

Salidas:

Carpeta pages/XPage/ con index.tsx, components/, hooks.ts, styles.ts.

Integración con AuthContext, ProtectedRoute, roles y permisos.

Cliente Axios correspondiente (services/xApi.ts).

Test con Jest + React Testing Library.

🔹 Codex.PostmanAgent

Especialidad: Generación y validación de colecciones Postman para microservicios.

Funciones:

Exporta endpoints con headers, bodies de prueba y JWT simulados.

Organiza por carpeta por microservicio (collections/Siemprende_*.json).

Puede generar scripts de prueba test.js (Pre-request, Tests).

🔹 Codex.CIEngineerAgent

Especialidad: Automatización CI/CD profesional con GitHub Actions y Cloud Run.

Salidas esperadas:

.github/workflows/ci-cd.yml por servicio.

Push a Google Artifact Registry.

Despliegue con deploy_to_cloudrun.sh y variables desde Secret Manager.

🔹 Codex.SmartSupportAgent

Especialidad: Asistente inteligente para:

Soporte técnico.

Capacitación RRHH interna.

Clasificación automática de clientes (GPT).

🔹 Codex.DocGenAgent

Especialidad: Generador de documentación automática (README, OpenAPI, diagramas).

Entradas: app.py, models.py, routes/, README.md, Postman.

Salidas:

docs/README_SERVICIO.md, docstrings, diagramas ASCII.

🔹 Codex.DataEngineerAgent

Especialidad: KPIs, dashboards React, alertas Prometheus.

Salidas:

ml_models/, dashboard_logic/, prometheus.yml, alert rules.

🔐 Seguridad

No incluir secretos en código. Usar os.getenv().

JWTs simulados para pruebas. Claves reales sólo desde Secret Manager.

HTTPS obligatorio en ejemplos.

📅 Estado de Activación

Agente

Estado

Observaciones

DevArchitectAgent

✅ Activo

Servicios backend listos para Cloud Run

FrontendPageAgent

✅ Activo

React con RBAC y i18n

PostmanAgent

✅ Activo

Exporta desde definiciones OpenAPI

CIEngineerAgent

✅ Activo

CI/CD multi-entorno con secrets

SmartSupportAgent

✅ Activo

Tutor y GPT contextual

DocGenAgent

✅ Activo

Documentación técnica auto-generada

DataEngineerAgent

✅ Activo

Dashboards + predicción + alertas

🔹 Ejemplos de Activación por Prompt

# Generar microservicio completo
/codex agent DevArchitectAgent generate microservice inventory_service

# Crear página frontend de CRM
/codex agent FrontendPageAgent create page CrmPage

# Crear colección Postman
/codex agent PostmanAgent export collection for billing_service

# Configurar CI/CD
/codex agent CIEngineerAgent init pipeline for chatbot_service

# Entrenar dashboard
/codex agent DataEngineerAgent setup dashboard predictive_kpis

📚 Referencias Base

Documento Técnico de Diseño Detallado v3.0

Documento Inicial v1.2

Guías Organizacionales Clave

Estructura del repo /siemprende/backend, /frontend, /docs, /scripts
