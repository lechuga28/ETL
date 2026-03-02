# ETL
Proyecto ETL

## Elección de Base de Datos

Se eligió una base de datos relacional por las siguientes razones:

- Permite integridad referencial.
- Facilita consultas estructuradas mediante SQL.
- Garantiza consistencia en los datos transformados.
- Es adecuada para análisis estructurado posterior.

Las bases relacionales son ideales en procesos ETL donde se requiere limpieza, normalización y control de calidad de datos.

## Elección del Lenguaje y Formato

Se utilizó **Python** debido a:

- Su facilidad para manipulación de datos.
- Amplio ecosistema (pandas, SQLAlchemy, psycopg2, etc.).
- Sintaxis clara y rápida implementación.
- Integración sencilla con bases de datos.

El formato CSV fue utilizado como fuente de datos por:

- Ser un estándar ampliamente aceptado.
- Facilidad de lectura y procesamiento.
- Compatibilidad con múltiples herramientas.

## Transformaciones Realizadas

Durante el proceso ETL se realizaron las siguientes transformaciones:

- Limpieza de valores nulos.
- Conversión de tipos de datos.
- Normalización de campos.
- Eliminación de duplicados.
- Validación de integridad de registros.
- Estandarización de formatos (fechas, strings, etc.).

## Retos Encontrados

### Inconsistencia en los datos
Se encontraron valores nulos y formatos incorrectos.  
**Solución:** Se implementaron validaciones y limpieza previa con pandas.

### Problemas de codificación
Algunos archivos presentaban caracteres especiales.  
**Solución:** Se especificó encoding UTF-8 en la lectura de archivos.

### Manejo de errores en carga
Errores al insertar registros duplicados en la base de datos.  
**Solución:** Se implementaron validaciones previas y manejo de excepciones.

## Diagrama de Base de Datos

```mermaid
erDiagram

    CLIENTES {
        int id
        string nombre
        string email
        string telefono
    }

    TRANSACCIONES {
        int id
        int cliente_id
        float monto
        date fecha
    }