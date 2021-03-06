# Ejercicios Contenedores

## Ejercicio 1
Instala LXC en tu versión de Linux favorita. Normalmente la versión en desarrollo, disponible tanto en GitHub como en el sitio web está bastante más avanzada; para evitar problemas sobre todo con las herramientas que vamos a ver más adelante, conviene que te instales la última versión y si es posible una igual o mayor a la 2.0.

Instalación de lxc2 

![captura de pantalla de 2018-01-17 10-07-43](https://user-images.githubusercontent.com/6852023/35050381-f9d660ec-fba2-11e7-89a3-38119be7032b.png)

## Ejercicio 2
Instalar una distro tal como Alpine y conectarse a ella usando el nombre de usuario y clave que indicará en su creación

![captura de pantalla de 2018-01-17 11-02-13](https://user-images.githubusercontent.com/6852023/35050590-7892c556-fba3-11e7-8fb2-f16328638e15.png)

## Ejercicio 4
Buscar alguna demo interesante de Docker y ejecutarla localmente, o en su defecto, ejecutar la imagen anterior y ver cómo funciona y los procesos que se llevan a cabo la primera vez que se ejecuta y las siguientes ocasiones.

Como podemos ver en las imagenes, en la primera ejecución se descarga e instala la imagen y en las siguientes solo se ejecuta el proceso, la imagen ya está instalada.

![captura de pantalla de 2018-01-17 15-49-41](https://user-images.githubusercontent.com/6852023/35050825-ff232d0e-fba3-11e7-872a-56fb7428349f.png)

![captura de pantalla de 2018-01-17 15-50-36](https://user-images.githubusercontent.com/6852023/35050847-0cf59098-fba4-11e7-9fba-f5cfb09e3c4f.png)

## Ejercicio 5
Comparar el tamaño de las imágenes de diferentes sistemas operativos base, Fedora, CentOS y Alpine, por ejemplo.

Hay grandes diferencias de tamaño entre unas y otras imagenes, de 4 a 252MB en éstos casos.

![captura de pantalla de 2018-01-17 15-59-47](https://user-images.githubusercontent.com/6852023/35050972-6883193a-fba4-11e7-81f2-4e99af533369.png)

## Ejercicio 6
Crear a partir del contenedor anterior una imagen persistente con commit.

A partir de contenedor Alpine actualizado, voy a crear una nueva imagen con el comando

```
sudo docker commit ec6af182147b alpineactualizada
```

![captura de pantalla de 2018-01-17 17-21-28](https://user-images.githubusercontent.com/6852023/35053598-e0184c12-fbaa-11e7-828a-2e8939b20889.png)


## Ejercicio 7
Examinar la estructura de capas que se forma al crear imágenes nuevas a partir de contenedores que se hayan estado ejecutando.

![captura de pantalla de 2018-01-17 17-38-47](https://user-images.githubusercontent.com/6852023/35054652-5dae05ac-fbad-11e7-9aab-d364cdcbd28e.png)

## Ejercicio 8

Crear un volumen y usarlo, por ejemplo, para escribir la salida de un programa determinado.

He creado el bm.sh dentro de /app y he seguido ese ejemplo para probarlo en 3 sistemas diferentes. Nos muestra en cada sistema la cantidad de archivos. 

![benchmarkenotrasdistro](https://user-images.githubusercontent.com/6852023/35059500-9c9fbe46-fbbb-11e7-912b-688db38f1420.png)

*He intentado probar con el microservicio de Perl del docente y no me ha funcionado la descarga. 

## Ejercicio 9 (En desarrollo)
Usar un miniframework REST para crear un servicio web y introducirlo en un contenedor, y componerlo con un cliente REST que sea el que finalmente se ejecuta y sirve como “frontend”.

Utilizando el microframework [Flask](http://flask.pocoo.org/) he desarrollado un pequeño servicio que muestra las vias de escalada. Aunque el sistema de dos contenedores conectados funciona, tengo un problema con el servicio del cliente que estoy solucionando. El servidor si funciona desde mi navegador.

![captura de pantalla de 2018-01-18 14-40-06](https://user-images.githubusercontent.com/6852023/35100939-eca987da-fc5d-11e7-8371-1c6cfcea72b4.png)


## Ejercicio 10
Reproducir los contenedores creados anteriormente usando un Dockerfile.

[Dockerfile-servidor](https://github.com/migadepan/Master_CC_Ejercicios/blob/master/composePrueba/server/Dockerfile)
[Dockerfile-cliente](https://github.com/migadepan/Master_CC_Ejercicios/blob/master/composePrueba/client/Dockerfile)