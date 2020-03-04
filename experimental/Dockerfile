FROM jupyter/scipy-notebook:latest

USER root

# dependencies for icommands, curl, and wget
RUN apt-get update && apt-get install -y software-properties-common nodejs less vim nano htop libpq-dev lsb wget gnupg apt-transport-https python3 python-requests curl gcc 
RUN apt-get install -y libfuse2 libssl1.0

# iCommands
RUN wget https://files.renci.org/pub/irods/releases/4.1.12/ubuntu14/irods-icommands-4.1.12-ubuntu14-x86_64.deb && \
    dpkg -i irods-icommands-4.1.12-ubuntu14-x86_64.deb && \
    rm irods-icommands-4.1.12-ubuntu14-x86_64.deb

# JupyterLab
RUN pip install ipython-sql jupyterlab jupyterlab_sql psycopg2 \
    && conda update -n base conda \
    && conda install -c conda-forge nodejs \
    && jupyter serverextension enable jupyterlab_sql --py --sys-prefix \
    && jupyter lab build

# CyVerse iRODS plugin
#RUN pip install jupyterlab_irods==3.0.2 \
#    && jupyter serverextension enable --py jupyterlab_irods \
#    && jupyter labextension install ijab

# jupyterlab hub-extension, lab-manager, bokeh
RUN jupyter lab --version \
    && jupyter labextension install @jupyterlab/hub-extension \
                                    @jupyter-widgets/jupyterlab-manager \
                                    jupyterlab_bokeh 

# jupyterlab git widget
RUN jupyter labextension install @jupyterlab/git && \
        pip install --upgrade jupyterlab-git && \
        jupyter serverextension enable --py jupyterlab_git

# jupyterlab github widget
RUN jupyter labextension install @jupyterlab/github

# Proxy Server for JupyterLab
RUN pip install jupyter-server-proxy && jupyter labextension install jupyterlab-server-proxy

# Compile Thiea

RUN mkdir /opt/theia

COPY package.json /opt/theia/package.json

RUN cd /opt/theia && curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.5/install.sh | bash && \
    nvm install 10 && npm install -g yarn && yarn && yarn theia build && \
    bash -e 'export PATH="$(pwd)/node_modules/.bin:${PATH}"'

# Install and configure jupyter lab.
COPY jupyter_notebook_config.json /opt/conda/etc/jupyter/jupyter_notebook_config.json

# Add the jovyan user to UID 1000
RUN groupadd jovyan && usermod -aG jovyan jovyan && usermod -d /home/jovyan -u 1000 jovyan
RUN chown -R jovyan:jovyan /home/jovyan
USER jovyan
WORKDIR /home/jovyan

EXPOSE 8888

COPY entry.sh /bin
RUN mkdir -p /home/jovyan/.irods

ENTRYPOINT ["bash", "/bin/entry.sh"]
