FROM python:3

ENV REGULAR_USER=cellfetcher
ENV REGULAR_USER_UID=1000
ENV REGULAR_USER_GID=1000
ENV REGULAR_USER_HOME=/home/${REGULAR_USER}
ENV REGULAR_USER_APP_HOME=${REGULAR_USER_HOME}/app

RUN groupadd -r --gid ${REGULAR_USER_GID} ${REGULAR_USER}
RUN useradd --system --no-log-init --uid ${REGULAR_USER_UID} --gid ${REGULAR_USER_GID} --home-dir ${REGULAR_USER_HOME} --create-home --shell /bin/bash ${REGULAR_USER}

RUN mkdir -p ${REGULAR_USER_APP_HOME} && chown -R ${REGULAR_USER}:${REGULAR_USER} ${REGULAR_USER_APP_HOME}

RUN apt update && \
    apt install -y tmux locales-all

USER ${REGULAR_USER}
WORKDIR ${REGULAR_USER_APP_HOME}
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY cell-fetcher.py .

CMD [ "python", "./cell-fetcher.py" ]
