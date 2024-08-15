# datamodelling_dp

## Commands to setup our project

1. Clone the repo

```bash
git clone https://github.com/rubaramanan/datamodelling_dp.git
```

2. Start airflow services

```bash
cd docker
docker build -f DockerfileAirflow . -t dataprogram_airflow:0.0.1

docker-compose -f docker-compose-airflow.yaml up -d
```

3. Access the Airflow UI

*url*: `http://localhost:8080`

*user*: `airflow`

*password*: `airflow`

4. Connect powerBi with db and visualize.

## Start schema data model

