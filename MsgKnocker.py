#-*-coding:utf-8-*-

import sys, os
import argparse
import logging
<<<<<<< HEAD
import smtplib
import time
from twilio.rest import Client
from email.mime.text import MIMEText
'''
    @params: global const
    @author: Jackie
    @date: 2019-09-24
    @desprition: global consts
'''
## define return code
MK_OK = 1
MK_ERR = 0

## define default values of triggered conditions
ENV_NAME = 'MK_TEST' # default env varible name
ENV_VAL_ON = '1' # default valid value of env
ENV_VAL_OFF = '0' # default invalid value of env

TIME_OFF = '299912312359' # time will never be satisfied at 2999-12-31 23:59
TIME_OFF_STR = '2999-12-31 23:59' # time will never be satisfied at 2999-12-31 23:59
TIME_ON = 0 # time will always satisfied the condition

FILE_ON = 'C:\\MsgKnocker.mk' # default file path to check
FILE_OFF = 'Z:\\MsgKnocker.mk' # file path that will never exist

DFLT_LOOP_TIME = 1e6 # max loop times
DFLT_TIME_INTERVAL = 1.0 # time gap between two checking

SENDER_TYPE_PHONE = 0 # send message by phone only
SENDER_TYPE_EMAIL = 1 # send message by email only
SENDER_TYPE_ALL = 2 #send message by phone and email

## define licenses
### twilio license, get them by log in twilio website
TWI_SID = 'ACd431dbd67e31093442870b60baba0253'
TWI_TOKEN = 'b65ecba131e6dc6661ee53fa641832e3'
TWI_PHONE = '+12055284634'

### email smtp licenses, get them by log in qq mail website
EMAIL_ADDR_FROM = '1160324585@qq.com'
EMAIL_AUTH_CODE = 'pxcuryutlaizbaef'
MSG = 'test'

'''
    @params: global varibles
    @author: Jackie
    @date: 2019-09-24
    @desprition: global varibles

'''
#log level
LOG_LEVEL = logging.DEBUG

# the email addr and phone num of receiver
PHONE_NUM_TO = '+8613093715581'
EMAIL_ADDR_TO = 'ldod393@163.com'


=======
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

>>>>>>> 1cac6ad5e2e88b02d9dd6deae8c287b2dfef9a42
'''
    @func: arg_parse
    @author: Jackie
    @date: 2019-09-24
    @desprition: parse input args
'''
def arg_parse():
    parser = argparse.ArgumentParser()

<<<<<<< HEAD
    parser.add_argument('--mode', '-O', type=str, default='', help='trigger mode: F(file) | E(env) | T(time)')
    parser.add_argument('--sender', '-R', type=int, default=SENDER_TYPE_EMAIL, help='sender mode: 0(Phone) | 1(Email) | 2(Both)')

    parser.add_argument('--mail', '-M', type=str, default=EMAIL_ADDR_TO, help='email addr of receiver')
    parser.add_argument('--phone', '-P', type=str, default=PHONE_NUM_TO, help='phone num of receiver')
    parser.add_argument('--msg', '-S', type=str, default=MSG, help='message that you want to send')


    parser.add_argument('--file', '-F', type=str, default=FILE_ON, help='file path to check')
    parser.add_argument('--time', '-T', type=str, default=TIME_OFF, help='time to check')

    parser.add_argument('--env', '-E', type=str, default=ENV_NAME, help='env varible to check')
    parser.add_argument('--val', '-V', type=str, default=ENV_VAL_ON, help='satisfied env value')

    parser.add_argument('--loop', '-L', type=int, default=DFLT_LOOP_TIME, help='max loop times of checking')
    parser.add_argument('--interval', '-I', type=float, default=DFLT_TIME_INTERVAL, help='time interval between two checkings, and the unit is second')
=======
    parser.add_argument('--mail', '-M', type=str, default=EMAIL_ADDR_TO, help='message sent to email')
    parser.add_argument('--phone', '-P', type=str, default=PHONE_NUM_TO, help='message sent to phone')
    parser.add_argument('--msg', '-S', type=str, default='', help='message you want to send')

    parser.add_argument('--env', '-E', type=str, default='', help='envirnment to check, triggrt while it equals setted value')
    parser.add_argument('--val', '-V', type=int, default=VAL_TRIG, help='env triggered value')
    parser.add_argument('--time', '-T', type=str, default='', help='time to check, triggrt while it equals setted value, format 201909241730')

    parser.add_argument('--loop', '-L', type=int, default=1e6, help='max check loop times')
    parser.add_argument('--interval', '-I', type=float, default=0.1, help='time interval to of env & time check')
>>>>>>> 1cac6ad5e2e88b02d9dd6deae8c287b2dfef9a42

    args = parser.parse_args()
    return args

'''
<<<<<<< HEAD
    @func: loop_check
    @author: Jackie
    @date: 2019-09-26
    @desprition: check loop params
'''
def loop_check(args):
    if args.loop <= 0:
        logging.error('Loop time %d is invalid, please input it again with op "-L [loop]"'%args.loop)
        return MK_ERR

    if args.interval <= 0:
        logging.error('Loop interval %f is invalid, please input it again with op "-I [interval]"'%args.interval)
        return MK_ERR

    return MK_OK

