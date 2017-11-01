# Abraxas DevOps Exercise

## Intro

Thank you for your interest and participation in our recruitment process for Engineer DevOps position, to continue with the process we ask you to take the following technical test to share your result with us.

If you have any questions or comments during the test, do not hesitate to contact us by email at reclutamiento@grupoabraxas.com

## Get your environment ready

You'll need a linux machine with the ability to run VMs.

1. Install [Docker](https://www.docker.com/)
2. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
3. Install [Vagrant](https://www.vagrantup.com/downloads.html)
4. Install [DC/OS Vagrant](https://github.com/dcos/dcos-vagrant)
5. Install [DC/OS CLI](https://github.com/dcos/dcos-cli)
6. Fork this repository, then clone it locally.
7. Start your DC/OS Vagrant cluster. If your local machine doesn't meet the recomended specs you can use this [VagrantConfig.yaml](VagrantConfig.yaml).
8. Configure your DC/OS CLI to work with your cluster.

**Important:** the infraestructure should work out of the box. There's no hidden part of the exersice in which you need to debug vagrant/virtualbox

## Ready for action?

Great!!
As a DevOps we need you to create a mechanism to deploy nanoservices. You'll be in charge of deploy, monitor, scaleapplications and promote the DevOps culture with the development team. But let's start by the begining, below you'll find the requirements for this test.

### Dockerize python services

Create a docker image for the [app.py](app.py) python service with all it's required dependencies installed and ready to rock.

### Deployment

Publish the created image on a public docker registry, like [docker hub](https://hub.docker.com/).  
Create a service configuration json file to deploy the service on your DC/OS cluster.

### Extra Points

- Improve the given python service so it maintains a counter of the amount of **POST** requests it served, and return it on **GET** requests.

## Deliverables

A Github pull request containing:

1. The Dockerfile(s) for the image(s).
2. The marathon file(s) for the service deployment(s).
3. Optionally the code for the improved version of the service.

## General Guidelines

Your code should be as simple as possible, yet well documented and robust.
Spend some time on designing your solution. Think about operational use cases from the real world. Few examples:

1. What happens if a service crashes?
2. How much effort will it take to create a new service? D.R.Y!

## Reference

- [Deploying a Docker-based Service](https://dcos.io/docs/1.10/deploying-services/creating-services/deploy-docker-app/)

