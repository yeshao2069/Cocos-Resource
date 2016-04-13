#!/usr/bin/python
# coding=utf-8

from bs4 import BeautifulSoup
import re
from collections import OrderedDict
import time
from urllib import quote
import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')

soup = BeautifulSoup(open("cocos2dx-download.html"))


# functions
def new_line(f):
	f.write("\n")

def generate_download_md(file_name, dict, download_files, desc):
	f = open(file_name, 'w')
	f.write(desc)
	new_line(f)
	for k in dict:
		# dict[k].sort()
		# dict[k].reverse()
		f.write("####" + k + '\n')
		new_line(f)
		f.write("| 文件名 | 下载链接 |\n|:-------------| :----------------------------------: |\n")
		for file_name in dict[k]:
			f.write("|" + file_name + "|" + "[" + "点击下载" + "](" + download_files[file_name] +")" + "|\n")
		new_line(f)
	f.close()


def getUrlEncode(str_line):
	lower_str_line = str_line.lower()
	lower_str_line = quote(lower_str_line)
	lower_str_line = lower_str_line.replace('%20', '-')
	return '#' + lower_str_line

cocos2dx_download_files = {}

cocos2dx_exclude_download_files = [
'js-fantasywarriors3d.apk', 
'Android-SDK.zip', 
'android-ndk-r10e-Windows.zip', 
'Android-SDK-Windows.zip', 
'jdk-8u45-windows-x64.exe', 
'tiled-0.11.0-win32-setup.exe', 
'android22-sdk-macosx.zip', 
'pu_editor_setup_bin_src.exe', 
'android-ndk-r10e-macosx.zip', 
'JDK8ForOSX.pkg', 
'jdk-6u32-windows-i586.exe', 
'EarthWarrior3D.zip', 
'android-ndk-r10d-windows.zip', 
'jdk-6u32-windows-x64.exe', 
'JavaForOSX.pkg', 
'arm-ds-5-5.20.0.20141022-for-cci.zip', 
'android-ndk-r10d-windows-x86.zip', 
'arm-ds-5-5.20.0.20141022-for-cci.zip', 
'FantasyWarrior3D.zip', 
'tiled-0.11.0.dmg', 
'CCS_Required_dotNetFx40_Full_x86_x64.exe', 
'LuaPublish_1.2.zip', 
'CCS_Required_gtk-sharp-2.12.22.msi', 
'LuaPublish_1.3.2.zip', 
'android-ndk-r10c-macosx.zip', 
'v226-jscompile.zip', 
'android-sdk-macosx.zip', 
'CCS_Required_vcredist_x86_2012.exe', 
'CCS_Required_vcredist_x86.exe', 
'update', 
'CCS_Required_AccessDatabaseEngine.exe', 
'FantasyWarrior3D-debug.apk.zip', 
'android-sdk-windows.zip', 
'CCS_Required_gtk-sharp.msi', 
'JavaForOSX2014-001.dmg', 
'LuaPublish_1.3.zip', 
'LuaPublish_1.1.zip', 
'Intel_CCF_SDK.zip', 
'android-ndk-r10d-windows-x86.exe', 
'LuaPublish.zip', 
'EarthWarrior3D-CSDK_store.rar', 
'jsbcc', 
'ds5-installer.zip', 
'BTest', 
'ATEST', 
'CCS_Required_MonoFramework_MRE_3.10.0.pkg',
'CocosVS_0.1.zip',
'cocos-reader',
'Cocos Animation Editor.exe',
'Cocos3dSamples.zip',
'CocosSkeletalAnimationEditor v1.6.0.exe',
'cocos2d-x-3.1-amazon',
'Cocos2d-JS-v3.0-API.zip',
'Cocos2d-JS-v3.6-API.zip',
'Cocos2d-JS-v3.0-beta-API.zip',
'Cocos2d-JS-v3.0-rc0-API.zip',
'Cocos2d-JS-v3.2-RC0-API.zip',
'Cocos2d-JS-v3.2-API.zip',
'Cocos2d-JS-v3rc2-API.zip',
'Cocos2d-JS-v3.3-API.zip',
'Cocos2d-JS-v3.0-rc3-API.zip', 
'CCS_Required_MonoFramework_MRE_3.10.0.pkg',
'CocosStudioSamples.zip',
'CocosForMacWithFramework_v2.3.2.dmg',
'Cocos 2d-JS-v3.0.zip', 
'cocos2d-x-3.1rc0-amazon',
'cocos2d-x-4.0alpha1.zip',
'cocos2d-x-4.0alpha0.zip',
'cocos2d-x-3.9RC0.zip',
'cocos2d-x-3.1-cn',
'cocos2d-x-3.0-zip-cncdn',
'cocos2d-x-4.0alpha0.zip', 
'cocos2d-x-4.0alpha1.zip',
'cocos2d-x-2.2.4',
]

