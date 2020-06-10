FROM jupyter/scipy-notebook:dc9744740e12

RUN jupyter lab --version

USER root

# Install a few dependencies for iCommands, text editing, and monitoring instances
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    gcc \
    gnupg \
    htop \
    less \
    libfuse2 \
    libpq-dev \
    libssl1.0 \
    lsb \
    nano \
    nodejs \  
    python-requests \
    software-properties-common \
    vim
    
# Install iCommands
RUN wget https://files.renci.org/pub/irods/releases/4.1.12/ubuntu14/irods-icommands-4.1.12-ubuntu14-x86_64.deb && \
    dpkg -i irods-icommands-4.1.12-ubuntu14-x86_64.deb && \
    rm irods-icommands-4.1.12-ubuntu14-x86_64.deb

# Add the jovyan user to UID 1000
RUN groupadd jovyan && usermod -aG jovyan jovyan && usermod -d /home/jovyan -u 1000 jovyan
RUN chown -R jovyan:jovyan /home/jovyan
USER jovyan

# install the irods plugin for jupyter lab -- non-functional beyond JupyterLab v1.0.9
# RUN pip install jupyterlab_irods==3.0.2 \
#   && jupyter serverextension enable --py jupyterlab_irods \
#    && jupyter labextension install ijab

# install jupyterlab git extension
RUN jupyter labextension install @jupyterlab/git && \
        pip install --upgrade jupyterlab-git && \
        jupyter serverextension enable --py jupyterlab_git

# install jupyterlab github extension
RUN jupyter labextension install @jupyterlab/github

# Install and configure jupyter lab.
COPY jupyter_notebook_config.json /opt/conda/etc/jupyter/jupyter_notebook_config.json

WORKDIR /home/jovyan

EXPOSE 8888

COPY entry.sh /bin
RUN mkdir -p /home/jovyan/.irods

ENTRYPOINT ["bash", "/bin/entry.sh"]
