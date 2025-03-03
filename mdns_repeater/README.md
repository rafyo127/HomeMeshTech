# mDNS Repeater Add-on for Home Assistant

## Overview

The mDNS Repeater add-on for Home Assistant allows you to extend the range of mDNS services across different network segments. This is particularly useful if you have devices on different subnets that need to discover each other using mDNS (Multicast DNS). The repeater captures mDNS packets on one network interface and resends them on another, effectively bridging the gap between different network segments.

## Installation

1. **Add the Custom Repository**:
    - Open your Home Assistant instance.
    - Go to the "Supervisor" tab.
    - Click on the "Add-on Store" button.
    - Click on the three dots in the top right corner and select "Repositories".
    - Add the URL of this GitHub repository.

2. **Install the Add-on**:
    - Find the "mDNS Repeater" add-on in the list of available add-ons.
    - Click on the add-on and then click the "Install" button.

3. **Configure the Add-on**:
    - Open the "mDNS Repeater" add-on.
    - Click on the "Configuration" tab.
    - Set the `iface_in` option to the name of the input network interface (e.g., `eth0`).
    - Set the `iface_out` option to the name of the output network interface (e.g., `wlan0`).
    - Click the "Save" button.

4. **Start the Add-on**:
    - Click on the "Info" tab.
    - Click the "Start" button to start the add-on.

## Configuration Options

- `iface_in`: The name of the network interface to capture mDNS packets from (e.g., `eth0`).
- `iface_out`: The name of the network interface to send mDNS packets to (e.g., `wlan0`).

## Example Configuration

```json
{
  "iface_in": "eth0",
  "iface_out": "wlan0"
}
```

## How It Works

The add-on uses a Python script that leverages the `scapy` library to capture and forward mDNS packets. The script listens for mDNS packets on the specified input interface and forwards them to the output interface, allowing devices on different subnets to discover each other.

## Troubleshooting

- Ensure that the network interfaces specified in the configuration are correct and active.
- Check the add-on logs for any error messages or warnings.
- Make sure that your Home Assistant instance has the necessary permissions to capture and send network packets.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## Support

For support, please open an issue on the GitHub repository.