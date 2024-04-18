import pandas as pd
from matplotlib import pyplot as plt

def main():

    instances = ['D1e-7', 'D1e-8', 'D1e-9', 'p0.01', 'p0.1', 'p1.0', 'v1e-5', 'v1e-6', 'v1e-7']

    plotConc('27deg', instances)
    plotConc('45deg', instances)
    plotConc('90deg', instances)

    print('Deg\tInst.\tVel\t\tRe\tPe\n')
    plotVel('27deg', instances)
    print("\n")
    plotVel('45deg', instances)
    print("\n")
    plotVel('90deg', instances)

def plotConc(directory, instances):

    counter = 0

    fig, ax = plt.subplots(3, 3)
    fig.tight_layout(h_pad=2)

    for instance in instances:
    
        fileNameA = directory + "/" + instance + "/concentrationField/A-A.csv"
        fileNameB = directory + "/" + instance + "/concentrationField/B-B.csv"
        fileNameC = directory + "/" + instance + "/concentrationField/C-C.csv"
        fileNameD = directory + "/" + instance + "/concentrationField/D-D.csv"
        fileNameE = directory + "/" + instance + "/concentrationField/E-E.csv"
        fileNameF = directory + "/" + instance + "/concentrationField/F-F.csv"

        dataA = pd.read_csv(fileNameA)
        dataB = pd.read_csv(fileNameB)
        dataC = pd.read_csv(fileNameC)
        dataD = pd.read_csv(fileNameD)
        dataE = pd.read_csv(fileNameE)
        dataF = pd.read_csv(fileNameF)

        row = counter//3
        col = counter%3

        ax[row, col].plot((1.0/(dataA['arc_length'].to_numpy()[-1]))*dataA['arc_length'].to_numpy(), dataA['C'].to_numpy(), label="A-A'")
        ax[row, col].plot((1.0/(dataB['arc_length'].to_numpy()[-1]))*dataB['arc_length'].to_numpy(), dataB['C'].to_numpy(), label="B-B'")
        ax[row, col].plot((0.5/(dataC['arc_length'].to_numpy()[-1]))*dataC['arc_length'].to_numpy(), dataC['C'].to_numpy(), label="C-C'")
        ax[row, col].plot((0.5/(dataD['arc_length'].to_numpy()[-1]))*dataD['arc_length'].to_numpy() + 0.5, dataD['C'].to_numpy(), label="D-D'")
        ax[row, col].plot((0.5/(dataE['arc_length'].to_numpy()[-1]))*dataE['arc_length'].to_numpy(), dataE['C'].to_numpy(), label="E-E'")
        ax[row, col].plot((0.5/(dataF['arc_length'].to_numpy()[-1]))*dataF['arc_length'].to_numpy() + 0.5, dataF['C'].to_numpy(), label="F-F'")

        #plt.legend()
        ax[row, col].set_ylim([0, 1.0])
        ax[row, col].set_title(instance)

        counter += 1

    fig.savefig(directory+".png", dpi=100)
    fig.clf()

def plotVel(directory, instances):

    counter = 0

    fig, ax = plt.subplots(3, 3)
    fig.tight_layout(h_pad=2)

    for instance in instances:
    
        fileNameA = directory + "/" + instance + "/flowField/A-A.csv"

        dataA = pd.read_csv(fileNameA)

        row = counter//3
        col = counter%3

        vel = ((2./3.)*dataA['U:0'].to_numpy().max())
        Re = (vel*1e-4)/(1e-6)
        
        print(directory + "\t" + instance + "\t%.6f" % )

        #ax[row, col].plot((1.0/(dataA['arc_length'].to_numpy()[-1]))*dataA['arc_length'].to_numpy(), dataA['U:0'].to_numpy(), label="A-A'")

        #plt.legend()
        #ax[row, col].set_title(instance)

        counter += 1

    #fig.savefig(directory+".png", dpi=100)
    #fig.clf()

if __name__ == "__main__":
    main()