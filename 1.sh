# part 1
cat input | sed -z 's/\n\n/|/g;s/\n/+/g;s/.$//;s/|/\n/g' | bc | sort | tail -n 1
# part 2
paste -sd+ <(cat input | sed -z 's/\n\n/|/g;s/\n/+/g;s/.$//;s/|/\n/g' | bc | sort | tail -n 3) | bc
