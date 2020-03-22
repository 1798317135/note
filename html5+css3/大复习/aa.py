import pandas as pd
 
sExcelFile="工作簿1.xlsx"
df = pd.read_excel(sExcelFile,sheet_name='Sheet1')

nrows=df.shape[0]
ncols=df.columns.size
# print('Max Rows:'+str(nrows))
# print('Max Columns'+str(ncols))
# print(df.iloc[0,0])
# print(df.iloc[0,1])

# #查看某列内容
# #sColumnName='fd1'
# print(df[sColumnName])

# #查看第3列的内容，列的序号从0开始
# sColumnName=df.columns[2]
# print(df[sColumnName])

# #查看某行的内容
# iRow=1
# for iCol in range(ncols):
#     print(df.iloc[iRow,iCol])

#遍历逐行逐列
for iRow in range(nrows):
    for iCol in range(ncols):
        print(df.iloc[iRow,iCol],end="")