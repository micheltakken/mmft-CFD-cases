import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def main():

    angles = ['14','27','45','63','90']
    channelLengths = ['2', '10', '20']
    velocities = ['0.01', '0.1']
    diffusivities = ['8.1', '8.2', '8.3', '8.4', '8.5', '8.6', '8.7', '8.8', '8.9', '8.10']

    #plotGraphCorrection(angles, channelLengths, velocities, diffusivities)
    plotErrors(angles, channelLengths, velocities, diffusivities)

def plotGraphCorrection(angles, channelLengths, velocities, diffusivities):

    counter = 0

    markers = ['ro', 'xr', 'bo', 'xb', 'go', 'xg']

    baseline = [0,11]

    gradientIn = []
    gradientout = []

    for angle in angles:
        counter = 0
        for length in channelLengths:
            for velocity in velocities:
                gradientIn = []
                gradientout = []
                for diffusivity in diffusivities:
                    try: 
                        directory = angle + "deg/cL" + length + "/U" + velocity + "/D" + diffusivity
                        (gradIn, gradOut) = getGradients(directory)
                        gradientIn.append(gradIn)
                        gradientout.append(gradOut)

                    except:
                        print(directory + " probably does not contain Concentration data.")
                        pass
    
                plt.plot(gradientIn, gradientout, markers[counter], label="cL " + length + ", u " + velocity)
                counter += 1
        plt.title(angle + " degree angle")
        plt.plot(baseline, baseline)
        plt.xlim(0,11)
        plt.legend()
        plt.savefig("angle" + angle +"deg.png", dpi=600)
        #plt.show()
        plt.clf()

def plotErrors(angles, channelLengths, velocities, diffusivities):
    
    xPoints = np.zeros((len(channelLengths), len(angles), len(velocities), len(diffusivities)))
    yPoints = np.zeros((len(channelLengths), len(angles), len(velocities), len(diffusivities)))

    anglePos = 0
    lengthPos = 0
    velPos = 0
    diffpos = 0

    for length in channelLengths:
        anglePos = 0
        for angle in angles:
            velPos = 0
            for velocity in velocities:
                diffpos = 0
                for diffusivity in diffusivities:
                    try: 
                        directory = angle + "deg/cL" + length + "/U" + velocity + "/D" + diffusivity
                        # Peclet Nr.
                        if diffusivity != '8.10':
                            xPoints[lengthPos][anglePos][velPos][diffpos] = (10**(-float(diffusivity)))
                        else:
                            xPoints[lengthPos][anglePos][velPos][diffpos] = (10**(-9))
                        # Error value
                        yPoints[lengthPos][anglePos][velPos][diffpos] = MSE_Error(directory)
                    except:
                        print(directory + " probably does not contain Concentration data.")
                        pass

                    diffpos += 1
                velPos += 1
            anglePos += 1
        lengthPos += 1

    for length in range(len(channelLengths)):
        for vel in range(len(velocities)):
            plt.title("channel length " + channelLengths[length] + ", velocity " + velocities[vel])
            plt.xlabel('Diffusion coefficient [m2/s]')
            plt.ylabel('MSE')
            #plt.xlim(200, 2*10**4.1)
            plt.ylim(0, 0.01)
            #plt.xscale("log")
            plt.plot(xPoints[length][0][vel][:], yPoints[length][0][vel][:], 'ro', label=angles[0])
            plt.plot(xPoints[length][1][vel][:], yPoints[length][1][vel][:], 'xb', label=angles[1])
            plt.plot(xPoints[length][2][vel][:], yPoints[length][2][vel][:], 'xg', label=angles[2])
            plt.plot(xPoints[length][3][vel][:], yPoints[length][3][vel][:], 'bo', label=angles[3])
            plt.plot(xPoints[length][4][vel][:], yPoints[length][4][vel][:], 'xr', label=angles[4])
            plt.legend()
            plt.savefig("cL" + channelLengths[length] + "U" + velocities[vel]+ ".png", dpi=100)
            #plt.show()
            plt.clf()

