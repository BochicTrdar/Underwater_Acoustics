from numpy import *

def sioread(filename=None,p1=None,npi=None,channels=None):
    #*******************************************************************************
    # reads sio data files from SWellEX
    # Faro, Seg 28 Jun 2021 20:34:44 WEST 
    # Written by Orlando Camargo Rodriguez
    # Based on sioread.m
    # Big endian => bs = 32677!!!!!!
    # All these *.sio files are big endian. 
    # To read little endian sio files just remove .newbyteorder()
    #*******************************************************************************
    x = []
    fid = open(filename,'rb')
    ide = fromfile( fid, uint32, 1 ).newbyteorder()[0]  
    nr  = fromfile( fid, uint32, 1 ).newbyteorder()[0]  # Number of Records in File
    rl  = fromfile( fid, uint32, 1 ).newbyteorder()[0]  # Record Length in Bytes
    nc  = fromfile( fid, uint32, 1 ).newbyteorder()[0]  # Number of Channels in File
    sl  = fromfile( fid, uint32, 1 ).newbyteorder()[0]
    if (sl == 2): 
        thetype = 'int16'
    else:
        thetype = 'float32'
    f0  = fromfile( fid, uint32, 1 ).newbyteorder()[0]  # 0 = integer, 1 = real
    np = fromfile( fid, uint32, 1 ).newbyteorder()[0]  # Number of Points per Channel
    bs = fromfile( fid, uint32, 1 ).newbyteorder()[0]  # should be 32677
    fn = fid.read(24) # Read in the file name
    com= fid.read(72) # Read in the Comment String
    rechan = int( ceil(nr/nc) ) # records per channel
    ptrec  = int( rl/sl )       # points/record
    if (max(channels) > nc ):
       themessage = 'Requested channel higher than ' + str(nc)
       print(themessage)
    else: 
       r1 = int( floor(p1/ptrec) ) + 1 # record where we wish to start recording
       if ( npi <= 0 ):		       # if npi is 0, then we want all points		
            npi = np
       p2 = p1 + npi - 1	       # ending position in points for each channel
       r2 = int( ceil(1.0*p2/ptrec) )  # record where we end recording
       if ( p2 > np ):		       # error checking to prevent reading past EOF
          print('Warning: p1 + npi > np')
          p2 = np 
          r2 = rechan
       totalrec = r2 - r1 + 1 # number of records desired read
# we're going to read in entire records into the variable tmpx, then
# we'll worry about the start point 
       pp1 = remainder(p1,ptrec) # p1's position in record
       if ( pp1 == 0 ):		 # no remainder means last point in record
          pp1 = 2048
       lchannels = len( channels )
       x    = zeros( (p2-p1+1,lchannels) ) # allocate a matrix for final result
       tmpx = zeros(totalrec*ptrec)	   # make a temporary matrix
# Loop over the desired channels
       for J in range(lchannels):
           count = 0			    # Start 
           trec = (r1 - 1)*nc + channels[J] # First Record to read for this channel
           for R in range(totalrec):
               fid.seek(rl*trec,0) # position to the desired record
               tmpx[count:count+ptrec] = fromfile( fid, thetype, ptrec ).newbyteorder() # Read in a record's worth of points
               count = count + ptrec	# adjust for the next set of points
               trec = trec + nc		# Next record for this channel is nc records away 
           x[0:p2-p1+1,J] = tmpx[pp1:pp1+p2-p1+1]
    fid.close()
    x = squeeze( x )
    return x
