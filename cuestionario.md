## Evaluacion: Opcion multiple
Evaluación: Opción Múltiple.
¿Qué comando mueve cambios al staging area?git add.

¿Qué tipo de VCS es Git? Distribuido.

¿Quién creó Git y en qué año? Linus Torvalds, 2005.

¿Qué hace git fetch?  Descarga sin fusionar​.

Quieres deshacer un commit que ya subiste. ¿Qué usas? git revert​.

¿Qué es origin?  El nombre por defecto del remot.

¿Qué es un fork?  Una copia de un repositorio pero en tu cuenta y es independiente del original

Los marcadores <<<<<<<, =======, >>>>>>> indican…  diferencias y conflictos en lineas de archivos

## Evaluación: Preguntas Abiertas​
Explica con una analogía propia las tres áreas de Git. Estas escribiendo un libro, tienes el escritorio con lo que ya llevas (working directory), y por cada cambio lo dejas en una hoja con una nota (staging area). tienes distinas versiones del mismo pero con cambios cada una, puedes regresar a una version mejor.

¿Cuándo usarías git stash? cuando quiero guardar lo que llevo pero volver a una version funcional.

Encontraste un bug en una librería open source que usa tu sistema. Describe el flujo completo para enviar la corrección. se debe clonar, hacer una rama, solucionar errores o bugs y hacer un pull request y relacionarla con un issue si existe.

Un compañero subió el .env con la contraseña de producción. ¿Por qué es grave y qué pasos sigues? Son datos sensibles y no debes ser publicos, se debe añadir al .gitignore y quitarlo com git rm --cached

Un deploy de ayer rompió producción y el commit ya está en main. ¿Usas reset o revert? ¿Por qué?
git revert es la opcion correcta para remover el commit del commit anterior

## Ejercicio De Diagnóstico​
Ordena correctamente esta secuencia para publicar un cambio nuevo:​

''git pull​ ''
''git switch -c feat/x​''
​''editar archivos​​''
​''git add .​''
​''git commit -m "..."​​''
​''git push​''