cocos2dx_framework_download_files = [
'CocosFramework-V3.7.1-Mac.pkg',
'CocosFramework-v3.6.exe', 
'CocosFramework-v3.5.exe', 
'CocosFramework-v3.4rc1-windows.exe', 
'CocosFramework-V3.9-Windows.exe', 
'CocosFramework-v3.6.pkg', 
'CocosFramework-V3.8-Windows.exe', 
'CocosFramework-V3.8.1-Windows.exe', 
'CocosFramework-V3.9-Mac.pkg', 
'CocosFramework-V3.9-Mac.pkg', 
'CocosFramework-V3.8-Mac.pkg', 
'CocosFramework-v3.7.exe', 
'CocosFramework-V3.7.1-Windows.exe', 
'CocosFramework-V3.8.1-Mac.pkg', 
'CocosFramework-v3.4-windows.exe', 
'CocosFramework-v3.4-mac.pkg', 
'CocosFramework-v3.5.pkg', 
'CocosFramework-v3.7.pkg', 
'CocosFramework-v3.4rc1-mac.pkg', 
'CocosFramework-v3.4.2-windows.exe', 
'CocosFramework-v3.4.2-mac.pkg',
'CocosFrameworkSamples_v3.8.zip',
'CocosFrameworkSamples_v3.9.zip'
]

cocos2dx_ide_download_files = [
'cocos-code-ide-win64-1.0.0-rc1.exe',
'cocos-code-ide-win64-1.0.0-beta-zip-cncdn', 
'cocos-code-ide-win32-1.2.0.exe', 
'cocos-code-ide-mac64-1.2.0.dmg', 
'cocos-code-ide-win64-1.2.0.exe', 
'cocos-code-ide-2.0.0-beta.dmg', 
'cocos-code-ide-2.0.0-beta.exe', 
'cocos-code-ide-mac64-1.1.0.dmg', 
'cocos-code-ide-win64-1.0.2.exe', 
'cocos-code-ide-win64-1.0.2.exe', 
'cocos-code-ide-mac64-1.0.0-rc2.dmg', 
'cocos-code-ide-mac64-1.0.0-rc1.dmg', 
'cocos-code-ide-mac64-1.0.0-beta-zip-cncdn', 
'cocos-code-ide-win64-1.0.0-rc2.zip', 
'cocos-code-ide-win64-1.0.0-rc1.zip', 
'cocos-code-ide-win32-1.0.0-beta-zip-cncdn', 
'cocos-code-ide-win64-1.1.0.exe', 
'cocos-code-ide-win32-1.0.0-rc1.zip', 
'cocos-code-ide-win32-1.1.0.exe', 
'cocos-code-ide-mac64-1.0.1.dmg', 
'cocos-code-ide-mac64-1.0.2.dmg', 
'cocos-code-ide-win64-1.0.1.exe', 
'cocos-code-ide-win32-1.0.0-rc1.exe', 
'cocos-code-ide-win32-1.0.2.exe', 
'cocos-code-ide-mac64-1.0.0-rc0.dmg', 
'cocos-code-ide-win32-1.0.1.exe', 
'cocos-code-ide-1.1.0-update.zip', 
'cocos-code-ide-1.0.2-update.zip', 
'cocos-code-ide-win64-1.0.0-rc2.exe', 
'cocos-code-ide-win32-1.0.0-rc2.zip', 
'cocos-code-ide-win32-1.0.0-rc2.exe', 
'cocos-code-ide-win64-1.0.0-rc0.zip', 
'cocos-code-ide-win32-1.0.2-beta.zip', 
'cocos-code-ide-mac64-1.0.2-beta.zip', 
'cocos-code-ide-win64-1.0.0-final.exe', 
'cocos-code-ide-win64-1.0.0-rc0.exe', 
'cocos-code-ide-mac64-1.0.0-rc0.zip', 
'cocos-code-ide-win32-1.0.0-rc0.zip', 
'cocos-code-ide-win64-1.0.2-beta.zip', 
'cocos-code-ide-win32-1.0.0-final.exe', 
'cocos-code-ide-mac64-1.0.0-final.dmg', 
'cocos-code-ide-win32-1.0.0-rc0.exe', 
'cocos-code-ide-win32-1.0.0-final.zip', 
'cocos-code-ide-win64-1.0.0-final.zip',
'cocos-intellij-plugin-2.0.0-beta.zip'
]

