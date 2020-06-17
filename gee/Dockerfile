FROM cyversevice/jupyterlab-scipy:2.0.1

# Install Geospatial dependencies and Google Earth Engine API
RUN conda update -n base conda && \
    conda install --quiet --yes -c conda-forge \
    altair \
    earthengine-api \
    entwine \
    fiona \    
    folium \
    humanize \
    gdal \
    geemap \
    google-api-python-client \
    ipyleaflet \
    ipyvolume \
    ipywidgets \
    nbdime \
    nodejs \ 
    oauth2client \
    palettable \
    pathlib2 \
    pdal \
    planet \
    proj4 \
    pycrypto \
    rasterio \
    shapely \
    udunits2 \
    vega_datasets \
    && \
    conda clean --all -f -y 

RUN jupyter labextension install \
    @bokeh/jupyter_bokeh \
    @jupyter-widgets/jupyterlab-manager \
    @jupyter-widgets/jupyterlab-sidecar \
    @jupyterlab/geojson-extension \
    @jupyterlab/toc \
    ipyvolume \
    itkwidgets \    
    jupyterlab_iframe \ 
    jupyter-leaflet \
    jupyter-threejs \
 && npm cache clean --force

# add bqplot extension
RUN jupyter labextension install bqplot && \
    jupyter nbextension install bqplot --py --symlink --sys-prefix && \ 
    jupyter nbextension enable --py --sys-prefix bqplot


# theme stuff
RUN jupyter labextension install \
    jupyterlab-topbar-extension \
    jupyterlab-system-monitor \
    jupyterlab-theme-toggle --no-build 

RUN jupyter lab build

RUN conda clean --all -f -y

USER root

# Install CyberDuck CLI
RUN echo -e "deb https://s3.amazonaws.com/repo.deb.cyberduck.io stable main" | tee /etc/apt/sources.list.d/cyberduck.list > /dev/null && \
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FE7097963FEFBE72 && \
apt-get update && \
apt-get install duck=6.7.1.28683

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER jovyan

CMD source /opt/conda/etc/profile.d/conda.sh && \
    conda activate entwine

# Entrypoint is set in previous cyversevice/jupyterlab-scipy:latest container


