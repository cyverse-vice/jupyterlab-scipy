FROM cyversevice/jupyterlab-scipy:latest

# reset user to root to install depenencies
USER root

# Install Geospatial dependencies and Google Earth Engine API
RUN conda update -n base conda && \
    conda create -n entwine -y -c conda-forge earthengine-api pandas folium nodejs cython gdal proj4 udunits2 pdal entwine 

# install a bunch of dependencies with pip
RUN pip install --upgrade pip && \
    pip install altair && \
    pip install bqplot && \
    pip install fiona && \
    pip install google-api-python-client && \
    pip install humanize && \
    pip install ipyleaflet && \
    pip install ipywidgets && \
    pip install ipyvolume && \
    pip install kml2geojson && \
    pip install matplotlib && \
    pip install nbdime && \
    pip install oauth2client && \
    pip install palettable && \
    pip install pathlib && \
    pip install planet && \
    pip install pyCrypto && \
    pip install rasterio && \
    pip install vega_datasets

# add GEOJSON widget
RUN jupyter labextension install @jupyterlab/geojson-extension && \
    jupyter labextension install jupyter-leaflet && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager
    
# add IPyleaflet 
RUN jupyter nbextension install --py --symlink --sys-prefix ipyleaflet && \
    jupyter nbextension enable --py --sys-prefix ipyleaflet && \
    jupyter labextension install ipyvolume

# add widgets extension manager
RUN jupyter nbextension enable --py --sys-prefix widgetsnbextension && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager && \
    jupyter nbextension enable --py widgetsnbextension --sys-prefix

# add bqplot extension
RUN jupyter labextension install bqplot && \
    jupyter nbextension install bqplot --py --symlink --sys-prefix && \ 
    jupyter nbextension enable --py --sys-prefix bqplot

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Last clean things up a bit
RUN conda clean --all -f -y && \
    fix-permissions $CONDA_DIR

RUN jupyter lab build

USER jovyan

CMD source /opt/conda/etc/profile.d/conda.sh && \
    conda activate entwine

# Entrypoint is set in previous cyversevice/jupyterlab-scipy:latest container

