from flask import Flask
from flask import Markup
from flask import request
from flask import render_template
from datetime import timedelta
from datetime import datetime
import copy
import sys


def ping_pong_index(start_idx, end_idx):
    delta = end_idx - start_idx
    curr_index = start_idx
    while abs(delta) > 0:
        delta_sign = int(delta / abs(delta))
        next_index = curr_index + delta_sign
        yield (curr_index, next_index)
        curr_index += delta
        delta = abs(delta) - 1
        delta *= -delta_sign
    while curr_index < end_idx:
        yield (curr_index, curr_index + 1)
        curr_index += 1


def recursive_find(src, ladder_steps, idx, max_idx, target, found_dict, data):
    if idx < max_idx and src in ladder_steps[idx]:
        for fword in ladder_steps[idx][src]:
            if idx + 1 < max_idx + 1 and fword not in found_dict.values():
                found_dict[idx] = fword
                # print('found_list=', found_dict)
                if fword == target and idx == max_idx - 1:
                    data.append(found_dict.values())
                recursive_find(fword, ladder_steps, idx + 1, max_idx, target, copy.copy(found_dict), data)


app = Flask(__name__)

@app.route('/ladder', methods=['GET'])
def do_chart():
    if len(request.args) == 0:
        return render_template('word_ladder_index.html')

    start = str(request.args.get('top'))
    end = str(request.args.get('bottom'))
    max_steps = int(request.args.get('max_steps'))

    word_len = len(start)
    words = []
    letters = 'abcdefghijklmnopqrstuvwxyz'
    with open('brit-a-z.txt') as fd:
        for l in fd:
            word = l.strip()
            if len(word) == word_len and '\'' not in word:
                words.append(word)

    stages = {0: {start: [start]}, max_steps: {end: [end]}}

    for source_step, target_step in ping_pong_index(0, max_steps):
        # print('source={0}, target={1}'.format(source_step, target_step))
        stage = {}
        for source_word in stages[source_step]:
            for working_word in stages[source_step][source_word]:
                new_words = []
                for pos in range(0, word_len):
                    for ltr in letters:
                        if ltr != working_word[pos]:
                            new_word = working_word[0:pos] + ltr + working_word[pos + 1:]
                            if new_word not in new_words and new_word in words:
                                # print(new_word)
                                new_words.append(new_word)
                if len(new_words) > 0:
                    # print(working_word, new_words)
                    new_words.sort()
                    stage[working_word] = new_words
        # print('stage=', stage)
        try:
            if stages[target_step] is not None and len(stages[target_step]) > 0:
                # print('stop reversal')
                prefound_words = []
                for keyword in stage:
                    prefound_words.append(keyword)
                    for word in stage[keyword]:
                        if word not in prefound_words:
                            prefound_words.append(word)
                words = prefound_words
                words.sort()
                for clear_idx in range(target_step + 1, max_steps + 1):
                    stages[clear_idx] = None
            else:
                stages[target_step] = stage
        except KeyError:
            stages[target_step] = stage
        # print('stages=', stages)

    # for idx in range(0, max_steps + 1):
    #    print('{0}: {1},'.format(idx, stages[idx]))

    ret_data = []
    for key in stages[0].keys():
        recursive_find(key, stages, 0, max_steps + 1, end, {}, ret_data)

    max_show = min(6, len(ret_data))
    table='<table>'
    table += '<tr>'
    for idx in xrange(0, max_show):
        table += '<th>{idx}</th>'.format(idx=idx+1)
    table += '</tr>'

    for idx in xrange(0, max_steps+1):
        table += '<tr>'
        for l in ret_data[:max_show]:
            table += '<td>{d}</td>'.format(d=l[idx])
        table += '</tr>'
    table += '</table>'

    return render_template('word_ladder_solutions.html',top=start, bottom=end, steps=max_steps, solutions=len(ret_data), max_show=max_show, data=Markup(table))


if __name__ == '__main__':
    app.run(debug=False, port=5001, host='0.0.0.0')
