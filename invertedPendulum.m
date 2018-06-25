function dydt = invertedPendulum(t,y,K)
M       = 2;   % kg
m       = 0.1; % kg
l       = 0.5; % m
g       = 9.8; % m/s^2
f_theta = 0.005; % N-m.s/rad 
b       = 0;   % N-s/m

% Apply full-state feedback
u       = -K*y;
dydt    = zeros(4,1);
% F       = u;
% F       = exp(-5 *t);
F       = 1;

% Equations obtained by running sym_solve.m
dydt(1) = y(2);
dydt(2) = (F*l + f_theta*y(4)*cos(y(3)) - b*l*y(2) + l^2*m*y(4)^2*sin(y(3))...
           - g*l*m*cos(y(3))*sin(y(3)))/(l*(M + m - m*cos(y(3))^2));
dydt(3) = y(4);
dydt(4) = -(M*f_theta*y(4) + f_theta*m*y(4) + F*l*m*cos(y(3)) - g*l*m^2*sin(y(3)) ...
          + l^2*m^2*y(4)^2*cos(y(3))*sin(y(3)) - M*g*l*m*sin(y(3)) ...
          - b*l*m*y(2)*cos(y(3)))/(l^2*m*(M + m - m*cos(y(3))^2));

end
