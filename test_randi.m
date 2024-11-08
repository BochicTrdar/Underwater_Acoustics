% Gambelas, qui 07 nov 2024 10:49:44 
% Written by Tordar

% SHIP TYPE       LENGTH (ft) SPEED (kt)
% Fishing Vessel  50-150       7-10
% Merchant       275-400      10-15
% Tanker         400-500      12-16
% Large Tanker   500-700      15-18
% Super Tanker   800-1200     15-22

% SHIP TYPE      10 Hz 25 Hz 50 Hz 100 Hz 300 Hz
% Fishing Vessel 142.7 146.5 144.8 136.0  120.0
% Merchant Ship  160.9 167.8 162.6 153.5  137.1
% Tanker         167.0 170.8 168.6 159.2  141.6  
% Large Tanker   174.8 178.6 176.0 166.3  149.3
% Super Tanker   185.0 188.8 185.4 174.6  156.8
clear all, close all, clc

l = 0.5*[50+150,275+400,400+500,500+700,800+1200]; % In feet !!!!
s = 0.5*[7+10,10+15,12+16,15+18,15+22];            % in knots!!!!
f = [10, 25, 50, 100, 300];

L1 = randi_ship_source_level(f,s(1),150);
L2 = randi_ship_source_level(f,s(2),l(2));
L3 = randi_ship_source_level(f,s(3),l(3));
L4 = randi_ship_source_level(f,s(4),l(4));
L5 = randi_ship_source_level(f,s(5),l(5));

f2 = [10:1:300];
L12 = randi_ship_source_level(f2,s(1),150);
L22 = randi_ship_source_level(f2,s(2),l(2));
L32 = randi_ship_source_level(f2,s(3),l(3));
L42 = randi_ship_source_level(f2,s(4),l(4));
L52 = randi_ship_source_level(f2,s(5),l(5));

figure(1)
hold on
plot(f,L1)
plot(f,L1,'bo')
plot(f,L2)
plot(f,L2,'ro')
plot(f,L3)
plot(f,L3,'g*')
plot(f,L4)
plot(f,L4,'gd')
plot(f,L5)
plot(f,L5,'gs')
hold off
ylabel('L_s (dB)')
xlabel('Frequency (Hz)')
title('RANDI model')
box on, grid on

figure(2)
hold on
plot(f2,L12,'b','LineWidth',2)
plot(f2,L22,'r','LineWidth',2)
plot(f2,L32,'g','LineWidth',2)
plot(f2,L42,'m','LineWidth',2)
plot(f2,L52,'y','LineWidth',2)
hold off
ylabel('L_s (dB)')
xlabel('Frequency (Hz)')
title('RANDI model')
box on, grid on