cocos2dx_studio_download_files = [
'CocosStudioForWin-v2.0.6.exe',
'CocosStudio_v1.0.0.0_Beta.dmg', 
'CocosStudio_v1.6.0.0.exe', 
'CocosStudioForMac-v2.0.2.dmg', 
'CocosStudioForMac-v2.0.5.dmg', 
'CocosStudioForMac-v2.0.6.dmg', 
'CocosStudioForWin-v2.1.exe', 
'CocosStudioForWin-v2.1.exe', 
'CocosStudio_v1.5.0.1.exe', 
'CocosStudioForMac-v2.1.dmg', 
'CocoStudio(2DX3.0)_v1.4.0.1.exe', 
'CocosStudioForMac-v2.1-Beta.dmg', 
'CocoStudio_v1.4.0.1.exe', 
'CocosStudioForWin-v2.1-Beta.exe', 
'CocosStudio_v1.5.0.0.exe',
'CocosStudioForWin-v2.0.0.0-Beta0.exe', 
'CocosStudioForWin-v2.0.5.exe', 
'CocosStudioForWin-v2.0.2.exe', 
'CocosStudioForMac-v2.1-Update.pkg', 
'CocosStudioForMac-v2.0.5-Update.pkg', 
'CocosStudioForMac-2.0.0.0-Alpha.dmg', 
'CocosStudioForMac-2.0.0.0-Beta0.dmg', 
'CocoStudio_v1.0.0.0_Alpha1.dmg', 
'CocoStudio(2DX2.2.3)_v1.4.0.1.exe', 
'CocosStudioForMac-v2.0.0.0-Beta0.dmg', 
'CocosStudioForWin_v2.0.0.0_Alpha.exe', 
'CocosStudio_v1.6.0.0_store.exe', 
'CocosStudioForWin-v2.0.6-Update.exe', 
'CocosStudioForMac-v2.0.6-Update.pkg', 
'CocosStudioForWin-v2.1-Update.exe', 
'CocosStudioForWin-v2.0.5-Update.exe', 
'CocosStudioForWin-v2.0.2-Update.exe', 
'CocosStudioForMac-v2.0.2-Update.pkg', 
'CocosStudioForMac_v2.0.0.0_Alpha.dmg', 
'CocosStudioForMac_2.0.0.0_Alpha.dmg', 
'CocosStudioForMac-2.0.0.0_Alpha.dmg', 
'CocosStudioForWin-2.0.0.0-Beta0.exe'
]

