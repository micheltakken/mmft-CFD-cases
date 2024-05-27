import pandas as pd
from matplotlib import pyplot as plt

def main():

    plotConc('.')

def plotConc(directory):

    fig, ax = plt.subplots(3, 3)
    fig.tight_layout(h_pad=2)
    
    fileNameA = directory + "/concentrationField/A-A.csv"
    fileNameB = directory + "/concentrationField/B-B.csv"
    fileNameC = directory + "/concentrationField/C-C.csv"
    fileNameD = directory + "/concentrationField/D-D.csv"
    fileNameE = directory + "/concentrationField/E-E.csv"
    fileNameF = directory + "/concentrationField/F-F.csv"
    fileNameG = directory + "/concentrationField/G-G.csv"
    fileNameH = directory + "/concentrationField/H-H.csv"

    filenameAbstB = directory + "/Case2-B.csv"
    filenameAbstF = directory + "/Case2-F.csv"
    filenameAbstG = directory + "/Case2-G.csv"
    filenameAbstH = directory + "/Case2-H.csv"

    filenameTestB = directory + "/Case2Test-B.csv"
    filenameTestC = directory + "/Case2Test-C.csv"
    filenameTestD = directory + "/Case2Test-D.csv"
    filenameTestE = directory + "/Case2Test-E.csv"
    filenameTestF = directory + "/Case2Test-F.csv"
    filenameTestG = directory + "/Case2Test-G.csv"
    filenameTestH = directory + "/Case2Test-H.csv"

    dataA = pd.read_csv(fileNameA)
    dataB = pd.read_csv(fileNameB)
    dataC = pd.read_csv(fileNameC)
    dataD = pd.read_csv(fileNameD)
    dataE = pd.read_csv(fileNameE)
    dataF = pd.read_csv(fileNameF)
    dataG = pd.read_csv(fileNameG)
    dataH = pd.read_csv(fileNameH)

    dataAbstB = pd.read_csv(filenameAbstB)
    dataAbstF = pd.read_csv(filenameAbstF)
    dataAbstG = pd.read_csv(filenameAbstG)
    dataAbstH = pd.read_csv(filenameAbstH)

    dataTestB = pd.read_csv(filenameTestB)
    dataTestC = pd.read_csv(filenameTestC)
    dataTestD = pd.read_csv(filenameTestD)
    dataTestE = pd.read_csv(filenameTestE)
    dataTestF = pd.read_csv(filenameTestF)
    dataTestG = pd.read_csv(filenameTestG)
    dataTestH = pd.read_csv(filenameTestH)

    ax[0, 0].plot((1.0/(dataA['arc_length'].to_numpy()[-1]))*dataA['arc_length'].to_numpy(), dataA['C'].to_numpy(), label="A-A'")
    ax[0, 1].plot((1.0/(dataB['arc_length'].to_numpy()[-1]))*dataB['arc_length'].to_numpy(), dataB['C'].to_numpy(), label="B-B'")
    ax[0, 1].plot((1.0/(dataAbstB['x'].to_numpy()[-1]))*dataAbstB['x'].to_numpy(), dataAbstB['f(x)'].to_numpy(), label="B-B'-Abst", color="red")
    ax[0, 1].plot((1.0/(dataTestB['x'].to_numpy()[-1]))*dataTestB['x'].to_numpy(), dataTestB['f(x)'].to_numpy(), label="B-B'-Test", color="green")
    ax[1, 0].plot((1.0/(dataC['arc_length'].to_numpy()[-1]))*dataC['arc_length'].to_numpy(), dataC['C'].to_numpy(), label="C-C'")
    ax[1, 0].plot((1.0/(dataTestC['x'].to_numpy()[-1]))*dataTestC['x'].to_numpy(), dataTestC['f(x)'].to_numpy(), label="C-C'-Test", color="green")
    ax[1, 1].plot((1.0/(dataD['arc_length'].to_numpy()[-1]))*dataD['arc_length'].to_numpy(), dataD['C'].to_numpy(), label="D-D'")
    ax[1, 1].plot((1.0/(dataTestD['x'].to_numpy()[-1]))*dataTestD['x'].to_numpy(), dataTestD['f(x)'].to_numpy(), label="D-D'-Test", color="green")
    ax[1, 2].plot((1.0/(dataE['arc_length'].to_numpy()[-1]))*dataE['arc_length'].to_numpy(), dataE['C'].to_numpy(), label="E-E'")
    ax[1, 2].plot((1.0/(dataTestE['x'].to_numpy()[-1]))*dataTestE['x'].to_numpy(), dataTestE['f(x)'].to_numpy(), label="E-E'-Test", color="green")
    ax[2, 0].plot((1.0/(dataF['arc_length'].to_numpy()[-1]))*dataF['arc_length'].to_numpy(), dataF['C'].to_numpy(), label="F-F'")
    ax[2, 0].plot((1.0/(dataAbstF['x'].to_numpy()[-1]))*dataAbstF['x'].to_numpy(), dataAbstF['f(x)'].to_numpy(), label="F-F'-Abst", color="red")
    ax[2, 0].plot((1.0/(dataTestF['x'].to_numpy()[-1]))*dataTestF['x'].to_numpy(), dataTestF['f(x)'].to_numpy(), label="F-F'-Test", color="green")
    ax[2, 1].plot((1.0/(dataG['arc_length'].to_numpy()[-1]))*dataG['arc_length'].to_numpy(), dataG['C'].to_numpy(), label="G-G'")
    ax[2, 1].plot((1.0/(dataAbstG['x'].to_numpy()[-1]))*dataAbstG['x'].to_numpy(), dataAbstG['f(x)'].to_numpy(), label="G-G'-Abst", color="red")
    ax[2, 1].plot((1.0/(dataTestG['x'].to_numpy()[-1]))*dataTestG['x'].to_numpy(), dataTestG['f(x)'].to_numpy(), label="G-G'-Test", color="green")
    ax[2, 2].plot((1.0/(dataH['arc_length'].to_numpy()[-1]))*dataH['arc_length'].to_numpy(), dataH['C'].to_numpy(), label="H-H'")
    ax[2, 2].plot((1.0/(dataAbstH['x'].to_numpy()[-1]))*dataAbstH['x'].to_numpy(), dataAbstH['f(x)'].to_numpy(), label="H-H'-Abst", color="red")
    ax[2, 2].plot((1.0/(dataTestH['x'].to_numpy()[-1]))*dataTestH['x'].to_numpy(), dataTestH['f(x)'].to_numpy(), label="H-H'-Test", color="green")

    #plt.legend()
    ax[0, 0].set_ylim([0, 1.0])
    ax[0, 1].set_ylim([0, 1.0])
    ax[1, 0].set_ylim([0, 1.0])
    ax[1, 1].set_ylim([0, 1.0])
    ax[1, 2].set_ylim([0, 1.0])
    ax[2, 0].set_ylim([0, 1.0])
    ax[2, 1].set_ylim([0, 1.0])
    ax[2, 2].set_ylim([0, 1.0])

    ax[0, 0].set_title("A-A")
    ax[0, 1].set_title("B-B")
    ax[1, 0].set_title("C-C")
    ax[1, 1].set_title("D-D")
    ax[1, 2].set_title("E-E")
    ax[2, 0].set_title("F-F")
    ax[2, 1].set_title("G-G")
    ax[2, 2].set_title("H-H")


    fig.savefig("Case2-comparison.png", dpi=100)
    fig.clf()

if __name__ == "__main__":
    main()