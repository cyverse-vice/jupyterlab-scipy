FROM cyversevice/jupyterlab-scipy:latest

RUN conda update -n base conda 

RUN conda install -y -c conda-forge earthengine-api pandas folium nodejs cython gdal

RUN pip install --upgrade pip && \
    pip install altair && \
    pip install bqplot && \
    # pip install earthengine-api && \
    pip install fiona && \
    # pip install folium && \ 
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

# RUN jupyter labextension install js && \

RUN jupyter nbextension enable --py --sys-prefix widgetsnbextension && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager && \
    jupyter nbextension enable --py widgetsnbextension --sys-prefix

RUN jupyter labextension install bqplot && \
    jupyter nbextension install bqplot --py --symlink --sys-prefix && \ 
    jupyter nbextension enable --py --sys-prefix bqplot
