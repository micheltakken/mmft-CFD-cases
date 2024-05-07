from paraview.simple import *

def main():
    diffusivities = ['8.1', '8.2', '8.3', '8.4', '8.5', '8.6', '8.7', '8.8', '8.9', '8.10']
    velocities = ['0.01', '0.1']

    for velocity in velocities:
        for diffusivity in diffusivities:
            location = "./U" + velocity + "/D" + diffusivity + "/"
            generateCSV(location)

def generateCSV(folder):
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    # create a new 'OpenFOAMReader'
    filefoam = OpenFOAMReader(registrationName=folder+'openfoam.foam', FileName=folder+'openfoam.foam')
    filefoam.MeshRegions = ['internalMesh']
    filefoam.CellArrays = ['C']

    # create a new 'Plot Over Line'
    plotOverLineA = PlotOverLine(registrationName='PlotOverLineA', Input=filefoam)
    plotOverLineA.Point1 = [0.010, 0.00195, 5e-5]
    plotOverLineA.Point2 = [0.010, 0.00205, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineB = PlotOverLine(registrationName='PlotOverLineB', Input=filefoam)
    plotOverLineB.Point1 = [0.01995, 0.00195, 5e-5]
    plotOverLineB.Point2 = [0.02095, 0.00205, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineC = PlotOverLine(registrationName='PlotOverLineC', Input=filefoam)
    plotOverLineC.Point1 = [0.01995, 0.00195, 5e-5]
    plotOverLineC.Point2 = [0.02005, 0.00195, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineD = PlotOverLine(registrationName='PlotOverLineD', Input=filefoam)
    plotOverLineD.Point1 = [0.02005, 0.00205, 5e-5]
    plotOverLineD.Point2 = [0.01995, 0.00205, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineE = PlotOverLine(registrationName='PlotOverLineE', Input=filefoam)
    plotOverLineE.Point1 = [0.01995, 0.0, 5e-5]
    plotOverLineE.Point2 = [0.02005, 0.0, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineF = PlotOverLine(registrationName='PlotOverLineF', Input=filefoam)
    plotOverLineF.Point1 = [0.02005, 0.004, 5e-5]
    plotOverLineF.Point2 = [0.01995, 0.004, 5e-5]

    # Properties modified on plotOverLine1
    plotOverLineB.Resolution = 2000
    plotOverLineC.Resolution = 1000
    plotOverLineD.Resolution = 1000

    # save data
    SaveData(folder+'A-A.csv', proxy=plotOverLineA, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'B-B.csv', proxy=plotOverLineB, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'C-C.csv', proxy=plotOverLineC, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'D-D.csv', proxy=plotOverLineD, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'E-E.csv', proxy=plotOverLineE, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'F-F.csv', proxy=plotOverLineF, PointDataArrays=['C', 'arc_length'])


if __name__ == "__main__":
    main()