'''
    @func: receiver_check
    @author: Jackie
    @date: 2019-09-26
    @desprition: check input receiver (phone num  and email addr)
'''
def receiver_check(args):
    global EMAIL_ADDR_TO, PHONE_NUM_TO, MSG

    if args.mail == EMAIL_ADDR_TO:
        logging.warning('Using default email addr %s, please change it to your own with op "-M [mail]"'%(args.mail))

    if args.phone == PHONE_NUM_TO:
        logging.warning('Using default phone number %s, please change it to your own with op "-P [phone]"'%(args.phone))

    if args.msg == MSG:
        logging.warning('Using default msg "%s", please change it to your own with op "-S [message]"'%(args.msg))
    elif len(args.msg) <= 0:
        logging.error('Message to send is empty, please input it again with op "-S [message]"')
        return MK_ERR
    else:
        logging.info('Message to send is %s'%(args.msg))

    return MK_OK

'''
    @func: mode_check
    @author: Jackie
    @date: 2019-09-26
    @desprition: check input mode
'''
def mode_check(args):
    # sender check
    if args.sender < SENDER_TYPE_PHONE or args.sender > SENDER_TYPE_ALL:
        logging.error('Sender is invalid, please set sender again with op "-R [sneder]"')
        return MK_ERR

    # mode check
    if args.mode == '':
        logging.error('Mode is not setted, please set work mode first with op "-O [mode]"')
        return MK_ERR

    # file-check
    elif args.mode == 'F' or args.mode == 'file' or args.mode == 'File' or args.mode == 'FILE':
        args.mode = 'FILE'
        logging.info('Project will be running in "file-checking" mode')
        if args.file == FILE_ON:
            logging.warning('Using default file-checking path %s, please change it to your own with op "-F [filepath]"'%(FILE_ON))
        elif args.file == '':
            logging.error('File-checking path %s is empty, please change it to your own with op "-F [filepath]"%s'%(args.file))
            return MK_ERR
        else:
            logging.info('Using file-checking path %s'%(args.file))

        if os.path.exists(args.file):
            logging.error('Checking file already satisfied, file %s exists'%(args.file))
            return MK_ERR

    # time-check
    elif args.mode == 'T' or args.mode == 'time' or args.mode == 'Time' or args.mode == 'TIME':
        args.mode = 'TIME'
        logging.info('Project will be running in "time-checking" mode')
        if args.time == TIME_OFF: # using default time which will never be satisfied
            logging.error('Using default invalid time-checking time %s, please change it to your own with op "-T [time]"'%(TIME_OFF_STR))
            return MK_ERR
        else:
            if len(args.time) != 12: # time format check
                logging.error('Checking time format is invalid, please input again with op "-T [time]" like "-T 201909301430"')
                return MK_ERR
            # time value check
            (time_set, time_str) = time_trns(args.time)
            time_cur = time.time()
            time_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_cur))
            if time_cur >= time_set:
                logging.error('Checking time already satisfied, time set %s, time current %s'%(time_str, time_date))
                return MK_ERR
            else:
                logging.info('Set checking time %s'%time_str)
    # env check
    elif args.mode == 'E' or args.mode == 'env' or args.mode == 'Env' or args.mode == 'ENV':
        args.mode = 'ENV'
        logging.info('Project will be running in "env-checking" mode')

        if args.env == ENV_NAME:
            logging.info('Using default env-checking name %s, please change it to your own with op "-E [envname]"'%(args.env))
        elif args.env == '':
            logging.error('Env-checking name %s is empty, please input again with op "-E [envname]"%s'%(args.env))
            return MK_ERR
        else:
            logging.info('Using env-checking name %s'%(args.env))
        
        if args.val == ENV_VAL_ON:
            logging.info('Using default env-checking val %s, please change it to your own with op "-V [envval]"'%(args.val))
        elif args.val == '':
            logging.error('Env-checking name %s is empty, please input again with op "-E [envname]"%s'%(args.val))
            return MK_ERR
        else:
            logging.info('Using env-checking name %s'%(args.val))
    else:
        logging.error('Mode is invalid, please input again with op "-O [mode]"')
        return MK_ERR

    return MK_OK

'''
    @func: arg_parse
    @author: Jackie
    @date: 2019-09-24
    @desprition: check input args
'''
def args_check(args):
    if mode_check(args) != MK_OK:
        logging.error("Mode check failed, please check the log")
        return MK_ERR

    if receiver_check(args) != MK_OK:
        logging.error("Mode check failed, please check the log")
        return MK_ERR

    if loop_check(args) != MK_OK:
        logging.error("Mode check failed, please check the log")
        return MK_ERR

    return MK_OK

