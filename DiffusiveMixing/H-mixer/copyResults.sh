angles=( '27' '45' '90' )
diffusivities=( '1e-7' '1e-8' '1e-9' )
pressures=( '1.0' '0.1' '0.01' )
viscosities=( '1e-5' '1e-6' '1e-7' )

workdirectories=()

for angle in "${angles[@]}"
do
    for diffusivity in "${diffusivities[@]}"
    do
        workdirectories+=("${angle}deg/D${diffusivity}")
    done
    for pressure in "${pressures[@]}"
    do
        workdirectories+=("${angle}deg/p${pressure}")
    done
    for viscosity in "${viscosities[@]}"
    do
        workdirectories+=("${angle}deg/v${viscosity}")
    done
done

for workdirectory in "${workdirectories[@]}"
do
	
    cp "${workdirectory}/flowField/[1-9]*/p" "${workdirectory}/concentrationField/0/p"
    cp "${workdirectory}/flowField/[1-9]*/phi" "${workdirectory}/concentrationField/0/phi"
    cp "${workdirectory}/flowField/[1-9]*/U" "${workdirectory}/concentrationField/0/U"

done
