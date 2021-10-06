# Aplicación práctica Senasoft (2)

En el siguiente documento se establecerá información relacionada a la API  y documentación del sistema a desarrollar, indicando rutas, códigos de respuesta, estados, cuerpos de respuesta, etc.

## Rutas de la API

### /api/ => Información general ###

- GET /api/

```json
    {
        "response": {
            "statusCode": 1xx | 2xx | 3xx | 4xx | 5xx,
            "message": "Any message",
            "data": [
            ]
        }
    }
```

- POST /api/
  
```json
    {
        "body": {
        }
    }
```

### /api/schedules => Ofrece los horarios disponibles ###

- GET /api/schedules

```json
    {
        "response": {
            "statusCode": 1xx | 2xx | 3xx | 4xx | 5xx,
            "message": "Any message",
            "data": [
            ]
        }
    }
```

### /api/products => Ofrece los productos/combos disponibles ###

- GET /api/products

```json
    {
        "response": {
            "statusCode": 1xx | 2xx | 3xx | 4xx | 5xx,
            "message": "Any message",
            "data": [
            ]
        }
    }
```

### /api/invoicing => Generación de factura ###
