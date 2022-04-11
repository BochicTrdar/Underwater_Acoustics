from numpy import *

def hreadchn( filename=None, channel=None):
    #*******************************************************************************
    # reads HIFT sam file and extracts specified channel's time series
    # Faro, Qui 24 Jun 2021 21:18:56 WEST 
    # Written by Orlando Camargo Rodriguez
    # Based on hreadchn.m
    #*******************************************************************************
    sam = []
    fid = open(filename,'rb')
    # read header (uncomment disp commands to print header)
    N_chans    = 0
    chan_index = 0
    theline = str( fid.readline() )
    print( theline )
    i0 = theline.find('*DATA*')
    while i0 == -1:
         theline = str( fid.readline() )
         print( theline )
         i0 = theline.find('*DATA*')
         off = theline.find('Julian:')
         if off == 0:
            time_text = theline
         off = theline.find('channel:')
         if off > -1:
            N_chans = N_chans + 1
            chan_num = int( theline[off+8:off+10] )
            if chan_num == channel:
               chan_index = N_chans
    if chan_index == 0:
       print('channel not found in input file...')
    else:
       start = fid.tell()
       fid.seek(0,2)
       stop = fid.tell()
       fid.seek(start,0)
       sizs = int( ( stop - start )/2 )
       scan_count = int( floor(sizs/N_chans) )
       if N_chans == 1:
          sam = fromfile( fid, dtype=int16, count=sizs )
       else:
          dummy = fromfile( fid, dtype=int16, count=chan_index-1 )
      #try to read all items:
          sam = fromfile( fid, dtype=int16, count=-1 )
    fid.close()
    return sam