cocos2dx_cocos_download_files = [
'CocosForWin-v3.10.exe', 
'CocosForMac-v3.10-Update.pkg', 
'CocosForWin-v2.3.3.exe', 
'CocosForWin-v3.10-Update.exe', 
'CocosForMac-v3.10.dmg', 
'CocosForWinWithFramework-v2.3.2.3.exe', 
'CocosForMacWithFramework-v2.3.3.dmg', 
'CocosForWinWithFramework-v2.3.3.exe', 
'CocosForMacWithFramework-v2.3.2.3.dmg', 
'CocosForWinWithFramework-v2.3.2.exe', 
'CocosForMacWithFramework-v2.3.2.dmg',
'CocosForWin-v2.2.5.exe', 
'CocosForMac-v2.3.3.dmg', 
'CocosForWin-v2.3.2.3.exe', 
'CocosForWin-v2.1.5.exe', 
'CocosForWin-v2.2.9-Update.exe', 
'CocosForMac-v2.3.1.2-Update.pkg', 
'CocosForWin--v2.3.0.exe', 
'CocosForWin-v2.2.6-Update.exe', 
'CocosForWin-v2.1.5-Update.exe', 
'CocosForWin-v2.2.6.exe', 
'CocosForWin-v2.3.3-Update.exe', 
'CocosForWin-v2.3.1.1.exe', 
'CocosForWin-v2.2.5-Update.exe', 
'CocosForWin-V2.2.8.exe', 
'CocosForWin-v2.3.2Beta.exe', 
'CocosForWin-v2.2.1.exe', 
'CocosForWin-v2.3.1.1-Update.exe', 
'CocosForWin-v2.1.exe', 
'CocosForMac-v2.1.dmg', 
'CocosForMac-v2.3.3-Update.pkg', 
'CocosForMac-v2.3.2.3-Update.pkg', 
'CocosForWin-v2.1.2Beta.exe', 
'CocosForMac-v2.3.2Beta1.dmg', 
'CocosForMac-v2.3.2.3.dmg', 
'CocosForMac-v2.3.1.dmg', 
'CocosForMac-v2.3.2.dmg', 
'CocosForMac-v2.3.1.1.dmg', 
'CocosForMac-v2.2.1.dmg', 
'CocosForMac-v2.2.5.dmg', 
'CocosForMac-v2.2.6.dmg', 
'CocosForMac-V2.2.8.dmg', 
'CocosForMac-v2.1.5.dmg', 
'CocosForWin-V2.3.0.exe', 
'CocosForMac_v2.3.0.dmg', 
'CocosForWin-v2.3.1.2.exe', 
'CocosForMac_v2.3.2Beta.dmg', 
'CocosForWin-v2.3.1.exe', 
'CocosForMac-v2.1.2Beta.dmg', 
'CocosForWin-v2.3.2.3-Update.exe', 
'CocosForMac-v2.1.5-Update.pkg', 
'CocosForWin-v2.2.9.exe', 
'CocosForWin-v2.3.2.exe', 
'CocosForMac-v2.3.1.2.dmg', 
'CocosForWin-V2.2.8-Update.exe', 
'CocosForMac-v2.3.2Beta.dmg', 
'CocosForWin-V2.3.0-Update.exe', 
'CocosForWin-v2.3.1.2-Update.exe', 
'CocosForWin-v2.2.1-Update.exe', 
'CocosForWin-v2.2.1-Update-WithNet45.exe', 
'CocosForMac-V2.3.0.dmg', 
'CocosForMac_v2.3.2.dmg', 
'CocosForMac_v2.3.2-Update.pkg', 
'CocosForWin-v2.1-Update.exe', 
'CocosForMac-v2.3.2-Update.pkg', 
'CocosForWin-v2.3.2-Update.exe', 
'CocosForMac-v2.2.1-Update.pkg', 
'CocosForWin--v2.3.0-Update.exe', 
'CocosForMac-v2.3.1.1-Update.pkg', 
'CocosForMac_v2.3.0_Update.pkg', 
'CocosForWin-v2.3.1-Update.exe', 
'CocosForMac-v2.3.1-Update.pkg', 
'CocosForMac-v2.2.9-Update.pkg', 
'CocosForMac-V2.3.0-Update.pkg', 
'CocosForMac-V2.2.8-Update.pkg', 
'CocosForMac-v2.2.6-Update.pkg', 
'CocosForMac-v2.2.5-Update.pkg', 
'CocosForWin-v2.1.5-UpdateWithDotNet.exe', 
'CocosForMac-v2.1-Update.pkg',
'Cocos-v1.0-preview-win32.exe',
'Cocos-v1.0-preview-mac64.dmg',
'Cocos-v1.0-preview-win64.exe'
]

cocos2dx_creator_download_files = [
'CocosCreator_v1.0.0_win_en',
'CocosCreator_v1.0.0_win',
'CocosCreator_v1.0.0_mac_en',
'CocosCreator_v1.0.0_mac',
'CocosCreator_v0.7.1_win_en',
'CocosCreator_v0.7.1_mac_en',
'CocosCreator_v0.7.0_mac.zip', 
'CocosCreator_v0.7.0_win.zip'
]

cocos2dx_simulator_download_files = [
'CocosSimulatorWin_v1.0.exe',
'CocosSimulatorMac_v1.0.pkg'
]

