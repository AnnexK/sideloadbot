#!/usr/bin/python3

import argparse
import telepot
import urllib3.exceptions
import tokencheck


def main():
    p = argparse.ArgumentParser()
    p.add_argument('token')
    p.add_argument('--http-proxy')

    args = p.parse_args()

    if args.http_proxy is not None:
        print(args.http_proxy)
        telepot.api.set_proxy(f'http://{args.http_proxy}')

    try:
        if not tokencheck.check_token(args.token):
            raise tokencheck.InvalidTokenError()

        bot = telepot.Bot(args.token)
        print(bot.getMe())
        print('Bot create success')
    except urllib3.exceptions.MaxRetryError:
        print('could not establish connection')
    except telepot.exception.TelegramError:
        print('bot not found')
    except tokencheck.InvalidTokenError:
        print('invalid token')


if __name__ == '__main__':
    main()
