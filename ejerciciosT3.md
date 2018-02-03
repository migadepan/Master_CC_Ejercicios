# Ejercicios Tema 3

## Ejercicio 1: Crear una máquina virtual Ubuntu e instalar en ella un servidor nginx para poder acceder mediante web.

![capturaej1](https://user-images.githubusercontent.com/6852023/35771377-195979ea-092c-11e8-99b2-c37cd0127f8e.png)

Creo la máquina virtual, y me conecto por ssh a la ip que nos muestra la imagen.
Una vez dentro ejecuto 
```
sudo apt-get install nginx
```
La siguiente imagen nos muestra que el estado del servidor

![capturaej1-1](https://user-images.githubusercontent.com/6852023/35771394-58ff0074-092c-11e8-8cb8-f06b07dcbd0d.png)

## Ejercicio 2: Crear una instancia de una máquina virtual Debian y provisionarla usando alguna de las aplicaciones vistas en el tema sobre herramientas de aprovisionamiento

De la misma forma que la máquina anterior, creamos otra con Debian, agregamos la dirección pública en /etc/ansible/hosts y creamos la receta. En la siguiente imagen está la receta y el resultado de la ejecución.

![capturaej2-2](https://user-images.githubusercontent.com/6852023/35771840-5b7a45f0-0933-11e8-96e9-3e464ff038dd.png)