__author__ = 'jmsfilipe'

def getKey(customobj):
    return customobj.getKey()

if __name__ == '__main__':
    import gpxpy
    import gpxpy.gpx
    import glob
    import psycopg2
    import ppygis
    import os
    from time import mktime
    import StringIO
    import datetime
    import gpxpy
    import gpxpy.gpx
    import glob
    import os
    import time
    import sys
    print "STARTING..."
    directory_name = 'tracks/'
    saving_name = 'save/'
    saving_directory = os.path.join(directory_name, saving_name)
    DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

    print datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    file_count = 0;
    total_size = 0;
    if not os.path.exists(saving_directory):
        os.makedirs(saving_directory)
    current_day = ""
    for entry in sorted(glob.glob(directory_name + "*.[gG][pP][xX]")):

        name = 0
        file = open(entry, 'rb')
        gpx_xml = file.read()
        file.close()

        gpx = gpxpy.parse(gpx_xml)
        gpx_list = gpx.track2trip(True, 60, 100, None)

        for segment in sorted(gpx_list):
            if segment.points[0].time.strftime("%Y-%m-%d") != current_day:
                name = 0
            else:
                name += 1

            segment.smooth(True, 1.5)
            segment.simplify(0.01,5) #RDP
            segment.reduce_points(10, 5)

            gpx_write = gpxpy.gpx.GPX()

            # Create first track in our GPX:
            gpx_track = gpxpy.gpx.GPXTrack()

            # Create first segment in our GPX track:
            gpx_segment = gpxpy.gpx.GPXTrackSegment()
            gpx_track.segments.append(segment)
            gpx_write.tracks.append(gpx_track)

            current_day =  segment.points[0].time.strftime("%Y-%m-%d")
            fo = open("{}-part{}.gpx".format(os.path.join(saving_directory,current_day),name), "wb")

            gpx_string = gpx_write.to_xml()
            file_count+=1
            total_size += sys.getsizeof(gpx_string)

            fo.write(gpx_string)
            fo.close()
    print "generated nr files " , file_count
    print "total size "  , total_size
    print datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    print "ALL DATA IS PROCESSED.\nYOU CAN NOW CLOSE THIS."
