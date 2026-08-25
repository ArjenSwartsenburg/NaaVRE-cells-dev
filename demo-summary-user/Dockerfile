FROM ghcr.io/arjenswartsenburg/naavre-fl-vanilla-cell-build:v0.1.9 AS build
USER root
# ADD fetches the URL natively in BuildKit: cell-build base images are
# minimal and ship no wget/curl.
ADD "https://scruffy.lab.uvalight.net:9000/dev-arjen/conda_environments/3e2023d9-932b-40ec-ae90-794d5e60ceaf_workflow-demo.tar.gz?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=TFz2G3VsnJeZIJk3bHw6%2F20260825%2Fnl-uvalight%2Fs3%2Faws4_request&X-Amz-Date=20260825T200939Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b1c9470449207d7d25230af3c2a1c66f62242ad610f9adf912b7b1d415937c1c" /tmp/env.tar.gz
RUN mkdir /venv && \
    tar xzf /tmp/env.tar.gz -C /venv && \
    rm /tmp/env.tar.gz
# Invoke with the env's own interpreter: conda-unpack's `/usr/bin/env python`
# shebang finds nothing on PATH here (no activated env in this branch).
RUN /venv/bin/python /venv/bin/conda-unpack

FROM ghcr.io/arjenswartsenburg/naavre-fl-vanilla-cell-runtime:v0.1.9 AS runtime
COPY --from=build /venv /venv
WORKDIR /app
COPY . .