# Networking

### A Network??

What is a network??! 

Basically it's just a collection of actors which are able to communicate with each other. This is the basis of it all. 

After that we add a lot of functionality to be able to communicate, we have to speak the same language to get information accross, otherwise we're just sending electrical(or light) energy through a little wire and nobody knows what to do with it. 

If you want to understand it a lot better than I can explain it visit [networking](https://beej.us/guide/bgnet/). This will explain at quite a low level what happens. Not on the physics level, but a low level nonetheless. 

### IP address

Maybe we should start with defining what an IP address is. (if you've read the socket guide above you should skip this part). It's basically an address.. (no shit..) but then for computers within the network. There are two versions, ipv4, ipv6. The purpose of these is the same, but ipv6 was thought to be a solution of some of ipv4's problems. 

But how do we use the ip adresses?? It's kind of the same as a normal addres of a house, it tells your mailman where it should put the mail. But it looks a bit different from your house address. So let's have a look at ipv4 (which is a bit more understandable in it's notation than ipv6). For example we have 10.6.0.2, what is that as an IP address? The four numbers are very nice to look at but are kind of a trick to make it more understandable to us simply base10 understanding humans. The IP address itself would identify as binary (very modern). Okay, so what does it think it looks like?

```text
00001010000001100000000000000010 or which is a little bit easier to understand with some dots -> 00001010.00000110.00000000.00000010
```
Do you see what's going on? We are taking 32 digits, we start with all zeroes, and then on a per byte level we add the numbers that we see in in our original description. 10, 6, 0, and 2. (I took some low numbers to make it a bit easy for myself). It's the same as before but completely impossible to read. So the notation that we know makes a lot of sense. Now there is another thing we see often which is a CIDR or Classless-Inter-Domain-Routing. We often see things like:

```text
192.168.0.0/16
```

Now what does this mean? We see an IP address, a slash and a number.. The IP address we now know, the slash is simply syntax (this is how we see its a CIDR), but then we see the 16, this is the important part. This actually tells us the amount of digits that can either be a 0 or a 1. And this freedom implies a degree of freedom, or the space in which the IP addresses can exist. Since the last 16 digits can be either a 0 or a 1 the following addresses are valid:

```text
192.168.0.0 <- obviously..
192.168.1.1 <- makes sense so far..
192.168.210.132 <- also valid! :D 
192.168.xxx.xxx <- all of these are possible within the CIDR
```

```text
193.168.0.0 <- this is outside the space since 193 is not equal to 192
10.0.0.0 <- outside because both the first and second byte are unequal
```

How can we practically use this?

Say for example that we go to a cloud provider, and we want some network room to be able to host some virtual machines. Since these machines need to be able to communicate with other stuff they need to exist somewhere in a network, and therefore have an address. Now let's say that network, or Virtual network, or Vnet, we get assigned to us to play with is:

```text
10.0.0.0/16
```

That's quite a lot of adresses, 2^16=65536 to be exact. So within this space we could host that many VMs. Seems a bit overkill but o well. After this we actually want to host an additional set of VMs but we kind of do not want to have them communicate with the other VMs. What do we do? First of we take a piece of the network and tell Azure to seperate that from the rest somehow. Here come the `subnets`! which is a logical separation of addresses from the rest of the VNET. Do note, so far it's still one big happy network where everything can communicate with each other. Hold up, whats a subnet? 

So we go to the cloud provider and we say, within this Vnet I want to create a subnet. Which is telling the system to take a chunk of the Vnet space, and from now on we determine that part to belong to the subnet which we give a name, snet-with-og-vms for example. For this subnet however we need to state which chunk of the vnet we want to take. And thats where the CIDR comes into play! So we tell Azure:

```text
10.0.0.0/24 -> I want this space to be defined as the snet-with-og-vms subnet
```
that's it.. We have now defined a subnet and nothing actually changed, we just added a definition to a list. When it becomes interesting though is when we assign a so called `Network Security Group` or `nsg` to that subnet. We first have to create that thing of course, after which we can assign it to our subnet. In the nsg we can now state that we want to limit the traffic that comes into the subnet. For example, we don't want ANY traffic from anywhere except from within the subnet to come in. So we create a rule, give it a priority and state BLOCK everything from coming into this network. This actually means that no connection can be initialized from outside of 10.0.0.0/24 into 10.0.0.0/24 but the VMs within the subnet are allowed to send requests outwards. There are also rules to tell the system that no requests can be initialized outwards, those are OUTBOUND rules and you can block stuff and then very precisely unblock small parts with specific ports bla bla bla. This allows you to control exactly which IPs can communicate from and to the subnet on which ports. Pretty handy if you're trying to block bad actors from moving through your network if they're not able to communicate with other parts of your network. 




### port




### Sending a request

Let's see what happens when we fire off a request, for example with 

```shell
nslookup reddit.com
```

```text
Server:		xx.xx.xx.xx
Address:	xx.xx.xx.xx#53 <-- port 53, standard for DNS

Non-authoritative answer:
Name:	reddit.com
Address: 151.101.193.140
Name:	reddit.com
Address: 151.101.65.140
Name:	reddit.com
Address: 151.101.1.140
Name:	reddit.com
Address: 151.101.129.140
```

this means that reddit.com actually listens on 4 different IP adresses. 

(Also look at wireshark what is happening)

Yay, so now we know where we should go if we want to retrieve the webpages from reddit. Your computer automatically now translates all of the adresses like `reddit.com/somepath?with=param&equals=value` to that IP address. Another little trick they use is to translate `http` and `https` to the two ports `80` and `443`. So if you go into your terminal and fire off:

```shell
curl https://reddit.com
```
What happens is that it first queries the DNS server that you have registered in your network/computer/application. Send a UDP DNS request to that server on port 53. That server figures out if it knows the corresponding IP address, or knows someone who knows and asks that server. The response then contains the IP adress of the host that we are asking for. Now your computer knows which IP adress corresponds to that hostname reddit.com. 

Okay great! now your computer sends the next request to that IP adress! Thats the end of the hostname functioning as a target address. We are now talking computer language, a binary address of either 32 digits (ipv4) or 128 digits (ipv6). But where to send this request?? There is no cable running from my computer to the server that is registered under 151.101.129.140... I'm in my office, all ip adresses here look like  `10.0.0.95`, where am I sending a request that looks nothing like this?? First off, your request is sent to the router, that thing knows everything, it's the damned router. But... there is also no cable running from that router to reddit, they're in the US probably (or have a service running in Europe somewhere for low latency ofcourse). either way, there is a single cable running from my router into the floor. And that's not going to Reddit. So what happens? First off, your router (or the first server that your ISP manages) has a big list of CIDRs with a corresponding IP address which apparently is knowledgable of the location of this `151.101.129.140`. So the router checks his little list, figures out which address it can send this request to, and off it goes to the next server! which in the case of a router tends to be always the same sever, its connected to a single thing.. but the nice thing is, that next server, according to our request the next `hop` again looks at it's little list of ip address to CIDR mapping. And it sends it to the next server. Note that we are now "on the public internet network". This way of doing things keeps going untill we hit a hop that actually knows the server which IS 151.101.129.140. So the request gets sent there and the server should know what to do with the string of text or binary blubber it's receiving. If not it probably responds with some HTTP response code like 404, 5xx or something else. But how does this response reach you?? Well, it fires of the response in the same way as we sent the request in the first place. Allthough now it doesnt have to translate a hostname to an address, since the request contains the source of the request in the first place, so we just send the response there. But there is not active line here or anything. It just fires off the response to your location which you mentioned in your request. And off it goes! I have something for (IP ADDRESS of your local router) who knows where this should go?? etc. To me it's a bunch of simple rules glueing everything together based on rules that some people thought up 30-40 years ago. There is a lot of trust going on, and then there are a lot of layers of distrust going on. 

### Visiting an address

Now let's translate this to us visiting a website in a browser. And let's do it in a way that is not "safe". 
