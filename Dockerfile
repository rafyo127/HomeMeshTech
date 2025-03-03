# Stage 1: Build
FROM alpine:3.13 AS builder

# Install build tools
RUN apk add --no-cache build-base

WORKDIR /usr/src

# Copy source files and build
COPY mdns-repeater.c Makefile ./
RUN make

# Stage 2: Runtime
FROM alpine:3.15

# Install supervisor for process management
RUN apk add --no-cache supervisor

WORKDIR /usr/src

# Copy the built binary and runtime files from the builder stage
COPY --from=builder /usr/src/mdns-repeater /usr/src/mdns-repeater
COPY run.sh supervisord.conf ./

# Ensure run.sh is executable
RUN chmod +x run.sh

# (Optional) Expose any ports if mdns-repeater listens on one, for example:
EXPOSE 5353

# Set the default command to start your service via run.sh
CMD ["/usr/src/run.sh"]
