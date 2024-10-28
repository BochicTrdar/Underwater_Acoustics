function slout = jomopans_ship_source_level(vessel_class,vessel_speed,vessel_length,frequencies);
%   JOMOPANS-ECHO source level model
%   Implements the JE-model as set out in ref 
%   "A Reference Spectrum Model for Estimating Source Levels of Marine 
%   Shipping Based on Automated Identification System Data"
%   Alexander MacGillivray and Christ de Jong
%   https://doi.org/ 10.3390/jmse9040369
%
%   Output SL values are validated through the Excel file given as
%   supplement in the Reference paper.
%
%   Inputs:     Vessel AIS id, class,  speed [knots], length [m], frequencies
%
%   Output:
%   slout       array with SL(fc1),...SL(fcN)
%
%=====================================================================================
% Based on jmse-09-00369-s001.xlsx

% Don't like it? Don't use it... 
slout = [];
nfreqs = length(frequencies);

% conversion constants
foot    = 0.3048;                   % m
knot    = 1852/3600;                % m/s
fref    = 1;                        % Hz
lref    = 300/3.28084;              % 91.44 for all vessels

% Parameters:
K       = 191*ones(1,nfreqs);
B       =    zeros(1,nfreqs);
D       =    zeros(1,nfreqs);
f1      =    zeros(1,nfreqs);

Vc      = struct('Fishing'     , 6.4,'Tug'          ,3.7,'Naval' ,11.1,...
                 'Recreational',10.6,'Government'   ,8  ,'Cruise',17.1,'Passenger',9.7,'Research',8,...
                 'Bulker'      ,13.9,'Containership',18,'VCarrier',15.8,'Tanker'  ,12.4,...
                 'Other'        , 7.4,'Dredger'     ,9.5);     % knots!
Cargo   = struct('Fishing'     ,0,'Tug'          ,0,'Naval'   ,0,...
                 'Recreational',0,'Government'   ,0,'Cruise'  ,0,'Passenger',0,'Research',0,...
                 'Bulker'      ,1,'Containership',1,'VCarrier',1,'Tanker'   ,1,...
                 'Other'       ,0,'Dredger'     ,0);     % knots!
Vref = 1; % knot
D_lo = 1;
D_hi = 3;
Vcc          = getfield(Vc   ,vessel_class);
vessel_cargo = getfield(Cargo,vessel_class);

LF_Hump = (vessel_cargo == 1)&( frequencies < 100 );
K( LF_Hump ) = 208;
B( LF_Hump ) = 2;

if strcmp(vessel_class,'Bulker')|strcmp(vessel_class,'Containership')
D_lo = 0.8;
endif

if strcmp(vessel_class,'Cruise')
D_hi = 4;
endif 

D(1:nfreqs) = D_hi; D( LF_Hump ) = D_lo;
f1(1:nfreqs) = 480/Vcc; f1( LF_Hump ) = 600/Vcc; 

slout = K - 10*( B + 2 ).*log10( f1 ) + 5*B.*log10( frequencies ) - 10*log10( (1 - (frequencies./f1).^(0.5*(B+2))).^2 + D.^2 ) + ...
60*log10( vessel_speed/Vcc ) + 20*log10( vessel_length/lref ); % Source Pressure Spectral Density (dB re uPa²/Hz m)
slout = slout + 10*log10( 0.231*frequencies ); % Decidecade Band Source Level (dB re 1 uPa.m)
