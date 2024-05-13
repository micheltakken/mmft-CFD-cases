# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
d80OpenFOAM = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
d80OpenFOAMDisplay = Show(d80OpenFOAM, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
d80OpenFOAMDisplay.Representation = 'Surface'
d80OpenFOAMDisplay.ColorArrayName = [None, '']
d80OpenFOAMDisplay.SelectTCoordArray = 'None'
d80OpenFOAMDisplay.SelectNormalArray = 'None'
d80OpenFOAMDisplay.SelectTangentArray = 'None'
d80OpenFOAMDisplay.OSPRayScaleArray = 'U'
d80OpenFOAMDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
d80OpenFOAMDisplay.SelectOrientationVectors = 'None'
d80OpenFOAMDisplay.ScaleFactor = 0.0006044721321813995
d80OpenFOAMDisplay.SelectScaleArray = 'None'
d80OpenFOAMDisplay.GlyphType = 'Arrow'
d80OpenFOAMDisplay.GlyphTableIndexArray = 'None'
d80OpenFOAMDisplay.GaussianRadius = 3.0223606609069977e-05
d80OpenFOAMDisplay.SetScaleArray = ['POINTS', 'U']
d80OpenFOAMDisplay.ScaleTransferFunction = 'PiecewiseFunction'
d80OpenFOAMDisplay.OpacityArray = ['POINTS', 'U']
d80OpenFOAMDisplay.OpacityTransferFunction = 'PiecewiseFunction'
d80OpenFOAMDisplay.DataAxesGrid = 'GridAxesRepresentation'
d80OpenFOAMDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
d80OpenFOAMDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.03000354953110218, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
d80OpenFOAMDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.03000354953110218, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(d80OpenFOAMDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
d80OpenFOAMDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# Properties modified on d80OpenFOAM
d80OpenFOAM.Fields = ['C', 'U', 'p']

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(d80OpenFOAMDisplay, ('CELLS', 'C'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
d80OpenFOAMDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
d80OpenFOAMDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'C'
cLUT = GetColorTransferFunction('C')

# get opacity transfer function/opacity map for 'C'
cPWF = GetOpacityTransferFunction('C')

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.GoToLast()

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=d80OpenFOAM)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.002999999980602297, 0.0009999999565479811, 4.999999873689376e-05]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.002999999980602297, 0.0009999999565479811, 4.999999873689376e-05]

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
slice1Display.ScaleFactor = 0.0006044721321813995
slice1Display.SelectScaleArray = 'C'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'C'
slice1Display.GaussianRadius = 3.0223606609069977e-05
slice1Display.SetScaleArray = ['POINTS', 'C']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'C']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [-1.3620621073237222e-40, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [-1.3620621073237222e-40, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(d80OpenFOAM, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# Properties modified on renderView1
renderView1.OrientationAxesVisibility = 0

# Rescale transfer function
cLUT.RescaleTransferFunction(0.0, 1.0)

# Rescale transfer function
cPWF.RescaleTransferFunction(0.0, 1.0)

# get color legend/bar for cLUT in view renderView1
cLUTColorBar = GetScalarBar(cLUT, renderView1)

# change scalar bar placement
cLUTColorBar.Orientation = 'Vertical'
cLUTColorBar.WindowLocation = 'Any Location'
cLUTColorBar.Position = [0.06940639269406391, 0.34394124847001223]
cLUTColorBar.ScalarBarLength = 0.3299999999999998

# Properties modified on cLUTColorBar
cLUTColorBar.TitleJustification = 'Left'
cLUTColorBar.HorizontalTitle = 1
cLUTColorBar.RangeLabelFormat = '%-#6.1f'

# change scalar bar placement
cLUTColorBar.Position = [0.09315068493150683, 0.3353733170134639]

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1095, 817)

# current camera placement for renderView1
renderView1.CameraPosition = [0.002999999980602297, 0.0009999999565479811, 0.012406970420835535]
renderView1.CameraFocalPoint = [0.002999999980602297, 0.0009999999565479811, 4.999999873689376e-05]
renderView1.CameraParallelScale = 0.003198219285007663

# save screenshot
SaveScreenshot('/home/michel/Git/mmft-CFD-cases/DiffusiveMixing/H-mixer/27deg/cL2/U0.01/D8.0/H-concentration-render.png', renderView1, ImageResolution=[1095, 817],
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
renderView1.CameraPosition = [0.002999999980602297, 0.0009999999565479811, 0.012406970420835535]
renderView1.CameraFocalPoint = [0.002999999980602297, 0.0009999999565479811, 4.999999873689376e-05]
renderView1.CameraParallelScale = 0.003198219285007663

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).