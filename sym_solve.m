clear all;
clc;

syms y1 y2 y3 y4 z1 z2 m M l g F f_theta b I
%{
% Self
eqns = [(M+m)*z1 + (b*y2) - (m*l*z2*cos(y3)) + (m*l*y4^2*sin(y3)) == F, ...
         m*l^2*z2 - (m*l*z1*cos(y3)) - (m*g*l*sin(y3)) == -f_theta*y4];
%}
%{
% CTMS equations
eqns = [(M+m)*z1 + (b*y2) + (m*l*z2*cos(y3)) - (m*l*y4^2*sin(y3)) == F,...
         (I+ m*l^2)*z2 + (m*g*l*sin(y3)) == -(m*l*z1*cos(y3))];
%}
% Online equations (corrected)
eqns = [(M+m)*z1 + (m*l*z2*cos(y3)) - (m*l*y4^2*sin(y3)) == F - (b*y2), ...
        m*l^2*z2 + (m*l*z1*cos(y3)) - (m*g*l*sin(y3)) == -f_theta*y4 ];
S = solve(eqns,z1,z2)     
S.z1
S.z2