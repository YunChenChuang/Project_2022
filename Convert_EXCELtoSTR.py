import pandas as pd

FILENAEM = 'Subtitle_0613-Chinese.xlsx'  # InputFile name, with '.xlsx'
OUTFILENAME = 'Subtitle_0613-Korean'  # OutFile name, without '.srt'
SHEEI_NAME = 'ELEANOR_SEARLE_V04'  # enter sheet name that you want to cover, or 'None' to cover the 1st sheet.
HEADER = 1  # input the row number of header, or '0' if no header.


def main():
    """
    SRTMaker
    Requirement : Python3 , Pandas Library
    This program use python3 to convert excel file (.xlsx) into subtitle file (.srt)
    The excel file will in the following format：

    Column 1: Index ( # 1, 2, 3, ...
    Column 2: timecode (hh:mm:ss,milliseconds -> hh:mm:ss,milliseconds ) format
    Column 3: text

    Start from first row - HEADER column
    """

    column_names = ['index',"timecode", "text"]
    input_file = pd.ExcelFile(FILENAEM)

    sheet1 = input_file.parse(sheet_name=SHEEI_NAME, header=HEADER, names=column_names)

    counter = 1
    with open(OUTFILENAME+'.srt', 'w') as file:
        for index, row in sheet1.iterrows():
            print("%d\n%s\n%s\n" % (
                counter, row['timecode'], row["text"]), file=file)
            counter += 1


if __name__ == '__main__':
    main()