function [thetavals postvals] = ...
  opt_compute_posterior(joint, theta_min, theta_max, num_steps)
% Computes a table representation of the posterior distribution
% with at most num_steps joint density evaluations, covering the
% range from theta_min to theta_max.
%
% People interested in fancier integrators should feel free to
% modify the signature for this procedure, as well as its callers,
% as appropriate.

%TODO: compute Z along with an unnormalized table

%TODO: normalize joint
