import pandas as pd

def readAndPrint():
    a = df['category'].unique()
    print(sorted(a))

def readColumn():

    print("Total Columns: ",df.shape[0])

if __name__=="__main__":

    df = pd.read_csv (r'D:\Python\Context Based Spell Checker using RNN\corpusDhakaTribune_2.csv')
    #df = pd.read_csv (r'D:\Python\Context Based Spell Checker using RNN\corpusDhakaTribune_n.csv')
    #df = pd.read_csv (r'D:\Python\Context Based Spell Checker using RNN\Corpus Backup\corpusDhakaTribune.csv')
    readColumn()
    #readAndPrint()