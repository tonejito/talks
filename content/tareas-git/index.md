---
title: Tareas en GIT
subtitle: add, commit, push, repeat.
author:
- Andrés Hernández - `tonejito`
date: 21 de Abril de 2023
affiliation:
- http://localhost/
abstract: |
  ¿Por qué 🤬 pido a los alumnos que entreguen las tareas en GIT?
description: |
  ¿Por qué 🤬 pido a los alumnos que entreguen las tareas en GIT?
copyright: CC-BY-SA-4.0
ROBOTS:	NOINDEX, UNFOLLOW
baseheaderlevel: 2
lang: es-MX
---

<!--	= ^ . ^ =	-->

### ¿Por qué 🤬 pido a los alumnos que entreguen las tareas en `git`?	{ .slide: data-visibility="hidden,uncounted" }

&nbsp;

Andrés Hernández - `tonejito`

&nbsp;

:::::::::::::: {.columns}
::: {.column width="33%"}

[![][cc-by-sa-img-big]][cc-by-sa-page]

:::
::: {.column width="33%"}

![][🐰]

:::
::: {.column width="33%"}

[![][github-badge]][github-repo]

:::
::::::::::::::

<!--
This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License:

* <http://creativecommons.org/licenses/by-sa/4.0/>
-->

::: notes
- ¿Por qué 🤬 pido a los alumnos que entreguen las tareas en `git`?
:::

[🐰]: https://gravatar.com/avatar/4cc702785290b4934c531c56f6061e5e.png "🐰"
[cc-by-sa-page]: http://creativecommons.org/licenses/by-sa/4.0/ "CC-BY-SA-4.0"
[cc-by-sa-img-big]: img/cc-by-sa.png "Creative Commons Attribution ShareAlike 4.0 International License"
[cc-by-sa-img-big-ext]: https://i.creativecommons.org/l/by-sa/4.0/88x31.png "Creative Commons Attribution ShareAlike 4.0 International License"
[cc-by-sa-img-small]: img/cc-by-sa-small.png "Creative Commons Attribution ShareAlike 4.0 International License"
[cc-by-sa-img-small-ext]: https://i.creativecommons.org/l/by-sa/4.0/80x15.png "Creative Commons Attribution ShareAlike 4.0 International License"
[github-repo]: https://github.com/tonejito/conferencias
[github-badge]: https://github.com/tonejito/conferencias/actions/workflows/github-pages.yaml/badge.svg?branch=main

--------------------------------------------------------------------------------

### Contexto

- Doy clases a los alumnos de **Ciencias de la Computación** en la **Facultad de Ciencias**

- Imparto materias de tronco común	😴

    - Sistemas Operativos
    - Redes de Computadoras

- La gran mayoría de mis alumnos _quieren ser programadores_ 💻 y no les interesan _tanto_ mis materias

::: notes
:::

--------------------------------------------------------------------------------

### Contexto

- _Allá afuera_ piden <u>mucho más</u> que algoritmos y estructuras de datos

    - Control de versiones
    - Revisión de código (_peer review_)
    - Estándares de código
    - **Documentación**
    - **Automatización** (CI/CD)
    - <span class="red">Trabajo en equipo</span> y otros _soft-skills_

::: notes
:::

--------------------------------------------------------------------------------

### Contexto

- Siempre dejamos la documentación "para después" y nunca se escribe
- La documentación no es entregar un documento <u>**sin texto**</u> que sólo tenga capturas de pantalla
- Los alumnos no están familiarizados con las revisiones de código
    - Tampoco con escribir documentación
    - Y aún así quieren ser programadores \
      _full-snack_	🥨

::: notes
- No estamos acostumbrados a escribir la documentación
:::

--------------------------------------------------------------------------------

# ¿Y por qué no entregamos las tareas en `%s`?

--------------------------------------------------------------------------------

### Entrega de tareas vía correo electrónico

<!--  -->
<img alt="Thunderbird" src="img/1_1-thunderbird.png" class="icon" />
<img alt="Gmail" src="img/1_1-gmail.svg" class="icon" />
<img alt="Apple Mail" src="img/1_1-apple-mail.png" class="icon" />
<img alt="Outlook" src="img/1_1-outlook.svg" class="icon" />
<!--  -->

--------------------------------------------------------------------------------

### Entrega de tareas vía correo electrónico

