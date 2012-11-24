#!/bin/python
'''
    get the image's name used in project
'''
import os
curPath = os.path.abspath('.')
print curPath
print 'find zhe game images........'
imgs =[]
fname = 'TEImagesResources.h'
format1 = '.png'
#imgcount=0
imgs.append('''
#ifndef %s
#define %s
'''%(fname.replace('.','_').upper(),fname.replace('.','_').upper()))

def findImages(path):
    for i in os.listdir(path):
        if os.path.isdir(path+'/'+i):
            findImages(path+'/'+i)
        #           print path+'/'+i
        elif  i.lower()[-4:] == format1:
            name=i[:-4]
            if name.find('/+') :
                name=name.replace('+','_p')
            if name.find('/-') :
                name=name.replace('-','_m')
            if name.find('/@') :
                name=name.replace('@','_a')
            name =name.lower()
            imgName ='static const char '+'s_img_%s'%name+'[]'+'\t =\"%s\";'%i
            print imgName
            if imgName not in imgs:
                # imgcount=imgcount+1;
                imgs.append(imgName)

findImages(curPath)
imgs.append('''\n/* total %d images */'''% (len(imgs) -1))
imgs.append('''
#endif
    ''')

fobj = open(fname,'w')
ls=os.linesep
fobj.writelines(['%s%s'%(x,ls) for x in imgs])
fobj.close()
del  imgs
