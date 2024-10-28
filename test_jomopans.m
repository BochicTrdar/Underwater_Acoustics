% Faro, sex 27 set 2024 15:28:34 
clear all, close all, clc

frequencies = [10.0, 12.6, 15.8, 20.0, 25.1, 31.6, 39.8, 50.1, 63.1, 79.4, 100.0, 125.9, 158.5, 199.5, 251.2, 316.2, 398.1, 501.2, ...
631.0, 794.3, 1000.0, 1258.9, 1584.9, 1995.3, 2511.9, 3162.3, 3981.1, 5011.9, 6309.6, 7943.3, 10000.0, 12589.3, 15848.9, 19952.6, ... 
25118.9, 31622.8 ];

vessel_class = 'Bulker'; vessel_speed = 13.5; vessel_length = 211;
%vessel_class = 'Containership'; vessel_speed = 13.5; vessel_length = 211;
%vessel_class = 'Cruise'; vessel_speed = 13.5; vessel_length = 211;
%vessel_class = 'Dredger'; vessel_speed = 13.5; vessel_length = 211;
%vessel_class = 'Fishing'; vessel_speed = 13.5; vessel_length = 211;
%vessel_class = 'Government'; vessel_speed = 13.5; vessel_length = 211;
%vessel_class = 'Research'; vessel_speed = 13.5; vessel_length = 211;
%vessel_class = 'Naval'; vessel_speed = 13.5; vessel_length = 211;
%vessel_class = 'Other'; vessel_speed = 13.5; vessel_length = 211;
%vessel_class = 'Passenger'; vessel_speed = 13.5; vessel_length = 211;
%vessel_class = 'Recreational'; vessel_speed = 13.5; vessel_length = 211;
%vessel_class = 'Tanker'; vessel_speed = 13.5; vessel_length = 211;
%vessel_class = 'VCarrier'; vessel_speed = 13.5; vessel_length = 211;

SL = jomopans_ship_source_level(vessel_class, vessel_speed, vessel_length, frequencies);

figure(1)
semilogx(frequencies,SL,'LineWidth',3)
ylim([100,190])
box on, grid on
xlabel('Frequency (Hz)','FontWeight','Bold')
ylabel('Decidecade Band Source Level (dB re 1 uPa.m)','FontWeight','Bold')
title( vessel_class )