- Formato libre (_y rebelde_)
- No hay control sobre _quién envía un correo_, _a quién va dirigido_ y el contenido del mensaje
    - Asunto, Para, CC, BCC
    - Responder vs Responder a todos
        - (_excepto a los que no_)
    - _En el archivo adjunto…_
        - (pero el correo no tiene archivo adjunto)

::: notes
:::

--------------------------------------------------------------------------------

### Entrega de tareas vía correo electrónico

| Campo        | Valor
|:------------:|:------------:|
| Remitente    | `nombre_generico123@example.com`
| Destinatario | `profesor@correo.edu`
| Asunto       | _(sin asunto)_
| Mensaje      | "Entrego mi práctica"
| Adjunto      | _(sin archivo adjunto)_

::: notes
:::

--------------------------------------------------------------------------------

### Entrega de tareas vía correo electrónico

- ¿«Quién» entrega?
- ¿«Qué» está entregando?
- ¿«Cuándo» lo mandó?
- ¿Mandó archivo adjunto?
- ¿Es válida la entrega?
- ¿Entrega individual o en equipo? (CC, BCC)

::: notes
:::

--------------------------------------------------------------------------------

### Entrega de tareas vía correo electrónico

- ¿Qué pasa si hay correcciones?
- ¿Qué pasa si no mandó los archivos adjuntos?
- ¿Cuánto pesan los archivos adjuntos?
- ¿Adjuntas nuevos archivos cada vez que hay correcciones?

::: notes
:::

--------------------------------------------------------------------------------

### Entrega de tareas vía correo electrónico

- ¿Qué pasa si enviaste tu correo con un adjunto _"fake"_ para cumplir con la fecha de entrega?
    - Y "lo arreglas después" enviando otro correo "con el adjunto _corregido_"

- ¿Qué pasa si el correo electrónico «nunca llega»?
    - _Profe, el servidor de correo se comió mi tarea_

::: notes
:::

--------------------------------------------------------------------------------

### Entrega de tareas vía correo electrónico

Nombre de los archivos : Expectativa 🧐 🤓

- `tarea-1-AndresHernandez-prog.c`
- `tarea1-ALHB-programa-1.c`
- `AndresHdz-tarea-1.c`
- `programa-AndresH-tarea-1.c`

::: notes
:::

--------------------------------------------------------------------------------

### Entrega de tareas vía correo electrónico

Nombre de los archivos : Realidad 🤨 🤦 🔥

- `tarea/prog.c`
- `modificado2/prog.c`
- `vers-28sep/prog.c`
- `Proyecto_2023-1_(Andres)/prog1.c`
    - 🚩 Estamos en el semestre `2023-2` 🚩

::: notes
:::

--------------------------------------------------------------------------------

## Entrega de tareas en una carpeta compartida

&nbsp;

<!--  -->
<img alt="Dropbox" src="img/1_2-dropbox.svg" class="icon" />
<img alt="GoogleDrive" src="img/1_2-google_drive.png" class="icon" />
<img alt="Evernote" src="img/1_2-evernote.svg" class="icon" />
<img alt="box.net" src="img/1_2-box.svg" class="icon" />
<img alt="OneDrive" src="img/1_2-onedrive.svg" class="icon" />
<img alt="ownCloud" src="img/1_2-owncloud.svg" class="icon" />
<!--  -->

--------------------------------------------------------------------------------

### Entrega de tareas en una carpeta compartida

- Pones tu archivo en un _"lugar externo"_ y mandas la liga para que se pueda descargar la tarea desde tu _"servidor local"_ 💻 o en _"la nube"_ ☁️

- No necesitas mandar nuevos archivos adjuntos si corriges tu tarea 😎
    - Incluso puedes corregir tu tarea después de la fecha límite de entrega

::: notes
:::

--------------------------------------------------------------------------------

### Entrega de tareas en una carpeta compartida

- ¿Qué pasa si _"ese otro lado"_ donde almacenas tu tarea queda fuera de línea?
    - <span class="yellow">_Mamá, ¡Te dije que no apagaras la laptop!_. <br/> _Ahora el profe ya no puede bajar mi tarea_.</span>
        - 💻 <span class="red">I'm in danger</span> 🔥 <!-- ⟦_chuckles_⟧ -->

- ¿Qué pasa si te suspenden la cuenta de _"ese otro lado"_ y nadie puede acceder a los archivos que tengas allá? ⛈️ ⛔

::: notes
:::

--------------------------------------------------------------------------------

### Entrega de tareas en una _plataforma_

- No hay una interfaz de línea de comandos para las plataformas

    - Moodle
    - Google Classroom
    - etc.

