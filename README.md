<BODY>
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
42741 Friedrich der Große<BR>
41786 Littorio<BR>
40841 Richelieu<BR>
40813 Bismarck<BR>
40665 Nagato<BR>
40640 Kaga (Battleship)<BR>
40312 Washington<BR>
40077 Warspite (Retrofit)<BR>
39988 Howe<BR>
39926 Sovetskaya Rossiya<BR>
39733 Tirpitz<BR>
39704 King George V<BR>
39598 Izumo<BR>
39542 Suruga<BR>
39493 Duke of York<BR>
39428 South Dakota<BR>
38879 Warspite<BR>
38847 Jean Bart<BR>
38787 North Carolina<BR>
38685 Alabama<BR>
38494 Massachusetts<BR>
37355 Tosa<BR>
37179 Rodney<BR>
37121 Nelson<BR>
37101 Mutsu<BR>
37015 Prince of Wales<BR>
36567 Georgia<BR>
36350 Super Gamer Kizuna AI<BR>
36216 Monarch<BR>
36120 Gascogne µ<BR>
35990 Valiant<BR>
35960 Gascogne<BR>
35884 Maryland<BR>
35480 Colorado<BR>
35228 West Virginia<BR>
34731 Giulio Cesare<BR>
34707 Queen Elizabeth<BR>
34023 Tennessee<BR>
33848 Ise<BR>
33848 Hyuuga<BR>
33727 Pennsylvania<BR>
33700 Nevada (Retrofit)<BR>
33445 California<BR>
32934 Conte di Cavour<BR>
32918 Yamashiro<BR>
32443 Gangut<BR>
32223 Oklahoma (Retrofit)<BR>
31433 Arizona<BR>
31149 Oklahoma<BR>
31122 Fusou<BR>
25508 Mikasa<BR>
14335 Champagne<BR>
<P>
<h2>BBV</h2>
34495 Yamashiro (Retrofit)<BR>
34413 Ise (Retrofit)<BR>
32697 Fusou (Retrofit)<BR>
<P>
<h2>BC</h2>
32589 Odin<BR>
18467 Hood<BR>
16937 Gneisenau<BR>
16841 Amagi<BR>
16504 Scharnhorst<BR>
15156 Dunkerque<BR>
15029 Little Renown<BR>
14599 Haruna<BR>
14529 Kongou<BR>
14424 Kirishima<BR>
14424 Hiei<BR>
14386 Renown<BR>
14359 Hiei-chan<BR>
12873 Repulse<BR>
<P>
<h2>BM</h2>
5415 Erebus<BR>
5206 Abercrombie<BR>
4891 Terror<BR>
<P>
<h2>CA</h2>
16673 Prinz Eugen<BR>
15514 Portland (Retrofit)<BR>
15255 Roon<BR>
14747 Myoukou<BR>
14656 Nachi<BR>
14413 Drake<BR>
13940 Saint Louis<BR>
13131 Cheshire<BR>
13130 Algérie<BR>
12955 Admiral Hipper<BR>
12779 Ibuki<BR>
12762 Zara<BR>
12626 Admiral Hipper µ<BR>
12554 Norfolk<BR>
12517 Elegant Kizuna AI<BR>
12262 Mogami (Retrofit)<BR>
12258 Dorsetshire<BR>
12249 Takao<BR>
12125 Bremerton<BR>
11968 Choukai<BR>
11931 Maya<BR>
11931 Atago<BR>
11908 Portland<BR>
11553 Ashigara<BR>
11546 Baltimore<BR>
11445 Indianapolis<BR>
11271 Black Heart<BR>
11093 Suzuya<BR>
10946 York (Retrofit)<BR>
10739 Minneapolis<BR>
10732 Kuon<BR>
10615 Exeter (Retrofit)<BR>
10501 Admiral Graf Spee<BR>
10453 Noire<BR>
10102 Deutschland<BR>
9969 Exeter<BR>
9929 Furutaka (Retrofit)<BR>
9914 Kinugasa<BR>
9719 Aoba<BR>
9518 Vincennes<BR>
9481 Quincy<BR>
9417 York<BR>
9236 Astoria<BR>
9182 Kako<BR>
9182 Furutaka<BR>
6082 London (Retrofit)<BR>
5610 Nakiri Ayame<BR>
5546 Suffolk (Retrofit)<BR>
5243 Sussex<BR>
5238 London<BR>
5191 Shropshire<BR>
5175 Kent<BR>
5165 Trento<BR>
5132 Suffolk<BR>
5026 Wichita<BR>
4616 Houston<BR>
4595 Salt Lake City<BR>
4445 Chicago<BR>
4355 Northampton<BR>
<P>
<h2>CB</h2>
16971 Azuma<BR>
<P>
<h2>CL</h2>
13381 Mainz<BR>
10743 Mogami<BR>
10727 Mikuma<BR>
9468 Avrora<BR>
9459 Pamiat Merkuria<BR>
8056 Seattle<BR>
7377 Edinburgh<BR>
7348 Montpelier<BR>
7348 Chapayev<BR>
7338 Biloxi<BR>
7245 Cleveland<BR>
7233 Columbia<BR>
7220 Denver<BR>
7133 HMS Neptune<BR>
7001 Belfast<BR>
6976 San Diego (Retrofit)<BR>
6927 Newcastle (Retrofit)<BR>
6842 Birmingham<BR>
6727 Rurutie<BR>
6694 Sheffield<BR>
6679 Purple Heart<BR>
6598 Dido<BR>
6569 Cleveland µ<BR>
6557 San Diego<BR>
6538 Glasgow<BR>
6514 Leipzig (Retrofit)<BR>
6503 Newcastle<BR>
6427 Sirius<BR>
6347 Émile Bertin (Retrofit)<BR>
6340 Gloucester<BR>
6290 Jamaica<BR>
6276 Sheffield µ<BR>
6270 Hermione<BR>
6212 Swiftsure<BR>
6200 Reno<BR>
6195 Köln (Retrofit)<BR>
6111 Clevelad<BR>
6095 Leipzig<BR>
6094 Black Prince<BR>
6057 San Juan<BR>
6028 La Galissonnière<BR>
6026 Helena (Retrofit)<BR>
6015 Southampton<BR>
5995 HDN Neptune<BR>
5959 Karlsruhe (Retrofit)<BR>
5953 Phoenix<BR>
5948 St. Louis<BR>
5902 Émile Bertin<BR>
5847 Leander (Retrofit)<BR>
5783 Köln<BR>
5774 Raleigh<BR>
5734 Memphis<BR>
5734 Concord<BR>
5707 Little Bel<BR>
5655 Fiji<BR>
5650 Helena<BR>
5647 Noshiro<BR>
5643 Richmond<BR>
5643 Isuzu (Retrofit)<BR>
5634 Brooklyn<BR>
5633 Li'l Sandy<BR>
5617 Marblehead<BR>
5591 Königsberg<BR>
5589 Honolulu<BR>
5563 Karlsruhe<BR>
5555 Ajax (Retrofit)<BR>
5498 Juneau<BR>
5447 Atlanta<BR>
5444 Leander<BR>
5379 Kinu (Retrofit)<BR>
5369 Achilles (Retrofit)<BR>
5305 Abukuma (Retrofit)<BR>
5251 Isuzu<BR>
5202 Jeanne d'Arc<BR>
5193 Aurora<BR>
5141 Agano<BR>
5140 Ajax<BR>
5110 Lena<BR>
5021 Curacoa (Retrofit)<BR>
4968 Achilles<BR>
4966 Kinu<BR>
4912 Arethusa<BR>
4899 Abukuma<BR>
4853 Jintsuu (Retrofit)<BR>
4841 Nagara<BR>
4758 Sendai (Retrofit)<BR>
4647 Curacoa<BR>
4571 Galatea<BR>
4495 Curlew<BR>
4445 Jintsuu<BR>
4431 Naka<BR>
4347 Sendai<BR>
4037 Yuubari (Retrofit)<BR>
3840 Ning Hai (Retrofit)<BR>
3752 Yuubari<BR>
3714 Ping Hai (Retrofit)<BR>
2985 Ning Hai<BR>
2950 Yat Sen<BR>
2877 Ping Hai<BR>
<P>
<h2>CV</h2>
38727 Taihou<BR>
35580 Formidable<BR>
35122 Victorious<BR>
34937 Illustrious<BR>
31662 Little Illustrious<BR>
18526 Zuikaku<BR>
18163 Saratoga (Retrofit)<BR>
17845 Graf Zeppelin<BR>
17627 Saratoga<BR>
17239 Essex<BR>
17205 Zeppy<BR>
17069 Shangri-La<BR>
16893 Lexington<BR>
16887 Enterprise<BR>
16682 Intrepid<BR>
16670 Shoukaku<BR>
15991 Akagi<BR>
15982 Kaga<BR>
15896 Bunker Hill<BR>
15877 Akagi µ<BR>
15693 Tokino Sora<BR>
15679 Ark Royal<BR>
15190 Green Heart<BR>
15171 Akagi-chan<BR>
15084 Ookami Mio<BR>
14994 Anniversary Kizuna AI<BR>
14875 Glorious<BR>
14414 Eagle<BR>
14015 Yorktown<BR>
13986 Souryuu (Retrofit)<BR>
13876 Vert<BR>
13671 Béarn<BR>
13642 Hornet<BR>
13310 Hiryuu<BR>
12770 Souryuu<BR>
12459 Fumiruiru<BR>
11355 Wasp<BR>
<P>
<h2>CVL</h2>
18297 Centaur<BR>
15591 Perseus<BR>
14556 Bataan<BR>
14542 Unicorn<BR>
14412 Murasaki Shion<BR>
14374 Junyou<BR>
14235 Independence<BR>
14029 Ranger (Retrofit)<BR>
13636 Ryuuhou<BR>
13609 Hiyou<BR>
13359 Ranger<BR>
13157 Long Island (Retrofit)<BR>
12803 Langley (Retrofit)<BR>
12627 Chaser<BR>
12318 Casablanca<BR>
12149 Langley<BR>
11939 Ryuujou<BR>
11625 Shouhou (Retrofit)<BR>
11404 Bogue (Retrofit)<BR>
11274 Hermes (Retrofit)<BR>
11008 Shouhou<BR>
10828 Bogue<BR>
10732 Hermes<BR>
9881 Houshou<BR>
6396 Saraana<BR>
6158 Uruuru<BR>
<P>
<h2>DD</h2>
6309 Tashkent<BR>
5798 Minsk<BR>
5605 Yukikaze<BR>
5545 Hanazuki<BR>
5495 Yoizuki<BR>
5495 Harutsuki<BR>
5451 Kitakaze<BR>
5389 Grozny<BR>
5380 Z46<BR>
5207 Hamakaze (Retrofit)<BR>
5175 Le Triomphant<BR>
5159 Niizuki<BR>
5133 Tanikaze (Retrofit)<BR>
5133 An Shan<BR>
5115 Nowaki<BR>
5047 Nicholas (Retrofit)<BR>
5020 Tai Yuan<BR>
4988 Shigure (Retrofit)<BR>
4943 Naganami<BR>
4937 Z23 (Retrofit)<BR>
4912 Chang Chun<BR>
4852 Le Malin<BR>
4808 Fu Shun<BR>
4807 Hamakaze<BR>
4779 Makinami<BR>
4777 Mullany<BR>
4744 Kasumi<BR>
4743 Stanly<BR>
4741 Tanikaze<BR>
4730 Javelin (Retrofit)<BR>
4682 Nicholas<BR>
4666 Charles Ausburne<BR>
4664 Laffey (Retrofit)<BR>
4642 Hatsushimo (Retrofit)<BR>
4632 Bache<BR>
4630 Jenkins<BR>
4614 Kiyonami<BR>
4591 Radford<BR>
4576 Hatsuharu (Retrofit)<BR>
4560 Ayanami (Retrofit)<BR>
4555 Oyashio<BR>
4555 Kuroshio<BR>
4544 Z25<BR>
4528 Fletcher<BR>
4525 Cooper<BR>
4517 Kimberly<BR>
4510 Z23<BR>
4497 Hazelwood<BR>
4496 Hibiki<BR>
4489 Smalley<BR>
4486 Urakaze<BR>
4484 White Heart<BR>
4453 Carabiniere<BR>
4442 Vauquelin<BR>
4437 Bailey (Retrofit)<BR>
4430 Michishio<BR>
4418 Cassin (Retrofit)<BR>
4416 Z1 (Retrofit)<BR>
4411 Tartu<BR>
4407 Kagerou (Retrofit)<BR>
4401 Isokaze<BR>
4394 Nekone<BR>
4394 Halsey Powell<BR>
4387 Downes (Retrofit)<BR>
4367 Uranami<BR>
4366 Maury<BR>
4360 Eldridge<BR>
4348 Natsuiro Matsuri<BR>
4337 Thatcher<BR>
4333 Shirakami Fubuki<BR>
4316 Shigure<BR>
4302 Shiranui (Retrofit)<BR>
4292 Ooshio<BR>
4283 Kamikaze (Retrofit)<BR>
4272 Foote<BR>
4270 Fortune (Retrofit)<BR>
4266 Matchless<BR>
4255 Cygnet (Retrofit)<BR>
4227 Aulick<BR>
4217 Asashio<BR>
4217 Arashio<BR>
4208 Z36<BR>
4199 Z35<BR>
4191 Kizuna AI<BR>
4191 Foxhound (Retrofit)<BR>
4178 Hammann (Retrofit)<BR>
4170 Musketeer<BR>
4168 Eskimo<BR>
4167 Icarus<BR>
4160 Z20<BR>
4160 Sims (Retrofit)<BR>
4127 Bush<BR>
4096 Yuugure (Retrofit)<BR>
4090 Blanc<BR>
4057 Z2<BR>
4057 Amazon (Retrofit)<BR>
4054 Inazuma<BR>
4052 Kagerou<BR>
4037 Hatsushimo<BR>
4036 Kalk<BR>
4026 Kawakaze<BR>
4025 Z1<BR>
4010 Benson<BR>
4008 Ikazuchi<BR>
3983 Hatsuharu<BR>
3980 Bailey<BR>
3979 Ayanami<BR>
3978 Z19<BR>
3975 Hobby<BR>
3974 Gridley<BR>
3973 Shiranui<BR>
3970 Z18<BR>
3969 Yuudachi<BR>
3966 Comet (Retrofit)<BR>
3945 Akatsuki<BR>
3931 Fubuki<BR>
3923 Z21<BR>
3898 Javelin<BR>
3897 Wakaba<BR>
3895 Craven<BR>
3887 Laffey<BR>
3886 Ariake<BR>
3883 Hatakaze<BR>
3882 Spence<BR>
3876 Acasta (Retrofit)<BR>
3873 Kamikaze<BR>
3857 Matsukaze (Retrofit)<BR>
3834 L'Opiniâtre<BR>
3799 Ardent (Retrofit)<BR>
3792 Shiratsuyu<BR>
3766 Aylwin<BR>
3749 McCall<BR>
3749 Cassin<BR>
3744 Hammann<BR>
3740 Crescent (Retrofit)<BR>
3729 Sims<BR>
3724 Downes<BR>
3670 Jupiter<BR>
3638 Mutsuki (Retrofit)<BR>
3605 Dewey<BR>
3567 Juno<BR>
3542 Yuugure<BR>
3526 Hardy<BR>
3488 Matsukaze<BR>
3485 Kisaragi (Retrofit)<BR>
3484 Forbin (Retrofit)<BR>
3474 Fortune<BR>
3470 Le Téméraire<BR>
3461 Grenville<BR>
3446 Amazon<BR>
3443 Echo<BR>
3410 Cygnet<BR>
3409 Jersey<BR>
3402 Foxhound<BR>
3367 Beagle<BR>
3349 Minazuki<BR>
3339 Nagatsuki<BR>
3338 Forbin<BR>
3318 Bulldog<BR>
3311 Mikazuki<BR>
3289 Uzuki<BR>
3281 Fumizuki<BR>
3275 Mutsuki<BR>
3262 Comet<BR>
3249 Glowworm<BR>
3196 Acasta<BR>
3138 Ardent<BR>
3137 Kisaragi<BR>
3120 Crescent<BR>
3068 Hunter<BR>
3010 Le Mars<BR>
2954 Vampire<BR>
2823 22<BR>
2781 33<BR>
456 Prototype Bulin MKII<BR>
<P>
<h2>SS</h2>
3144 Surcouf<BR>
2570 I-26<BR>
2563 I-58<BR>
2526 I-56<BR>
2497 Albacore<BR>
2462 Cavalla<BR>
2437 I-168<BR>
2416 I-25<BR>
2165 Dace<BR>
2157 Bluegill<BR>
1765 U-522<BR>
1738 U-110<BR>
1618 U-101<BR>
1548 U-47<BR>
1546 U-81<BR>
1529 U-556<BR>
1498 U-73<BR>
1481 U-557<BR>
<P>
<h2>SSV</h2>
3108 I-13<BR>
<P>
</BODY>
</HTML>
