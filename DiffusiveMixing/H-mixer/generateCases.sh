angles=( '14' '27' '45' '63' '90' )
channelLengths=( '2' '10' '20' )
velocities=('0.1' '0.01')

# 10^-8.1, 10^-8.2, ..., 10^-9.0
exponentials=('7.943282347242822e-09' '6.309573444801943e-09' '5.011872336272715e-09' '3.981071705534969e-09' '3.1622776601683795e-09' '2.511886431509582e-09' '1.9952623149688828e-09' '1.584893192461111e-09' '1.2589254117941663e-09' '1e-9')

NUMCONC=10

for angle in "${angles[@]}"
do
    for length in "${channelLengths[@]}"
    do
	for velocity in "${velocities[@]}"
	do
		for ((i=0;i<NUMCONC;i++));
		do
			cp -r templateConc/ "${angle}deg/cL${length}/U${velocity}/D8.$((i+1))"
			cd "${angle}deg/cL${length}/U${velocity}/D8.$((i+1))"
			cp ../flowField/system/blockMeshDict system/blockMeshDict
    		cp ../flowField/[1-9]*/p 0/p
    		cp ../flowField/[1-9]*/U 0/U
    		cp ../flowField/[1-9]*/phi 0/phi
			sed -i "s/D = 1e-8)/D = ${exponentials[i]})/g" system/controlDict
			cd ../../../..
		done
	done
    done
done

for workdirectory in "${workdirectories[@]}"
do
	

    cp ${workdirectory}/flowField/[1-9]*/phi ${workdirectory}/concentrationField/0/phi
    cp ${workdirectory}/flowField/[1-9]*/U ${workdirectory}/concentrationField/0/U

done
