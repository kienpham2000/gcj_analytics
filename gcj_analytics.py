#!/usr/bin/env python3
import os
import sys
import requests
import operator
import json
import grequests
import yaml
from zipfile import ZipFile
import argparse
import operator
from collections import OrderedDict
import operator
from os import listdir
from os.path import isfile, join

class GCJ:
    def __init__(self, contest_id, worker):
        self.contest_id = contest_id.strip()
        self.worker = int(worker)
        self.url = "https://code.google.com/codejam/contest/{}/scoreboard/do".format(contest_id)
        self.scoreboard_file_path = "raw/{}/scoreboard.json".format(contest_id)

    def get_stats(self):
        payload = {
            'total_participants': self.get_total_participants()
        }

        return json.dumps(payload)

    def get_total_participants(self):
        params = {"cmd": "GetScoreboard", "contest_id": self.contest_id, "show_type": "all", "start_pos": 1}
        total = requests.get(self.url, params).json()

        return total['stat']['nrp']

    def download_scoreboard(self):
        pos = 1
        records_per_page = 30
        total = self.get_total_participants()

        os.makedirs('raw/{}'.format(self.contest_id), exist_ok=True)
        with open(self.scoreboard_file_path, 'w') as f:
            while True:

                gen_params = []
                for x in range(pos, pos+records_per_page*self.worker, records_per_page):
                    params = {"start_pos": x, "cmd": "GetScoreboard", "contest_id": self.contest_id, "show_type": "all"}
                    gen_params.append(params)

                rs = (grequests.get(self.url, params=p) for p in gen_params)
                res = grequests.map(rs)

                for each_res in res:
                    try:
                        each_res_data = each_res.json()

                        if 'err' in each_res_data:
                            print('Done!')

                            return True

                        print("{}".format(json.dumps(each_res_data)), file=f)
                    except AttributeError:
                        continue

                pos = pos + (records_per_page*self.worker)
                print("pos {} out of total {}: {}%".format(pos, total, int(pos/total*100)))
                if pos > total:
                    break

    def download_source_code(self, problem_id):
        records_per_page = 30
        processed = 0
        total = self.get_total_participants()

        os.makedirs('raw/{}/{}'.format(self.contest_id, problem_id), exist_ok=True)
        with open(self.scoreboard_file_path, 'r') as f:
            batch_url = []

            for line in f:
                line_data = json.loads(line)

                gen_params = []
                for v in line_data['rows']:
                    params = {"cmd": "GetSourceCode", "problem": problem_id, "io_set_id": "0", "username": v['n']}
                    gen_params.append(params)

                rs = (grequests.get(self.url, params=p) for p in gen_params)
                res = grequests.map(rs)
                # print(res)
                # exit()
                for each_res in res:
                    try:
                        file_name = each_res.headers.get('Content-Disposition').split('=')[1]

                        with open('raw/{}/{}/{}'.format(self.contest_id, problem_id, file_name), 'wb+') as f:
                            print(file_name)
                            f.write(each_res.content)
                    except:
                        print('problem download / saving file...')
                        pass


    def countries(self):
        countries = {}

        with open(self.scoreboard_file_path, 'r') as f:
            for line in f:
                line_data = json.loads(line)

                for row in line_data['rows']:
                    name = row['c']
                    print(name)
                    if name in countries:
                        countries[name] += 1
                    else:
                        countries[name] = 1

                    # users[row['n']] = {
                    #     'country': row['c'],
                    #     'penalty': row['pen'],
                    #     'avatar': row['fu'],
                    # }
                    # countries[row['c']] = countries[row['c']] + 1 if row['c'] in countries else 1

        countries = sorted(countries.items(), key=operator.itemgetter(1), reverse=True)
        print(countries)

    def detect_programming_language(self, problem_id):
        with open('extensions.json') as data_file:
            extensions = json.load(data_file)

        path = 'raw/{}/{}'.format(self.contest_id, problem_id)
        files = [f for f in listdir(path) if isfile(join(path, f))]

        languages = {}
        for f in files:
            input_zip = ZipFile("{}/{}".format(path, f))
            for name in input_zip.namelist():
                try:
                    name = extensions['.' + name.split('.')[1].lower()]
                    print(name)
                    if name in languages:
                        languages[name] += 1
                    else:
                        languages[name] = 1
                except:
                    languages['Unknown'] = 1

        languages = sorted(languages.items(), key=operator.itemgetter(1), reverse=True)
        # languages = OrderedDict(sorted(languages.items(), reverse=True))
        print(languages)
        return languages

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", help="What task to run", required=True)
    parser.add_argument("--contest-id", help="The contest id", required=True)
    parser.add_argument("--worker", help="The # of worker", default=60, type=int)
    parser.add_argument("--problem-id", help="The problem id")
    args = parser.parse_args()

    if args.worker <= 0:
        exit("Seriously?")

    gcj = GCJ(args.contest_id, worker=args.worker)

    if args.task == 'download-scoreboard':
        gcj.download_scoreboard()
    elif args.task == 'download-source-code':
        if not args.problem_id:
            exit('--problem-id is required')
        gcj.download_source_code(problem_id=args.problem_id)
    elif args.task == 'detect-programming-language':
        if not args.problem_id:
            exit('--problem-id is required')
        gcj.detect_programming_language(problem_id=args.problem_id)
    elif args.task == 'total-participants':
        print(gcj.get_total_participants())
    elif args.task == 'stats':
        print(gcj.get_stats())
    elif args.task == 'countries':
        gcj.countries()