- Eso complica la automatización de las revisiones

::: notes
:::

--------------------------------------------------------------------------------

<div class="caption">Queremos _Google Classroom_</div>
<div class="margin-zero">
  <p class="margin-zero">
    <img class="caption margin-zero" src="img/rick-harrison.jpg" title="Lo mejor que puedo hacer es una página con notas" data-lazy-loaded="">
  </p>
</div>
<div class="caption">Lo mejor que puedo hacer es una página con notas</div>

::: notes
- Y me estoy arriesgando
:::

--------------------------------------------------------------------------------

# ¿Existe otra solución?

&nbsp;

⌗SpoilerAlert: Si

::: notes
:::

--------------------------------------------------------------------------------

## `git`

- <u>Software libre y de código abierto</u> para control de versiones distribuido
- Es utilizado por proyectos «muy grandes» con «muchos» desarrolladores
    - Kernel Linux, GNU coreutils, Kubernetes, etc.
- <https://git-scm.com/>

![](img/2-git.svg "git")

::: notes
- <https://git-scm.com/doc>
:::

--------------------------------------------------------------------------------

### Características de git

+ Velocidad
+ Diseño simple
+ Soporte para múltiples ramas
+ Enfoque distribuido
+ Capacidad de alojar grandes proyectos
+ Varios desarrolladores pueden trabajar en el mismo proyecto
+ Incluye verificación de integridad en los archivos

::: notes
:::

--------------------------------------------------------------------------------

## Entrega de tareas en un repositorio de git

&nbsp;

<span class="icon-text">📓 📝 📋 ⇒ </span><img alt="GIT" src="img/2-git.svg" class="icon" />

--------------------------------------------------------------------------------

### Hospedaje de repositorios

:::::::::::::: {.columns}
::: {.column width="33%"}

_Self-hosted_

- `localhost`
    - `cgit`
    - HTTP(S)
    - SSH
- GitLab CE

:::
::: {.column width="33%"}

_Git as a Service_

- SourceForge
- GitHub
- GitLab
- BitBucket
- LaunchPad
- CodeBerg

:::
::: {.column width="34%"}

Cloud

- AWS CodeCommit
- GCP Source Repositories
- Azure DevOps

:::
::::::::::::::

[git-hosting]: https://git-scm.com/book/en/v2/Git-on-the-Server-Third-Party-Hosted-Options
[git-providers-comparison]: https://www.git-tower.com/blog/git-hosting-services-compared/
[git-essentials]: https://www.ibm.com/training/badge/git-and-github-essentials

::: notes
:::

--------------------------------------------------------------------------------

### Entrega de actividades en git

- Elegí **GitLab** para que los alumnos entreguen sus actividades
- ¿Por qué no `%s`?
    - Porque **GitLab** puede ser utilizado en la nube y también puedes instalar una instancia local si quieres

::: notes
- Y además porque tengo muchas cosas en GitHub y no quiero que se mezclen con lo que hago para las clases
:::

--------------------------------------------------------------------------------

### Evolución de las entregas

- Repositorio central compartido
- Publicación de las entregas en una página web
- Repositorios individuales en un "subgrupo"
- Repositorios _fork_ individuales
    - Una rama de trabajo por cada entrega
    - Los alumnos conservan copia de sus actividades
- Verificación de las entregas
    - De manera local y en el servidor

::: notes
:::

--------------------------------------------------------------------------------

### Repositorio central compartido

- Hay que darle acceso a todos al repositorio
- Cada quién tiene "su carpeta" o "su rama" y sube ahí sus entregas
    - <span class="orange">¿Qué pasa si borras las tareas de alguién que no te cae bien?</span>
- <span class="red">¿Cómo se resuelven los conflictos en el repositorio?</span>
- <span class="yellow">¿Los alumnos tienen copia de sus actividades entregadas?</span>

::: notes
- <span class="cyan">¿Qué pasa con las altas y bajas del curso?</span>
:::

--------------------------------------------------------------------------------

### Repositorios individuales en un "subgrupo"

- Hay que darle acceso a todos al grupo
- Cada quién sube sus tareas "como quiere", "donde quiere" y "cuando quiere"
- ¿De qué manera sé que ya entregaron sus actividades?
- Ahora hay que monitorear manualmente «`N`» repositorios
    - Se complica bastante hacer correcciones

::: notes
- <span class="cyan">¿Qué pasa con las altas y bajas del curso?</span>
- O crear un repositorio para cada quién dentro del grupo
- <span class="yellow">¿Los alumnos tienen copia de sus actividades entregadas cuando se acaba el semestre?</span>
:::

