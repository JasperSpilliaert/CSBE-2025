# CHALLENGE_TITLE
Our encryption is secret

## Category
Programming

## Estimated difficulty
Medium

## Description

Me and my best friend communicate exclusively via password-protected ZIP files.
It's a great way to ensure our privacy, and on top of that, it's extremely portable.
It does, however, tend to wear down our numpads.

## Write-up

We get a file with 19 ZIP files. 

I first tried to crack just using /usr/share/worlists/rockyou.txt

Then I saw I got the first 2 cracked

0.zip: 1 -> C
1.zip: 9 -> S

I quickly made a script to make a wordlist with only numbers till 999

![numbers.py](./Resources/numbers.py)

plus a script to bruteforce with john (ChatGPT xp):

![zip.py](./Resources/zip.py)

I quickly got the next few:

```
2.zip: 251 -> C
3.zip: 31591 -> { 
4.zip: 10862713 -> O 
```

We let it run for some time for the next one but it didn't come quickly. We moved on but knew there was some sort of pattern

Then the next morning we put it in here https://oeis.org/ and got the solution directly :

```
5.zip: 14467532003 -> E
6.zip: 31797494201591 -> I
7.zip: 156248170093443583 -> S
8.zip: 1071839248022015186797 -> _
9.zip: 13041980716182955257968099 -> 5
10.zip: 318091971114753602661286869511 -> e
11.zip: 9476548712979446302049526230869201 -> q
12.zip: 480023689406029082552168595228062835253 -> 5
13.zip: 33084121337970195065727147329321045432113013 -> _
14.zip: 2630447399124194597215353875856630495447910685591 -> r
15.zip: 273103179546961363755681110617046977877856027619141393 -> U
16.zip: 40659014544749437043977893440134416866913234596211623386661 -> I
17.zip: 8350542359607778288560184757448232740362339786695496947100866519 -> 3
18.zip: 1895421563785307091692560351018414917406309718462035628632253986992139 -> }
```

## Solve script

/

## Flag

`CSC{OEIS_5eq5_rUI3}`


