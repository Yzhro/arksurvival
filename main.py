# module
from os import system
from time import sleep
import sys, datetime
import os,sys,time
import requests, json, time, threading, os, sys
from colorama import Fore, init

import time

def countdownTimer(start_minute, start_second):
    total_second = start_minute * 60 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{mins:02d}:{secs:02d}', end='\r')
        time.sleep(1)
        total_second -= 1
    print("""\33[0;35m==========================""") 
    
 
# Config
red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
blue = Fore.LIGHTBLUE_EX
white = Fore.WHITE
system("clear")
auth = input(f"{yellow}𝗬𝗢𝗨 𝗧𝗢𝗞𝗘𝗡::{red}")







record = [{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SBY', 'routePassed': ['SBY', 'BKL'], 'activityRewards': None}, 'Value': 40},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'SBY'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'BKL'], 'activityRewards': None}, 'Value': 20},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SMG'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SBY'], 'activityRewards': None}, 'Value': 13},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'BKL'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'CBN'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SMG'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SBY'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'BKL', 'routePassed': ['BKL', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'JKT'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'CBN'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SMG'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SBY'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'BKL'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'P_Merak'], 'activityRewards': None}, 'Value': 5}, {'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'JKT'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SMG'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SBY'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'BKL'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'P_Merak'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SMG'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PLB', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 55},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 11},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'JKT'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'CBN'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SMG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SBY'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'BKL'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'PLB'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'LPG'], 'activityRewards': None}, 'Value': 10},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'CBN'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SMG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'JMB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JMB'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'PLB'], 'activityRewards': None}, 'Value': 12},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'LPG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'CBN'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SMG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SBY'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'BKL'], 'activityRewards': None}, 'Value': 1},{"Key":{"sourceCity":"PBR","destinationCity":"BKT","routePassed":["BKT","PBR"],"activityRewards":None},"Value":50},{"Key":{"sourceCity":"PBR","destinationCity":"PDG","routePassed":["PDG","BKT","PBR"],"activityRewards":None},"Value":9},{"Key":{"sourceCity":"BKT","destinationCity":"PDG","routePassed":["PDG","BKT"],"activityRewards":None},"Value":50},]            




                                
headers = {'User-Agent': 'UnityEngine-Unity; Version: 2018.4.26f1','X-ReportErrorAsSuccess': 'true','X-PlayFabSDK': 'UnitySDK-2.20.170411','X-Authorization': '','Content-Type': 'application/json','Content-Length': '223','Host': '4ae9.playfabapi.com'}



