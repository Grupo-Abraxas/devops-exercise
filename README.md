# Abraxas DevOps Exercise

## Intro

Thank you for your interest and participation in our recruitment process for our DevOps Engineer position, to continue with the process we ask you to take the following technical test and share your result with us.

If you have any questions or comments during the test, do not hesitate to contact us by email at reclutamiento@grupoabraxas.com

## Get your environment ready

You'll need:

1. A Github account
2. A docker hub account
3. Access to a kubernetes cluster for testing purposes (It can be Minikube or any other public or private option)
4. Fork this repository, then clone it locally.

## Ready for action?

Great!!
As a DevOps we need you to create a mechanism to deploy nanoservices. You'll be in charge of deploy, monitor, scale applications and promote the DevOps culture with the development team. But let's start by the begining, below you'll find the requirements for this test.

### Dockerize services

Dockerize the given service at [app.py](app.py), including all it's required dependencies installed and ready to rock.

### CI/CD

Implement a Github Actions workflow to build and publish your docker image on [docker hub](https://hub.docker.com/).

### Deployment

Create a service configuration file to deploy the service on your kubernetes cluster and expose it to the world.

### Extra Points

- Improve the given python service so it maintains a counter of the amount of **POST** requests it served, and return it on **GET** requests.

## Deliverables

- A link to the public docker registry where the image is published.

- A link to your repository containing:

    1. The Dockerfile(s) for the image(s).
    2. The kubernetes file(s) for the service deployment(s). The deployment should be replicable on our kubernetes cluster.
    3. Optionally the code for the improved version of the service.

## General Guidelines

Your code should be as simple as possible, yet well documented and robust.
Spend some time on designing your solution. Think about operational use cases from the real world. Few examples:

1. What happens if a service crashes?
2. How much effort will it take to create a new service? D.R.Y!

## Reference

- [Run a Stateless Application Using a Deployment](https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/)