--------------------------------------------------------------------------------

### Repositorios _fork_ individuales	🔱

- Hay un solo repositorio central de actividades
- Cada alumno hace una copia del repositorio (_fork_) asociado a su cuenta
- Los alumnos suben sus tareas a su propio repositorio (_fork_)
- Las actividades se entregan vía _merge request_ al repositorio central

::: notes
- Ya no hay que manejar permisos ni crear repositorios a mano
- Los alumnos tienen copia de sus actividades entregadas cuando se acaba el semestre
:::

--------------------------------------------------------------------------------

### Ramas de trabajo en el repositorio

- Hay una "rama base" para todas las entregas que da un entorno de trabajo "limpio"
- Los alumnos utilizan esa "rama base" para crear la rama de trabajo para su actividad
    - `tarea-1`, `practica-2`, `proyecto-3`, etc.
- Los alumnos envían su actividad a una rama con el mismo nombre cuando crean su _merge request_

::: notes
:::

--------------------------------------------------------------------------------

### Entrega de actividades con _merge requests_

- Los alumnos envían sus actividades en un _merge request_ desde su repositorio _fork_ al repositorio central

    - Se puede hacer revisión de código para pedir correcciones
    - Existe un historial del _merge request_
    - Notificaciones por correo electrónico

::: notes
:::

--------------------------------------------------------------------------------

### Revisión de código

- Se verifica la entrega y se piden correcciones

    - Nombre de archivos y carpetas
    - Formato de archivos
    - No deben existir conflictos
    - El _pipeline_ debe ser exitoso

- Los alumnos corrigen, envían sus cambios al servidor, se actualiza _merge request_ y eventualmente se acepta la entrega

::: notes
:::

--------------------------------------------------------------------------------

### Manejo de conflictos

- Conflictos en el repositorio _fork_	❗
    - Cada alumno o equipo lo soluciona por separado sin afectar a los demás

- Conflictos en el _merge request_	❌
    - Se piden correcciones al alumno o equipo
    - No se acepta la entrega hasta que se solucionen	⚠️

::: notes
:::

--------------------------------------------------------------------------------

### `pre-commit`

- Verifica errores comunes y repara los archivos antes de versionarlos

- Se instala en el repositorio y se ejecuta cada vez que se hace `commit`

    - Requiere que los alumnos lo instalen en su copia local de trabajo

- Se puede ejecutar pre-commit desde el _pipeline_ de CI/CD en GitLab

::: notes
- Comúnmente se les olvida instalarlo y/o ejecutarlo
:::

--------------------------------------------------------------------------------

### GitLab Pages

- Permite publicar un sitio web hospedado en GitLab

    - `NOMBRE.gitlab.io/repositorio`
    - `NOMBRE.gitlab.io/grupo/repositorio`
    - `NOMBRE.gitlab.io/grupo/subgrupo/repositorio`

- Se puede versionar diréctamente el código HTML, o bien convertirlo en un _pipeline_ de CI/CD

[gitlab-pages]: https://docs.gitlab.com/ee/user/project/pages/

::: notes
- GitHub:
    - `NOMBRE.github.io/repositorio`
:::

--------------------------------------------------------------------------------

### GitLab Pages

- Decidí que utilizaramos `mkdocs` porque me gusta utilizar Markdown 📝 y Python 🐍

- El contenido del sitio se convierte utilizando un _pipeline_ de CI/CD ⚙️

    - La conversión se hace utilizando un `Makefile` que invoca `mkdocs` 🔧 <!-- 🛠️ -->

- Las entregas todas las actividades se publican en un sitio web 🌎 <!-- 🌐 -->

::: notes
- He desarrollado varias configuraciones interesantes de `mkdocs` durante varios semestres
- Se utiliza un contenedor de Debian/Python para ejecutar todo
:::

--------------------------------------------------------------------------------

### _Pipeline_ de CI/CD

- **CI/CD**: Continuous Integration / Continuous Deployment

- Automatización para ejecutar acciones "del lado del servidor" después de un evento (`push`, etc.)

- Configuración <u>específica</u> para GitLab:

    - El _pipeline_ define las acciones (_jobs_) y los estados (_stages_) que contienen las acciones a ejecutar para reaccionar a un evento

::: notes
- GitLab
    - `.gitlab-ci.yml`
- GitHub
    - `.github/workflows/github-pages.yaml`
