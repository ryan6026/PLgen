# coding=utf-8
import requests
from bs4 import BeautifulSoup as bs
import os, sys, glob
import re
import numpy as np
from requests_html import HTMLSession 
import eyed3

googleBase = 'https://www.google.com/search?q='
YTbase = 'https://www.youtube.com/results?search_query='

print(r"""\
;:;;;:;:;,;;;:;;::;:::;;;;;;;;;:;;:;;,'.';:;;:;;;::;;;;;:;;'.;oOXW
;;;;;;;;:::;;:;;::;;;;:;;;;;;;;:;;:;;;:;..;:;;;;;::;;:;;;;;:;;',:xXWW
;;;;;;;;::;;;;;;;;;;;;;:::::::::::::::::;'.,;;;;;;;;;;;;;;;:::;:,';k
;;;;;;::::;::;,,,,,,,,''''''''.'',,,,,'',;'.,:;;;;;;;;;;::;;;;;;;;''l0
;;;;;;:;:;,''''',,'''''..'..'''......',,''...;;;;;;;;;;;;'''''''''''.;lxKW
;:;:;;:;;'.',,''''',,',,,,,,'''''',,'..,::,..';:;::;;:;,'..',,,,,,,,,'..'o0W
:;;;::;'.','..',;;;:::::::::::;,,'.',,'.'';;,..;:;;;,'.''..'',,,,,,,'',,..;0W
;;;;:;..;,.';;;;;;;;;;;;;;;,,;,,;,'........';;.';:;'',''...';;;;,;;;;,.'',x
;;;;;;'''...',coooooc'.,'.      .;dxxkxo:'''.,'.;:;;,''.........:oc,,,'..,O
;;;:;;;;;;;,',cloxKO, .:;   .,;. .OMMMMMWO,,,..';:;';l' ,c.   ..'xKkdl,.'xW
:;;;;;;:;;;;;;;;,','   .'.  lXK: .xMMMMMMWd';,.':,.ld.  ..   ,kO,;XMMMWXc.d
::;;;;;::;;;;,'',;;,.. .'.  .'.  .kWMMMMMMo';,,;.:Ko   ...  .cc.;XMMWKo,.oWW
::;;;;;;;:;;:;,'..,;:;;,,'...    :XWWWWWOxl'.';;.;o;           .ckxdl,'';kWW
;;;;;;;;;;::;;;;;,'''',,,;;;;,''.,clolol:,,,,..,:;;;,''''''''''',;,,,,''l0W
;;:;;;;;;;::;;;;;:;;,,'''',,'',,',,,,,,',''''',;:;''..',,,,,;;;;;,,,'..lXW
:;;::;;;;;::;;:;;::;;::::;;;;;;;,,,,,,,'..';;::;::;,'.....',;;;;,'''..',lKW
;:;:;,'',;:;;:;;;;;;:;;:;;;;;;:;;:;:;,'..;;;::::::;;;;,,'..,;:;;,,,,,;:;'cKW
::;;;,,;;;;::;;;;;;;;;:;;;;;::;;:;;,'.',;:;;:::;;;;:;;;;;;,..,;:;;;:::::;.;0W
;;;,''',,,;::;::;;;;;;::;;;:;;,''''',;;;;;;;;;;;;;;;;;;;;;:;,';::;;::::;;'.'x
:;'....','',;;::;;;;:::::;;,'''',;:::;;;;;;;;;;;;;:::;;;;;;;:::;;;:;;;;:;..',OW
:;;;..'''..''''',,;;;;:::;;;;;:;;;;:::::;;;;;;;;;;;;;;;;;;:;::;;;:;;:;:;..'':0
;;:;'.',,...''''..'''''''',,;;::;;:;;;;;;;;;;:;;:;;;;;;;:;;;;;;:;:;;;:;'..'oKWW
::;;;,...'''....',,,,,''''''.''''',,,,;;;;;;::::::::::::::::::::::;,'.'..'x
;::;;:;;,'..'''.....'..'',,,,,,'''''''''''''''''',,,,,,',,,,,,,''''..''..o
;;;;::;;::;,''..''',,'''''...''''''''''',,,,,,,,,,,,,,,,,,,,,,,,,,''...''lX
:;;:::;;::;;:;,,'''..,,,,,,,,,,,,,''''..'..'''''''''''''''''''''''...',,.cK
;;;;;;;;;;;;;;;::::,'...',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,''cOW
::;;;;;;;;;;;;:::::;:;,''...'''',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'..d
;;;;;;;;;;;;;;;;;:;;:;:::;;,'''''...'''''''''''''''''''''''''''''...'.,k
;;;;;;;;;;;;;;;;;;::;;:;;;;;;::::;;;;,,,,,,,,,,,,,,,,,,,,,',,,,,',,;:':KW
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::::::::::;;:::;;;:;,''''',;;;,,x
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:;;;;:;;;,'..',;,'....;kX
_____________                 __   __          __      _______                                    __
\______   \  | _____  ___.__.|  | |__| _______/  |_   /  _____/  ____   ____   ________________ _/  |_  ___________ 
 |     ___/  | \__  \<   |  ||  | |  |/  ___/\   __\ /   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
 |    |   |  |__/ __ \\___  ||  |_|  |\___ \  |  |   \    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
 |____|   |____(____  / ____||____/__/____  > |__|    \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|   
                    \/\/                  \/                 \/     \/     \/     \/           \/                   
    _                     ___                                        ___  
   FJ___    _    _       F _ ",    _    _     ___ _    _ ___        F _ ",
  J  __ J  J |  | L     J `-'(|   J |  | L   F __` L  J '__ J      J `-' |
  | |--| | | |  | |     |  _  L   | |  | |  | |--| |  | |__| |     |  __/F
  F L__J J F L__J J     F |_\  L  F L__J J  F L__J J  F L  J J     F |__/ 
 J__,____/L)-____  L   J__| \\__L )-____  LJ\____,__LJ__L  J__L   J__|    
 J__,____FJ\______/F   |__|  J__|J\______/F J____,__F|__L  J__|   |__L    
           J______F               J______F                                

""")

