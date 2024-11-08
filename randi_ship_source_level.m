function Ls = randi_ship_source_level(frequencies,speed_knots,ship_length)

% Reference: Research Ambient Noise Directionality (RANDI) 3.1 Physics Description
% Breeding et al., 1996. 
% Ls is the noise source levels in dB, speed in knots, lenght in feet. 

Ls  = nan*ones( size( frequencies) );
df  =    zeros( size( frequencies) );
Ls0 =    zeros( size( frequencies) );
Ls0 = 173.2 - 18*log10( frequencies );

% Correction factor:
dl = ship_length^( 1.15 )/3643.0;
indexes = find( frequencies <= 28.4 ); df( indexes ) = 8.1;
indexes = find( (frequencies > 28.4)&( frequencies <= 191.6 ) ); df(indexes) = 22.3 - 9.77*log10( frequencies(indexes) );
indexes = find( frequencies < 500 ); fi = frequencies( indexes );
Ls0( indexes ) = -10*log10( 10.^( -1.06*log10( fi ) - 14.34 ) + 10.^( 3.32*log10( fi ) - 21.425 ) );

Ls = Ls0 + 60*log10(speed_knots/12.0); + 20*log10(ship_length/300.0) + df*dl + 3;
