import pandas as pd
from matplotlib import pyplot as plt

def main():

    plotConc('.')

def plotConc(directory):

    fig, ax = plt.subplots(3, 2, figsize=(6.0,6.75))
    fig.suptitle(" ", x=0.38, size=10, weight='bold')
    #fig.suptitle("Concentration Distributions Case 2", x=0.38, size=16, weight='bold')

    fileNameA = directory + "/concentrationField/C-C.csv"
    fileNameB = directory + "/concentrationField/D-D.csv"
    fileNameC = directory + "/concentrationField/F-F.csv"
    fileNameD = directory + "/concentrationField/H-H.csv"
    fileNameE = directory + "/concentrationField/K-K.csv"
    fileNameF = directory + "/concentrationField/L-L.csv"

    filenameTestA = directory + "/Case-C.csv"
    filenameTestB = directory + "/Case4-D.csv"
    filenameTestC = directory + "/Case4-F.csv"
    filenameTestD = directory + "/Case4-H.csv"
    filenameTestE = directory + "/Case4-K.csv"
    filenameTestF = directory + "/Case4-L.csv"

    dataA = pd.read_csv(fileNameA)
    dataB = pd.read_csv(fileNameB)
    dataC = pd.read_csv(fileNameC)
    dataD = pd.read_csv(fileNameD)
    dataE = pd.read_csv(fileNameE)
    dataF = pd.read_csv(fileNameF)

    dataTestA = pd.read_csv(filenameTestA)
    dataTestB = pd.read_csv(filenameTestB)
    dataTestC = pd.read_csv(filenameTestC)
    dataTestD = pd.read_csv(filenameTestD)
    dataTestE = pd.read_csv(filenameTestE)
    dataTestF = pd.read_csv(filenameTestF)


    ax[0, 0].plot((100/(dataA['arc_length'].to_numpy()[-1]))*dataA['arc_length'].to_numpy(), dataA['C'].to_numpy(), label="CFD")
    ax[0, 0].plot((100/(dataTestA['x'].to_numpy()[-1]))*dataTestA['x'].to_numpy(), dataTestA['f(x)'].to_numpy(), label="Abstract", color="red")
    ax[0, 1].plot((100/(dataB['arc_length'].to_numpy()[-1]))*dataB['arc_length'].to_numpy(), dataB['C'].to_numpy(), label="B-B'")
    ax[0, 1].plot((100/(dataTestB['x'].to_numpy()[-1]))*dataTestB['x'].to_numpy(), dataTestB['f(x)'].to_numpy(), label="B-B'-Test", color="red")
    ax[1, 0].plot((100/(dataC['arc_length'].to_numpy()[-1]))*dataC['arc_length'].to_numpy(), dataC['C'].to_numpy(), label="C-C'")
    ax[1, 0].plot((100/(dataTestC['x'].to_numpy()[-1]))*dataTestC['x'].to_numpy(), dataTestC['f(x)'].to_numpy(), label="C-C'-Test", color="red")
    ax[1, 1].plot((100/(dataD['arc_length'].to_numpy()[-1]))*dataD['arc_length'].to_numpy(), dataD['C'].to_numpy(), label="D-D'")
    ax[1, 1].plot((100/(dataTestD['x'].to_numpy()[-1]))*dataTestD['x'].to_numpy(), dataTestD['f(x)'].to_numpy(), label="D-D'-Test", color="red")
    ax[2, 0].plot((100/(dataE['arc_length'].to_numpy()[-1]))*dataE['arc_length'].to_numpy(), dataE['C'].to_numpy(), label="E-E'")
    ax[2, 0].plot((100/(dataTestE['x'].to_numpy()[-1]))*dataTestE['x'].to_numpy(), dataTestE['f(x)'].to_numpy(), label="E-E'-Test", color="red")
    ax[2, 1].plot((100/(dataF['arc_length'].to_numpy()[-1]))*dataF['arc_length'].to_numpy(), dataF['C'].to_numpy(), label="F-F'")
    ax[2, 1].plot((100/(dataTestF['x'].to_numpy()[-1]))*dataTestF['x'].to_numpy(), dataTestF['f(x)'].to_numpy(), label="F-F'-Test", color="red")

    #plt.legend()
    ax[0, 0].set_xlim([0, 100])
    ax[0, 0].set_ylim([-0.05, 1.0])
    ax[0, 1].set_xlim([0, 100])
    ax[0, 1].set_ylim([-0.05, 1.0])
    ax[1, 0].set_xlim([0, 100])
    ax[1, 0].set_ylim([-0.05, 1.0])
    ax[1, 1].set_xlim([0, 100])
    ax[1, 1].set_ylim([-0.05, 1.0])
    ax[2, 0].set_xlim([0, 100])
    ax[2, 0].set_ylim([-0.05, 1.0])
    ax[2, 1].set_xlim([0, 100])
    ax[2, 1].set_ylim([-0.05, 1.0])

    ax[0, 0].set_title("A-A'")
    ax[0, 1].set_title("B-B'")
    ax[1, 0].set_title("C-C'")
    ax[1, 1].set_title("D-D'")
    ax[2, 0].set_title("E-E'")
    ax[2, 1].set_title("F-F'")

    lines_labels = [ax[0,0].get_legend_handles_labels()]
    lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
    

    fig.legend(lines, labels, loc='upper right', ncol=2)
    fig.supxlabel("Channel width ($\mu$m)")
    fig.supylabel("Concentration (%)")
    fig.tight_layout(w_pad=1.5)
    fig.tight_layout(h_pad=1)
    fig.savefig("Complex-Plots.png")
    fig.clf()

if __name__ == "__main__":
    main()