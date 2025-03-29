#!/bin/sh

echo "[DEBUG] Installed packages:"
apk info

echo "[DEBUG] Checking for jq:"
which jq

SOURCE_INTERFACE=$(jq -r '.source_interface' /data/options.json)
DESTINATION_INTERFACE=$(jq -r '.destination_interface' /data/options.json)

echo "[INFO] Starting mDNS repeater..."
echo "[INFO] Source Interface: $SOURCE_INTERFACE"
echo "[INFO] Destination Interface: $DESTINATION_INTERFACE"

exec mdns-repeater "$SOURCE_INTERFACE" "$DESTINATION_INTERFACE"
