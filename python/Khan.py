from os import system
from string import ascii_uppercase
import json
from colorama import init, Fore, Style
init()

g = Style.BRIGHT + Fore.GREEN
red = Style.BRIGHT + Fore.RED
r = Style.RESET_ALL

dbg = False


def files(file: str, action: str, content=None):
    with open(file, f'{action}+') as f:
        x = json.load(f) if action == 'r' else json.dump(content, f)
        if x:
            return x


def strip_trash(response: str):
    remove_list = files('remove.json', 'r')

    for word in remove_list:
        response = response.replace(word, '')

    response = response.replace('[]', '')
    response = response.replace('{}', '')
    response = response.replace('()', '')

    return response


def stringsearch(response: str, substring: str, a_loc: int, a_len: int, skipper: int):
    loc = a_loc
    length = a_len

    if ((loc < a_loc and loc != 1) or (a_loc == -1)):
        loc = response.find(substring, skipper)
        length = len(substring)

    return (loc, length)


def log_answers(a: str):
    with open('answers.log', 'a+') as fi:
        fi.write(str(a.encode('utf-8')) + '\n')


def add_remove(response: str):
    remove_list = files('remove.json', 'r')

    if response.lower().startswith('remove '):
        remove_list.append(response.replace('remove ', ''))
        files('remove.json', 'w', remove_list)
        return True
    return False


def dbg_toggle(response: str):
    global dbg
    if response.lower() == 'dbg':
        dbg = not dbg

        print(f'Debugging: {str(dbg)}')
        return True
    return False


def a_format(a: str):

    a = a.replace('"correct":true', g + '"correct":true' + r)
    a = a.replace('"status":"correct"', g + '"status":"correct"' + r)
    a = a.replace('"considered":"correct"', g + '"considered":"correct"' + r)
    a = a.replace('"answers"', g + '"answers"' + r)
    a = a.replace('"correct":[', g + '"correct":[' + r)
    a = a.replace('"correct":{', g + '"correct":{' + r)
    a = a.replace('"options":{', g + '"options":{' + r)
    a = a.replace('^circ', '°')
    a = a.replace('cdot', '·')
    a = a.replace('left(', '(')
    a = a.replace('right)', ')')
    a = a.replace('rightarrow', '→')
    a = a.replace('leftarrow', '←')
    a = a.replace('infty', '∞')
    a = a.replace('sqrt{', '\\sqrt{')
    a = a.replace('frac{', '\\frac{')
    a = a.replace('d\\frac{', '\\frac{')
    a = a.replace('times ', ' X ')
    a = a.replace('"hints"', g + '"hints"' + r)
    a = a.replace('"content"', g + '"content"' + r)

    return a


def parse_answer(response: str):

    loopchk = -1
    while loopchk != len(response):
        loopchk = len(response)
        response = strip_trash(response)
        response = response.replace(',,', ',')
        response = response.replace('{,', '{')
        response = response.replace('[,', '[')
        response = response.replace('(,', '(')
        response = response.replace(',}', '}')
        response = response.replace(',]', ']')
        response = response.replace(',)', ')')

        if ('"maxError":' in response):
            meindx = response.index('"maxError":')
            melen = len('"maxError":')
            afterME = meindx + melen

            while ((response[afterME].isdigit()) or response[afterME] == '.'):
                afterME += 1

            response = response.replace(response[meindx:afterME], '')

    response_copy = response[:]

    if dbg:
        print(a_format(response) + '\n')

    a_cnt = response.count('"correct":true')
    a_cnt = response.count('"status":"correct"') + a_cnt
    a_cnt = response.count('"considered":"correct"') + a_cnt
    a_cnt = response.count('"answers"') if a_cnt == 0 else a_cnt
    a_cnt = response.count('"correct":') if a_cnt == 0 else a_cnt
    a_cnt = response.count('"options":') if a_cnt == 0 else a_cnt

    answers = []
    skipper = 0

    for i in range(0, a_cnt):
        a_loc = -1
        a_len = -1

        a_loc, a_len = stringsearch(response, '"correct":true', a_loc, a_len, skipper)
        a_loc, a_len = stringsearch(response, '"status":"correct"', a_loc, a_len, skipper)
        a_loc, a_len = stringsearch(response, '"considered":"correct"', a_loc, a_len, skipper)

        if (a_loc == -1):
            a_loc, a_len = stringsearch(response, '"correct":[', a_loc, a_len, skipper)
            a_loc, a_len = stringsearch(response, '"correct":{', a_loc, a_len, skipper)
            a_loc, a_len = stringsearch(response, '"options":{', a_loc, a_len, skipper)
            a_loc, a_len = stringsearch(response, '"answers"', a_loc, a_len, skipper)

        first = -1
        last = -1

        b_right = False
        b_left = False

        if ('{' in response[a_loc - 1:a_loc + a_len]):
            f_tmp = response[a_loc - 1:a_loc + a_len].find('{')
            first = (f_tmp + a_loc - 1) if f_tmp == 0 else (f_tmp + a_loc - a_len)
            b_left = True
        elif ('[' in response[a_loc - 1:a_loc + a_len]):
            f_tmp = response[a_loc - 1:a_loc + a_len].find('[')
            first = (f_tmp + a_loc - 1) if f_tmp == 0 else (f_tmp + a_loc - a_len)
            b_left = True

        if (response[a_loc + a_len] == '}'):
            last = a_loc + a_len + 1
            b_right = True

        if (first == -1):
            first = (a_loc)
        if (last == -1):
            last = (a_loc + a_len)

        skipper = a_loc + 2

        a_tmp = response[first:last]

        if (b_left or b_right):
            while (a_tmp.count('{') != a_tmp.count('}')) or (a_tmp.count('[') != a_tmp.count(']')):
                if b_left:
                    last += 1

                if b_right:
                    first -= 1

                a_tmp = response[first:last]

        else:
            first = (a_loc - 80) if a_loc >= 80 else (0)
            last = (a_loc + 90) if ((a_loc + 90) <= len(response)) else (len(response))

        a = response[first:last]

        if ('"choices":[' in response):
            c_loc = response.rfind('"choices":[', 0, a_loc)
            a_id = response.count('"correct":', c_loc, last)
            a_id = response.count('"status":', c_loc, last) + a_id
            a_id = response.count('"considered":', c_loc, last) + a_id

            if '"randomize":true' in response:
                a = f'{red}Answers are randomized.{r}\nAnswer: {a}'
            else:
                a = f'{g}Correct answer should be: {ascii_uppercase[a_id-1]}{r}\nTo check: {a}'

        a = a_format(a)

        answers.append(a)

    answers.append('\n' + a_format(response))
    answers = (('\n'.join(answers) if answers else response_copy) + '\n')

    return answers


def main():
    print('To use this script: \
    \n1) Open your web browsers console \
    \n2) Navigate to network \
    \n3) Filter for the word assessment \
    \n4) Open a task \
    \n5) Click the second to last assessment \
    \n6) Response \
    \n7) Paste into here \
    \n')

    while True:
        response = input('Input Khan Assessment Response: ')

        system('cls')

        if not (add_remove(response) or dbg_toggle(response)):
            answer = parse_answer(response)

            print(answer)


main()
