FROM ghcr.io/arjenswartsenburg/naavre-fl-vanilla-cell-build:v0.1.8 AS build
USER root
# ADD fetches the URL natively in BuildKit: cell-build base images are
# minimal and ship no wget/curl.
ADD "https://scruffy.lab.uvalight.net:9000/dev-arjen/conda_environments/e14e7bc0-9018-4c94-a77e-18e0e2656eb2_workflow-demo.tar.gz?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=TFz2G3VsnJeZIJk3bHw6%2F20260728%2Fnl-uvalight%2Fs3%2Faws4_request&X-Amz-Date=20260728T102351Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=847515518e1db5822c9cd837a1559af66cfae92ce239aafa2a9ffb7de754583b" /tmp/env.tar.gz
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