# OpenFaaS linpack sample function

This is a reproduction repo for


## Deploying
To use the prebuilt image, run

```sh
IMAGE_PREFIX=ghcr.io/lucasroesler/ faas-cli deploy
```

## Invoking

```sh
$ faas-cli invoke linpack <<< 5
0.9658731145653424
```
