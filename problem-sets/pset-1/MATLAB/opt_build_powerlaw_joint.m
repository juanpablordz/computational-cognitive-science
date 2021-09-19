function joint = build_powerlaw_joint(tobs)
% returns an (anonymous) procedure of one argument - ttotal - that
% computes the joint density evaluated on that argument and tobs.
%
% uses step to get around the MATLAB limitation on 'if' - that is,
% to produce a powerlaw but truncated to 0 when ttotal is less than
% tobs.

% TODO: construct and return anonymous procedure
