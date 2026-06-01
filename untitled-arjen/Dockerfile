FROM ghcr.io/qcdis/naavre/naavre-cell-build-python:v0.22.18 AS build
USER root
RUN mkdir /venv && \
    wget -qO /tmp/env.tar.gz "http://localhost:9000/dev-bucket/conda_environments/691fce67-e7a2-47d9-a272-4994a9470d7e_example-packages.tar.gz?AWSAccessKeyId=fake-s3-access-key&Signature=h%2ByeK80FX%2BbEdLV%2Fs7696qBzTX0%3D&Expires=1780411747" && \
    tar xzf /tmp/env.tar.gz -C /venv && \
    rm /tmp/env.tar.gz
RUN /venv/bin/conda-unpack

FROM ghcr.io/qcdis/naavre/naavre-cell-runtime-python:v0.22.18 AS runtime
COPY --from=build /venv /venv
WORKDIR /app
COPY . .