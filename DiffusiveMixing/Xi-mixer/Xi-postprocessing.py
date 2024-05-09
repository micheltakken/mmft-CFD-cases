from paraview.simple import *

def main():
    location = "./concentrationField/"
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
    plotOverLineA.Point1 = [0.00212361, 0.00095, 5e-5]
    plotOverLineA.Point2 = [0.00212361, 0.00105, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineB = PlotOverLine(registrationName='PlotOverLineB', Input=filefoam)
    plotOverLineB.Point1 = [0.00387639, 0.00095, 5e-5]
    plotOverLineB.Point2 = [0.00387639, 0.00105, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineC = PlotOverLine(registrationName='PlotOverLineC', Input=filefoam)
    plotOverLineC.Point1 = [0.00423281, 0.0007718, 5e-5]
    plotOverLineC.Point2 = [0.00432361, 0.00095, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineD = PlotOverLine(registrationName='PlotOverLineD', Input=filefoam)
    plotOverLineD.Point1 = [0.00432361, 0.00095, 5e-5]
    plotOverLineD.Point2 = [0.00432361, 0.00105, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineE = PlotOverLine(registrationName='PlotOverLineE', Input=filefoam)
    plotOverLineE.Point1 = [0.00421180, 0.00105, 5e-5]
    plotOverLineE.Point2 = [0.00416640, 0.00113910, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineF = PlotOverLine(registrationName='PlotOverLineF', Input=filefoam)
    plotOverLineF.Point1 = [0.00595528, -0.00008944, 5e-5]
    plotOverLineF.Point2 = [0.00604472, 0.00008944, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineG = PlotOverLine(registrationName='PlotOverLineG', Input=filefoam)
    plotOverLineG.Point1 = [0.006, 0.00095, 5e-5]
    plotOverLineG.Point2 = [0.006, 0.00105, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineH = PlotOverLine(registrationName='PlotOverLineH', Input=filefoam)
    plotOverLineH.Point1 = [0.00602236, 0.00195528, 5e-5]
    plotOverLineH.Point2 = [0.00597764, 0.00204472, 5e-5]

    # Properties modified on plotOverLine1
    plotOverLineA.Resolution = 1000
    plotOverLineB.Resolution = 1000
    plotOverLineC.Resolution = 1000
    plotOverLineD.Resolution = 1000
    plotOverLineE.Resolution = 1000
    plotOverLineF.Resolution = 1000
    plotOverLineG.Resolution = 1000
    plotOverLineH.Resolution = 1000

    # save data
    SaveData(folder+'A-A.csv', proxy=plotOverLineA, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'B-B.csv', proxy=plotOverLineB, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'C-C.csv', proxy=plotOverLineC, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'D-D.csv', proxy=plotOverLineD, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'E-E.csv', proxy=plotOverLineE, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'F-F.csv', proxy=plotOverLineF, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'G-G.csv', proxy=plotOverLineG, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'H-H.csv', proxy=plotOverLineH, PointDataArrays=['C', 'arc_length'])


if __name__ == "__main__":
    main()
