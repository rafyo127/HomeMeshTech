# mDNS Repeater Integration

The mDNS Repeater integration allows you to bridge mDNS traffic between different network interfaces.

## Installation

1. Add the repository URL to HACS: `https://github.com/rafyo127/homeassistant-mdns-repeater`
2. Install the "mDNS Repeater" integration.
3. Configure the integration in Home Assistant.

## Configuration

Add the following to your `configuration.yaml` file:

```yaml
mdns_repeater:
  iface_in: eth0
  iface_out: wlan0
```

## Usage

Once configured, the mDNS Repeater integration will bridge mDNS traffic between the specified network interfaces.