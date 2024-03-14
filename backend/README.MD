# Running an application

We've built an application here surrounding ducks, adding them reading them etc.

We can run this on our own system:

first setup the DB, go to the local folder and run

```shell
docker-compose up
```

then 

```shell
psql -h localhost -U teaching_de -d teaching_de
\i START_SERVER.sql
```

And exit. Now we start the webserver:


```shell
uvicorn http-svc.backend:app --reload
```

yay! test this with some http test calls:

```shell
curl http://localhost:8080/duck/1
curl http://localhost:8080/duck -H "Content-Type: application/json" -d '{"age": 12, "address": "ducktown 35A", "name": "Donald", "favorite_pond": "Kralingse plas"}'
```

This means we have a running database and webserver on our own system. We can also containarize the webserver using docker

```shell
docker build . -t duckbackend
```

And run it locally 

```shell
docker run -it -p 8080:8080 -e POSTGRES_HOSTNAME=local-timescaledb-de-1 --network=local_default duckbackend
```

- '-it' interactive mode
- '-p' map a host port to the container port (8080 in this case)
- '-e' add an environment variable to the running container. In this case we add a hostname specific to the docker 
network so we can reach the database. 
- '--network' we connect this container to the docker network that was created by docker-compose earlier

Now again we try and see if it works:

```shell
curl http://localhost:8080/duck/2
curl http://localhost:8080/duck -H "Content-Type: application/json" -d '{"age": 12, "address": "ducktown 35A", "name": "Donald", "favorite_pond": "Kralingse plas"}'
```

Now everything is containerized, everything works. Next step is to deploy to kubernetes.

First we need to allow kubernetes to access our docker image. We have a container registry on azure, so lets use that

```shell
docker build . -t testcrbatto.azurecr.io/teaching-de/http-svc:latest
docker push testcrbatto.azurecr.io/teaching-de/http-svc:latest 
```

If we get a pesky warning telling us "we dont have access bla bla bla"

```shell
az login
az acr login -n testcrbatt
```
### Kubernetes

Now off to the actual kubernetes stuff &#128526;

Move into the aks database folder and get kubectl ready. 

```shell
kubectl apply -f configmap.yaml
kubectl apply -f deployment.yaml
kubectl apply -f svc.yaml
```

now the database is up and running lets instantiate the proper schemas and tables

```shell
kubectl port-forward <database pod name> 5432
 
```
In another window move to the local folder and call

```shell
psql -d teaching_de -h localhost -U teaching_de
\i START_SERVER.sql
```

Now the database is up and running we can go ahead and start the webserver, change directories to the http-svc folder

```shell
kubectl apply -f configmap.yaml
kubectl apply -f deployment.yaml
```

The svc an ingress are also defined, but probably out of scope for this session. 

```shell
kubectl port-forward <http-svc pod name> 8080
```

now again we can call 

```shell
curl http://localhost:8080/duck -H "Content-Type: application/json" -d '{"age": 12, "address": "ducktown 35A", "name": "Donald", "favorite_pond": "Kralingse plas"}'
curl http://localhost:8080/duck/1
```

Whoehoe, we have a small setup running in kubernetes 