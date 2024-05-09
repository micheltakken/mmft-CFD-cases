import pandas as pd
from matplotlib import pyplot as plt

def main():

    plotConc('.')

def plotConc(directory):

    fig, ax = plt.subplots(3, 4)
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


    ax[0, 0].plot((1.0/(dataA['arc_length'].to_numpy()[-1]))*dataA['arc_length'].to_numpy(), dataA['C'].to_numpy(), label="A-A'")
    ax[0, 1].plot((1.0/(dataB['arc_length'].to_numpy()[-1]))*dataB['arc_length'].to_numpy(), dataB['C'].to_numpy(), label="B-B'")
    ax[0, 2].plot((1.0/(dataC['arc_length'].to_numpy()[-1]))*dataC['arc_length'].to_numpy(), dataC['C'].to_numpy(), label="C-C'")
    ax[0, 3].plot((1.0/(dataD['arc_length'].to_numpy()[-1]))*dataD['arc_length'].to_numpy(), dataD['C'].to_numpy(), label="D-D'")
    ax[1, 0].plot((1.0/(dataE['arc_length'].to_numpy()[-1]))*dataE['arc_length'].to_numpy(), dataE['C'].to_numpy(), label="E-E'")
    ax[1, 1].plot((1.0/(dataF['arc_length'].to_numpy()[-1]))*dataF['arc_length'].to_numpy(), dataF['C'].to_numpy(), label="F-F'")
    ax[1, 2].plot((1.0/(dataG['arc_length'].to_numpy()[-1]))*dataG['arc_length'].to_numpy(), dataG['C'].to_numpy(), label="G-G'")
    ax[1, 3].plot((1.0/(dataH['arc_length'].to_numpy()[-1]))*dataH['arc_length'].to_numpy(), dataH['C'].to_numpy(), label="H-H'")
    ax[2, 0].plot((1.0/(dataI['arc_length'].to_numpy()[-1]))*dataH['arc_length'].to_numpy(), dataI['C'].to_numpy(), label="I-I'")
    ax[2, 1].plot((1.0/(dataJ['arc_length'].to_numpy()[-1]))*dataH['arc_length'].to_numpy(), dataJ['C'].to_numpy(), label="J-J'")
    ax[2, 2].plot((1.0/(dataK['arc_length'].to_numpy()[-1]))*dataH['arc_length'].to_numpy(), dataK['C'].to_numpy(), label="K-K'")
    ax[2, 3].plot((1.0/(dataL['arc_length'].to_numpy()[-1]))*dataH['arc_length'].to_numpy(), dataL['C'].to_numpy(), label="L-L'")

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


    fig.savefig("Plots.png", dpi=100)
    fig.clf()

if __name__ == "__main__":
    main()