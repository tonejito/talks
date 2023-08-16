---
title: Introducción a GNU/Linux
subtitle: "% ENV=var ./a.out 0<STDIN 1>STDOUT 2>STDERR"
author:
- Andrés Hernández - `tonejito`
date: Agosto 2023
affiliation:
- http://localhost/
abstract: |
  Introducción a GNU/Linux
description: |
  Introducción a GNU/Linux
copyright: CC-BY-SA-4.0
ROBOTS:	NOINDEX, UNFOLLOW
baseheaderlevel: 2
lang: es-MX
---

<!--	= ^ . ^ =	-->

### Historia de C y UNIX

:::::::::::::: {.columns}
::: {.column width="100%"}

<div class="container">
  <iframe class="responsive-iframe" src="https://www.youtube-nocookie.com/embed/t6faJyGB2aY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

:::
::::::::::::::

--------------------------------------------------------------------------------

### Historia de C y UNIX

- <https://eylenburg.github.io/os_familytree.htm>
- <https://upload.wikimedia.org/wikipedia/commons/5/50/Unix_history-simple.png>

--------------------------------------------------------------------------------

### Historia de **MINIX**

- **MINIX**: Andrew Tanenbaum
- <https://www.linuxjournal.com/article/10754>
- <https://minix3.org/>

--------------------------------------------------------------------------------

### Historia de Linux

- **Linux**: Linus Torvalds
- <https://upload.wikimedia.org/wikipedia/commons/1/1b/Linux_Distribution_Timeline.svg>
- <https://www.linuxjournal.com/article/10754>

--------------------------------------------------------------------------------

### Código abierto

- Compartir el _software_
- Acceso al código fuente
- Crear versiones modificadas
- Copy-Left

--------------------------------------------------------------------------------

### Filosofía Open Source

- Richard Stallman
- **FSF**: Free Software Foundation
- **GNU**: GNU is Not UNIX

--------------------------------------------------------------------------------

### Las cuatro libertades del software libre

_«Free as in **freedom**»_

0. Libertad para ejecutar el programa para cualquier propósito
1. Libertad para estudiar el funcionamiento del programa y modificarlo para cualquier propósito
    <!-- - Libre acceso al código fuente -->
2. Libertad de redistribuir copias del programa
3. Libertad de redistribuir versiones modificadas del programa
    <!-- - Libre acceso al código modificado -->

--------------------------------------------------------------------------------

### Licencias para _software_

- Licencia "de dominio público"
- <https://opensource.org/licenses/>
    - **BSD**
    - **MIT** License
    - **GNU GPL**: GNU General Public License
    - Apache Software License
    - Mozilla Public License
    - etc.

<!-- https://www.gnu.org/philosophy/categories.html -->

--------------------------------------------------------------------------------

### Licencias para contenido

- Licencia "de dominio público"
- Creative Commons: <https://choosealicense.org/>
    - CC-BY, CC-BY-SA, CC-BY-NC, CC-BY-NC-SA, CC-BY-ND
- **GNU FDL**: GNU Free Documentation License
- etc.

--------------------------------------------------------------------------------

# Línea de comandos

--------------------------------------------------------------------------------

### El intérprete de comandos `shell`

- Interfaz de línea de comandos
- No requiere interfaz gráfica
- Lee las entradas del usuario e invoca programas en el sistema operativo
- `sh`, `bash`, `csh`, `ksh`, `zsh`, etc.
- Prompt de usuario (`$`) y de súper-usuario (`#`)
- Argumentos de línea de comandos
- Variables de entorno

--------------------------------------------------------------------------------

### ¿Cómo obtener ayuda en Linux?

- `whoami`
- `which`, `whereis`
- `man`, `info`
- Opciónes `-h` y `--help`
- `find`, `locate`

--------------------------------------------------------------------------------

### FHS: Filesystem Hierarchy Standard

- **LSB**: Linux Standard Base
- Define el contenido de cada directorio
- Cada distribución puede tener directorios específicos

--------------------------------------------------------------------------------

### Administración de archivos

- Tipos de archivo
- Creación de directorios
- Creación de archivos
- Renombrar y mover archivos
- Renombrar y mover directorios
- Permisos en archivos

--------------------------------------------------------------------------------

### Administración de archivos

- Ligas simbólicas
- Ligas duras
