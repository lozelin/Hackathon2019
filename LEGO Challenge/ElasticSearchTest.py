
#%%% CURL function to run in your command line 

#%% Download images to computer with comments 
import xlsxwriter
import json

with open('example-output.json') as json_file:
    data = json.load(json_file)

import urllib.request
print('Beginning file download with urllib2...')

workbook = xlsxwriter.Workbook('metadata.xlsx')
worksheet = workbook.add_worksheet()

for i in range(0,len(data['hits']['hits'])):
    
    print("File number:'",i)
    url = data['hits']['hits'][i]['_source']['generatedCoverImage']
    id = data['hits']['hits'][i]['_source']['id']
    try:
        urllib.request.urlretrieve(url, filename = 'images/'+ id + '.jpg')
        worksheet.write(i, 0, id)
        worksheet.write(i, 1, url)
        worksheet.write(i, 2, data['hits']['hits'][i]['_source']['description'])
    except:
        print('Error')
workbook.close()


