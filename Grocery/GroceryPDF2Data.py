
import json
import camelot
# python3 -m pip uninstall camelot
# python3 -m pip uninstall camelot-py
# python3 -m pip install camelot-py[cv]
import pandas as pd

def splitter(t):
    t = t.split('    ')
    t = t[1]
    t = t.split('\\n')
    return t

def columnRename(t):
    t = t.replace('\n','_').replace(' ','_')
    return t

def pdf2df():
    pd.reset_option("max_columns")
    # extract all the tables in the PDF file
    abc = camelot.read_pdf('D:\Livings\Home\Grocery\ITNUP23IGAA04292.pdf')   #address of file location
    # abc = camelot.read_pdf('D:\Library\Civics\Constitution of India 2023050195.pdf')   #address of file location 

    # # print the first table as Pandas DataFrame
    # for ab in abc:
    #     print(ab.df)
    # dfdata = abc[2].df
    # df2 = dfdata.to_json(orient = 'table')
    # with open('D:\\Livings\\Home\\Grocery\\data.json', 'w') as outfile:
    #     outfile.write(json.dumps(df2))
    # dfdata.to_csv('D:\\Livings\\Home\\Grocery\\data.csv')
    print(abc[2].df)
    df1=abc[2].df
    # converting first row as column name
    df1.columns = df1.iloc[0]
    df1 = df1[1:]
    # or
    # df1.drop(['0'], axis=1)
    df1 = df1.reset_index(drop=True)

    # renaming column 
    for a in df1.columns:
        df1.columns = df1.columns.str.replace(a,columnRename(a))
    # for a in df1.columns:
        # print(a)
    print(df1)
    df1.to_csv('D:\\Livings\\Home\\Grocery\\data2.csv', index=False)
    exit()
    
# pdf2df()
def csv2AnalyseData():
    df1 = pd.read_csv('D:\\Livings\\Home\\Grocery\\data2.csv',index_col=[0])
    # df1 = pd.DataFrame(df)
    print(df1)
    CGST_rate = []
    CGST_amt = []
    SGST_rate = []
    SGST_amt = []
    GroceryDataFrame = []
    # for a in df1.columns:
    #     if(a=='Item_Description'):
    #         df2 = df1[a].iloc[:5]
    #         t = df2.to_string()
    #         # t = splitter(t)
    #         # print(t)
    # # exit()
    for a in df1.columns:
        df2 = df1[a].iloc[:1]
        t = df2.to_string()
        print(t)
        t = splitter(t)
        if(a=='CGST_Rate(%)__Amount'):
            for i,s in enumerate(t):
                if(i%2==0):
                    CGST_rate.append(t[i])
                else :
                    CGST_amt.append(t[i])
        if(a=='SGST/_UTGST%_Rate(%)__Amount'):
            for i,s in enumerate(t):
                if(i%2==0):
                    SGST_rate.append(t[i])
                else :
                    SGST_amt.append(t[i])
        df_t = pd.DataFrame(t)
        if(len(GroceryDataFrame)== 0):
            GroceryDataFrame = pd.concat([df_t], axis=1)
        elif(a=='CGST_Rate(%)__Amount'):
            CGST_rate_df = pd.DataFrame(CGST_rate)
            GroceryDataFrame = pd.concat([GroceryDataFrame, CGST_rate_df], axis=1)
            CGST_amt_df = pd.DataFrame(CGST_amt)
            GroceryDataFrame = pd.concat([GroceryDataFrame, CGST_amt_df], axis=1)
        elif(a=='SGST/_UTGST%_Rate(%)__Amount'):
            SGST_rate_df = pd.DataFrame(SGST_rate)
            GroceryDataFrame = pd.concat([GroceryDataFrame, SGST_rate_df], axis=1)
            SGST_amt_df = pd.DataFrame(SGST_amt)
            GroceryDataFrame = pd.concat([GroceryDataFrame, SGST_amt_df], axis=1)
        else :
            GroceryDataFrame = pd.concat([GroceryDataFrame, df_t], axis=1)
    GroceryDataFrame.drop(GroceryDataFrame.columns[0])
    print(GroceryDataFrame)
    
csv2AnalyseData()