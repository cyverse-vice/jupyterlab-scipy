FROM cyversevice/jupyterlab-scipy:latest

USER root

RUN conda update -n base conda 

# Install Geospatial dependencies and Google Earth Engine API
RUN conda install -y -c conda-forge earthengine-api pandas folium nodejs cython gdal proj4 udunits2 pdal entwine 

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

RUN jupyter labextension install @jupyterlab/geojson-extension && \
    jupyter labextension install jupyter-leaflet && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager
    
RUN jupyter nbextension install --py --symlink --sys-prefix ipyleaflet && \
    jupyter nbextension enable --py --sys-prefix ipyleaflet && \
    jupyter labextension install ipyvolume

RUN jupyter nbextension enable --py --sys-prefix widgetsnbextension && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager && \
    jupyter nbextension enable --py widgetsnbextension --sys-prefix

RUN jupyter labextension install bqplot && \
    jupyter nbextension install bqplot --py --symlink --sys-prefix && \ 
    jupyter nbextension enable --py --sys-prefix bqplot

# Planet Labs stuff
RUN conda install -c conda-forge cartopy
RUN conda install -y -c conda-forge gdal

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt 

RUN jupyter nbextension enable --py widgetsnbextension --sys-prefix && \
    jupyter nbextension enable --py --sys-prefix ipyleaflet

RUN mkdir -p /etc/pki/tls/certs
RUN cp /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt

RUN conda install -y -c conda-forge ncurses

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Last update and re-build

RUN jupyter lab build


USER jovyan

# Entrypoint is set in previous cyversevice/jupyterlab-scipy:latest container

