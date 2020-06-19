[![Project Supported by CyVerse](https://img.shields.io/badge/Supported%20by-CyVerse-blue.svg)](https://learning.cyverse.org/projects/vice/en/latest/) [![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3246934.svg)](https://doi.org/10.5281/zenodo.3246934) [![license](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://opensource.org/licenses/GPL-3.0)

# jupyterlab-scipy

Jupyter Lab base Docker container recipe based on [Jupyter datascience-notebook](https://hub.docker.com/r/jupyter/scipy-notebook) for [CyVerse VICE](https://cyverse-visual-interactive-computing-environment.readthedocs-hosted.com/en/latest/index.html). VICE requires additional configuration files to be compatible with our Condor and Kubernetes orchestration.

[![CircleCI](https://circleci.com/gh/cyverse-vice/jupyterlab-scipy.svg?style=svg)](https://circleci.com/gh/cyverse-vice/jupyterlab-scipy) [![DockerHub](https://img.shields.io/badge/DockerHub-brightgreen.svg?style=popout&logo=Docker)](https://hub.docker.com/r/cyversevice/jupyterlab-scipy)


quick launch | tag | size | metrics | build | 
------------ | --- | ---- | ------- | ------|
<a href="https://de.cyverse.org/de/?type=quick-launch&quick-launch-id=91c72a5d-0ce9-484f-a1f1-feba4cab75a5&app-id=bc93504c-d584-11e9-8413-008cfa5ae621" target="_blank"><img src="https://de.cyverse.org/Powered-By-CyVerse-blue.svg"></a> | [![TAG](https://images.microbadger.com/badges/version/cyversevice/jupyterlab-scipy.svg)](https://microbadger.com/images/cyversevice/jupyterlab-scipy) | [![SIZE](https://images.microbadger.com/badges/image/cyversevice/jupyterlab-scipy.svg)](https://microbadger.com/images/cyversevice/jupyterlab-scipy) | [![Docker Pulls](https://img.shields.io/docker/pulls/cyversevice/jupyterlab-scipy?color=blue&label=pulls&logo=docker&logoColor=white)](https://hub.docker.com/r/cyversevice/jupyterlab-scipy) | [![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/cyversevice/jupyterlab-scipy?color=blue&logo=docker&logoColor=white)](https://hub.docker.com/r/cyversevice/jupyterlab-scipy)

old versions | tag | size | metrics | build | 
------------ | --- | ---- | ------- | ------|
<a href="" target="_blank"><img src="https://de.cyverse.org/Powered-By-CyVerse-blue.svg"></a> | [![TAG](https://images.microbadger.com/badges/version/cyversevice/jupyterlab-scipy:0.35.0.svg)](https://microbadger.com/images/cyversevice/jupyterlab-scipy:0.35.0) | [![SIZE](https://images.microbadger.com/badges/image/cyversevice/jupyterlab-scipy:0.35.0.svg)](https://microbadger.com/images/cyversevice/jupyterlab-scipy:0.35.0) | [![Docker Pulls](https://img.shields.io/docker/pulls/cyversevice/jupyterlab-scipy?color=blue&label=pulls&logo=docker&logoColor=white)](https://hub.docker.com/r/cyversevice/jupyterlab-scipy) | [![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/cyversevice/jupyterlab-scipy?color=blue&logo=docker&logoColor=white)](https://hub.docker.com/r/cyversevice/jupyterlab-scipy)
<a href="" target="_blank"><img src="https://de.cyverse.org/Powered-By-CyVerse-blue.svg"></a> | [![TAG](https://images.microbadger.com/badges/version/cyversevice/jupyterlab-scipy:1.1.0.svg)](https://microbadger.com/images/cyversevice/jupyterlab-scipy:1.1.0) | [![SIZE](https://images.microbadger.com/badges/image/cyversevice/jupyterlab-scipy:1.1.0.svg)](https://microbadger.com/images/cyversevice/jupyterlab-scipy:1.1.0) | [![Docker Pulls](https://img.shields.io/docker/pulls/cyversevice/jupyterlab-scipy?color=blue&label=pulls&logo=docker&logoColor=white)](https://hub.docker.com/r/cyversevice/jupyterlab-scipy) | [![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/cyversevice/jupyterlab-scipy?color=blue&logo=docker&logoColor=white)](https://hub.docker.com/r/cyversevice/jupyterlab-scipy)  
<a href="" target="_blank"><img src="https://de.cyverse.org/Powered-By-CyVerse-blue.svg"></a> | [![TAG](https://images.microbadger.com/badges/version/cyversevice/jupyterlab-scipy:1.2.0.svg)](https://microbadger.com/images/cyversevice/jupyterlab-scipy:1.2.0) | [![SIZE](https://images.microbadger.com/badges/image/cyversevice/jupyterlab-scipy:1.2.0.svg)](https://microbadger.com/images/cyversevice/jupyterlab-scipy:1.2.0) | [![Docker Pulls](https://img.shields.io/docker/pulls/cyversevice/jupyterlab-scipy?color=blue&label=pulls&logo=docker&logoColor=white)](https://hub.docker.com/r/cyversevice/jupyterlab-scipy) | [![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/cyversevice/jupyterlab-scipy?color=blue&logo=docker&logoColor=white)](https://hub.docker.com/r/cyversevice/jupyterlab-scipy)  
<a href="" target="_blank"><img src="https://de.cyverse.org/Powered-By-CyVerse-blue.svg"></a> | [![TAG](https://images.microbadger.com/badges/version/cyversevice/jupyterlab-scipy:2.0.1.svg)](https://microbadger.com/images/cyversevice/jupyterlab-scipy:2.0.1) | [![SIZE](https://images.microbadger.com/badges/image/cyversevice/jupyterlab-scipy:2.0.1.svg)](https://microbadger.com/images/cyversevice/jupyterlab-scipy:2.0.1) | [![Docker Pulls](https://img.shields.io/docker/pulls/cyversevice/jupyterlab-scipy?color=blue&label=pulls&logo=docker&logoColor=white)](https://hub.docker.com/r/cyversevice/jupyterlab-scipy) | [![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/cyversevice/jupyterlab-scipy?color=blue&logo=docker&logoColor=white)](https://hub.docker.com/r/cyversevice/jupyterlab-scipy) 
<a href="" target="_blank"><img src="https://de.cyverse.org/Powered-By-CyVerse-blue.svg"></a> | [![TAG](https://images.microbadger.com/badges/version/cyversevice/jupyterlab-scipy:2.0.2.svg)](https://microbadger.com/images/cyversevice/jupyterlab-scipy:2.0.2) | [![SIZE](https://images.microbadger.com/badges/image/cyversevice/jupyterlab-scipy:2.0.2.svg)](https://microbadger.com/images/cyversevice/jupyterlab-scipy:2.0.2) | [![Docker Pulls](https://img.shields.io/docker/pulls/cyversevice/jupyterlab-scipy?color=blue&label=pulls&logo=docker&logoColor=white)](https://hub.docker.com/r/cyversevice/jupyterlab-scipy) | [![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/cyversevice/jupyterlab-scipy?color=blue&logo=docker&logoColor=white)](https://hub.docker.com/r/cyversevice/jupyterlab-scipy) 
<a href="" target="_blank"><img src="https://de.cyverse.org/Powered-By-CyVerse-blue.svg"></a> | [![TAG](https://images.microbadger.com/badges/version/cyversevice/jupyterlab-scipy:2.1.0.svg)](https://microbadger.com/images/cyversevice/jupyterlab-scipy:2.1.0) | [![SIZE](https://images.microbadger.com/badges/image/cyversevice/jupyterlab-scipy:2.1.0.svg)](https://microbadger.com/images/cyversevice/jupyterlab-scipy:2.1.0) | [![Docker Pulls](https://img.shields.io/docker/pulls/cyversevice/jupyterlab-scipy?color=blue&label=pulls&logo=docker&logoColor=white)](https://hub.docker.com/r/cyversevice/jupyterlab-scipy) | [![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/cyversevice/jupyterlab-scipy?color=blue&logo=docker&logoColor=white)](https://hub.docker.com/r/cyversevice/jupyterlab-scipy) 

# Instructions


## Run Docker locally or on a Virtual Machine

To run the JupyterLab, you must first `pull` from DockerHub, or activate a [CyVerse Account](https://user.cyverse.org/services/mine) and launch in the Discovery Environment VICE.

The container for running JupyterLab is hosted on DockerHub and can be started locally:


```
docker pull cyversevice/jupyterlab-scipy:latest
```

```
docker run -it --rm -d cyversevice/jupyterlab-scipy:latest
```

## Run Docker container in CyVerse VICE

Unless you plan on making changes to this container, you should just use the existing launch button above.

You can build a new Docker container with additional dependencies from this Docker Hub image by using the `FROM cyversevice/jupyterlab-scipy:latest` at the beginning of your own Dockerfile.

###### Developer notes

To test the container locally:

```
docker run -it --rm -v /$HOME:/app --workdir /app -p 8888:8888 -e REDIRECT_URL=http://localhost:8888 cyversevice/jupyterlab-scipy:latest
```
