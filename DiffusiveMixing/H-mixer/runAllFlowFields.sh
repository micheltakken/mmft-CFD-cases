angles=( '63' )
lengths=( '2' '10' '20' )
velocities=( '0.1' '0.01' )

workdirectories=()

for angle in "${angles[@]}"
do
    for length in "${lengths[@]}"
    do
        for velocity in "${velocities[@]}"
        do
            workdirectories+=("${angle}deg/cL${length}/U${velocity}/flowField/")
        done
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
