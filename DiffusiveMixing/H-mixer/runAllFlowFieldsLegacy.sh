angles=( '27' '45' '90' )
diffusivities=( '1e-7' '1e-8' '1e-9' )
pressures=( '1.0' '0.1' '0.01' )
viscosities=( '1e-5' '1e-6' '1e-7' )

workdirectories=()

for angle in "${angles[@]}"
do
    for diffusivity in "${diffusivities[@]}"
    do
        workdirectories+=("${angle}deg/D${diffusivity}/flowField/")
    done
    for pressure in "${pressures[@]}"
    do
        workdirectories+=("${angle}deg/p${pressure}/flowField/")
    done
    for viscosity in "${viscosities[@]}"
    do
        workdirectories+=("${angle}deg/v${viscosity}/flowField/")
    done
done

count=0
for workdirectory in "${workdirectories[@]}"
do
    blockMesh -case "${workdirectory}" & (( count ++ ))
    if (( count > 5 )); then
        wait
        count=0
    fi
done

count=0
for workdirectory in "${workdirectories[@]}"
do
    foamRun -case "${workdirectory}" & (( count ++ ))
    if (( count > 5 )); then
        wait
        count=0
    fi
done