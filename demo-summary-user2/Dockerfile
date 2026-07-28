FROM ghcr.io/arjenswartsenburg/naavre-fl-vanilla-cell-build:v0.1.9 AS build
USER root
# ADD fetches the URL natively in BuildKit: cell-build base images are
# minimal and ship no wget/curl.
ADD "https://scruffy.lab.uvalight.net:9000/dev-arjen/conda_environments/6cf682f0-966c-4a2d-8c9f-f36fcb9378b6_workflow-demo2.tar.gz?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=TFz2G3VsnJeZIJk3bHw6%2F20260728%2Fnl-uvalight%2Fs3%2Faws4_request&X-Amz-Date=20260728T133233Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=93a5a644dfa58406e5d88fdc45dd1c9fc29fcb005e5a96f17f944d464c8f25d1" /tmp/env.tar.gz
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