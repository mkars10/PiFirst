import re
import subprocess

response = subprocess.Popen('/usr/local/bin/speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)[0]
download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)[0]
upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)[0]
