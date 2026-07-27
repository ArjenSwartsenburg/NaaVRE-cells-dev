FROM ghcr.io/arjenswartsenburg/naavre-fl-vanilla-cell-build:v0.1.8 AS build
USER root
# ADD fetches the URL natively in BuildKit: cell-build base images are
# minimal and ship no wget/curl.
ADD "https://scruffy.lab.uvalight.net:9000/dev-arjen/conda_environments/4f3424d4-8af1-44d7-95f9-c3e291e86683_example-packages.tar.gz?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=TFz2G3VsnJeZIJk3bHw6%2F20260727%2Fnl-uvalight%2Fs3%2Faws4_request&X-Amz-Date=20260727T204500Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a6be47948c8116612cfe25f941b2160508e0f611ed1f2aa3a4b4224897911675" /tmp/env.tar.gz
RUN mkdir /venv && \
    tar xzf /tmp/env.tar.gz -C /venv && \
    rm /tmp/env.tar.gz
# Invoke with the env's own interpreter: conda-unpack's `/usr/bin/env python`
# shebang finds nothing on PATH here (no activated env in this branch).
RUN /venv/bin/python /venv/bin/conda-unpack

FROM ghcr.io/arjenswartsenburg/naavre-fl-vanilla-cell-runtime:v0.1.8 AS runtime
COPY --from=build /venv /venv
WORKDIR /app
COPY . .