:::

--------------------------------------------------------------------------------

### _Pipeline_ de CI/CD

- Convierte el sitio de Markdown a HTML utilizando `mkdocs`

- Se pueden ejecutar verificaciones adicionales

    - `pre-commit` del lado del servidor

- Todas las acciones se invocan utilizando un `Makefile` y un _script_ de `shell`

::: notes
- Utiliza el contenedor de Python para instalar las dependencias (`pre-commit`, `mkdocs`, etc.)
:::

--------------------------------------------------------------------------------

### _Pipeline_ de CI/CD

- **Idealmente** se ejecuta cada vez que los alumnos hacen `push` al servidor

- [Por desgracia ya no es así porque abusaron del servicio de CI/CD de GitLab][gitlab-prevent-crypto-mining-abuse]

- Cada _pipeline_ se ejecuta en un _runner_ de GitLab (compartido o propio)

- Muchos de los alumnos no pueden ejecutar el _pipeline_

[workflow-local]: https://redes-ciencias-unam.gitlab.io/workflow/agregar-contenido/#probar-los-cambios-localmente
[gitlab-prevent-crypto-mining-abuse]: https://about.gitlab.com/blog/2021/05/17/prevent-crypto-mining-abuse/

::: notes
:::

--------------------------------------------------------------------------------

### GitLab Runner

- Es una aplicación que se conecta a GitLab para ejecutar los trabajos de CI/CD
- Antes GitLab daba acceso a los <u>_runners_ compartidos</u>, pero ya no lo hace porque [abusaron del servicio][gitlab-prevent-crypto-mining-abuse] 🔥
- Los usuarios pueden configurar <u>_runners_ propios</u> (_self-managed_) para correr sus _pipelines_

::: notes
:::

--------------------------------------------------------------------------------

### GitLab Runner

:::::::::::::: {.columns}
::: {.column width="50%"}

Infraestructura

- ¿Cuáles son los requermientos del sistema?
- ¿De dónde se descarga?
- ¿Cómo se configura `gitlab-runner`?

:::
::: {.column width="50%"}

Configuración

- ¿Cómo se configura GitLab Runner?
- ¿Cada quién tiene que utilizar el suyo?
- ¿Se puede reutilizar en otros proyectos?

:::
::::::::::::::

::: notes
:::

--------------------------------------------------------------------------------

### GitLab Runner

:::::::::::::: {.columns}
::: {.column width="50%"}

**Project Runner** 🔵 <!-- 🏠 -->

- Está asociado a un proyecto
- <u>Puede ser compartido con otros proyectos</u>
- Incluso de otros usuarios 🎉

:::
::: {.column width="50%"}

**Group Runner** 🫐 <!-- 🏘️ -->

- Está asociado a un grupo o subgrupo
- <u>Se hereda la configuración</u>
- No puede ser compartido con otros proyectos

:::
::::::::::::::

::: notes
:::

--------------------------------------------------------------------------------

### GitLab Runner

- Hay varias maneras de ejecutar `gitlab-runner`

    - Shell, SSH, Docker, Kubernetes

- Terminé ejecutando mis _runners_ con Docker 🐳 <!-- 🐋 -->

:::::::::::::: {.columns}
::: {.column width="50%"}

**Project Runner** 🔵 <!-- 🏠 -->

Para el sitio de la clase

:::
::: {.column width="50%"}

**Group Runner** 🫐 <!-- 🏘️ -->

Para los alumnos

:::
::::::::::::::

[gitlab-runner-executors]: https://docs.gitlab.com/runner/executors/

::: notes
- [Executors][gitlab-runner-executors]
    - SSH, Shell, VirtualBox, Docker, Kubernetes
:::

--------------------------------------------------------------------------------

### Configuración de GitLab Runner

- Los <u>_project runners_</u> se autentican con GitLab utilizando un tóken

- Necesitas permisos de _maintainer_ para configurar los _runners_ en un repositorio

- Puedes registrar un _project runner_ en un repositorio y después habilitarlo en otros

    - Incluso en repositorios de otros usuarios 🎉

::: notes
- Al finalizar este semestre voy a desactivar los _runners_ en los repositorios de los alumnos

- El siguiente semestre configuraré otros runners
:::

--------------------------------------------------------------------------------

<div class="caption">&nbsp;<br/>&nbsp;</div>
<div class="margin-zero">
  <p class="margin-zero">
    <img class="caption margin-zero" src="img/pool-boy.jpg" title="Yo también quiero vivir ese sueño señor Pool" data-lazy-loaded="">
  </p>
