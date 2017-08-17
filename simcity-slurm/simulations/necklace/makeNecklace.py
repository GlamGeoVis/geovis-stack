import sys
import json
import numpy as np
import urllib.request
import subprocess

inputsFile = sys.argv[1]
outputFile = sys.argv[2]

inputs = json.load(open(inputsFile))

baseUrl = 'http://nginx:8008/'
agaJar = '/home/xenon/simulations/necklace/agalib-r1.jar'
layerFile = 'input.geojson'

x = float(inputs['centre'][0]['x'])
y = float(inputs['centre'][0]['y'])
r = float(inputs['radius'])
columnName = inputs['myDataLayer']['columnName']
layer = inputs['myDataLayer']['layerName']
layerUrl = baseUrl + layer

print('WGET: ' + layerUrl)

urllib.request.urlretrieve(layerUrl, filename=layerFile)

javaLine = 'java -jar ' + agaJar + ' --in-file ' + layerFile + ' --auto-guide ' + str(r) + ' --data-column ' + columnName + ' --out-file ' + outputFile
print(javaLine)

subprocess.call(javaLine.split())