cocos2dx_cpp_download_file = [
'cocos2d-x-3.10.zip', 
'cocos2d-x-3.6.zip', 
'cocos2d-x-3.9.zip', 
'cocos2d-x-3.7.zip', 
'cocos2d-x-3.9beta0.zip', 
'cocos2d-x-3.5.zip', 
'cocos2d-x-3.7.1.zip', 
'cocos2d-x-3.8.zip', 
'cocos2d-x-2.2.6.zip', 
'cocos2d-x-3.3.zip', 
'cocos2d-x-3.0-cn', 
'cocos2d-x-3.3beta0', 
'cocos2d-x-3.8.1.zip', 
'cocos2d-x-3.2.zip', 
'cocos2d-x-3.4.zip', 
'cocos2d-x-3.8beta0.zip', 
'cocos2d-x-3.3rc0.zip', 
'cocos2d-x-2.2.5.zip', 
'cocos2d-x-3.4beta0.zip', 
'cocos2d-x-3.6beta0.zip', 
'cocos2d-x-3.8-rc0.zip', 
'cocos2d-x-3.0rc2-cn', 
'cocos2d-x-3.1.1.zip', 
'cocos2d-x-3.3rc1.zip', 
'cocos2d-x-3.1.zip',  
'cocos2d-x-3.6alpha0.zip', 
'cocos2d-x-3.2rc0.zip', 
'cocos2d-x-3.4rc1.zip', 
'cocos2d-x-3.3rc2.zip', 
'cocos2d-x-3.4rc0.zip', 
'cocos2d-x-3.5-tizen.zip', 
'cocos2d-x-2.2.4.zip', 
'cocos2d-x-3.5beta0.zip', 
'cocos2d-x-3.7rc1.zip', 
'cocos2d-x-3.7beta0.zip', 
'cocos2d-x-3.5rc0.zip', 
'cocos2d-x-3.7rc0.zip', 
'cocos2d-x-3.2alpha0.zip', 
'cocos2d-x-3.1rc0', 
'cocos2d-x-3.9rc0.zip', 
'cocos2d-x-3.9RC0.zip'
]

cocos2dx_js_download_file = [
'cocos2d-js-v3.6.1.zip', 
'cocos2d-js-v3.6.zip', 
'cocos2d-js-v3.3.zip', 
'cocos2d-js-v3.1.zip', 
'cocos2d-js-v3.2-rc0.zip', 
'cocos2d-js-v3.0-rc2.zip',
'cocos2d-js-v3.0.zip', 
'cocos2d-js-v3.5.zip', 
'cocos2d-js-v3.2.zip', 
'cocos2d-js-v3.0-beta.zip', 
'cocos2d-js-v3.3-rc0.zip', 
'cocos2d-js-v3.0-rc1.zip', 
'cocos2d-js-v3.1-beta.zip', 
'cocos2d-js-v3.0-rc3.zip', 
'cocos2d-js-v3.0-alpha2-zip-cncdn', 
'cocos2d-js-v3.0-rc0.zip', 
'cocos2d-js-v3.3-beta.zip', 
'cocos2d-js-v3.6-beta.zip', 
'cocos2d-js-v3.0-rc0-hotfix.zip', 
'cocos2d-js-v3.4-beta0.zip', 
'cocos2d-js-v3.7beta0.zip', 
'cocos2d-js-v3.0-pre.zip'
]

# Get all files
for link in soup.find_all('a'):
	internalLink = "http://www.cocos2d-x.org" + link.get('href')
	# print(internalLink)
	file_name = link.string
	# print(file_name)
	download_link = "http://www.cocos2d-x.org/filedown/" + link.string
	# print(download_link)
	cocos2dx_download_files[file_name] = download_link


# Check new files
record_download_files = [
	cocos2dx_cpp_download_file,
	cocos2dx_js_download_file,
	cocos2dx_cocos_download_files,
	cocos2dx_studio_download_files,
	cocos2dx_framework_download_files,
	cocos2dx_simulator_download_files,
	cocos2dx_ide_download_files,
	cocos2dx_creator_download_files,
	cocos2dx_exclude_download_files
]

not_find_files = []
for i in cocos2dx_download_files:
	isFindFile = False
	for j in record_download_files:
		for k in j:
			if i == k :
				isFindFile = True
				break
	if not isFindFile:
		not_find_files.append(i)
		print '\'' + i + '\','
if len(not_find_files) > 0 :
	print 'Please add not_find_files to cocos2dx_download_files'
	sys.exit(1)

