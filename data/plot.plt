set grid
set logscale y
set xrange [1:500]
set yrange [1:1e7]
plot "run_20by20_500turns_250foodturns.dat" using 1:2 w p pt 6, "run_20by20_500turns_250foodturns.dat" using 1:3 w p pt 6 lc 1, \
"run_40by40_500turns_250foodturns.dat" using 1:2 w p pt 6, "run_40by40_500turns_250foodturns.dat" using 1:3 w p pt 6 lc -1