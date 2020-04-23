set grid
set logscale y
set xrange [0:1200]
set yrange [0.1:1e7]
set xtics font "Courier 34"
set ytics font "Courier 34"
set xlabel "Time (turns)" font "Courier 38"
set ylabel "Number" font "Courier 38"
set key box on bottom right font "Courier 28"
set terminal postscript color enhanced
set output "April23_plot2.eps"
plot "run_100by100_1000turns_100_500_foodturns.dat" using 1:2 w l lc -1 lw 3 title "FSMs scenario 2", "run_100by100_1000turns_100_500_foodturns.dat" using 1:3 w l lc 3 lw 3 title "Cases scenario 2"