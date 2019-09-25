#-*-coding:utf-8-*-

import sys, os
import argparse
import logging
import time
from twilio.rest import Client

'''
'''
# define gloal const
MK_OK = 1
MK_ERR = 0
'''
'''
# define global variables
LOG_LEVEL = logging.INFO
ACCOUUNT_SID = 'ACd431dbd67e31093442870b60baba0253'
AUTH_TOKEN = 'b65ecba131e6dc6661ee53fa641832e3'
PHONE_NUM_FROM = '+12055284634'

VAL_TRIG = 1
VAL_UNTRIG = 0

PHONE_NUM_TO = '+8613093715581'
EMAIL_ADDR_TO = 'ldod393@163.com'

'''
    @func: arg_parse
    @author: Jackie
    @date: 2019-09-24
    @desprition: parse input args
'''
def arg_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('--mail', '-M', type=str, default=EMAIL_ADDR_TO, help='message sent to email')
    parser.add_argument('--phone', '-P', type=str, default=PHONE_NUM_TO, help='message sent to phone')
    parser.add_argument('--msg', '-S', type=str, default='', help='message you want to send')

    parser.add_argument('--env', '-E', type=str, default='', help='envirnment to check, triggrt while it equals setted value')
    parser.add_argument('--val', '-V', type=int, default=VAL_TRIG, help='env triggered value')
    parser.add_argument('--time', '-T', type=str, default='', help='time to check, triggrt while it equals setted value, format 201909241730')

    parser.add_argument('--loop', '-L', type=int, default=1e6, help='max check loop times')
    parser.add_argument('--interval', '-I', type=float, default=0.1, help='time interval to of env & time check')

    args = parser.parse_args()
    return args

'''
    @func: arg_parse
    @author: Jackie
    @date: 2019-09-24
    @desprition: check input args
'''
def args_check(args):
    ret = MK_OK
    if args.mail.find(EMAIL_ADDR_TO) >= 0:
        logging.warning('You are using the default email address, please change it to your own')

    if args.phone.find(PHONE_NUM_TO) >= 0:
        logging.warning('You are using the default phone number, please change it to your own')

    if len(args.msg) <= 0:
        logging.error('The message to send is empty, please input again')
        ret = MK_ERR

    if len(args.env) <= 0:
        logging.warning('Env input is empty, project will run in time trigger mode')
    else:
        if args.env in os.environ:
            logging.info('Monitoring env %s with trigger val %d'%(args.env, args.val))
        else:
            os.putenv(args.env, str(VAL_UNTRIG))
            logging.info('Env %s is not setted, setting it to %d'%(args.env, args.val))

    if len(args.time) <= 0:
        logging.warning('Trigger time is not setted, project will run in env trigger mode')

    if len(args.env) <= 0 and len(args.time) <= 0:
        logging.error('Neither trigger time nor tigger env is setted, please check again')
        ret = MK_ERR

    if args.loop <= 0:
        logging.error('Loop time %d is invalid, please check again'%args.loop)
        ret = MK_ERR

    if args.interval <= 0:
        logging.error('Loop interval s %f is invalid, please check again'%args.interval)
        ret = MK_ERR

    return ret


def send_check(args):

    time_cur = time.time()


    return True

'''
    @func: process
    @author: Jackie
    @date: 2019-09-24
    @desprition: 
'''
def process(args):
    ret = MK_OK
    try:
        client = Client(ACCOUUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            to = args.phone,
            from_ = PHONE_NUM_FROM,
            body = unicode(args.msg)
        )
        logging.info('Msg sid is %r'%message.sid)
    except Exception:
        ret = MK_ERR
        logging.error('Sent message to phone %s failed'%(args.phone))
    return ret

'''
    @func: main
    @author: Jackie
    @date: 2019-09-24
    @desprition: entrance of running
'''
if __name__ == "__main__":
    # step0: set log output level
    logging.basicConfig(level=LOG_LEVEL)

    # step1: parse args
    logging.debug('Parse args of input')
    args = arg_parse()
    logging.debug('Args: time %s, env %s, val %d'%(args.time, args.env, args.val))

    # step2: check args
    ret = args_check(args)
    if ret == MK_ERR:
        logging.error('Input args check failed! Please check the log')
        exit()

    # step3: process
    ret = process(args)
    if ret == MK_ERR:
        logging.error('Failed, please check the error log')
    else:
        logging.info('Operation success!')
    exit()