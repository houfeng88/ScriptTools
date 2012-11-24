# coding=utf-8
'''
use texturePacker pack imgs ,for cocos2d
'''
import os
import stat
import time
import shelve
import getImgName
TP = "/usr/local/bin/TexturePacker"
ResourcesPath = os.path.abspath("../Resources/sheet")
Srcrootpath = './Assets/'
print 'packing images ..........................'

timedb = shelve.open('packimagetime');

def fixedScoureFile(srcpath):
    filepath = Srcrootpath+srcpath
    return filepath

def isFileChanged(resname,srcpath):
    changed = False
    strlist =srcpath.split('|')
    for value in strlist:
        lastM = None
        timekey = resname+'_'+value+'-mtime'
        fileName = os.path.abspath(fixedScoureFile(value))
        if timedb and timedb.get(timekey):
            lastM=timedb[timekey]
        else:
            changed= True
        fs2 = os.stat(fileName)
        if lastM != time.ctime(fs2[stat.ST_MTIME]):
            lastM = time.ctime(fs2[stat.ST_MTIME])
            timedb[timekey]=lastM;
            changed= True
    return changed


#    scale 缩放系数 rgbformat RGB565|RGBA4444 resname 打包后文件名 srcpath 图片路径
#    forced 强迫打包
def  packimage(scale,rgbformat,resname,srcpath,forced=False):
    datafileName = ResourcesPath+"/%s.plist"%resname
    sheetfileName = ResourcesPath+"/%s.pvr.ccz"%resname
    hasdata = (os.path.exists(datafileName) or os.path.exists(sheetfileName))
    if isFileChanged(resname,srcpath) or forced or not hasdata:
        print 'packing %s iamges...'%resname
        if os.path.exists(datafileName):
            print 'remove... '+ datafileName
            os.remove(datafileName)
        if os.path.exists(sheetfileName):
            print 'remove... '+ sheetfileName
            os.remove(sheetfileName)
        
        cmd = TP+' --smart-update --scale %f'%scale
        cmd = cmd+ ' --opt %s --dither-fs-alpha  --premultiply-alpha --format cocos2d '%rgbformat
        cmd = cmd +' --max-height 4096  --max-width 4096  --data '
        cmd = cmd + ResourcesPath+"/%s.plist"%resname
        cmd = cmd +' --sheet '+ResourcesPath+"/%s.pvr.ccz"%resname
        strlist =srcpath.split('|')
        print srcpath
        for value in strlist:
            cmd = cmd+' '+Srcrootpath+value+'/*.png '
        print cmd
        os.system(cmd)
    else:
        print srcpath+' images is not changed!'

#help
packimage(1,'RGB565','help-hd','help')
packimage(0.5,'RGB565','help','help')
packimage(0.5,'RGB565','help-ipad','help-ipad')
packimage(1,'RGB565','help-ipadhd','help-ipad')
#bg
packimage(1,'RGB565','bg-hd','bg')
packimage(0.5,'RGB565','bg','bg')
packimage(0.5,'RGB565','bg-ipad','bg-ipad')
packimage(1,'RGB565','bg-ipadhd','bg-ipad')
#story
packimage(1,'RGB565','story-hd','story')
packimage(0.5,'RGB565','story','story')
packimage(0.5,'RGB565','story-ipad','story-ipad')
packimage(1,'RGB565','story-ipadhd','story-ipad')
#native
#en
packimage(0.5,'RGBA4444','en.lproj/native-hd','en.lproj')
packimage(0.25,'RGBA4444','en.lproj/native','en.lproj')
packimage(0.5,'RGBA4444','en.lproj/native-ipad','en.lproj')
packimage(1.0,'RGBA4444','en.lproj/native-ipadhd','en.lproj')
#zh
packimage(0.5,'RGBA4444','zh-Hant.lproj/native-hd','zh.lproj')
packimage(0.25,'RGBA4444','zh-Hant.lproj/native','zh.lproj')
packimage(0.5,'RGBA4444','zh-Hant.lproj/native-ipad','zh.lproj')
packimage(1.0,'RGBA4444','zh-Hant.lproj/native-ipadhd','zh.lproj')
#jp
packimage(0.5,'RGBA4444','ja.lproj/native-hd','ja.lproj')
packimage(0.25,'RGBA4444','ja.lproj/native','ja.lproj')
packimage(0.5,'RGBA4444','ja.lproj/native-ipad','ja.lproj')
packimage(1.0,'RGBA4444','ja.lproj/native-ipadhd','ja.lproj')
#anim
packimage(0.5,'RGBA4444','anim-hd','anim')
packimage(0.25,'RGBA4444','anim','anim')
packimage(0.5,'RGBA4444','anim-ipad','anim')
packimage(1.0,'RGBA4444','anim-ipadhd','anim')
#earth
packimage(0.51,'RGBA4444','earth-hd','earth')
packimage(0.255,'RGBA4444','earth','earth')
packimage(0.51,'RGBA4444','earth-ipad','earth')
packimage(1.05,'RGBA4444','earth-ipadhd','earth')
#view
packimage(0.5,'RGBA4444','view-hd','view|other')
packimage(0.25,'RGBA4444','view','view|other')
packimage(0.5,'RGBA4444','view-ipad','view|other-ipad')
packimage(1.0,'RGBA4444','view-ipadhd','view|other-ipad')


os.remove('getImgName.pyc')
#other
timedb.close()
