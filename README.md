# Where Have I Been
## GPX Library

###Auxiliary library to process GPX tracks

Important methods specified by calling order:

####Dividing and splitting tracks

The algorithm to split tracks works as follows: if there is a strange variation (given as a parameter) of distance or time between two points, the track is divided in two - the first track ending in that point, and the second track starting in that point. The algorithm to join tracks checks temporal and spatial distances and if those distances are too close (given as a parameter), it implies those tracks should be the same and are, therefore, combined into one track.

`track2trip(split_on_new_track, split_on_new_track_interval, min_sameness_distance, min_sameness_interval)` 

**split_on_new_track** - whether or not a track should be split into a different file
**split_on_new_track_interval** - temporal distance between two points in order to consider splitting it
**min_sameness_distance** - minimum distance (in meters) in order to consider splitting the file

####Smoothing tracks

Smooths track data, based on the implementation by Tkrajina, focuses on two different ideas: calculating average distance between points to understand which points are outliers and therefore need to be removed, and applying a ratio to the other points to achieve a smooth, well-fitting path.

`smooth(remove_extremes, how_much_to_smooth, min_sameness_distance, min_sameness_interval)` 

remove_extremes
how_much_to_smooth
min_sameness_distance
min_sameness_interval

####Visually simplifying tracks (Ramer Douglas-Peucker)

Adaptation of Ramer Douglas-Peucker, by Tkrajina, including both spatial and temporal constraints. The modified version of the algorithm introduced in this work also takes in account the temporal distance between the original curve and the simplified curve. By doing this, we can preserve the form of the path, even when we have different speeds (which cause different sample rates).

`simplify(max_distance, max_time)` 

max_distance
max_time

####Reducing number of points

Ĩntended to remove points that are not within a minimum distance of each other. This minimum separation between points is specified in meters. 

`reduce_points(min_distance, min_time)` 

min_distance
min_time