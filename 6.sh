# part 1
seq 1 $(paste <(cat input | wc -c) <(echo - 4) | bc) | sed -r 's/(.*)/echo "$(echo \1-3 | bc)-\1"/ge' | xargs -I{} sh -c 'cat input | cut -c {} | fold -w1 | sort | uniq | wc -l' | grep -n 4 | head -n 1
# part 2
seq 1 $(paste <(cat input | wc -c) <(echo - 13) | bc) | sed -r 's/(.*)/echo "$(echo \1-13 | bc)-\1"/ge' | xargs -I{} sh -c 'cat input | cut -c {} | fold -w1 | sort | uniq | wc -l' | grep -n 13 | head -n 1
