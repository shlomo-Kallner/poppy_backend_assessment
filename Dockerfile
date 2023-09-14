
FROM python:3.10-bullseye

RUN apt update && apt upgrade -y && mkdir /app


COPY requirements/* /app/requirements/

ARG INSTALL_DEV="False"

RUN python3 -m venv /app/.venv && \
    python3 -m pip install -U -r /app/requirements/basic.txt \
    -r /app/requirements/requirements.txt && \
    [ "${INSTALL_DEV}" = "y" || "${INSTALL_DEV}" = "Y" || "${INSTALL_DEV}" = "1" ] && \
    python3 -m pip install -U -r /app/requirements/dev.txt

