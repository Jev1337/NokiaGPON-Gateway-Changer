![Logo](https://www.nokia.com/themes/custom/onenokia_reskin/logo.svg)

# NokiaGPON Restarter
A Simple Python Script that restarts your router until it gets a specific IP




## Installation

Install by cloning project or downloading source code

```bash
  git clone https://github.com/Jev1337/NokiaGPON-Restarter.git
```


    
## Usage/Examples

Modify the following lines and make sure you change them with the desired IP:

```python
if ip_address.startswith("197.15") or ip_address.startswith("197.25"):
            print("IP already starts with 197.15 or 197.25!")
```




## FAQ

#### What does this do and why?

In some countries, routing differs from an IP to another and some people have better latency and performance with certain IPs than others, and to obtain the IP that you like might be a pain to get, using this script, you can leave it open to keep rebooting until you get the IP range that you like.

#### Does this get me in trouble with the ISP?

Honestly I don't think it will as these restarts are not logged as far as I've seen, but you can always be careful, so at your own risk you use this script.


## Optimizations

There are optimizations that are yet to be done such as ease of configuration. Feel free to fork and do pull requests.


## Used By

This is tested on:
- G-240W-F

This project may be used in the following countries as they commonly use these modems:

- Morocco
- Tunisia
- Algeria


## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

