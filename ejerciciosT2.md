## Ejercicios Tema 2

Para la realización de los ejercicios se utilizará una maquina virtual con ubuntu 16.04 desde amazon web service.

### Ejercicio 1-Instalar chef-solo en la máquina virtual que vayamos a usar.

Utilizamos el siguiente comando para la instalación

```
curl -L https://www.opscode.com/chef/install.sh | bash
```

![capt1](https://user-images.githubusercontent.com/6852023/32617267-dc32bcfc-c574-11e7-9ef6-550f903b08b1.png)

Podemos mostrar la versión y de paso comprobamos que está correctamente instalado

![capt2](https://user-images.githubusercontent.com/6852023/32617334-0729865c-c575-11e7-8bed-8f16eaf915eb.png)

### Ejercicio 2-Crear una receta para instalar nginx, tu editor favorito y algún directorio y fichero que uses de forma habitual.

Se crea el direcitorio para la receta

```
mkdir -p chef/cookbooks/nginx/recipes
```
Se crea la receta en default.rb

![capt3](https://user-images.githubusercontent.com/6852023/32693894-38a2169e-c733-11e7-9d2c-eb4d44dffce0.png)

En el directorio chef se crea el fichero node.json con el siguiente contenido

![capt4](https://user-images.githubusercontent.com/6852023/32693902-7ef023ac-c733-11e7-9fbe-fe32e47262ca.png)

Se crea el fichero solo.rb con el siguiente contenido

![capt5](https://user-images.githubusercontent.com/6852023/32694056-f25ade2e-c736-11e7-9de8-d74dfdad9bde.png)

Y se ejecuta

![capt6](https://user-images.githubusercontent.com/6852023/32694061-0436c176-c737-11e7-9931-19835950e58d.png)

