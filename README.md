# Aplicación práctica Senasoft (2) #

En el siguiente documento se establecerá información relacionada a la API  y documentación del sistema a desarrollar, indicando rutas, códigos de respuesta, estados, cuerpos de respuesta, etc.

## Rutas de la API ##

Se especifican las rutas de la API, el recuerpo de respuesta y los códigos de estado, además se modela el objeto response

### /api/ => Recursos generales ###

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

        },
        "reponse": {
            "statusCode": 1xx | 2xx | 3xx | 4xx | 5xx,
            "message": "Any message"
        }
    }
```

### /api/schedules => Recursos de los horarios disponibles ###

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

### /api/products => Recursos de productos/combos disponibles ###

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

### /api/invoicing => Recursos de facturación ###

- POST /api/invoicing

```json
    {
        "body": {

        },
        "response": {
            "statusCode": 1xx | 2xx | 3xx | 4xx | 5xx,
            "message": "Any message"
        }
    }
```
