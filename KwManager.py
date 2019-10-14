#-*-coding:utf-8-*-

import sys, os
import argparse
import platform
import logging
import base64
'''
'''
# define gloal const
KW_OK = 1
KW_ERR = 0
STR_ENC_ON = 1
STR_ENC_OFF = 0
'''
'''
# define global variables
LOG_LEVEL = logging.INFO
PATH_NOTE = ''
'''
    @func: arg_parse
    @author: Jackie
    @date: 2019-09-24
    @desprition: parse input args
'''
def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-F', type=str, default=PATH_NOTE, help='note file path')
    parser.add_argument('--mode', '-M', type=str, default='F', help='using mode, I(insert) | D(delete) | E(edit) | F(find)')
    parser.add_argument('--line', '-L', type=int, default=0, help='edit line, using on delete or edit mode')
    parser.add_argument('--str', '-S', type=str, default='none', help='line content string')
    parser.add_argument('--enc', '-E', type=int, default=STR_ENC_OFF, help='whether encrypt or not')
    args = parser.parse_args()
    return args
'''
    @func: init_globals
    @author: Jackie
    @date: 2019-09-24
    @desprition: init default file path
'''
def init_globals():
    global PATH_NOTE
    # get system string
    sysstr = platform.system()
    if sysstr == "Windows":
        PATH_NOTE = 'C:\\KwManagerNote.txt'
        logging.debug('Running on Windows system, system string is %s, default note path is %s'%(sysstr, PATH_NOTE))
        return KW_OK
    elif sysstr == "Linux":
        PATH_NOTE = '/home/KwManagerNote.txt'
        logging.debug('Running on Linux system, system string is %s, default note path is %s'%(sysstr, PATH_NOTE))
        return KW_OK
    else:
        logging.error('Running on Unknown system, system string is %s'%(sysstr))
        return KW_ERR
'''
    @func: str_encrypt
    @author: Jackie
    @date: 2019-09-26
    @desprition: str_encrypt
'''
def str_encrypt(str_src):
    str_enc = base64.b64encode(str_src)
    return str_enc
'''
    @func: str_decrypt
    @author: Jackie
    @date: 2019-09-26
    @desprition: str_decrypt
'''
def str_decrypt(str_enc):
    str_dec = base64.b64decode(str_enc)
    return str_dec
'''
    @func: process
    @author: Jackie
    @date: 2019-09-24
    @desprition: process acording to chhsen mode
'''
def process(args):
    ret = KW_OK
    if args.mode == 'I' or args.mode == 'insert' or args.mode == 'Insert' or args.mode == 'INSERT':
        if args.enc == STR_ENC_ON:
            args.str = '[C]' + str_encrypt(args.str)
        else:
            args.str = '[P]' + args.str
        ret = insert_note(args.file, args.str)
    elif args.mode == 'D' or args.mode == 'delete' or args.mode == 'Delete' or args.mode == 'DELETE':
        ret = del_note(args.file, args.line)
    elif args.mode == 'E' or args.mode == 'edit' or args.mode == 'Edit' or args.mode == 'EDIT':
        ret = edit_note(args.file, args.line, args.str)
    elif args.mode == 'F' or args.mode == 'find' or args.mode == 'Find' or args.mode == 'FIND':
        ret = find_note(args.file, args.str)
    else:
        logging.error('Mode "%s" is invalid, please input again'%(args.mode))
    return ret
'''
    @func: insert_note
    @author: Jackie
    @date: 2019-09-24
    @desprition: insert line into file
'''
def insert_note(path_note, str_note):
    if file_check(path_note) == KW_ERR:
        return KW_ERR

    with open(path_note, 'a+') as fp:
        fp.write('%s\n'%str_note)
        logging.info('Insert line \"%s\" in fle %s'%(str_note, path_note))
    return KW_OK
'''
    @func: del_note
    @author: Jackie
    @date: 2019-09-24
    @desprition: delete line in file
'''
def del_note(path_note, str_line):
    if file_check(path_note) == KW_ERR:
        return KW_ERR

    fp = open(path_note, 'r')
    lines = fp.readlines()
    fp.close()

    fp = open(path_note, 'w')
    fp.close()

    with open(path_note, 'a+') as fp:
        idx = 0
        while idx < len(lines):
            if idx != str_line - 1:
                fp.write(lines[idx])
            else:
                logging.info('Delete line %d, content %s, in file %s'%(str_line, lines[idx], path_note))
            idx += 1
    return KW_OK
'''
    @func: find_note
    @author: Jackie
    @date: 2019-09-24
    @desprition: find line in file with key worlds
'''
def find_note(path_note, str_note):
    if file_check(path_note) == KW_ERR:
        return KW_ERR
    logging.info('Search content %s in file %s'%(str_note, path_note))
    with open(path_note, 'r') as fp:
        lines = fp.readlines()
        found = False
        idx = 0
        for line in lines:
            idx += 1
            tag = line[1]
            if tag == 'P':
                line_note = line[3:-1]
            elif tag == 'C':
                line_note = str_decrypt(line[3:-1])
            else:
                logging.error('Invalid line tag %s'%(tag))
                return KW_ERR
            logging.debug('idx %d, note %s, key %s'%(idx, line_note, str_note))
            if line_note.upper().find(str_note.upper()) >= 0:
                found = True
                logging.info('\t[%d]: %s'%(idx, line_note))
    if found == False:
        logging.warning('No line matched!')
    return KW_OK
'''
    @func: edit_note
    @author: Jackie
    @date: 2019-09-24
    @desprition: change line in file into input string
'''
def edit_note(path_note, str_line, str_note):
    if file_check(path_note) == KW_ERR:
        return KW_ERR

    fp = open(path_note, 'r')
    lines = fp.readlines()
    fp.close()

    fp = open(path_note, 'w')
    fp.close()

    with open(path_note, 'a+') as fp:
        idx = 0
        while idx < len(lines):
            if idx != str_line - 1:
                fp.write(lines[idx])
            else:
                fp.write(str_note + '\n')
                logging.info('Edit line %d to content %s, in file %s'%(str_line, str_note, path_note))
            idx += 1
    return KW_OK

'''
    @func: file_check
    @author: Jackie
    @date: 2019-09-24
    @desprition: check existance of note file
'''
def file_check(path_note):
    try:
        fp = open(path_note, 'a+')
        fp.close()
    except IOError:
        logging.error('File %s is not accessable'%path_note)
        return KW_ERR
    return KW_OK

'''
    @func: main
    @author: Jackie
    @date: 2019-09-24
    @desprition: entrance of running
'''
if __name__ == "__main__":
    # step0: set log output level
    logging.basicConfig(level=LOG_LEVEL)

    # step1: get system platform
    logging.debug('Init global varivles: get system type and default note path')
    ret = init_globals()
    if ret == KW_ERR:
        logging.error('Init global varibles failed')
        exit()
    else:
        logging.debug('Init global varibles success')

    # step2: parse args
    logging.debug('Parse args of input')
    args = arg_parse()
    logging.debug('Args: file %s, line %d, mode %s, content %s'%(args.file, args.line, args.mode, args.str))

    # step3: process
    ret = process(args)
    if ret == KW_ERR:
        logging.error('Failed, please check the error log')
    else:
        logging.info('Operation success!')
    exit()