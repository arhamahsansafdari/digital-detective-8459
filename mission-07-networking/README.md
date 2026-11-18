# Mission 7 — How Computers Communicate

## 1. Task / objective

The objective of Mission 7 is to understand the basic concepts of computer networking and learn how devices communicate over networks.

This mission focuses on understanding different network types, DNS, routers, protocols, packet switching and the client-server model.

It also involves using Terminal commands to test network connectivity, perform DNS lookups and explain the process of opening a website.

## 2. Work completed

### Task 7.1 — Explain network concepts

A computer network connects two or more devices so that they can communicate and share information or resources.

The following table explains the networking concepts studied in this mission.

| Concept | Explanation | Example |
|---|---|---|
| LAN (Local Area Network) | A network connecting devices within a small geographical area. | Computers connected to the same home or college lab network. |
| MAN (Metropolitan Area Network) | A network covering a city or large campus area. | A network connecting several institutional buildings across a city. |
| WAN (Wide Area Network) | A network connecting devices and smaller networks over large geographical distances. | The internet. |
| DNS (Domain Name System) | A system that translates domain names into IP addresses. | Resolving `example.com` to a network address. |
| Router | A networking device that connects networks and forwards data packets between them. | A home Wi-Fi router. |
| Protocol | A set of rules that devices follow when communicating. | HTTP, HTTPS, TCP and IP. |
| Packet switching | A method of transmitting data by dividing it into smaller packets. | Sending and receiving webpage data over the internet. |
| Client-server | A communication model in which a client requests a service and a server provides it. | A web browser requesting a page from a web server. |

**My understanding of network types**

A LAN is suitable for connecting devices in a small area, such as a home or office.

A MAN connects networks across a larger area, such as a city.

A WAN connects networks over large geographical distances. The internet is a major example.

**My understanding of DNS**

DNS stands for Domain Name System.

It helps translate human-readable domain names into network addresses that computers can use for communication.

**My understanding of routers**

A router forwards packets between networks and helps data reach its destination.

**My understanding of protocols**

A network protocol defines rules for exchanging information between devices.

For example, HTTPS is used for secure communication between web browsers and web servers.

**My understanding of packet switching**

Packet switching divides data into packets that can be transmitted through a network.

The receiving system processes the arriving packets to reconstruct the information required by the application.

**My understanding of client-server communication**

In the client-server model, a client requests information or services from a server.

For example, a browser acts as a client when it requests a webpage from a web server.

### Task 7.2 — Observe network information

For this task, I used Terminal commands to investigate network connectivity and DNS.

**1. Connectivity test**

Command:

```bash
ping -c 4 example.com
```

The `ping` command sends ICMP echo requests to a destination.

The `-c 4` option limits the test to four requests.

The results can show whether the destination responds, the round-trip time and the amount of packet loss.

**Interpretation:**

A successful response indicates that the destination is reachable using ICMP echo requests.

If the destination does not respond, it may be due to network problems or restrictions on ICMP traffic.

**2. DNS lookup**

Command:

```bash
nslookup example.com
```

The `nslookup` command requests DNS information associated with a domain name.

Its output may include the DNS resolver and one or more IP addresses associated with the domain.

**3. Additional DNS command**

```bash
dig +short example.com
```

The `dig` command is another tool for querying DNS records.

The `+short` option displays a more concise response.

**4. HTTPS connectivity check**

```bash
curl -I https://example.com
```

This command requests HTTP response headers from the website.

It can help determine whether the website responds over HTTPS.

**Q1. What does a connectivity test help you check?**

A connectivity test helps determine whether a computer can communicate with a particular destination over a network.

A ping test can also provide information about packet loss and round-trip time.

**Q2. What information does a DNS lookup display?**

A DNS lookup displays information associated with a domain name, such as its resolved IP addresses.

It may also show details about the DNS server that answered the query.

**Q3. What is the role of DNS when you enter a website name in a browser?**

DNS translates the website's domain name into an IP address so that the browser can locate the appropriate server.

This allows communication with the server to begin.

**Privacy and evidence**

Any network output or screenshot shared publicly must be checked to ensure that personal IP addresses, DNS resolver details, Wi-Fi names and device information are not exposed.

### Task 7.3 — What happens when you open a website?

**Step 1 — Entering the website address**

The user enters a website address into a browser. The browser acts as the client.

**Step 2 — DNS lookup**

The browser checks for a known network address and uses DNS when necessary to resolve the domain name into an IP address.

**Step 3 — Establishing network communication**

The computer sends traffic through its network and router toward the destination server. For HTTPS, a secure connection is established using TLS.

**Step 4 — Sending an HTTP request**

The browser sends an HTTP request to the server using the appropriate network protocols.

**Step 5 — Server processing**

The server receives the request and prepares the requested content, such as HTML, CSS, JavaScript or other resources.

**Step 6 — Receiving the response**

The server sends a response, and the data travels across the network in packets.

**Step 7 — Displaying the webpage**

The browser processes the received content and renders the webpage on the user's screen.

This process demonstrates how the client, DNS, router, network protocols and server work together to make websites accessible.

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `cd` | Navigate to the assignment directory. |
| `pwd` | Display the current working directory. |
| `ping -c 4 example.com` | Test whether a destination responds to ICMP echo requests. |
| `nslookup example.com` | Perform a DNS lookup. |
| `dig +short example.com` | Display a concise DNS lookup result. |
| `curl -I https://example.com` | Request HTTP response headers. |
| VS Code | Write and edit the Mission 7 README. |
| Git | Track and commit documentation changes. |
| GitHub | Publish the completed mission. |

## 4. My understanding

Through this mission, I learned how computers communicate using networks.

I understood the differences between LAN, MAN and WAN based on their geographical coverage.

I learned that DNS helps translate domain names into IP addresses.

I also understood that routers connect networks and forward packets toward their destinations.

Another important concept was the role of communication protocols such as HTTP, HTTPS, TCP and IP.

I learned that data can be divided into packets during transmission and that the client-server model is used for many internet services.

Finally, I understood the main steps involved when a browser requests and displays a webpage.

## 5. Difficulties faced

The concepts that required the most attention were understanding the differences between LAN, MAN and WAN, distinguishing DNS from routing, and understanding how packets travel across a network.

Another learning challenge was understanding what the `ping` and `nslookup` commands measure or display.

Understanding the order of events involved in opening a website also required connecting several networking concepts.

## 6. How I resolved them

I compared the different network types using their geographical coverage and practical examples.

I studied the roles of DNS and routers separately to understand their different responsibilities.

I examined the purpose of the `ping`, `nslookup` and `dig` commands and learned how their results relate to network communication.

I also organised the website-loading process into seven steps, from entering a URL to displaying the webpage.

This helped me understand how networking concepts work together.

## 7. Evidence / files

The Mission 7 folder contains:

```text
mission-07-networking/
└── README.md
```

**README.md** contains:

- The networking concepts table.
- Explanations of LAN, MAN, WAN, DNS, router, protocol, packet switching and client-server.
- Terminal commands for connectivity and DNS investigation.
- Answers to the three network-observation questions.
- A seven-step explanation of how a website opens.
- Learning reflections and documentation.

The network commands can be repeated in Terminal to verify the observations.

No private network information should be included in public evidence.

## 8. Commit details

**GitHub repository:** https://github.com/arhamahsansafdari/digital-detective-8459

**Branch:** `main`

**Commit message:** `Explain networking concepts and website communication`

**File to commit:**

- `mission-07-networking/README.md`

