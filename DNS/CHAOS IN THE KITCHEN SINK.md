# CHALLENGE_TITLE
CHAOS IN THE KITCHEN SINK

## Category
DNS

## Estimated difficulty
Easy

## Description

Imagine diving into a kitchen sink that's a chaotic wonderland of dirty dishes, rogue utensils, and mysterious leftovers.
Your mission? To find a hidden flag amidst this culinary catastrophe.
It's like playing hide-and-seek with a ninja spoon!
In this scenario, CHAOS is not just a state—it's a class !
To make your search easier, use the DNS (Domain Name System) protocol.
Just as DNS helps you find the exact address of a website among billions of possibilities, it will guide you to locate the flag in this mess.
Ready to tackle the CHAOS class and find that elusive flag in the SINK (DNS TYPE 40) ?

Let's get scrubbing and let DNS lead the way!

Start with the following info:
- domain name : dishes.be
- hints : hints.dishes.be
- server IP address : See below

The server is listening on
dig @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053

## Write-up

The description emphasizes that “CHAOS is not just a state—it's a class!” and it refers to the “SINK” (DNS TYPE 40). In DNS there is indeed a CHAOS class (often used to query things like the server’s version via a query for version.bind), but TYPE40 isn’t a standard type—it’s been repurposed for this CTF.

``` shell
┌──(osboxes㉿osboxes)-[~/Desktop]
└─$ dig @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 flag.dishes.be TYPE40 CHAOS


; <<>> DiG 9.19.17-2~kali1-Kali <<>> @chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be -p 5053 flag.dishes.be TYPE40 CHAOS
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 10289
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;flag.dishes.be.                        CH      SINK

;; ANSWER SECTION:
flag.dishes.be.         300     CH      SINK    40 0 0 Q1NDe05vTW9yZURpcnR5RGlzaGVzSW5UaGVLaXRjaGVuU0lOS30=

;; Query time: 39 msec
;; SERVER: 52.18.250.78#5053(chaos_in_the_kitchen_sink.challenges.cybersecuritychallenge.be) (UDP)
;; WHEN: Sat Mar 15 17:52:34 EDT 2025
;; MSG SIZE  rcvd: 85
```

go to [https://cyberchef.org](https://cyberchef.org):

Q1NDe05vTW9yZURpcnR5RGlzaGVzSW5UaGVLaXRjaGVuU0lOS30= from Base64 -> CSC{NoMoreDirtyDishesInTheKitchenSINK}

## Solve script
/

## Flag
`CSC{NoMoreDirtyDishesInTheKitchenSINK}`







