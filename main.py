#!/usr/bin/env python3
import sys
import requests
import operator

if __name__ == '__main__':
    print('Google Code Jam Analytics!')

    pos = 1
    contest_id = '6254486'
    page = requests.get("https://code.google.com/codejam/contest/6254486/scoreboard/do/?cmd=GetScoreboard&contest_id={}&show_type=all&start_pos={}".format(contest_id, pos))
    page_data = page.json()

    stats = page_data['stat']
    last_pos = page_data['stat']['nrp']
    print(last_pos)

    countries = {}
    users = {}
    for row in page_data['rows']:
        users[row['n']] = {
            'country': row['c'],
            'penalty': row['pen'],
            'avatar': row['fu'],
        }
        countries[row['c']] = countries[row['c']] + 1 if row['c'] in countries else 1
        # print(row)
        # exit()
    print(countries)
    print(sorted(countries.items(), key=operator.itemgetter(1)))

    # print(page_data)
    # print(stats)
