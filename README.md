# savitzky_golay
Savitzky Golay Filter Implementation in Python

Example is shown in comments at the end of the code

Pass the data to the savgol1Dfilt or savgol2Dfilt functions along with the other parameters
The functions will return the result

The implementation takes about 170 milliseconds for a 2nd order 2D filter with 11 data points in both direction for smoothing.

And about 3.2 milliseconds for a 3rd order filter taking 13 data pints for smoothing.

[[Intel i3 1.7GHz processor with 4GB RAM]]
