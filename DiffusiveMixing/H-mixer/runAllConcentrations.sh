angles=( '14' '27' '45' '63' '90' )
#angles=( '90' )
lengths=( '2' '10' '20' )
velocities=( '0.1' '0.01' )
concentrations=( '8.1' '8.2' '8.3' '8.4' '8.5' '8.6' '8.7' '8.8' '8.9' '8.10' )
#lengths=('20')
#velocities=('0.1')
#concentrations=('8.1')


workdirectories=()

for angle in "${angles[@]}"
do
    for length in "${lengths[@]}"
    do
        for velocity in "${velocities[@]}"
        do
            for concentration in "${concentrations[@]}"
            do
                workdirectories+=("${angle}deg/cL${length}/U${velocity}/D${concentration}/")
            done
        done
    done
done

count=0
for workdirectory in "${workdirectories[@]}"
do
    blockMesh -case "${workdirectory}" & (( count ++ ))
    if (( count > 20 )); then
        wait
        count=0
    fi
done
#wait

#count=0
#for workdirectory in "${workdirectories[@]}"
#do
#    foamRun -case "${workdirectory}" & (( count ++ ))
#    if (( count > 20 )); then
#        wait
#        count=0
#    fi
#done
