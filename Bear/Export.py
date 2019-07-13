
import pandas as pd
try:
    from io import BytesIO as IO, BytesIO  # for modern python
except ImportError:
    from io import StringIO as IO  # for legacy python

class ExportSpreadSheet():
    def __init__(self, filename):
        self.filename = filename
        self.excel_file = IO()
        self.xlwriter = pd.ExcelWriter(self.excel_file, engine='xlsxwriter')

    def addDataFrameTab(self, dataframe, tab_name):
        dataframe.to_excel(self.xlwriter, tab_name)

    def save(self):
        self.xlwriter.save()
        self.xlwriter.close()

    def getSpreadSheet(self):
        self.excel_file.seek(0)
        return self.excel_file.read()

    def processKmeansData(self):
        self.addDataFrameTab()

    def getFilename(self):
        return self.filename