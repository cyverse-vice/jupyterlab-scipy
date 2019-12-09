FROM jupyter/scipy-notebook:latest

USER root

# Install the icommands, curl, and wget
RUN apt-get update && apt-get install -y software-properties-common nodejs less vim nano htop libpq-dev lsb wget gnupg apt-transport-https python3 python-requests curl gcc 

RUN apt-get install -y libfuse2 libssl1.0

# Install iCommands
RUN wget https://files.renci.org/pub/irods/releases/4.1.12/ubuntu14/irods-icommands-4.1.12-ubuntu14-x86_64.deb && \
    dpkg -i irods-icommands-4.1.12-ubuntu14-x86_64.deb && \
    rm irods-icommands-4.1.12-ubuntu14-x86_64.deb

# Install Jupyter lab
RUN pip install ipython-sql jupyterlab==1.0.9 jupyterlab_sql psycopg2 \
    && conda update -n base conda \
    && conda install -c conda-forge nodejs \
    && jupyter serverextension enable jupyterlab_sql --py --sys-prefix \
    && jupyter lab build

# install the irods plugin for jupyter lab
RUN pip install jupyterlab_irods==3.0.2 \
    && jupyter serverextension enable --py jupyterlab_irods \
    && jupyter labextension install ijab

# install jupyterlab hub-extension, lab-manager, bokeh
RUN jupyter lab --version \
    && jupyter labextension install @jupyterlab/hub-extension \
                                    @jupyter-widgets/jupyterlab-manager \
                                    jupyterlab_bokeh 

# install jupyterlab git extension
RUN jupyter labextension install @jupyterlab/git && \
        pip install --upgrade jupyterlab-git && \
        jupyter serverextension enable --py jupyterlab_git

# install jupyterlab github extension
RUN jupyter labextension install @jupyterlab/github

# Install and configure jupyter lab.
COPY jupyter_notebook_config.json /opt/conda/etc/jupyter/jupyter_notebook_config.json

# Add the jovyan user to UID 1000
RUN usermod -d /home/jovyan -u 1000 jovyan
USER jovyan
WORKDIR /home/jovyan

EXPOSE 8888

COPY entry.sh /bin
RUN mkdir -p /home/jovyan/.irods

ENTRYPOINT ["bash", "/bin/entry.sh"]