def plotConc(directory):
    
    fileNameA = directory + "/A-A.csv"
    fileNameB = directory + "/B-B.csv"
    fileNameC = directory + "/C-C.csv"
    fileNameD = directory + "/D-D.csv"
    fileNameE = directory + "/E-E.csv"
    fileNameF = directory + "/F-F.csv"

    dataA = pd.read_csv(fileNameA)
    dataB = pd.read_csv(fileNameB)
    dataC = pd.read_csv(fileNameC)
    dataD = pd.read_csv(fileNameD)
    dataE = pd.read_csv(fileNameE)
    dataF = pd.read_csv(fileNameF)

    plt.plot((1.0/(dataA['arc_length'].to_numpy()[-1]))*dataA['arc_length'].to_numpy(), dataA['C'].to_numpy(), label="A-A'")
    plt.plot((1.0/(dataB['arc_length'].to_numpy()[-1]))*dataB['arc_length'].to_numpy(), dataB['C'].to_numpy(), label="B-B'")
    plt.plot((0.5/(dataC['arc_length'].to_numpy()[-1]))*dataC['arc_length'].to_numpy(), dataC['C'].to_numpy(), label="C-C'")
    plt.plot((0.5/(dataD['arc_length'].to_numpy()[-1]))*dataD['arc_length'].to_numpy() + 0.5, dataD['C'].to_numpy(), label="D-D'")
    plt.plot((0.5/(dataE['arc_length'].to_numpy()[-1]))*dataE['arc_length'].to_numpy(), dataE['C'].to_numpy(), label="E-E'")
    plt.plot((0.5/(dataF['arc_length'].to_numpy()[-1]))*dataF['arc_length'].to_numpy() + 0.5, dataF['C'].to_numpy(), label="F-F'")

    #plt.legend()
    plt.ylim([0, 1.0])

    plt.show()
    plt.clf()

def getGradients(directory):

    fileNameB = directory + "/B-B.csv"
    fileNameC = directory + "/C-C.csv"
    fileNameD = directory + "/D-D.csv"

    concB = pd.read_csv(fileNameB)['C'].to_numpy()
    concC = pd.read_csv(fileNameC)['C'].to_numpy()
    concD = pd.read_csv(fileNameD)['C'].to_numpy()
    concCD = np.concatenate((concC[0:-1], concD))

    dx = 1.0/concB.size

    gradIn = (concB[1050] - concB[950])/(100*dx)
    gradOut = (concCD[1050] - concCD[950])/(100*dx)

    return (gradIn, gradOut)

def MSE_Error(directory):

    fileNameB = directory + "/B-B.csv"
    fileNameC = directory + "/C-C.csv"
    fileNameD = directory + "/D-D.csv"

    concB = pd.read_csv(fileNameB)['C'].to_numpy()
    concC = pd.read_csv(fileNameC)['C'].to_numpy()
    concD = pd.read_csv(fileNameD)['C'].to_numpy()

    concCD = np.concatenate((concC[0:-1], concD))
    diff = concB - concCD
    diff_sq = diff**2

    return np.nansum(diff_sq)/concB.size

def L2_Error(directory):

    fileNameB = directory + "/B-B.csv"
    fileNameC = directory + "/C-C.csv"
    fileNameD = directory + "/D-D.csv"

    concB = pd.read_csv(fileNameB)['C'].to_numpy()
    concC = pd.read_csv(fileNameC)['C'].to_numpy()
    concD = pd.read_csv(fileNameD)['C'].to_numpy()

    concCD = np.concatenate((concC[0:-1], concD))
    diff = concB - concCD
    diff_sq = diff**2
    
    return np.sqrt(np.nansum(diff_sq))

def L_inf_Error(directory):

    fileNameB = directory + "/B-B.csv"
    fileNameC = directory + "/C-C.csv"
    fileNameD = directory + "/D-D.csv"

    concB = pd.read_csv(fileNameB)['C'].to_numpy()
    concC = pd.read_csv(fileNameC)['C'].to_numpy()
    concD = pd.read_csv(fileNameD)['C'].to_numpy()

    concCD = np.concatenate((concC[0:-1], concD))
    diff = concB - concCD
    
    return diff.max()



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
        
        print(directory + "\t" + instance + "\t%.6f")

        #ax[row, col].plot((1.0/(dataA['arc_length'].to_numpy()[-1]))*dataA['arc_length'].to_numpy(), dataA['U:0'].to_numpy(), label="A-A'")

        #plt.legend()
        #ax[row, col].set_title(instance)

        counter += 1

    #fig.savefig(directory+".png", dpi=100)
    #fig.clf()

if __name__ == "__main__":
    main()