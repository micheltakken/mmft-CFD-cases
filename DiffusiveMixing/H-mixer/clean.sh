# Remove all unnecessary timestep results
find . -name *00 -type d -exec rm -rf {} \;
