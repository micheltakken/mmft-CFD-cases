# Remove all unnecessary timestep results
#find . -name *000 -type d -exec rm -rf {} \;
find . -name 5 -type d -exec rm -rf {} \;
find . -name 10 -type d -exec rm -rf {} \;
find . -name 15 -type d -exec rm -rf {} \;
find . -name polyMesh -type d -exec rm -rf {} \;
find . -name dynamicCode -type d -exec rm -rf {} \;
