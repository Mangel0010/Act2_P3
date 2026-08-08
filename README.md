# Práctica 3.2: Autenticación en API (OpenWeatherMap)

Este repositorio contiene la solución a la práctica **P3.2 - Autenticación en API (OpenWeatherMap)** de la asignatura **Automatización de Infraestructura Digital I**.

## ¿En qué consiste?

La actividad consistió en desarrollar un script en Python (`clima.py`) que consume la API REST de [OpenWeatherMap](https://openweathermap.org/) para obtener la temperatura actual y las condiciones meteorológicas de cualquier ciudad ingresada por el usuario.

### Características implementadas:
* **Autenticación mediante API Key**: Uso de la librería `python-dotenv` para cargar la clave de acceso de forma segura desde un archivo `.env`.
* **Seguridad en Control de Versiones**: Exclusión de credenciales privadas mediante `.gitignore` e inclusión de un archivo `.env.example` como plantilla pública.
* **Manejo de Errores HTTP**: Intercepción de códigos de estado como `404` (ciudad no encontrada), `401` (API Key inválida) y excepciones de red (`ConnectionError`, `Timeout`).
