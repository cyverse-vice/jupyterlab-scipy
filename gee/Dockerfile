FROM cyversevice/jupyterlab-scipy:latest

RUN conda update -n base conda 

RUN conda install -y -c conda-forge earthengine-api pandas folium nodejs cython gdal

RUN pip install --upgrade pip && \
    pip install vega_datasets && \
    pip install oauth2client && \
    pip install pyCrypto && \
    pip install pathlib && \
    pip install kml2geojson && \
    pip install google-api-python-client

RUN jupyter labextension install @jupyterlab/geojson-extension