print(r"""\
""")
input("Press Enter to download playlist")

try:
  os.mkdir("playlist")
except:
  print("folder 'playlist' already exists.\nPlease rename or delete the folder and restart")
  input(' ')
  sys.exit('')

artists_file=open("art.txt")
artists=artists_file.readlines()
artists_file.close()
for query in artists:
  query=query.replace('\n','')
  print(query)
  session = HTMLSession()
  response = session.get(googleBase+query.replace(' ', '+')+'+songs')
  session.close()
  response.html.render(sleep=1)
  soup = bs(response.html.html, "html.parser")

  results=soup.find_all("h3", {"class": "zBAuLc l97dzf"})
  search_titles=[]
  for result in results:
      result=str(result)
      search=re.search('d">.*</div>',str(result))
      if search is not None:
          tmp=result[search.start()+3:search.end()-6]
          search_titles.append(tmp.lower())
  for test in search_titles:
      if test.find(query)>-1:
          search_titles.remove(test)
          
  print(search_titles) ## all lowercase
  for test in search_titles:
      test=test.replace('\n','')
      print(test)
      session = HTMLSession()
      response = session.get(YTbase+'intitle:"'+query.replace(' ', '+')+'+'+test.replace(' ', '+')+'"')
      session.close()
      response.html.render(sleep=1)
      soup = bs(response.html.html, "html.parser")
      results=soup.find_all("ytd-video-renderer", {"class": "style-scope ytd-item-section-renderer"})
      titles=[]
      views=[]
      runMins=[]
      vidIDs=[]
      viewCnt=0
      for result in results:
          data=''
          for line in result:
              data=data+str(line)
              
          ## get views
          try:
              viewTmp1 = re.findall('[0-9,KkM]{2,13} views', data)
              if(len(viewTmp1)>1):
                  viewTmp1=viewTmp1[0]
              viewTmp2=str(viewTmp1)
              viewCnt = int(viewTmp2[0:viewTmp2.find(' views')].replace(',',''))
          except:
              viewCnt = 0
              #print('views not found')
              
          ## get title
          try:
              title = re.findall('aria-label="[0-9A-Za-z-. ]{4,80}', data)
              if(len(title)>1):
                  title=title[0]
              title=title[12:len(title)]
          except:
              title=''
              #print('title not found')
              
          ## get ID
          try:
              ID = re.findall('href="/watch.v=...........', data)[0]
              ID=ID[6:len(ID)]
          except:
              ID=''
              #print('ID not found')
              
          ## get video length
          try:
              vidLen = re.findall('[0-9]{1,2} min.* [0-9]{1,2} sec', data)    
              if(len(vidLen)>1):
                  vidLen=vidLen[0]
                  mins = int(vidLen[0:vidLen.find(' minutes')])
              if(len(vidLen)<1):
                  mins=0
          except:
              #print('video over 1hour')
              vidLen = re.findall('[0-9]{1,2} hour.* [0-9]{1,2} min', data)
              mins=0
          
          #print( viewCnt>0, ", ", len(title)>0, ", ", mins > 0, ", ", title.find(test)>-1  )
          if viewCnt>0 and len(title)>0 and mins > 0 and title.lower().find(test)>-1:
              views.append(viewCnt)
              titles.append(title)
              runMins.append(mins)
              vidIDs.append(ID)
          #else:
              #print(viewCnt, ", ", title, ", ", mins, " mins, ", test)
              
      titles2 = np.array(titles)
      views2 = np.array(views)
      vidIDs2 = np.array(vidIDs)
      runMins2 = np.array(runMins)
      inds = views2.argsort()
      sorted_titles=titles2[inds]
      sorted_views=views2[inds]
      sorted_vidIDs=vidIDs2[inds]
      sorted_runMins = runMins2[inds]
      
      if(len(sorted_titles)>0):
        ## download with correct name depending on sorted_title[-1]
        ## proper name:  <artist> - <song name>
        # query is artist, test is song name
        if(len(re.findall(query+'[- ]{1,5}'+test, sorted_titles[-1].lower()))>0):
          save_title = sorted_titles[-1]
        else:
          save_title = query+' - '+test
        cmd='yt-dlp -P ./playlist -o "'+save_title+'" --extract-audio --geo-bypass "https://www.youtube.com'+sorted_vidIDs[-1]+'"'
        cmd=cmd.replace('\n', '')
        os.system(cmd)
        print(sorted_titles[-1], ", ", sorted_views[-1], " views, ", sorted_runMins[-1], " mins")
      else:
        print('no results')

