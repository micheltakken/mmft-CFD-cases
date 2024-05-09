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
    plotOverLineA.Point1 = [0.00208441, 0.00101370, 5e-5]
    plotOverLineA.Point2 = [0.00199013, 0.00106084, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineB = PlotOverLine(registrationName='PlotOverLineB', Input=filefoam)
    plotOverLineB.Point1 = [0.001990127, 0.00493916, 5e-5]
    plotOverLineB.Point2 = [0.002084408, 0.00498630, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineC = PlotOverLine(registrationName='PlotOverLineC', Input=filefoam)
    plotOverLineC.Point1 = [0.00402071, 0.00295, 5e-5]
    plotOverLineC.Point2 = [0.00392928, 0.003, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineD = PlotOverLine(registrationName='PlotOverLineD', Input=filefoam)
    plotOverLineD.Point1 = [0.00392928, 0.003, 5e-5]
    plotOverLineD.Point2 = [0.004, 0.00307071, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineE = PlotOverLine(registrationName='PlotOverLineE', Input=filefoam)
    plotOverLineE.Point1 = [0.00412071, 0.00295, 5e-5]
    plotOverLineE.Point2 = [0.00412071, 0.00305, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineF = PlotOverLine(registrationName='PlotOverLineF', Input=filefoam)
    plotOverLineF.Point1 = [0.00595, 0.00295, 5e-5]
    plotOverLineF.Point2 = [0.00595, 0.00305, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineG = PlotOverLine(registrationName='PlotOverLineG', Input=filefoam)
    plotOverLineG.Point1 = [0.00821180, 0.00305, 5e-5]
    plotOverLineG.Point2 = [0.00821180, 0.00295, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineH = PlotOverLine(registrationName='PlotOverLineH', Input=filefoam)
    plotOverLineH.Point1 = [0.00605, 0.00305, 5e-5]
    plotOverLineH.Point2 = [0.00605, 0.00295, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineI = PlotOverLine(registrationName='PlotOverLineI', Input=filefoam)
    plotOverLineI.Point1 = [0.00595, 0.00295, 5e-5]
    plotOverLineI.Point2 = [0.00605, 0.00295, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineJ = PlotOverLine(registrationName='PlotOverLineJ', Input=filefoam)
    plotOverLineJ.Point1 = [0.00605, 0.00305, 5e-5]
    plotOverLineJ.Point2 = [0.00595, 0.00305, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineK = PlotOverLine(registrationName='PlotOverLineK', Input=filefoam)
    plotOverLineK.Point1 = [0.00595, 0.001, 5e-5]
    plotOverLineK.Point2 = [0.00605, 0.001, 5e-5]

    # create a new 'Plot Over Line'
    plotOverLineL = PlotOverLine(registrationName='PlotOverLineL', Input=filefoam)
    plotOverLineL.Point1 = [0.00605, 0.005, 5e-5]
    plotOverLineL.Point2 = [0.00595, 0.005, 5e-5]

    # Properties modified on plotOverLine1
    plotOverLineA.Resolution = 1000
    plotOverLineB.Resolution = 1000
    plotOverLineC.Resolution = 1000
    plotOverLineD.Resolution = 1000
    plotOverLineE.Resolution = 1000
    plotOverLineF.Resolution = 1000
    plotOverLineG.Resolution = 1000
    plotOverLineH.Resolution = 1000
    plotOverLineI.Resolution = 1000
    plotOverLineJ.Resolution = 1000
    plotOverLineK.Resolution = 1000
    plotOverLineL.Resolution = 1000

    # save data
    SaveData(folder+'A-A.csv', proxy=plotOverLineA, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'B-B.csv', proxy=plotOverLineB, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'C-C.csv', proxy=plotOverLineC, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'D-D.csv', proxy=plotOverLineD, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'E-E.csv', proxy=plotOverLineE, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'F-F.csv', proxy=plotOverLineF, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'G-G.csv', proxy=plotOverLineG, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'H-H.csv', proxy=plotOverLineH, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'I-I.csv', proxy=plotOverLineI, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'J-J.csv', proxy=plotOverLineJ, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'K-K.csv', proxy=plotOverLineK, PointDataArrays=['C', 'arc_length'])
    SaveData(folder+'L-L.csv', proxy=plotOverLineL, PointDataArrays=['C', 'arc_length'])


if __name__ == "__main__":
    main()