'''
    @func: time_trns
    @author: Jackie
    @date: 2019-09-24
    @desprition: trans time date into time stamp
'''
def time_trns(time_str):
    time_target = args.time

    year = int(time_target[0:4])
    month = int(time_target[4:6])
    day = int(time_target[6:8])
    hour = int(time_target[8:10])
    mint = int(time_target[10:12])
    secs = 0

    time_str = '%04d-%02d-%02d %02d:%02d:%02d'%(year, month, day, hour, mint, secs)
    time_arry = time.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    time_stamp = int(time.mktime(time_arry))

    # logging.info('Target time: %s'%time_str)

    return (time_stamp, time_str)


'''
    @func: send_message
    @author: Jackie
    @date: 2019-09-24
    @desprition: send phone message by twilio
'''
def send_message(args):
    # message to phone
    try:
        client = Client(TWI_SID, TWI_TOKEN)
        message = client.messages.create(
            to = args.phone,
            from_ = TWI_PHONE,
            body = unicode(args.msg)
        )
        logging.info('Message send success, sid is %r'%message.sid)
        return MK_OK
    except Exception:
        logging.error('Message send to phone %s failed'%(args.phone))
        return MK_ERR

'''
    @func: send_email
    @author: Jackie
    @date: 2019-09-24
    @desprition: send email by smtp
'''
def send_email(args):
    ret = MK_OK
    msg_sender = EMAIL_ADDR_FROM
    msg_code = EMAIL_AUTH_CODE
    msg_receiver = args.mail

    subject = "MsgKnocker-Python"
    content = args.msg

    msg = MIMEText(content, _charset="utf-8")
    msg['Subject'] = subject
    msg['From'] = msg_sender
    msg['To'] = msg_receiver
    try:
        sender = smtplib.SMTP_SSL("smtp.qq.com", 465)
        sender.login(msg_sender, msg_code)
        sender.sendmail(msg_sender, msg_receiver, msg.as_string())

        logging.info('Email send to addr %s success'%(args.mail))
        ret = MK_OK
    except Exception as ex:
        logging.error('%r'%ex)
        logging.error('Email send to addr %s failed'%(args.mail))
        ret = MK_ERR
    finally:
        sender.quit()
        return ret
'''
    @func: send_check
    @author: Jackie
    @date: 2019-09-24
    @desprition: check send conditions
'''
def send_check(args):
    ret = True

    # time check
    if args.mode == 'TIME':
        (time_set, time_str) = time_trns(args)
        time_cur = time.time()
        time_date = time_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_cur))
        if time_cur >= time_set:
            logging.info('Time-checking YES, time cur %s, time target %s'%(time_date, time_str))
        else:
            logging.debug('Time-checking NO, time cur %s, time target %s'%(time_date, time_str))
            ret = False

    # file check
    elif args.mode == 'FILE':
        if os.path.exists(args.file):
            logging.info('File-checking YES, file %s exists'%(args.file))
        else:
            logging.info('File-checking NO, file %s does not exist'%(args.file))
            ret = False

    # env check
    else:
        env_val = os.getenv(args.env)
        if env_val == args.val:
            logging.info('Env-checking YES, env %s val is %d'%(args.env, args.val))
        else:
            logging.debug('Env-checking NO, env %s val is %s, trigger val %d'%(args.env, env_val, args.val))
            ret = False

    return ret
'''
    @func: process
    @author: Jackie
    @date: 2019-09-24
    @desprition: 
'''
def process(args):
    idx_loop = 0
    ret_mail = MK_OK
    ret_msg = MK_OK

    while idx_loop < args.loop:
        if send_check(args) == False:
            time.sleep(args.interval)
            idx_loop += 1
            continue

        # send message
        if args.sender == SENDER_TYPE_PHONE or args.sender == SENDER_TYPE_ALL:
            ret_msg = send_message(args)

        # email to email box
        if args.sender == SENDER_TYPE_EMAIL or args.sender == SENDER_TYPE_ALL:
            ret_mail = send_email(args)

        if ret_mail != MK_OK or ret_msg != MK_OK:
            logging.error('Message send failed')
        break

    logging.info('Checking finished, and the condition has not been satisfied')
    return MK_OK
=======
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
>>>>>>> 1cac6ad5e2e88b02d9dd6deae8c287b2dfef9a42

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
<<<<<<< HEAD
    logging.debug('Init input args')
    args = arg_parse()
=======
    logging.debug('Parse args of input')
    args = arg_parse()
    logging.debug('Args: time %s, env %s, val %d'%(args.time, args.env, args.val))
>>>>>>> 1cac6ad5e2e88b02d9dd6deae8c287b2dfef9a42

    # step2: check args
    ret = args_check(args)
    if ret == MK_ERR:
        logging.error('Input args check failed! Please check the log')
        exit()

    # step3: process
    ret = process(args)
    if ret == MK_ERR:
<<<<<<< HEAD
        logging.error('Process failed, please check the error log')
    else:
        logging.info('Process success')
=======
        logging.error('Failed, please check the error log')
    else:
        logging.info('Operation success!')
>>>>>>> 1cac6ad5e2e88b02d9dd6deae8c287b2dfef9a42
    exit()