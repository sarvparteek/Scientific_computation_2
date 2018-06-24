close all;
clear all;
clc;

tf    = 5; % end time [s]
dt    = [1e-5 1e-4 1e-3 1e-2 1e-1 1]; % s
y0    = [1 0 0.01 0]; % Initial conditions
K     = [-35 -34 -150 -34]; % Gains for full-state feedback. Stabilizes
                            % all coordinates to zero
% K     = [0 -34 -150 -34]; % This stabilizes every coordinate but x to 0
% K     = [0  0  -150 -34]; % This stabilizes every coordinate but x,xdot to 0

for i = 1:length(dt)
    tspan = 0:dt(i):tf;
    for j = 1:4
        solveOde(j,i*10+j,tspan,dt(i),y0,K);
    end
end

