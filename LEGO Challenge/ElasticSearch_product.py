
#%%% CURL function to run in your command line 

# When you CURL save all the information into: example-output-product.json
# To do that; add ">> example-output-product.json" at the end of the given CURL (as in challenge description)

# If you are using postman export the data to example-output-product.json file 
#%% Download images to computer with comments 
import xlsxwriter
import json
import os

if not os.path.exists('images'):
    os.makedirs('images')

with open('example-output-product.json') as json_file:
    data = json.load(json_file)

import urllib.request
print('Beginning file download with urllib2...')

workbook = xlsxwriter.Workbook('metadata_product.xlsx')
worksheet = workbook.add_worksheet()

for i in range(0,len(data['hits']['hits'])):
    
    print("File number:'",i)
    try:
        url = data['hits']['hits'][i]['_source']['media']['image']['url']
        id = data['hits']['hits'][i]['_source']['id']
        name = data['hits']['hits'][i]['_source']['name']
        description = data['hits']['hits'][i]['_source']['description']
        try:
            urllib.request.urlretrieve(url, filename = 'images/'+ id + '.jpg')
            worksheet.write(i, 0, id)
            worksheet.write(i, 1, url)
            worksheet.write(i, 2, name)
            worksheet.write(i, 3, description)
        except:
            print('Error 1; no module named images')
    except:
            print('Error 2; no module named media') 
workbook.close()


