clear all;
clc;

syms y1 y2 y3 y4 z1 z2 m M l g F f_theta b I
eqns = [(M+m)*z1 + (m*l*z2*cos(y3)) - (m*l*y4^2*sin(y3)) == F - (b*y2), ...
        m*l^2*z2 + (m*l*z1*cos(y3)) - (m*g*l*sin(y3)) == -f_theta*y4 ];
S = solve(eqns,z1,z2);
simplify(S.z1)
simplify(S.z2)