def create_mission():
	game_data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["BKL","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR","BKT","PDG"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=game_data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			return None
		elif parser['code'] == 200:
			data = parser['data']
			if "apiError" in str(data):
				return None
			else:
				carrer = data['FunctionResult']['careerSession']
				return carrer
	else:
		return None

def skip_mission(token):
	data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":record,"bonus":True,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			pass
		elif parser['code'] == 200:
			backend_data = parser['data']
			if "apiError" in str(backend_data):
				pass
			else:
				logs = backend_data['FunctionResult']
				ketik(f"{red}______________{green}________________________{red}_______________")
				ketik(f"""\33[0;34;44m\33[1;37m ✔ \33[1;34m\33[0m\33[   {blue}Add {green}{logs}{blue} 𝐌𝐨𝐧𝐞𝐲 {yellow}𝐀𝐝𝐝 𝐓𝐨 𝐘𝐨𝐮 𝐀𝐜𝐜𝐨𝐮𝐧𝐭""")
				chat = backend_data['Logs']
				uang= chat[len(chat)-1]['Message'].split()[5]
				ketik(f"_____________________________________________________")
				ketik(f"➤➤➤ {yellow}𝐓𝐨𝐭𝐚𝐥 𝐏𝐞𝐧𝐠𝐡𝐚𝐬𝐢𝐥𝐚𝐧 𝐍𝐠𝐞𝐩𝐞𝐭 𝐊𝐚𝐦𝐮 {red}Rp:{green}{uang}")
				ketik(f"{red}______________{green}________________________{red}_______________")
				

def pass_mission():
	carrer = create_mission()
	if carrer != None:	
		token = carrer['token']
		skip_mission(token)
		
headers['X-Authorization'] = auth



def skip_missionnnnn():
	data = json.dumps({"FunctionName":"RewardProcess","FunctionParameter":None,"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			pass
		elif parser['code'] == 200:
			backend_data = parser['data']
			if "apiError" in str(backend_data):
				pass
			else:
				logs = backend_data['FunctionResult']
				hook = logs['value']
				ketik(f"{red}______________{green}________________________{red}_______________")
				ketik(f"""\33[0;34;44m\33[1;37m ✔ \33[1;34m\33[0m\33[   {blue}Add {green}{hook}{blue} 𝐌𝐨𝐧𝐞𝐲 {yellow}𝐀𝐝𝐝 𝐓𝐨 𝐘𝐨𝐮 𝐀𝐜𝐜𝐨𝐮𝐧𝐭""")
				chat = backend_data['Logs']
				uang= chat[len(chat)-1]['Message'].split()[9]
				ketik(f"_____________________________________________________")
				ketik(f"➤➤➤ {yellow}𝐓𝐨𝐭𝐚𝐥 𝐏𝐞𝐧𝐠𝐡𝐚𝐬𝐢𝐥𝐚𝐧 𝐍𝐠𝐞𝐩𝐞𝐭 𝐊𝐚𝐦𝐮 {red}Rp:{green}{uang}")
				ketik(f"{red}______________{green}________________________{red}_______________")
				


headers['X-Authorization'] = auth



#bagian 2
#500 k
def create_missionn():
	game_data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["BKL","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR","BKT","PDG"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=game_data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			return None
		elif parser['code'] == 200:
			data = parser['data']
			if "apiError" in str(data):
				return None
			else:
				carrer = data['FunctionResult']['careerSession']
				return carrer
	else:
		return None

def skip_missionn(token):
	data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":record,"bonus":False,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			pass
		elif parser['code'] == 200:
			backend_data = parser['data']
			if "apiError" in str(backend_data):
				pass
			else:
				logs = backend_data['FunctionResult']
				ketik(f"{red}______________{green}________________________{red}_______________")
				ketik(f"""\33[0;34;44m\33[1;37m ✔ \33[1;34m\33[0m\33[   {blue}Add {green}{logs}{blue} 𝐌𝐨𝐧𝐞𝐲 {yellow}𝐀𝐝𝐝 𝐓𝐨 𝐘𝐨𝐮 𝐀𝐜𝐜𝐨𝐮𝐧𝐭""")
				chat = backend_data['Logs']
				uang= chat[len(chat)-1]['Message'].split()[5]
				ketik(f"_____________________________________________________")
				ketik(f"➤➤➤ {yellow}𝐓𝐨𝐭𝐚𝐥 𝐏𝐞𝐧𝐠𝐡𝐚𝐬𝐢𝐥𝐚𝐧 𝐍𝐠𝐞𝐩𝐞𝐭 𝐊𝐚𝐦𝐮 {red}Rp:{green}{uang}")
				ketik(f"{red}______________{green}________________________{red}_______________")
				

def pass_scs():
	carrer = create_missionn()
	if carrer != None:	
		token = carrer['token']
		skip_missionn(token)
		
headers['X-Authorization'] = auth

		

#800k
recordd = [{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SBY', 'routePassed': ['SBY', 'BKL'], 'activityRewards': None}, 'Value': 40},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'SBY'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'BKL'], 'activityRewards': None}, 'Value': 12},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SMG'], 'activityRewards': None}, 'Value': 50},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SBY'], 'activityRewards': None}, 'Value': 10},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'BKL'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'CBN'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SMG'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SBY'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'BKL', 'routePassed': ['BKL', 'JKT'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'JKT'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'CBN'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SMG'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SBY'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'BKL'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'P_Merak'], 'activityRewards': None}, 'Value': 5}, {'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'JKT'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SMG'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SBY'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'BKL'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'P_Merak'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'JKT'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SMG'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PLB', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 55},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 11},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'JKT'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'CBN'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SMG'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SBY'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'BKL'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'PLB'], 'activityRewards': None}, 'Value': 50},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'LPG'], 'activityRewards': None}, 'Value': 10},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Merak'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'JKT'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'CBN'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SMG'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'JMB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JMB'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'PLB'], 'activityRewards': None}, 'Value': 12},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'LPG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Merak'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JKT'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'CBN'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SMG'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SBY'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'BKL'], 'activityRewards': None}, 'Value': 1},]                                                   
headers = {'User-Agent': 'UnityEngine-Unity; Version: 2018.4.26f1','X-ReportErrorAsSuccess': 'true','X-PlayFabSDK': 'UnitySDK-2.20.170411','X-Authorization': '','Content-Type': 'application/json','Content-Length': '223','Host': '4ae9.playfabapi.com'}
def create_missionnn():
	game_data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["BKL","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=game_data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			return None
		elif parser['code'] == 200:
			data = parser['data']
			if "apiError" in str(data):
				return None
			else:
				carrer = data['FunctionResult']['careerSession']
				return carrer
	else:
		return None

def skip_missionnn(token):
	data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":recordd,"bonus":True,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			pass
		elif parser['code'] == 200:
			backend_data = parser['data']
			if "apiError" in str(backend_data):
				pass
			else:
				logs = backend_data['FunctionResult']
				ketik(f"{red}______________{green}________________________{red}_______________")
				ketik(f"""\33[0;34;44m\33[1;37m ✔ \33[1;34m\33[0m\33[   {blue}Add {green}{logs}{blue} 𝐌𝐨𝐧𝐞𝐲 {yellow}𝐀𝐝𝐝 𝐓𝐨 𝐘𝐨𝐮 𝐀𝐜𝐜𝐨𝐮𝐧𝐭""")
				chat = backend_data['Logs']
				uang= chat[len(chat)-1]['Message'].split()[5]
				ketik(f"_____________________________________________________")
				ketik(f"➤➤➤ {yellow}𝐓𝐨𝐭𝐚𝐥 𝐏𝐞𝐧𝐠𝐡𝐚𝐬𝐢𝐥𝐚𝐧 𝐍𝐠𝐞𝐩𝐞𝐭 𝐊𝐚𝐦𝐮 {red}Rp:{green}{uang}")
				ketik(f"{red}______________{green}________________________{red}_______________")
				

def pass_missionnn():
	carrer = create_missionnn()
	if carrer != None:	
		token = carrer['token']
		skip_missionnn(token)
		
		
headers['X-Authorization'] = auth




         
def ngopi():
    for i in range(jum):
             pass_mission()
def ngopii():
    for i in range(haya):
             pass_missionnn()
         
def crot():
    for i in range(gugun):
             pass_scs()
             
def crott():
    skip_missionnnnn()
    countdownTimer(36, 00) 

 
def ketik(c):
    for e in c + "\n" :
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.002)
ketik("SCRIPT BUSSID V3.7.1")   
system("clear")
kal = datetime.datetime.now()



