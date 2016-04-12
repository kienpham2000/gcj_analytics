#!/usr/bin/env python3
import sys
import requests
import operator
import json
import grequests
import yaml
from zipfile import ZipFile
import argparse

def download_scoreboard():
    pos = 1
    # pos = 99999999
    url = "https://code.google.com/codejam/contest/{}/scoreboard/do/?cmd=GetScoreboard&contest_id={}&show_type=all&start_pos=".format(contest_id, contest_id)

    while True:
        urls = ["{}{}".format(url, x) for x in range(pos, pos+threads)]
        rs = (grequests.get(u) for u in urls)
        res = grequests.map(rs)
        print("pos {} out of {}: {}%".format(pos, total_participated, int(pos/total_participated*100)))

        for each_res in res:
            try:
                each_res_data = each_res.json()
            except AttributeError:
                print(each_res_data)
                continue

            # {"err": "invalid value for parameter sp"}
            if 'err' in each_res_data:
                exit('Done!')

            total_participated = each_res_data['stat']['nrp']
            with open('raw/scoreboard.json', 'a+') as f:
                print("{}".format(json.dumps(each_res_data)), file=f)
            # exit()
        pos += threads


def download_source_code():
    threads = 100
    processed = 0
    url = "https://code.google.com/codejam/contest/6254486/scoreboard/do/?cmd=GetSourceCode&problem=5634697451274240&io_set_id=0&username="
    with open('raw/scoreboard.json', 'r') as f:
        batch_url = []

        for line in f:
            line_data = json.loads(line)
            total_participated = line_data['stat']['nrp']

            for v in line_data['rows']:
                username = v['n']
                # print(username)
                batch_url.append('{}{}'.format(url, username))
                if len(batch_url) >= threads:
                    rs = (grequests.get(u) for u in batch_url)
                    res = grequests.map(rs)
                    for each_res in res:
                        try:
                            file_name = each_res.headers.get('Content-Disposition').split('=')[1]

                            with open('raw/source/{}'.format(file_name), 'wb') as f:
                                # print(file_name)
                                f.write(each_res.content)
                        except:
                            pass

                    processed += threads
                    print("pos {} out of {}: {}%".format(processed, total_participated, int(processed/total_participated*100)))

def detect_programming_language(file_path):
    with open('extensions.json') as data_file:
        extensions = json.load(data_file)

    languages = {}
    input_zip=ZipFile('raw/source/kienpham_1_0.zip')
    for name in input_zip.namelist():
        try:
            languages[extensions['.' + name.split('.')[1].lower()]] = 1
        except:
            languages['Unknown'] = 1

    return languages

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.parse_args()
    parser.add_argument("echo")
    args = parser.parse_args()
    print(args.echo)
    exit()

    total_participated = 1
    countries = {}
    countries_top_30 = {}
    users = {}
    threads = 100

    contest_id = '6254486' if len(sys.argv) < 2 else sys.argv[1]

    download_scoreboard(contest_id)
    exit()

    # download_source_code()
    # exit()

    # detect_programming_language()
    # exit()



    exit()

    stats = page_data['stat']
    total_participated = page_data['stat']['nrp']

    for row in page_data['rows']:
        users[row['n']] = {
            'country': row['c'],
            'penalty': row['pen'],
            'avatar': row['fu'],
        }

        countries[row['c']] = countries[row['c']] + 1 if row['c'] in countries else 1

    if pos == 1:
        countries_top_30 = sorted(countries.items(), key=operator.itemgetter(1), reverse=True)

    # print(countries_top_30)
    # print(stats)
