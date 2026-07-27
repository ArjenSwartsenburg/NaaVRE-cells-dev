FROM ghcr.io/arjenswartsenburg/naavre-fl-vanilla-cell-build:v0.1.8 AS build
USER root
RUN mkdir /venv && \
    wget -qO /tmp/env.tar.gz "https://scruffy.lab.uvalight.net:9000/dev-arjen/conda_environments/83f71cc5-ddd0-41e1-b1e2-2dff85abb802_example-packages.tar.gz?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=TFz2G3VsnJeZIJk3bHw6%2F20260727%2Fnl-uvalight%2Fs3%2Faws4_request&X-Amz-Date=20260727T101800Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a29e346017ee9dc3cf42f83818120b2715cfb32f0ec99434cfc6d971f9977090" && \
    tar xzf /tmp/env.tar.gz -C /venv && \
    rm /tmp/env.tar.gz
RUN /venv/bin/conda-unpack

FROM ghcr.io/arjenswartsenburg/naavre-fl-vanilla-cell-runtime:v0.1.8 AS runtime
COPY --from=build /venv /venv
WORKDIR /app
COPY . .