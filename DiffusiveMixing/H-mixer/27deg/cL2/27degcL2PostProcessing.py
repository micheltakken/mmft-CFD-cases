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
    plotOverLineA.Point1 = [0.003, 0.00095, 5e-5]
    plotOverLineA.Point2 = [0.003, 0.00105, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineB = PlotOverLine(registrationName='PlotOverLineB', Input=filefoam)
    plotOverLineB.Point1 = [0.004, 0.00095, 5e-5]
    plotOverLineB.Point2 = [0.004, 0.00105, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineC = PlotOverLine(registrationName='PlotOverLineC', Input=filefoam)
    plotOverLineC.Point1 = [0.00406708, 0.000910557, 5e-5]
    plotOverLineC.Point2 = [0.00411180, 0.001, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineD = PlotOverLine(registrationName='PlotOverLineD', Input=filefoam)
    plotOverLineD.Point1 = [0.00411180, 0.001, 5e-5]
    plotOverLineD.Point2 = [0.00406708, 0.00108944, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineE = PlotOverLine(registrationName='PlotOverLineE', Input=filefoam)
    plotOverLineE.Point1 = [0.00597763, -0.00004472, 5e-5]
    plotOverLineE.Point2 = [0.00602236, 0.00004472, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineF = PlotOverLine(registrationName='PlotOverLineF', Input=filefoam)
    plotOverLineF.Point1 = [0.00602236, 0.00195528, 5e-5]
    plotOverLineF.Point2 = [0.00597763, 0.00204472, 5e-5]

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