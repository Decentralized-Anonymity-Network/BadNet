# BADNET
BADNET: A Blockchain-Based Decentralized Anonymity Network

## BADNET Test
#### Client end-to-end performance
At the client side, we use a Tor Browser and BADNET to download a 10 MB file from an HTTPS server, respectively. From the results we infer that the communication performance of BADNET is not worse than Tor.

We also evaluate the web latency when clients connect to a website through BADNET. We perform 1,000 measurements for each client that access the website without a proxy, with a Tor proxy, and with a BADNET proxy.

#### Relay test
We use a few relays to simulate different numbers of relays by shortening the upload interval of each relay.
