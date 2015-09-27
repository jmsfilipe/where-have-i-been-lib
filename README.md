# Where Have I Been
## GPX Library

###Auxiliary library to process GPX tracks

Important methods specified by calling order:

####Dividing and splitting tracks

`track2trip(split_on_new_track, split_on_new_track_interval, min_sameness_distance, min_sameness_interval)` 

Splits a track into smaller ones, according to how long has the user been standing without moving.

####Smoothing tracks

`smooth(remove_extremes, how_much_to_smooth, min_sameness_distance, min_sameness_interval)` 

Smooths gpx track

####Visually simplifying tracks (Ramer Douglas-Peucker)

`simplify(max_distance, max_time)` 

Simplify using the Ramer-Douglas-Peucker algorithm

####Reducing number of points

`reduce_points(min_distance, min_time)` 

Reduce overall points of a track
