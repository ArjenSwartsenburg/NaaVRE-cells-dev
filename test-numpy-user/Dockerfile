FROM ghcr.io/arjenswartsenburg/naavre-fl-vanilla-cell-build:v0.1.8 AS build
USER root
# ADD fetches the URL natively in BuildKit: cell-build base images are
# minimal and ship no wget/curl.
ADD "https://scruffy.lab.uvalight.net:9000/dev-arjen/conda_environments/83f71cc5-ddd0-41e1-b1e2-2dff85abb802_example-packages.tar.gz?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=TFz2G3VsnJeZIJk3bHw6%2F20260727%2Fnl-uvalight%2Fs3%2Faws4_request&X-Amz-Date=20260727T115624Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b899d94ef8c1153594f75045c72d5d5e8514d677be344680fe4c70e3f9923340" /tmp/env.tar.gz
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