# Remove all unnecessary timestep results
find . -name *00 -type d -exec rm -rf {} \;
find . -name 5 -type d -exec rm -rf {} \;
find . -name 10 -type d -exec rm -rf {} \;
find . -name 15 -type d -exec rm -rf {} \;

