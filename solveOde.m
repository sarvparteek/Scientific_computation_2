function [] = solveOde(solver, fig_handle, tspan, dt, y0,K)
if (solver == 1)
    [t,y] = ode45(@(t,y)invertedPendulum(t,y,K),tspan,y0);
                                   % Medium accuracy, for non-stiff systems
    solver_str = 'ode45';                               
elseif (solver == 2)
    [t,y] = ode23(@(t,y)invertedPendulum(t,y,K),tspan,y0);
                                      % Low accuracy, for non-stiff systems
    solver_str = 'ode23';
elseif (solver == 3)
    [t,y] = ode113(@(t,y)invertedPendulum(t,y,K),tspan,y0); 
                                 % Low-High accuracy, for non-stiff systems                                      
    solver_str = 'ode113'; 
elseif (solver == 4)
    [t,y] = ode15s(@(t,y)invertedPendulum(t,y,K),tspan,y0); 
                                  % Low-Medium accuracy, for stiff systems
    solver_str = 'ode15s'; 
end
 
figure(fig_handle)
subplot(2,2,1)
plot(t,y(:,1))
title(['x :' solver_str ',dt=' num2str(dt,6)])
axis([0 5 1 7])
grid on;

subplot(2,2,2)
plot(t,y(:,2))
title(['x dot:' solver_str ',dt=' num2str(dt,6)])
axis([0 5 0 2.5])
grid on;

subplot(2,2,3)
plot(t,y(:,3))
title(['\theta :' solver_str ',dt=' num2str(dt,6)])
grid on;

subplot(2,2,4)
plot(t,y(:,4))
title(['\theta dot :' solver_str ',dt=' num2str(dt,6)])
grid on;
   
saveas(fig_handle,[num2str(fig_handle) '.jpg'])
end