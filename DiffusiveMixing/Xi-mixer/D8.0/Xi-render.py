# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
concentrationFieldOpenFOAM = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
concentrationFieldOpenFOAMDisplay = Show(concentrationFieldOpenFOAM, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
concentrationFieldOpenFOAMDisplay.Representation = 'Surface'
concentrationFieldOpenFOAMDisplay.ColorArrayName = [None, '']
concentrationFieldOpenFOAMDisplay.SelectTCoordArray = 'None'
concentrationFieldOpenFOAMDisplay.SelectNormalArray = 'None'
concentrationFieldOpenFOAMDisplay.SelectTangentArray = 'None'
concentrationFieldOpenFOAMDisplay.OSPRayScaleArray = 'U'
concentrationFieldOpenFOAMDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
concentrationFieldOpenFOAMDisplay.SelectOrientationVectors = 'None'
concentrationFieldOpenFOAMDisplay.ScaleFactor = 0.0006089442591473926
concentrationFieldOpenFOAMDisplay.SelectScaleArray = 'None'
concentrationFieldOpenFOAMDisplay.GlyphType = 'Arrow'
concentrationFieldOpenFOAMDisplay.GlyphTableIndexArray = 'None'
concentrationFieldOpenFOAMDisplay.GaussianRadius = 3.044721295736963e-05
concentrationFieldOpenFOAMDisplay.SetScaleArray = ['POINTS', 'U']
concentrationFieldOpenFOAMDisplay.ScaleTransferFunction = 'PiecewiseFunction'
concentrationFieldOpenFOAMDisplay.OpacityArray = ['POINTS', 'U']
concentrationFieldOpenFOAMDisplay.OpacityTransferFunction = 'PiecewiseFunction'
concentrationFieldOpenFOAMDisplay.DataAxesGrid = 'GridAxesRepresentation'
concentrationFieldOpenFOAMDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
concentrationFieldOpenFOAMDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.06000272557139397, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
concentrationFieldOpenFOAMDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.06000272557139397, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(concentrationFieldOpenFOAMDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
concentrationFieldOpenFOAMDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# Properties modified on concentrationFieldOpenFOAM
concentrationFieldOpenFOAM.Fields = ['C', 'U', 'p']

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(concentrationFieldOpenFOAMDisplay, ('CELLS', 'C'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
concentrationFieldOpenFOAMDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
concentrationFieldOpenFOAMDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'C'
cLUT = GetColorTransferFunction('C')

# get opacity transfer function/opacity map for 'C'
cPWF = GetOpacityTransferFunction('C')

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.GoToLast()

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=concentrationFieldOpenFOAM)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.002999999935127562, 0.0009999999820138328, 4.999999873689376e-05]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.002999999935127562, 0.0009999999820138328, 4.999999873689376e-05]

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['CELLS', 'C']
slice1Display.LookupTable = cLUT
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleArray = 'C'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 0.0006089442591473926
slice1Display.SelectScaleArray = 'C'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'C'
slice1Display.GaussianRadius = 3.044721295736963e-05
slice1Display.SetScaleArray = ['POINTS', 'C']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'C']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [-3.325856161635749e-28, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [-3.325856161635749e-28, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(concentrationFieldOpenFOAM, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# Properties modified on renderView1
renderView1.OrientationAxesVisibility = 0

# get color legend/bar for cLUT in view renderView1
cLUTColorBar = GetScalarBar(cLUT, renderView1)

# change scalar bar placement
cLUTColorBar.Position = [0.8940639269406393, 0.014687882496940025]

# Properties modified on cLUTColorBar
cLUTColorBar.RangeLabelFormat = '%-#6.1f'

# Properties modified on cLUTColorBar
cLUTColorBar.TitleJustification = 'Left'
cLUTColorBar.HorizontalTitle = 1

# change scalar bar placement
cLUTColorBar.WindowLocation = 'Any Location'
cLUTColorBar.Position = [0.1013698630136986, 0.3390452876376989]
cLUTColorBar.ScalarBarLength = 0.3300000000000003

# change scalar bar placement
cLUTColorBar.Position = [0.08675799086757988, 0.3390452876376989]

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1095, 817)

# current camera placement for renderView1
renderView1.CameraPosition = [0.002999999935127562, 0.0009999999820138328, 0.012545788247791479]
renderView1.CameraFocalPoint = [0.002999999935127562, 0.0009999999820138328, 4.999999873689376e-05]
renderView1.CameraParallelScale = 0.0032341479824236075

# save screenshot
SaveScreenshot('/home/michel/Git/mmft-CFD-cases/DiffusiveMixing/Xi-mixer/concentrationField/Xi-concentration-result.png', renderView1, ImageResolution=[1095, 817],
    OverrideColorPalette='WhiteBackground',
    TransparentBackground=1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1095, 817)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.002999999935127562, 0.0009999999820138328, 0.012545788247791479]
renderView1.CameraFocalPoint = [0.002999999935127562, 0.0009999999820138328, 4.999999873689376e-05]
renderView1.CameraParallelScale = 0.0032341479824236075

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).