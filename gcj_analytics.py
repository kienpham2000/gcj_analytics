#!/usr/bin/env python3
import sys
import requests
import operator
import json
import grequests
import yaml
from zipfile import ZipFile
import argparse

class GCJ:
    def __init__(self, contest_id, worker):
        self.contest_id = contest_id.strip()
        self.worker = int(worker)
        self._base_url = "https://code.google.com/codejam/contest/{}/scoreboard/do".format(contest_id)

    def get_stats(self):
        payload = {
            'total_participants': self.get_total_participants()
        }

        return json.dumps(payload)

    def get_total_participants(self):
        params = {"cmd": "GetScoreboard", "contest_id": self.contest_id, "show_type": "all", "start_pos": 1}
        total = requests.get(self._base_url, params).json()

        return total['stat']['nrp']

    def download_scoreboard(self):
        pos = 1
        records_per_page = 30
        total = self.get_total_participants()

        with open('raw/scoreboard.json', 'w') as f:
            while True:

                gen_params = []
                for x in range(pos, pos+records_per_page*self.worker, records_per_page):
                    params = {"start_pos": x, "cmd": "GetScoreboard", "contest_id": self.contest_id, "show_type": "all"}
                    gen_params.append(params)
                # print(gen_params)
                # print(pos, pos+self.worker)
                # exit()
                rs = (grequests.get(self._base_url, params=p) for p in gen_params)
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
        problem_id = '5634697451274240'
        def _download(urls, params):
            rs = (grequests.get(u) for u in urls)
            res = grequests.map(rs)


        processed = 0

        total = self.get_total_participants()

        with open('raw/scoreboard.json', 'r') as f:
            batch_url = []

            for line in f:
                line_data = json.loads(line)

                gen_params = []
                for v in line_data['rows']:
                    params = {"cmd": "GetSourceCode", "problem": problem_id, "io_set_id": "0", "username": v['n']}
                    gen_params.append(params)
                # print(gen_params)
                # exit()

                rs = (grequests.get(self._base_url, params=p) for p in gen_params)
                res = grequests.map(rs)
                print(res)
                # exit()
                for each_res in res:
                    try:
                        file_name = each_res.headers.get('Content-Disposition').split('=')[1]

                        with open('raw/source/{}'.format(file_name), 'wb') as f:
                            print(file_name)
                            f.write(each_res.content)
                    except:
                        print('problem saving...')
                        pass

                # for v in line_data['rows']:
                #
                #     params['username'] = v['n']
                #
                #
                #     batch_url.append(self._base_url)
                #     if len(batch_url) >= self.worker:
                #         _download()
                #
                #         processed += threads
                #         print("pos {} out of {}: {}%".format(processed, total_participated, int(processed/total_participated*100)))

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
        gcj.download_source_code(problem_id=args.problem_id)
    elif args.task == 'total-participants':
        print(gcj.get_total_participants())
    elif args.task == 'stats':
        print(gcj.get_stats())


    # total_participated = 1
    # countries = {}
    # countries_top_30 = {}
    # users = {}
    # threads = 100
    # download_scoreboard(contest_id)

    # download_source_code()
    # exit()

    # detect_programming_language()
    # exit()
    #
    # stats = page_data['stat']
    # total_participated = page_data['stat']['nrp']
    #
    # for row in page_data['rows']:
    #     users[row['n']] = {
    #         'country': row['c'],
    #         'penalty': row['pen'],
    #         'avatar': row['fu'],
    #     }
    #
    #     countries[row['c']] = countries[row['c']] + 1 if row['c'] in countries else 1
    #
    # if pos == 1:
    #     countries_top_30 = sorted(countries.items(), key=operator.itemgetter(1), reverse=True)

    # print(countries_top_30)
    # print(stats)
