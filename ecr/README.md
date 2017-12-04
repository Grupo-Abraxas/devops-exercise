## Información del contenedor en Docker Hub
URL: https://hub.docker.com/r/ecamarillor/dockerize_pyapp/

## Despliegue en un cluster con marathon
Para permitir la escalabilidad de los contenedores, sea aprovechada; antes de desplegar el servicio (marathon.json), instalaremos un balanceador de carga llamado marathon-lb. Dicho balanceador, permitirá que las instancias de Docker sean aprovechadas ante la posibilidad de alta demanda del servicio; permitiendo agregar más instancias en caso de ser requeridas o disminuir su número en caso de que la demanda sea mínima.

Cabe mencionar que derivados de los recursos técnicos con los que cuenta mi equipo de cómputo, adjunto el archivo de configuración del cluster con Vagrant (VagrantConfig.yaml).

### Instrucciones
1. Desde la línea de comandos hay que autenticarse con el siguiente comando:
`$ docker auth login`
Hay que seguir las instrucciones y pegar el token de autenticación.
> MacBook-Air-de-Eduardo:ecr eduardo.camarillo$ dcos auth login
> If your browser didn't open, please go to the following link:
> 
>     http://m1.dcos/login?redirect_uri=urn:ietf:wg:oauth:2.0:oob
> 
> Enter OpenID Connect ID Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1…
> Login successful!
2. Instalación del paquete marathon-lb:
`$ docs package install marathon-lb`
> By Deploying, you agree to the Terms and Conditions https://mesosphere.com/catalog-terms-conditions/#community-services
> We recommend at least 2 CPUs and 1GiB of RAM for each Marathon-LB instance.
> 
> *NOTE*: For additional ```Enterprise Edition``` DC/OS instructions, see https://docs.mesosphere.com/administration/id-and-access-mgt/service-auth/mlb-auth/
> Continue installing? [yes/no] yes
> Installing Marathon app for package [marathon-lb] version [1.11.1]
> Package is already installed
3. Despliegue del servicio (marathon.json):
`docs marathon app add marathon`
> Created deployment 7107bdbf-f534-454a-98bb-f294d171a170

Al finalizar el despliegue del servicio en http://m1.dcos/#/services/overview, es posible verificar que las 3 instancias iniciales que se crean de la imagen de docker (ecamarillor/dockerize_pyapp) son balanceadas desde el agente público por la dirección IP: 192.168.65.60

Bastará con acceder a dicha dirección IP desde un navegador: 
Por el puerto 80: http://192.168.65.60/
O el 10004: http://192.168.65.60:10004/

### Probar funcionamiento de APP con contador de peticiones POST
Basta ejecutar desde la línea de comandos el comando curl:
`$ curl -X POST http://192.168.65.60/`
o podría ser:
`$ curl -X POST http://192.168.65.60:10004/`

Una vez realizadas dichas peticiones al acceder desde el navegador a http://192.168.65.60/ veremos que nos aparece el número de peticiones POST que se han realizado además, la dirección IP del contenedor que nos está respondiendo la petición.
