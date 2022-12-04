# part 1
paste -sd+ <(tr 'XYZ' 'ABC' < input | tr 'ABC' '123' | sed 's/\ //;s/\(.\)\1/\1+3/;s/21/1/;s/32/2/;s/13/3/;s/12/8/;s/23/9/;s/31/7/' | bc) | bc
# part 2
paste -sd+ <(cat input | sed -r 's/ //;s/([A-C])(Y)/\1\1/;s/AX/AC/;s/BX/BA/;s/CX/CB/;s/AZ/AB/;s/BZ/BC/;s/CZ/CA/' | tr 'ABC' '123' | sed 's/\(.\)\1/\1+3/;s/21/1/;s/32/2/;s/13/3/;s/12/8/;s/23/9/;s/31/7/' | bc) | bc
