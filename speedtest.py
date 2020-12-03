import datetime
import re
import subprocess

import mysql.connector


def test_speed():
	response = subprocess.Popen('/usr/local/bin/speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

	ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)[0]
	download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)[0]
	upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)[0]

	return datetime.datetime.now(), ping, download, upload


def add_row(dtim, ping, dwn_ld, up_ld):
	"""Adds a row to the SQL db"""
	results = {
		'datetime': dtime,
		'ping': ping,
		'download': dwnld,
		'upload': up_ld
		}
	add_test_results = ("INSERT INTO speed "
			   "(datetime, ping, download, upload) "
			   "VALUES (%s, %s, %s, %s)")

	conn = mysql.connector.connect(user='mypi', database='speed')
	cursor = conn.cursor()

	# Add the data
	cursor.execute(add_test_results, results)

	# Commit & close
	cursor.commit()
	cursor.close()
	conn.close()


if __name__ == '__main__':
	dtime, ping, upload, download = test_speed()
	add_row(dtime, ping, download, upload)
