% Wind Noise - Hildebrand model
% Faro, Thu 07 Nov 2024 10:59:28 PM WET 

clear all, close all, clc

disp('Hildebrand model test:')

z = 0; % Depth (change at will)

load wind_data % Copernicus prediction (converted to *.mat)

figure(1)
pcolor(longitudew,latitudew,thewind), shading interp
a = colorbar;
title(a,'Wind (m/s)','FontSize',20','FontWeight','Bold');
xlabel('Longitude (degrees)')
ylabel('Latitude (degrees)')
title( 'Copernicus Wind Data' )

% 1/3 octave bands (just some frequencies to test the model):
load frequencies_1_3oct.dat
       
f1 = frequencies_1_3oct(:,1);
fc = frequencies_1_3oct(:,2); % Central frequencies
f2 = frequencies_1_3oct(:,3);

nfreqs = length( fc );
nlon   = length( longitudew );
nlat   = length(  latitudew );

WIND_NOISE = zeros(nlon,nlat,nfreqs);

[fkHz,wmps,noise] = hildebrand_wind_noise( z );
fHz = 1000*fkHz;
[fHz,indexes] = unique( fHz ); % Remove duplicates in frequency
noise = noise( :, indexes );        

for j = 1:nlon
    for k = 1:nlat
        wjk = thewind(k,j);
        if wjk < 1
           wjk = 1;
        endif
        noisejk = interp2(fHz,wmps,noise,fc',wjk);
        WIND_NOISE(j,k,:) = noisejk;
    endfor
endfor

for ifreq = 1:nfreqs
    thetitle = [ 'FREQ = ' num2str( fc(ifreq) ) 'Hz' ]; 
    figure(2)
    pcolor(longitudew,latitudew,squeeze(WIND_NOISE(:,:,ifreq))), shading interp
    a = colorbar;
    title(a,'Wind Noise (dB)','FontSize',20','FontWeight','Bold');
    xlabel('Longitude (degrees)')
    ylabel('Latitude (degrees)')
    title(thetitle)
    pause(0.1) 
endfor

disp('done.')
