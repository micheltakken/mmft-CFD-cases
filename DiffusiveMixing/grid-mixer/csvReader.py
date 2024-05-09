import pandas as pd
from matplotlib import pyplot as plt

def main():

    plotConc('.')

def plotConc(directory):

    fig, ax = plt.subplots(4, 4)
    fig.tight_layout(h_pad=2)
    
    fileNameA = directory + "/concentrationField/A-A.csv"
    fileNameB = directory + "/concentrationField/B-B.csv"
    fileNameC = directory + "/concentrationField/C-C.csv"
    fileNameD = directory + "/concentrationField/D-D.csv"
    fileNameE = directory + "/concentrationField/E-E.csv"
    fileNameF = directory + "/concentrationField/F-F.csv"
    fileNameG = directory + "/concentrationField/G-G.csv"
    fileNameH = directory + "/concentrationField/H-H.csv"
    fileNameI = directory + "/concentrationField/I-I.csv"
    fileNameJ = directory + "/concentrationField/J-J.csv"
    fileNameK = directory + "/concentrationField/K-K.csv"
    fileNameL = directory + "/concentrationField/L-L.csv"
    fileNameM = directory + "/concentrationField/M-M.csv"
    fileNameN = directory + "/concentrationField/N-N.csv"
    fileNameO = directory + "/concentrationField/O-O.csv"
    fileNameP = directory + "/concentrationField/P-P.csv"

    filenameAbstD = directory + "/Case3-D.csv"
    filenameAbstG = directory + "/Case3-G.csv"
    filenameAbstH = directory + "/Case3-H.csv"
    filenameAbstK = directory + "/Case3-K.csv"
    filenameAbstL = directory + "/Case3-L.csv"
    filenameAbstO = directory + "/Case3-O.csv"
    filenameAbstP = directory + "/Case3-P.csv"

    dataA = pd.read_csv(fileNameA)
    dataB = pd.read_csv(fileNameB)
    dataC = pd.read_csv(fileNameC)
    dataD = pd.read_csv(fileNameD)
    dataE = pd.read_csv(fileNameE)
    dataF = pd.read_csv(fileNameF)
    dataG = pd.read_csv(fileNameG)
    dataH = pd.read_csv(fileNameH)
    dataI = pd.read_csv(fileNameI)
    dataJ = pd.read_csv(fileNameJ)
    dataK = pd.read_csv(fileNameK)
    dataL = pd.read_csv(fileNameL)
    dataM = pd.read_csv(fileNameM)
    dataN = pd.read_csv(fileNameN)
    dataO = pd.read_csv(fileNameO)
    dataP = pd.read_csv(fileNameP)

    dataAbstD = pd.read_csv(filenameAbstD)
    dataAbstG = pd.read_csv(filenameAbstG)
    dataAbstH = pd.read_csv(filenameAbstH)
    dataAbstK = pd.read_csv(filenameAbstK)
    dataAbstL = pd.read_csv(filenameAbstL)
    dataAbstO = pd.read_csv(filenameAbstO)
    dataAbstP = pd.read_csv(filenameAbstP)


    ax[0, 0].plot((1.0/(dataA['arc_length'].to_numpy()[-1]))*dataA['arc_length'].to_numpy(), dataA['C'].to_numpy(), label="A-A'")
    ax[0, 1].plot((1.0/(dataB['arc_length'].to_numpy()[-1]))*dataB['arc_length'].to_numpy(), dataB['C'].to_numpy(), label="B-B'")
    ax[0, 2].plot((1.0/(dataC['arc_length'].to_numpy()[-1]))*dataC['arc_length'].to_numpy(), dataC['C'].to_numpy(), label="C-C'")
    ax[0, 3].plot((1.0/(dataD['arc_length'].to_numpy()[-1]))*dataD['arc_length'].to_numpy(), dataD['C'].to_numpy(), label="D-D'")
    ax[0, 3].plot((1.0/(dataAbstD['x'].to_numpy()[-1]))*dataAbstD['x'].to_numpy(), dataAbstD['f(x)'].to_numpy(), label="D-D'-Abst", color="red")
    ax[1, 0].plot((1.0/(dataE['arc_length'].to_numpy()[-1]))*dataE['arc_length'].to_numpy(), dataE['C'].to_numpy(), label="E-E'")
    ax[1, 1].plot((1.0/(dataF['arc_length'].to_numpy()[-1]))*dataF['arc_length'].to_numpy(), dataF['C'].to_numpy(), label="F-F'")
    ax[1, 2].plot((1.0/(dataG['arc_length'].to_numpy()[-1]))*dataG['arc_length'].to_numpy(), dataG['C'].to_numpy(), label="G-G'")
    ax[1, 2].plot((1.0/(dataAbstG['x'].to_numpy()[-1]))*dataAbstG['x'].to_numpy(), dataAbstG['f(x)'].to_numpy(), label="G-G'-Abst", color="red")
    ax[1, 3].plot((1.0/(dataH['arc_length'].to_numpy()[-1]))*dataH['arc_length'].to_numpy(), dataH['C'].to_numpy(), label="H-H'")
    ax[1, 3].plot((1.0/(dataAbstH['x'].to_numpy()[-1]))*dataAbstH['x'].to_numpy(), dataAbstH['f(x)'].to_numpy(), label="H-H'-Abst", color="red")
    ax[2, 0].plot((1.0/(dataI['arc_length'].to_numpy()[-1]))*dataH['arc_length'].to_numpy(), dataI['C'].to_numpy(), label="I-I'")
    ax[2, 1].plot((1.0/(dataJ['arc_length'].to_numpy()[-1]))*dataH['arc_length'].to_numpy(), dataJ['C'].to_numpy(), label="J-J'")
    ax[2, 2].plot((1.0/(dataK['arc_length'].to_numpy()[-1]))*dataH['arc_length'].to_numpy(), dataK['C'].to_numpy(), label="K-K'")
    ax[2, 2].plot((1.0/(dataAbstK['x'].to_numpy()[-1]))*dataAbstK['x'].to_numpy(), dataAbstK['f(x)'].to_numpy(), label="K-K'-Abst", color="red")
    ax[2, 3].plot((1.0/(dataL['arc_length'].to_numpy()[-1]))*dataH['arc_length'].to_numpy(), dataL['C'].to_numpy(), label="L-L'")
    ax[2, 3].plot((1.0/(dataAbstL['x'].to_numpy()[-1]))*dataAbstL['x'].to_numpy(), dataAbstL['f(x)'].to_numpy(), label="L-L'-Abst", color="red")
    ax[3, 0].plot((1.0/(dataM['arc_length'].to_numpy()[-1]))*dataH['arc_length'].to_numpy(), dataM['C'].to_numpy(), label="M-M'")
    ax[3, 1].plot((1.0/(dataN['arc_length'].to_numpy()[-1]))*dataH['arc_length'].to_numpy(), dataN['C'].to_numpy(), label="N-N'")
    ax[3, 2].plot((1.0/(dataO['arc_length'].to_numpy()[-1]))*dataH['arc_length'].to_numpy(), dataO['C'].to_numpy(), label="O-O'")
    ax[3, 2].plot((1.0/(dataAbstO['x'].to_numpy()[-1]))*dataAbstO['x'].to_numpy(), dataAbstO['f(x)'].to_numpy(), label="O-O'-Abst", color="red")
    ax[3, 3].plot((1.0/(dataP['arc_length'].to_numpy()[-1]))*dataH['arc_length'].to_numpy(), dataP['C'].to_numpy(), label="P-P'")
    ax[3, 3].plot((1.0/(dataAbstP['x'].to_numpy()[-1]))*dataAbstP['x'].to_numpy(), dataAbstP['f(x)'].to_numpy(), label="P-P'-Abst", color="red")

    #plt.legend()
    ax[0, 0].set_ylim([0, 1.0])
    ax[0, 1].set_ylim([0, 1.0])
    ax[0, 2].set_ylim([0, 1.0])
    ax[0, 3].set_ylim([0, 1.0])
    ax[1, 0].set_ylim([0, 1.0])
    ax[1, 1].set_ylim([0, 1.0])
    ax[1, 2].set_ylim([0, 1.0])
    ax[1, 3].set_ylim([0, 1.0])
    ax[2, 0].set_ylim([0, 1.0])
    ax[2, 1].set_ylim([0, 1.0])
    ax[2, 2].set_ylim([0, 1.0])
    ax[2, 3].set_ylim([0, 1.0])
    ax[3, 0].set_ylim([0, 1.0])
    ax[3, 1].set_ylim([0, 1.0])
    ax[3, 2].set_ylim([0, 1.0])
    ax[3, 3].set_ylim([0, 1.0])

    ax[0, 0].set_title("A-A")
    ax[0, 1].set_title("B-B")
    ax[0, 2].set_title("C-C")
    ax[0, 3].set_title("D-D")
    ax[1, 0].set_title("E-E")
    ax[1, 1].set_title("F-F")
    ax[1, 2].set_title("G-G")
    ax[1, 3].set_title("H-H")
    ax[2, 0].set_title("I-I")
    ax[2, 1].set_title("J-J")
    ax[2, 2].set_title("K-K")
    ax[2, 3].set_title("L-L")
    ax[3, 0].set_title("M-M")
    ax[3, 1].set_title("N-N")
    ax[3, 2].set_title("O-O")
    ax[3, 3].set_title("P-P")


    fig.savefig("Plots.png", dpi=100)
    fig.clf()

if __name__ == "__main__":
    main()