</div>
<div class="caption">Yo también quiero vivir ese sueño señor Pool</div>

--------------------------------------------------------------------------------

### Evolución

###### Antes	🖋️ 🤔

- El perro se comió mi tarea (física)	🐶 📁 📝
- El perro se comió mi memoria USB	🐶 💾 💿
- El servidor de correo se comió mi tarea	✉️

###### Ahora	💻 😅

- El _repo_ local de `git` se comió mi tarea	👩‍💻 ❌
- El servidor de `git` se comió mi tarea	🌎 🚸
- El merge request se comió mi tarea	🧑‍🏫 ⛔

::: notes
:::

--------------------------------------------------------------------------------

### Resumen

- Los alumnos hacen _fork_ del repositorio central	<!-- 🔱 -->
- Los alumnos crean una rama para su actividad
- Los alumnos entregan con un _merge request_
- Se hace revisión de código en cada entrega
- _Pipeline_ de CI/CD: Ejecuta `pre-commit` y `mkdocs`
- GitLab _runner_ compartido con los alumnos
- Las entregas se publican en un sitio web

::: notes
:::

--------------------------------------------------------------------------------

### Ventajas para los alumnos

- Aprenden a trabajar con `git`
- Se acostumbran al manejo de ramas
- Conocen cómo hacer un _merge request_
- Se familiarizan con las revisiones de código
- Pueden revisar la configuración del _pipeline_
- No necesitan ejecutar su propio GitLab _runner_
- Ven sus entregas en un sitio web

::: notes
:::

--------------------------------------------------------------------------------

### Ventajas para el profesor

- Formato estándar de contenido (Markdown)
- Estructura definida para archivos y carpetas
- Una rama por actividad entregada
- Un solo mecanismo de revisión (_merge request_)
- Historial de cambios en el repositorio
- Correcciones puntuales en la revisión de código
- `pre-commit` reduce los problemas comunes
- El _pipeline_ detecta problemas en las entregas

::: notes
:::

--------------------------------------------------------------------------------

### Siguientes pasos

- Uso de `mkdocs serve`
- Detección de conflictos utilizando el _pipeline_
- Instrucciones para resolución de conflictos
- Automatización de configuración de _runners_
    - Esto se puede hacer con Ansible
- Instrucciones para W＊nd＊ws y CygWin/WSL 😞
- Uso de `glab`, [la herramienta CLI de GitLab][glab-docs]

[glab-docs]: https://docs.gitlab.com/ee/integration/glab/
[glab-blog]: https://about.gitlab.com/blog/2022/12/07/introducing-the-gitlab-cli/

::: notes
- No todos tienen un sistema operativo _de verdad_
:::

--------------------------------------------------------------------------------

### Curso actual: Redes

- <https://Redes-Ciencias-UNAM.gitlab.io/>
- <https://gitlab.com/Redes-Ciencias-UNAM/>

:::::::::::::: {.columns}
::: {.column width="50%"}

**GitLab** 🔧 <!-- 🛠️ -->

- [Proyecto](https://gitlab.com/Redes-Ciencias-UNAM/)
- [Repositorio del sitio](https://gitlab.com/Redes-Ciencias-UNAM/redes-ciencias-unam.gitlab.io/)
- [Semestre 2023-2](https://gitlab.com/Redes-Ciencias-UNAM/2023-2)

:::
::: {.column width="50%"}

**Sitio web** 🌎 <!-- 🌐 -->

- [Sitio](https://Redes-Ciencias-UNAM.gitlab.io/)
- [Flujo de trabajo](https://Redes-Ciencias-UNAM.gitlab.io/workflow)
- [Notas](https://Redes-Ciencias-UNAM.gitlab.io/2023-2/notas)
- [Actividades entregadas](https://Redes-Ciencias-UNAM.gitlab.io/2023-2/tareas-redes)

:::
::::::::::::::

::: notes
:::

--------------------------------------------------------------------------------

# ¿Preguntas?

--------------------------------------------------------------------------------

## Gracias

&nbsp;

Andrés Hernández

`tonejito`

&nbsp;

:::::::::::::: {.columns}
::: {.column width="33%"}

[![][cc-by-sa-img-big]][cc-by-sa-page]

:::
::: {.column width="33%"}

![][🐰]

:::
::: {.column width="33%"}

[![][github-badge]][github-repo]

:::
::::::::::::::

<!--	----------------------------------------------------------------	-->
