# -*- coding:utf-8 -*-
import os
from pymongo import MongoClient


# mongodb connection params
CONN_URL = '127.0.0.1'
CONN_PORT = 27017
COLLECTION_RECORDS = 'records'
COLLECTION_LOGS = 'logs'
COLLECTION_KEY = 'db_key'

# open connection
conn = MongoClient(CONN_URL, CONN_PORT)
db = conn.transaction # db named transaction


def insert(data, collection_type):
    if collection_type == COLLECTION_RECORDS:
        my_set = db.records
        my_set.insert(data)
    elif collection_type == COLLECTION_LOGS:
        my_set = db.logs
        my_set.insert(data)


def exist(collection_type, key, value):
    if collection_type == COLLECTION_RECORDS:
        my_set = db.records
        return my_set.find_one({key: value})
    elif collection_type == COLLECTION_LOGS:
        my_set = db.logs
        return my_set.find_one({key: value})


def query(collection_type, key):
    if collection_type == COLLECTION_RECORDS:
        return db.records.find({COLLECTION_KEY: key}, '{records:1, _id:0}')
    elif collection_type == COLLECTION_LOGS:
        return db.logs.find({COLLECTION_KEY: key}, '{records:1, _id:0}')

