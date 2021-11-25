# Outputs the first line of each file

for f in $@
do
    head -n1 $f
    tail -n1 $f
done
