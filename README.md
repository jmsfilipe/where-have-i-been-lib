# Where Have I Been
## GPX Library

###Intro

This repository offers the source code of the GPX library used in Where Have I Been.

We devised a library to process GPX files, based on the work of tkrajina.

This library has several main purposes:
* smoothing GPX files
* dividing GPX files into tracks representing, each, a moment of movement
* Reducing dataset size

###Auxiliary library to process GPX tracks

Important methods specified by calling order:


####Dividing and splitting tracks

If there is a strange variation of distance or time between two points, the track is divided in two.
If those distances are too close, it implies those tracks should be the same and are, therefore, combined into one track.

`track2trip(split_on_new_track, split_on_new_track_interval, min_sameness_distance)` 

**split_on_new_track** - whether or not a track should be split into a different file

**split_on_new_track_interval** - temporal distance between two points in order to consider splitting it

**min_sameness_distance** - minimum distance (in meters) in order to consider splitting the file


####Smoothing tracks

Smooths track data, based on the implementation by Tkrajina, focuses on two different ideas: calculating average distance between points to understand which points are outliers and therefore need to be removed, and applying a ratio to the other points to achieve a smooth, well-fitting path.

`smooth(remove_extremes, how_much_to_smooth)` 

**remove_extremes** - remove outlying points

**how_much_to_smooth** - decimal value that specifies how much to smooth


####Visually simplifying tracks (Ramer Douglas-Peucker)

Adaptation of Ramer Douglas-Peucker, by Tkrajina, including both spatial and temporal constraints. This version takes in account the temporal distance between the original curve and the simplified curve.

`simplify(max_distance, max_time)` 

**max_distance** - specifies, in kilometers, what is the expected maximum space between track points after the simplification

**max_time** - specifies, in seconds, the maximum time between two points that is expected after the simplification


####Reducing number of points

Intended to remove points that are not within a minimum distance of each other. This minimum separation between points is specified in meters. 

`reduce_points(min_distance, min_time)` 

**min_distance** - represents the maximum number of outputted points

**min_time** - the minimum distance between points