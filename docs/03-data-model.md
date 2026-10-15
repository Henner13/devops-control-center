# Modelo de datos inicial

## Role

Representa los permisos de un usuario.

### Campos

- id
- name
- description

### Ejemplo

```text
id: 1
name: Administrator
description: Full access
```

---

## User

Representa a una persona que utiliza la plataforma.

### Campos

- id
- username
- email
- password_hash
- role_id
- created_at
- updated_at

### Relación

Un usuario pertenece a un rol.

### Ejemplo

```text
id: 1
username: henner
email: henner@example.com
role_id: 1
```

---

## Server

Representa un servidor Linux gestionado por la plataforma.

### Campos

- id
- name
- hostname
- ip_address
- os_name
- os_version
- environment
- status
- description
- created_by
- created_at
- updated_at

### Relación

Un servidor es creado por un usuario.

### Ejemplo

```text
name: web-01
hostname: ubuntu-web-prod
ip_address: 192.168.1.100
environment: Production
status: Online
created_by: 1
```