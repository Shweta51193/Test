import pandas as pd
import xlsxwriter
# Create a Pandas dataframe from the data.
text1 = "some text here"
text2 = "other text here"
df = pd.DataFrame({"a": [1,2,3,4,5], "b": [6,7,8,9,10], "c": [11,12,13,14,15]})

writer = pd.ExcelWriter("test.xlsx")
df.to_excel(writer, startrow=4, startcol=0)

worksheet = writer.sheets['Sheet1']
worksheet.write(0, 0, text1)
worksheet.write(1, 0, text2)