def menu1():
    sys.stdout.write(e)
    sys.stdout.flush()
    sleep(0.002)
   
    
ketik(f"\33[36;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#ketik(f"{white}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
ketik(f"""     {white}╔══╗╔╗─╔╦═══╗──╔═══╦══╦═╗╔═╦╗─╔╦╗──╔═══╦════╦═══╦═══╗╔══╦═══╗
     {white}║╔╗║║║─║║╔═╗║──║╔═╗╠╣╠╣║╚╝║║║─║║║──║╔═╗║╔╗╔╗║╔═╗║╔═╗║╚╣╠╩╗╔╗║
     {white}║╚╝╚╣║─║║╚══╗──║╚══╗║║║╔╗╔╗║║─║║║──║║─║╠╝║║╚╣║─║║╚═╝╠╗║║─║║║║
     {red}║╔═╗║║─║╠══╗╠══╬══╗║║║║║║║║║║─║║║─╔╣╚═╝║─║║─║║─║║╔╗╔╝╚╣║─║║║║
     {red}║╚═╝║╚═╝║╚═╝╠══╣╚═╝╠╣╠╣║║║║║╚═╝║╚═╝║╔═╗║─║║─║╚═╝║║║╚╗╔╣╠╦╝╚╝║
     {red}╚═══╩═══╩═══╝──╚═══╩══╩╝╚╝╚╩═══╩═══╩╝─╚╝─╚╝─╚═══╩╝╚═╩╩══╩═══╝""")
#ketik(f"{white}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
ketik(f"\33[36;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
ketik(f"""   {white} - Pembuat {green}OTAK ATIK APK           {white}  - YouTube {green} OTAK ATIK APK """)
ketik(f"""   {white} - Script {green}BUS SIMULATOR ID        {white}  - Version {green} 5.0 """)
ketik(f"\33[36;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
ketik(f"""   {white} -  {green} JANGAN LUPA SUBSCRIBE LIKE KOMEN CHANNEL SAYA""")
ketik(f"""   {white} -  {green} DON'T FORGET TO SUBSCRIBE LIKE COMMENT MY CHANNEL""")
ketik(f"\33[36;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def mxx():
	data = json.dumps({"PlayFabId":None,"InfoRequestParameters":{"GetUserAccountInfo":True,"GetUserInventory":True,"GetUserVirtualCurrency":True,"GetUserData":False,"UserDataKeys":None,"GetUserReadOnlyData":True,"UserReadOnlyDataKeys":None,"GetCharacterInventories":False,"GetCharacterList":False,"GetTitleData":True,"TitleDataKeys":None,"GetPlayerStatistics":False,"PlayerStatisticNames":None}})
	response = requests.post('https://4ae9.playfabapi.com/Client/GetPlayerCombinedInfo', headers=headers, data=data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			pass
		elif parser['code'] == 200:
			backend_data = parser['data']
			if "apiError" in str(backend_data):
				pass
			else:
				chat = backend_data['InfoResultPayload']
				uang= chat['UserVirtualCurrency']
				money= uang['RP']
				
				gcc= chat['AccountInfo']
				id= gcc['TitleInfo']
				you= id['DisplayName']
				ketik(f"{white}    - Total_Money: {green}{money}       {white}    - You_Id: {green}{you}")
				
ketik(f"{white}                         Info Yo Account")				
def hack():
	mxx()
					
headers['X-Authorization'] = auth



hack()
ketik(f"\33[36;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
ketik(f" {white} Di Pilih Salah Satu:")
ketik(f"           {yellow}[{red}1{yellow}] {green}TopUp UB 1+JT/DeTik")
ketik(f"           {yellow}[{red}2{yellow}] {green}TopUp UB 800+RB/DeTik")
ketik(f"           {yellow}[{red}3{yellow}] {green}TopUp UB 500+RB/DeTik")
ketik(f"           {yellow}[{red}4{yellow}] {green}EXIT")












contoh = input (f"{white} options:")
if contoh =="1":
   jum = int(input(f"{yellow}                    𝐉𝐔𝐌𝐋𝐀𝐇 𝐍𝐔𝐘𝐔𝐋 :{red} "))
   ngopi()
elif contoh =="2":
   haya = int(input(f"{yellow}                    𝐉𝐔𝐌𝐋𝐀𝐇 𝐍𝐔𝐘𝐔𝐋 :{red} "))
   ngopii()
elif contoh =="3":
     gugun = int(input(f"{yellow}                    𝐉𝐔𝐌𝐋𝐀𝐇 𝐍𝐔𝐘𝐔𝐋 :{red} "))
     crot()
elif contoh =="4":    
     sys.exit()