LINK = "http://localhost/dashboard/excel-data/excel-name.xlsx"

import unittest
import pandas as pd
import openpyxl
import warnings
import requests

class TestPandas(unittest.TestCase) :
    
    # def test_download(self) :
    #     local_filename = LINK.split('/')[-1]
    # # NOTE the stream=True parameter below
    #     with requests.get(LINK, stream=True) as r:
    #         r.raise_for_status()
            
    #         with open(local_filename, 'wb') as f:
    #             for chunk in r.iter_content(chunk_size=8192): 
    #             # If you have chunk encoded response uncomment if
    #             # and set chunk_size parameter to None.
    #             #if chunk: 
    #                 f.write(chunk)
                
    #     return local_filename
    # def test_request(self) :
    #     # r = rq.get(LINK)
    #     with rq.get("http://localhost/dashboard/excel-data/excel-name.xlsx", stream=True) as r :
    #         with open('newfile', "wb") as o :
    #             for chunk in r.iter_content(chunk_size=1024) :
    #                 if chunk :
    #                     o.write(chunk)
    # # def test_read(self):
    # #     warnings.simplefilter("ignore")
    # #     openpyxl.load_workbook(LINK+'excel-name.xlsx')
    # #     #data = pd.read_excel(LINK+'excel-name.xlsx', engine='openpyxl')
    # #     #data.to_csv('.')
        
    # def test_open_file (self):
    #     data = open("http://localhost/dashboard/excel-data/excel-name.xlsx", "wb")  
    
    def test_open(self) :
        pd.DataFrame(openpyxl.load_workbook('excel-name.xlsx'))
              
if __name__ == "__main__" :
    unittest.main()
 