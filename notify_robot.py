#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests


def notify_robot(doc_number, filename):
    url = 'https://services.abcd.com/grafo/file'
    payload = {"docNum": doc_number, "docPath": filename}
    try:
        print 'payload %s' % payload
        r = requests.post(url, json=payload)
        print 'resultado: %s' % r.status_code
    except:
        print 'ERRO NOTIFY %s' % r.status_code
        print r
        r.status_code = 500
    return r.status_code == 200