# Generate auto files
cocos2dx_engine = OrderedDict()
cocos2dx_engine['Cocos2d-x 引擎下载'] = cocos2dx_cpp_download_file
cocos2dx_engine['Cocos2d-js 引擎下载'] = cocos2dx_js_download_file
generate_download_md('auto/cocos2d-x-engine.md', cocos2dx_engine, cocos2dx_download_files, '###Cocos 引擎下载\n\n*从 v3.7 开始，Cocos2d-js 合并入 Cocos2d-x。*\n')

cocos2dx_support_tools = OrderedDict()
cocos2dx_support_tools['Cocos 下载'] = cocos2dx_cocos_download_files
cocos2dx_support_tools['Cocos Studio 下载'] = cocos2dx_studio_download_files
cocos2dx_support_tools['Cocos FrameWork 下载'] = cocos2dx_framework_download_files
cocos2dx_support_tools['Cocos Simuator 下载'] = cocos2dx_simulator_download_files
cocos2dx_support_tools['Cocos IDE 下载'] = cocos2dx_ide_download_files
cocos2dx_support_tools['Cocos Creator 下载'] = cocos2dx_creator_download_files
generate_download_md('auto/cocos2d-x-support-tools.md', cocos2dx_support_tools, cocos2dx_download_files, '###Cocos 配套工具下载\n')

# Write README
md_files_name = [
	'manual/readme-titile',
	'manual/cocos2d-x-docs',
	'auto/cocos2d-x-engine',
	'manual/cocos2d-x-engine-ext',
	'auto/cocos2d-x-support-tools',
	'manual/cocos2d-x-version-relationship',
	'manual/cocos2d-x-android-related',
	'manual/cocos2d-x-3rd-tools'
]

f = open('README_temp.md','w')
for md_file_name in md_files_name:
	with open(md_file_name + '.md', 'r') as f_temp:
		f.write(f_temp.read())
new_line(f)
f.write("更新时间：" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
f.close()

# Add toc
toc = OrderedDict()
with open('README_temp.md', 'r') as f:
	last3sharp = ''
	for line in f.readlines():
		strLine = line.strip()
		if line.find("####") != -1:
			strLine = strLine.replace('####', '')
			# print(line.strip())
			toc[last3sharp].append(strLine)
		elif line.find("###") != -1:
			# print(line.strip())
			strLine = strLine.replace('###', '')
			last3sharp = strLine
			toc[last3sharp] = []

with open('toc_urlencode.md', 'w') as f:
	for _3sharp in toc:
		f.write('- ')
		f.write('[')
		f.write(_3sharp)
		f.write('](')
		f.write(getUrlEncode(_3sharp))
		f.write(')')
		f.write('\n')
		for _4sharp in toc[_3sharp]:
			f.write('\t- ')
			f.write('[')
			f.write(_4sharp)
			f.write('](')
			f.write(getUrlEncode(_4sharp))
			f.write(')')
			f.write('\n')

with open('toc_number.md', 'w') as f:
	count = 1
	for _3sharp in toc:
		f.write('- ')
		f.write('[')
		f.write(_3sharp)
		f.write('](')
		f.write('#toc_' + str(count))
		f.write(')')
		count = count + 1
		f.write('\n')
		for _4sharp in toc[_3sharp]:
			f.write('\t- ')
			f.write('[')
			f.write(_4sharp)
			f.write('](')
			f.write('#toc_' + str(count))
			f.write(')')
			f.write('\n')
			count = count + 1

with open('README_temp.md', 'r') as fReadMe:
	strReadMe = fReadMe.read()

with open('toc_urlencode.md', 'r') as fToc:
	strToc = fToc.read()

with open('README.md', 'w') as fReadMe:
	indexOfTocFlag = strReadMe.find('<!--TOC END-->')
	if  indexOfTocFlag != -1 :
		fReadMe.write(strReadMe[:indexOfTocFlag] + '\n' + strToc + '\n' + strReadMe[indexOfTocFlag:])
	else :
		print "Toc flag not found."

with open('toc_number.md', 'r') as fToc:
	strToc = fToc.read()

with open('README_number.md', 'w') as fReadMe:
	indexOfTocFlag = strReadMe.find('<!--TOC END-->')
	if  indexOfTocFlag != -1 :
		fReadMe.write(strReadMe[:indexOfTocFlag] + '\n' + strToc + '\n' + strReadMe[indexOfTocFlag:])
	else :
		print "Toc flag not found."

# Remove temp files
os.remove('README_temp.md')
os.remove('toc_number.md')
os.remove('toc_urlencode.md')

