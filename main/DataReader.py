class DataReader:
    def readFile(self, fileName):
        with open(fileName) as f:
            values = f.read().split()
        return values
