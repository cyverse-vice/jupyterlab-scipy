FROM cyversevice/jupyterlab-scipy:latest

# reset user to root to install depenencies
USER root

# Install PlantCV
RUN apt-get update \
    && apt-get install -y libx264-dev \
    && apt-get clean \
    && rm -rf /usr/lib/apt/lists/* \
    && fix-permissions $CONDA_DIR

RUN conda install nb_conda \
    && conda create -n plantcv -c bioconda plantcv nb_conda \
    && conda clean -tipsy \
    && fix-permissions $CONDA_DIR

USER jovyan



