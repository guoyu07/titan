#!/usr/local/bin/python2.7
#coding:utf-8

DEBUG = False
SECRET_KEY = 'sheep!@$titan!#$%^'

DATABASE_URI = 'mysql://'

SESSION_KEY = 'tid'
SESSION_ENVIRON_KEY = 'titan.session'
SESSION_COOKIE_DOMAIN = '127.0.0.1'
MAX_CONTENT_LENGTH = 3 * 1024 * 1024

TOKEN_LENGTH = 6

SMTP_SERVER = 'smtp.qq.com'
SMTP_USER = 'service@xiaomen.co'
SMTP_PASSWORD = 'xiaomenkou!@#$%^'

VERIFY_STUB_EXPIRE = 30*60
FORGET_STUB_EXPIRE = 30*60

GRAVATAR_BASE_URL = 'http://www.gravatar.com/avatar/'
GRAVATAR_EXTRA = ''

COMMITS_PER_PAGE = 10
REVISIONS_PER_PAGE = 5

PACKAGE_COST = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
}

REPOS_LIMIT = {
    1: 5,
    2: 100,
    3: 150,
    4: 999,
    5: 999,
    6: 999,
    7: 999,
}

MEMBERS_LIMIT = {
    1: 5,
    2: 30,
    3: 60,
    4: 100,
    5: 150,
    6: 200,
    7: 999
}

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

JAGARE_NODES = [
    'http://127.0.0.1:9000',
]

#TODO 因为现在还在本地测试，所以直接用文件路径
MARIA_STORE_PATH = '/Users/CMGS/Documents/Workplace/experiment/Jagare/permdir/'

try:
    from local_config import *
except:
    pass

