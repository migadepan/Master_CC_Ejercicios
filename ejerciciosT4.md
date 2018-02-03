# Ejercicios Tema 4

## Ejercicio 1: Instalar una máquina virtual Debian usando Vagrant y conectar con ella.

He seleccionado una imagen del enlace [Vagrant box](http://www.vagrantbox.es/) y utilizando el comando vagrant box add enlace se realiza la instalación.

![capturaej1](https://user-images.githubusercontent.com/6852023/35772030-4e65d1be-0937-11e8-8d0b-df31ad152651.png)

Para conectar utilizamos vagrant up después de iniciar la máquina con vagrant init

![capturaej1-1](https://user-images.githubusercontent.com/6852023/35772052-bc19b9be-0937-11e8-9d36-caf4e772d78e.png)

Para la conexión solo es necesario utilizar 
```
vagrant ssh
```
## Ejercicio 3: Crear un script para provisionar de forma básica una máquina
virtual para el proyecto que se esté llevando a cabo en la asignatura. Voy a provisionar la máquina Ubuntu del Tema 3.

```
Vagrant.configure("2") do |config|
	config.vm.box = "ubuntu"
	config.ssh.insert_key = false
	config.vm.provision "shell",
		inline: "sudo apt-get install -y python3-dev"
		inline: "sudo apt-get install redis-server"
  end
end
```

## Ejercicio 4: Configurar tu máquina virtual usando `vagrant` con el provisionador
ansible

Para realizar la provisión con ansible, solo es necesario sustituir el código de provisión shell por el de ansible en el VagrantFile, llevándolo a utilizar nuestra receta.

```
Vagrant.configure("2") do |config|
	config.vm.box = "ubuntu"
	config.ssh.insert_key = false
	config.vm.provision "ansible" do |ansible|
		ansible.playbook = "recipe.yml"
  end
end
```