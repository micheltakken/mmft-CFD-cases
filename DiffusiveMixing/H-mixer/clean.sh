# Remove all unnecessary timestep results
find . -name *00 -type d -exec rm -rf {} \;
find . -name 1 -type d -exec rm -rf {} \;
find . -name 2 -type d -exec rm -rf {} \;
find . -name 3 -type d -exec rm -rf {} \;
find . -name 4 -type d -exec rm -rf {} \;

