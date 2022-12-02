paste -sd+ <(tr 'XYZ' 'ABC' < input | tr 'ABC' '123' | sed 's/\ //g;s/\(.\)\1/\1+3/g;s/21/1/g;s/32/2/g;s/13/3/g;s/12/8/g;s/23/9/g;s/31/7/g' | bc) | bc
paste -sd+ <(tr -d ' ' < input | sed -r 's/([A-C])(Y)/\1\1/g;s/AX/AC/g;s/BX/BA/g;s/CX/CB/g;s/AZ/AB/g;s/BZ/BC/g;s/CZ/CA/g' | tr 'ABC' '123' | sed 's/\(.\)\1/\1+3/g;s/21/1/g;s/32/2/g;s/13/3/g;s/12/8/g;s/23/9/g;s/31/7/g' | bc) | bc
