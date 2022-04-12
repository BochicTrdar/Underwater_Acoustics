from numpy import *
def ReadVLAData(filename=None,DataType=None):
#
# Reads a Data File from the LOCAPASS DAQ System
#
#    [data, fs, NoSs, TITLE, TIMEPOS] = ReadVLAData(file,flag)
#
# Where:
#     data: is a matrix [ NoChannels * Total No Samples ]
#     fs: sampling frequency
#     NoSs: Number of Channels
#     TITLE: Description of the experiment
#     TIMEPOS: Time/Position information of the data in the file
#
#     file: name of file to be read, empty variable will allow the selection
#           of the file to read, recognized extensions:
#                      * "acoustic"          - Acoustic Data
#		       * "nonacoustic"
#		       * "timeposition"

# Faro, Ter 12 Abr 2022 20:59:16 WEST 
# Written by Tordar

# Don't like it? Don't use it... 

    data    = []
    Fs      = []
    NoSs    = []
    TITLE   = []
    TIMEPOS = []

    fid = open(filename,'rb')

    TITLE         = fid.readline().decode('UTF-8')
    TIMEPOS       = fid.readline().decode('UTF-8')
    NonAcdatainfo = fid.readline().decode('UTF-8')
    Acdatainfo    = fid.readline().decode('UTF-8')

    if DataType == 'timeposition':  
       count = 0
       Fs   = int( NonAcdatainfo[16:21] ) # Sampling frequency
       NoSs = int( NonAcdatainfo[28:30] ) # No of Channels
       SpSz = int( NonAcdatainfo[38:40] ) # No of Bits per Samples
       ToSp = int( NonAcdatainfo[46:54] ) # Total Number of Samples
    elif DataType == 'nonacoustic':
       Fs   = int( NonAcdatainfo[15:20] ) # Sampling frequency
       NoSs = int( NonAcdatainfo[28:30] ) # No of Channels
       SpSz = int( NonAcdatainfo[38:40] ) # No of Bits per Samples
       ToSp = int( NonAcdatainfo[46:54] ) # Total Number of Samples
       int_type = 'int' + str( SpSz )
       if NoSs > 0:
          count = NoSs
          k = int(ToSp/NoSs)
          data = zeros((NoSs,k))
          for i in range(k):
              data[:,i] = int( fromfile( fid, int_type , count=NoSs ) )
       else:
          count = 0
    elif DataType == 'acoustic':
       NoSs = int( NonAcdatainfo[28:30] ) # No of Channels
       SpSz = int( NonAcdatainfo[38:40] ) # No of Bits per Samples
       ToSp = int( NonAcdatainfo[46:54] ) # Total Number of Samples
       int_type = 'int' + str( SpSz )
       if NoSs > 0:
          k = int(ToSp/NoSs)
          data = zeros((NoSs,k))
          for i in range(k):
              data[:,i] = fromfile( fid, dtype=int_type, count=NoSs )
       Fs   = int( Acdatainfo[15:20] ) # Sampling frequency
       NoSs = int( Acdatainfo[28:30] ) # No of Channels
       SpSz = int( Acdatainfo[38:40] ) # No of Bits per Samples
       ToSp = int( Acdatainfo[46:54] ) # Total Number of Samples
       int_type = 'int' + str( SpSz )
       k = int(ToSp/NoSs)
       data = zeros((NoSs,k))
       for i in range(k):
           data[:,i] = fromfile( fid, dtype=int_type, count=NoSs )
    else:
       print( 'Invalid data type...' )

    fid.close()

    return data, Fs, NoSs, TITLE, TIMEPOS

