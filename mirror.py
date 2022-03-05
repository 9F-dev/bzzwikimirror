
# -*- coding: utf-8 -*-
#!/usr/bin/python3
import os
import json
import requests
import tarfile

wikipediaDir = os.path.join(os.environ['HOME'], 'docs')

htmlDir = os.path.join(os.environ['HOME'], 'docs/A')

fileHashs = dict()

def getFiles(path):
  items = os.listdir(path)
  files = []
  
  for item in items:
    item = os.path.join(path, item)
    if os.path.isdir(item):
      files.extend(getFiles(item))
    elif os.path.isfile(item):
      files.append(item)
  
  return files    

def uploadToSwarm(filepath):
  swarmUrl = 'https://gateway-proxy-bee-4-0.gateway.ethswarm.org/bzz'
  
  filename = filepath.split('/')[-1]
  
  data = filename.encode(encoding='utf-8') + open(filepath, 'rb').read()
  
  headers = {
              "accept":"application/json, text/plain, */*",
              "content-type": "application/octet-stream",
              "swarm-collection": "false",
              "swarm-index-document": filename,
              "swarm-postage-batch-id": "0000000000000000000000000000000000000000000000000000000000000000"
            }
                                     
  r = requests.post(swarmUrl, headers = headers,  data = data)
  
  if r.status_code < 200 or r.status_code > 299:
    r = requests.post(swarmUrl, headers = headers,  data = data)
    
  if r.status_code < 200 or r.status_code > 299:
    print(filepath, r.text)
    return r.text
  
  reference = json.loads(r.text).get('reference')
  fileHashs[filepath] = reference
  
  return reference

if __name__ == '__main__':
  for file in getFiles(wikipediaDir):
    result = uploadToSwarm(file)
    #print(file, result)                                 
                                     
                                     
                                     
  
