# Google Code Jam Analytics
https://www.facebook.com/notes/kien-pham/google-code-jam-analytics/10153427936615951

## Overview
**What is Google Code Jam?**
It's a yearly coding challenge to test your coding skill. [more info...](https://code.google.com/codejam)

## Analysis for Qualification Round 2016
contest id 6254486

### Participants
How many people participated: **27170**

### Programing Language Stats
How many different programming language being used: **59**

Top 30 most used programming language: **xxx**

Top 30 people used these programming language: **xxx**

raw data:

`[('C++', 10153), ('Python', 4618), ('Java', 4605), ('C', 858), ('Smalltalk', 827), ('Text', 328), ('Ruby', 316), ('JavaScript', 226), ('Haskell', 155), ('PHP', 147), ('Scala', 125), ('Go', 125), ('MUF', 80), ('Perl6', 62), ('RenderScript', 33), ('Swift', 33), ('Groovy', 24), ('OCaml', 24), ('Pascal', 21), ('Clojure', 21), ('Jupyter Notebook', 21), ('Kotlin', 19), ('R', 17), ('Common Lisp', 16), ('Lua', 16), ('Makefile', 15), ('HTML', 14), ('Elixir', 10), ('Erlang', 10), ('Visual Basic', 10), ('XML', 9), ('Groff', 8), ('CoffeeScript', 8), ('Julia', 7), ('Racket', 7), ('GLSL', 6), ('Shell', 5), ('Dart', 5), ('F#', 4), ('Limbo', 4), ('Crystal', 4), ('Scheme', 4), ('Awk', 2), ('Tcl', 2), ('J', 2), ('Factor', 2), ('Perl', 2), ('JSON', 1), ('PowerShell', 1), ('SQLPL', 1), ('YAML', 1), ('APL', 1), ('ActionScript', 1), ('Elm', 1), ('Turing', 1), ('LOLCODE', 1), ('AppleScript', 1), ('Processing', 1), ('Unknown', 1)]`

## Countries Stats

How many countries participated: **xxx**

Top 30 person came from these 15 countries:

raw data

`[('India', 6254), ('United States', 3746), ('China', 2022), ('Russia', 987), ('South Korea', 833), ('Canada', 788), ('Japan', 734), ('Brazil', 615), ('France', 583), ('Bangladesh', 544), ('Taiwan', 502), ('Egypt', 489), ('Ukraine', 459), ('Poland', 403), ('Germany', 380), ('Australia', 375), ('United Kingdom', 325), ('Thailand', 302), ('Spain', 281), ('Pakistan', 259), ('Indonesia', 254), ('Vietnam', 252), ('Singapore', 249), ('Colombia', 249), ('Mexico', 241), ('Romania', 237), ('Hong Kong', 225), ('Israel', 223), ('Italy', 220), ('Turkey', 174), ('Netherlands', 168), ('Hungary', 167), ('Iran', 153), ('Argentina', 146), ('Belarus', 146), ('Greece', 140), ('Sweden', 136), ('Slovakia', 133), ('South Africa', 131), ('New Zealand', 124), ('Czech Republic', 114), ('Belgium', 105), ('Portugal', 104), ('Switzerland', 94), ('Kazakhstan', 92), ('Sri Lanka', 90), ('Bulgaria', 84), ('Peru', 82), ('Tunisia', 78), ('Bolivia', 76), ('Nigeria', 68), ('Morocco', 66), ('Croatia', 61), ('Philippines', 59), ('Lithuania', 57), ('Decline to Answer', 56), ('Venezuela', 54), ('Austria', 52), ('Denmark', 50), ('Norway', 44), ('Malaysia', 43), ('Chile', 42), ('Georgia', 40), ('Slovenia', 39), ('Ireland', 37), ('Finland', 36), ('Jordan', 35), ('Serbia', 35), ('Cameroon', 34), ('Estonia', 32), ('Latvia', 31), ('Moldova', 30), ('Azerbaijan', 28), ('Nepal', 26), ('Lebanon', 26), ('Armenia', 25), ('Algeria', 25), ('Kenya', 23), ('Uzbekistan', 23), ('Iceland', 21), ('Palestine', 19), ('Macedonia [FYROM]', 18), ('Uruguay', 17), ('Benin', 14), ('Mongolia', 13), ('Turkmenistan', 12), ('Kyrgyzstan', 12), ('Ethiopia', 12), ('Saudi Arabia', 11), ('Albania', 11), ('Kosovo', 11), ('Jamaica', 11), ('Cyprus', 9), ('United Arab Emirates', 9), ('Dominican Republic', 8), ('Tajikistan', 8), ('Costa Rica', 8), ('Macau', 8), ('Afghanistan', 8), ('Syria', 8), ('Zimbabwe', 7), ('Cambodia', 7), ('Ghana', 7), ('Malta', 7), ('Ecuador', 7), ('Guatemala', 6), ('Antarctica', 6), ('Togo', 5), ('Nicaragua', 5), ('Kuwait', 5), ('Paraguay', 5), ('Luxembourg', 5), ('Bosnia and Herzegovina', 5), ('Senegal', 4), ('Guadeloupe', 3), ('Trinidad and Tobago', 3), ('Cuba', 3), ('Andorra', 3), ('Namibia', 3), ('Yemen', 3), ('Mauritius', 3), ('Haiti', 3), ('Anguilla', 3), ("Côte d'Ivoire", 3), ('Rwanda', 3), ('Mozambique', 2), ('Angola', 2), ('U.S. Minor Outlying Islands', 2), ('U.S. Virgin Islands', 2), ('Bahrain', 2), ('Zambia', 2), ('Puerto Rico', 2), ('Mali', 2), ('Åland Islands', 2), ('Lesotho', 2), ('Tanzania', 2), ('Gabon', 2), ('Oman', 2), ('Réunion', 2), ('Qatar', 1), ('Sint Maarten', 1), ('Saint Barthélemy', 1), ('Uganda', 1), ('French Polynesia', 1), ('Guernsey', 1), ('Vatican City', 1), ('Montenegro', 1), ('Guinea', 1), ('Christmas Island', 1), ('New Caledonia', 1), ('Bhutan', 1), ('Isle of Man', 1), ('Botswana', 1), ('Wallis and Futuna', 1), ('Brunei', 1), ('Congo [Republic]', 1), ('Marshall Islands', 1), ('Congo [DRC]', 1), ('Aruba', 1), ('Western Sahara', 1), ('Panama', 1), ('Tonga', 1), ('Myanmar [Burma]', 1), ('Cayman Islands', 1), ('North Korea', 1), ('San Marino', 1), ('Greenland', 1), ('Burundi', 1), ('Liechtenstein', 1), ('Papua New Guinea', 1), ('Madagascar', 1), ('Somalia', 1), ('Eritrea', 1)]
`

## How to do your own analysis
There are two set of raw data you can download: the scoreboard and the submission source code.

    # Download the scoreboard for a specific contest
    $ python gcj_analytics.py --contest-id 6254486 --task download-scoreboard

    # Download all code submission
    $ python gcj_analytics.py --contest-id 6254486 --task download-source-code