print("converting files to mp3")
files=glob.glob('./playlist/*.opus')
for file in files:
  print('ffmpeg.exe -i "'+ file + '" -vn ' +  file[0:len(file)-5]+'.mp3')
  os.system('ffmpeg.exe -i "'+ file + '" -vn "' +  file[0:len(file)-5]+'.mp3"')
  os.remove(file)


## fixing names???
  
for file in os.listdir('./playlist'):
  name=file
  os.rename(os.path.join('./playlist/',file), os.path.join('./playlist/', name))
  if(file.count('-')==2 and not '--' in file):
    file=name
    name=name[name.find('-')+1:len(name)]
  os.rename(os.path.join('./playlist/',file), os.path.join('./playlist/', name))


files=glob.glob('./playlist/*.mp3')
for file in files:
  name=file
  if '[' in name:
    pos1 = name.find('[')
    pos2 = name.find(']')
    name=name[0:pos1]+name[pos2+1:]
  if '[' in name:
    pos1 = name.find('[')
    pos2 = name.find(']')
    name=name[0:pos1]+name[pos2+1:]
  if '(Official)' in name:
    name.replace("(Official)", '')
  if '(official)' in name:
    name.replace("(official)", '')
  if '(Official Video)' in name:
    name.replace("(Official Video)", '')
  if '(video)' in name:
    name.replace("(video)", '')
  if '(Video)' in name:
    name.replace("(Video)", '')
  print(name+'\n')
  os.rename(file, name)

files=glob.glob('./playlist/*.mp3')
for i in range(len(files)):
  audiofile = eyed3.load(files[i])
  files[i]=files[i][11:len(files[i])]
  try:
    artist=files[i][0:files[i].find('-')]
    title = files[i][files[i].find('-')+1:len(files[i])].replace('.mp3','')
    
  except:
    artist=files[i][0:files[i].find('"')]
    title = files[i][files[i].find('"'):len(files[i])].replace('.mp3','')

  audiofile.tag.artist = artist
  audiofile.tag.title = title
  audiofile.tag.save()

for file in os.listdir('./playlist'):
  try:
    os.rename(os.path.join('./playlist/',file), os.path.join('./playlist/',file[(file.find('-')+1):len(file)]))
  except:
    ''
  try:
    os.rename(os.path.join('./playlist/',file), os.path.join('./playlist/',file[(file.find('"')+1):len(file)]))
  except:
    ''

## to do: remove the by __artist__ years minutes...
##files=glob.glob('*.mp3')
##for file in files:
##    name=file
##    name.replace('#','')
##    s = re.findall('by.*[0-9]{1,2} year.*[0-9]{1,2} minutes', name)
##    if(len(s)>0):
##        s = re.search('by.*[0-9]{1,2} year.*[0-9]{1,2} minutes', name)
##        name=name[0:s.start()].strip()
##    os.rename(file,name)        
