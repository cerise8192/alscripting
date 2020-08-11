<HTML>
<HEAD><TITLE>eHP list</TITLE></HEAD>
<BODY>
# alscripting

- build-al.py
Reads the wiki at https://azurlane.koumakan.jp/List_of_Ships_by_Stats and
builds al.json

- al.json
A cached version so you don't hit koumakan a ton.

- ehp.py
Reads al.json and computes effective HP for all ships by the following formula:

HP/(1-DR)/((0.1+(eHIT/(eHIT+(EVA*(1+EVA_stat_buff)+2)))+((eLUCK-LUCK)/1000)-(EVA_rate_buff)))/armor_mod

armor_mod is .25 for Heavy, .55 for Medium, 1 for Light
EVA_rate_buff and EVA_stat_buff are assumed to be 0
eHIT is the enemy's chance to hit.  Set to 100.
eLUCK is the enemy's luck.  Set to 50.
DR is the effect of current damage reduction.  Set to 0
LUCK and HP are your ship's luck & hp.

- build_list.sh
The script that I use to generate ehp.html

- ehp.html
The actual listing
<P>
<h2>BB</h2>
42741 Friedrich der Große
41786 Littorio
40841 Richelieu
40813 Bismarck
40665 Nagato
40640 Kaga (Battleship)
40312 Washington
40077 Warspite (Retrofit)
39988 Howe
39926 Sovetskaya Rossiya
39733 Tirpitz
39704 King George V
39598 Izumo
39542 Suruga
39493 Duke of York
39428 South Dakota
38879 Warspite
38847 Jean Bart
38787 North Carolina
38685 Alabama
38494 Massachusetts
37355 Tosa
37179 Rodney
37121 Nelson
37101 Mutsu
37015 Prince of Wales
36567 Georgia
36350 Super Gamer Kizuna AI
36216 Monarch
36120 Gascogne µ
35990 Valiant
35960 Gascogne
35884 Maryland
35480 Colorado
35228 West Virginia
34731 Giulio Cesare
34707 Queen Elizabeth
34023 Tennessee
33848 Ise
33848 Hyuuga
33727 Pennsylvania
33700 Nevada (Retrofit)
33445 California
32934 Conte di Cavour
32918 Yamashiro
32443 Gangut
32223 Oklahoma (Retrofit)
31433 Arizona
31149 Oklahoma
31122 Fusou
25508 Mikasa
14335 Champagne
<P>
<h2>BBV</h2>
34495 Yamashiro (Retrofit)
34413 Ise (Retrofit)
32697 Fusou (Retrofit)
<P>
<h2>BC</h2>
32589 Odin
18467 Hood
16937 Gneisenau
16841 Amagi
16504 Scharnhorst
15156 Dunkerque
15029 Little Renown
14599 Haruna
14529 Kongou
14424 Kirishima
14424 Hiei
14386 Renown
14359 Hiei-chan
12873 Repulse
<P>
<h2>BM</h2>
5415 Erebus
5206 Abercrombie
4891 Terror
<P>
<h2>CA</h2>
16673 Prinz Eugen
15514 Portland (Retrofit)
15255 Roon
14747 Myoukou
14656 Nachi
14413 Drake
13940 Saint Louis
13131 Cheshire
13130 Algérie
12955 Admiral Hipper
12779 Ibuki
12762 Zara
12626 Admiral Hipper µ
12554 Norfolk
12517 Elegant Kizuna AI
12262 Mogami (Retrofit)
12258 Dorsetshire
12249 Takao
12125 Bremerton
11968 Choukai
11931 Maya
11931 Atago
11908 Portland
11553 Ashigara
11546 Baltimore
11445 Indianapolis
11271 Black Heart
11093 Suzuya
10946 York (Retrofit)
10739 Minneapolis
10732 Kuon
10615 Exeter (Retrofit)
10501 Admiral Graf Spee
10453 Noire
10102 Deutschland
9969 Exeter
9929 Furutaka (Retrofit)
9914 Kinugasa
9719 Aoba
9518 Vincennes
9481 Quincy
9417 York
9236 Astoria
9182 Kako
9182 Furutaka
6082 London (Retrofit)
5610 Nakiri Ayame
5546 Suffolk (Retrofit)
5243 Sussex
5238 London
5191 Shropshire
5175 Kent
5165 Trento
5132 Suffolk
5026 Wichita
4616 Houston
4595 Salt Lake City
4445 Chicago
4355 Northampton
<P>
<h2>CB</h2>
16971 Azuma
<P>
<h2>CL</h2>
13381 Mainz
10743 Mogami
10727 Mikuma
9468 Avrora
9459 Pamiat Merkuria
8056 Seattle
7377 Edinburgh
7348 Montpelier
7348 Chapayev
7338 Biloxi
7245 Cleveland
7233 Columbia
7220 Denver
7133 HMS Neptune
7001 Belfast
6976 San Diego (Retrofit)
6927 Newcastle (Retrofit)
6842 Birmingham
6727 Rurutie
6694 Sheffield
6679 Purple Heart
6598 Dido
6569 Cleveland µ
6557 San Diego
6538 Glasgow
6514 Leipzig (Retrofit)
6503 Newcastle
6427 Sirius
6347 Émile Bertin (Retrofit)
6340 Gloucester
6290 Jamaica
6276 Sheffield µ
6270 Hermione
6212 Swiftsure
6200 Reno
6195 Köln (Retrofit)
6111 Clevelad
6095 Leipzig
6094 Black Prince
6057 San Juan
6028 La Galissonnière
6026 Helena (Retrofit)
6015 Southampton
5995 HDN Neptune
5959 Karlsruhe (Retrofit)
5953 Phoenix
5948 St. Louis
5902 Émile Bertin
5847 Leander (Retrofit)
5783 Köln
5774 Raleigh
5734 Memphis
5734 Concord
5707 Little Bel
5655 Fiji
5650 Helena
5647 Noshiro
5643 Richmond
5643 Isuzu (Retrofit)
5634 Brooklyn
5633 Li'l Sandy
5617 Marblehead
5591 Königsberg
5589 Honolulu
5563 Karlsruhe
5555 Ajax (Retrofit)
5498 Juneau
5447 Atlanta
5444 Leander
5379 Kinu (Retrofit)
5369 Achilles (Retrofit)
5305 Abukuma (Retrofit)
5251 Isuzu
5202 Jeanne d'Arc
5193 Aurora
5141 Agano
5140 Ajax
5110 Lena
5021 Curacoa (Retrofit)
4968 Achilles
4966 Kinu
4912 Arethusa
4899 Abukuma
4853 Jintsuu (Retrofit)
4841 Nagara
4758 Sendai (Retrofit)
4647 Curacoa
4571 Galatea
4495 Curlew
4445 Jintsuu
4431 Naka
4347 Sendai
4037 Yuubari (Retrofit)
3840 Ning Hai (Retrofit)
3752 Yuubari
3714 Ping Hai (Retrofit)
2985 Ning Hai
2950 Yat Sen
2877 Ping Hai
<P>
<h2>CV</h2>
38727 Taihou
35580 Formidable
35122 Victorious
34937 Illustrious
31662 Little Illustrious
18526 Zuikaku
18163 Saratoga (Retrofit)
17845 Graf Zeppelin
17627 Saratoga
17239 Essex
17205 Zeppy
17069 Shangri-La
16893 Lexington
16887 Enterprise
16682 Intrepid
16670 Shoukaku
15991 Akagi
15982 Kaga
15896 Bunker Hill
15877 Akagi µ
15693 Tokino Sora
15679 Ark Royal
15190 Green Heart
15171 Akagi-chan
15084 Ookami Mio
14994 Anniversary Kizuna AI
14875 Glorious
14414 Eagle
14015 Yorktown
13986 Souryuu (Retrofit)
13876 Vert
13671 Béarn
13642 Hornet
13310 Hiryuu
12770 Souryuu
12459 Fumiruiru
11355 Wasp
<P>
<h2>CVL</h2>
18297 Centaur
15591 Perseus
14556 Bataan
14542 Unicorn
14412 Murasaki Shion
14374 Junyou
14235 Independence
14029 Ranger (Retrofit)
13636 Ryuuhou
13609 Hiyou
13359 Ranger
13157 Long Island (Retrofit)
12803 Langley (Retrofit)
12627 Chaser
12318 Casablanca
12149 Langley
11939 Ryuujou
11625 Shouhou (Retrofit)
11404 Bogue (Retrofit)
11274 Hermes (Retrofit)
11008 Shouhou
10828 Bogue
10732 Hermes
9881 Houshou
6396 Saraana
6158 Uruuru
<P>
<h2>DD</h2>
6309 Tashkent
5798 Minsk
5605 Yukikaze
5545 Hanazuki
5495 Yoizuki
5495 Harutsuki
5451 Kitakaze
5389 Grozny
5380 Z46
5207 Hamakaze (Retrofit)
5175 Le Triomphant
5159 Niizuki
5133 Tanikaze (Retrofit)
5133 An Shan
5115 Nowaki
5047 Nicholas (Retrofit)
5020 Tai Yuan
4988 Shigure (Retrofit)
4943 Naganami
4937 Z23 (Retrofit)
4912 Chang Chun
4852 Le Malin
4808 Fu Shun
4807 Hamakaze
4779 Makinami
4777 Mullany
4744 Kasumi
4743 Stanly
4741 Tanikaze
4730 Javelin (Retrofit)
4682 Nicholas
4666 Charles Ausburne
4664 Laffey (Retrofit)
4642 Hatsushimo (Retrofit)
4632 Bache
4630 Jenkins
4614 Kiyonami
4591 Radford
4576 Hatsuharu (Retrofit)
4560 Ayanami (Retrofit)
4555 Oyashio
4555 Kuroshio
4544 Z25
4528 Fletcher
4525 Cooper
4517 Kimberly
4510 Z23
4497 Hazelwood
4496 Hibiki
4489 Smalley
4486 Urakaze
4484 White Heart
4453 Carabiniere
4442 Vauquelin
4437 Bailey (Retrofit)
4430 Michishio
4418 Cassin (Retrofit)
4416 Z1 (Retrofit)
4411 Tartu
4407 Kagerou (Retrofit)
4401 Isokaze
4394 Nekone
4394 Halsey Powell
4387 Downes (Retrofit)
4367 Uranami
4366 Maury
4360 Eldridge
4348 Natsuiro Matsuri
4337 Thatcher
4333 Shirakami Fubuki
4316 Shigure
4302 Shiranui (Retrofit)
4292 Ooshio
4283 Kamikaze (Retrofit)
4272 Foote
4270 Fortune (Retrofit)
4266 Matchless
4255 Cygnet (Retrofit)
4227 Aulick
4217 Asashio
4217 Arashio
4208 Z36
4199 Z35
4191 Kizuna AI
4191 Foxhound (Retrofit)
4178 Hammann (Retrofit)
4170 Musketeer
4168 Eskimo
4167 Icarus
4160 Z20
4160 Sims (Retrofit)
4127 Bush
4096 Yuugure (Retrofit)
4090 Blanc
4057 Z2
4057 Amazon (Retrofit)
4054 Inazuma
4052 Kagerou
4037 Hatsushimo
4036 Kalk
4026 Kawakaze
4025 Z1
4010 Benson
4008 Ikazuchi
3983 Hatsuharu
3980 Bailey
3979 Ayanami
3978 Z19
3975 Hobby
3974 Gridley
3973 Shiranui
3970 Z18
3969 Yuudachi
3966 Comet (Retrofit)
3945 Akatsuki
3931 Fubuki
3923 Z21
3898 Javelin
3897 Wakaba
3895 Craven
3887 Laffey
3886 Ariake
3883 Hatakaze
3882 Spence
3876 Acasta (Retrofit)
3873 Kamikaze
3857 Matsukaze (Retrofit)
3834 L'Opiniâtre
3799 Ardent (Retrofit)
3792 Shiratsuyu
3766 Aylwin
3749 McCall
3749 Cassin
3744 Hammann
3740 Crescent (Retrofit)
3729 Sims
3724 Downes
3670 Jupiter
3638 Mutsuki (Retrofit)
3605 Dewey
3567 Juno
3542 Yuugure
3526 Hardy
3488 Matsukaze
3485 Kisaragi (Retrofit)
3484 Forbin (Retrofit)
3474 Fortune
3470 Le Téméraire
3461 Grenville
3446 Amazon
3443 Echo
3410 Cygnet
3409 Jersey
3402 Foxhound
3367 Beagle
3349 Minazuki
3339 Nagatsuki
3338 Forbin
3318 Bulldog
3311 Mikazuki
3289 Uzuki
3281 Fumizuki
3275 Mutsuki
3262 Comet
3249 Glowworm
3196 Acasta
3138 Ardent
3137 Kisaragi
3120 Crescent
3068 Hunter
3010 Le Mars
2954 Vampire
2823 22
2781 33
456 Prototype Bulin MKII
<P>
<h2>SS</h2>
3144 Surcouf
2570 I-26
2563 I-58
2526 I-56
2497 Albacore
2462 Cavalla
2437 I-168
2416 I-25
2165 Dace
2157 Bluegill
1765 U-522
1738 U-110
1618 U-101
1548 U-47
1546 U-81
1529 U-556
1498 U-73
1481 U-557
<P>
<h2>SSV</h2>
3108 I-13
<P>
</BODY>
</HTML>
