function [hypotheses, priors] = ...
  number_game_simple_init(N, interval_prior, math_prior)

if (abs( (interval_prior + math_prior) - 1) > 0.05)
  error('Sum of interval prior and math prior should be 1!');
end

h = 1;

vals = 1:N;

% put in all intervals of small and medium length
for step=1:20,
%  for start=1:step:(N-step) % this is not right!
  for start=1:(N-step)
     hypotheses(:,h) = (vals >= start) & (vals <= (start + step));
    h = h + 1;
  end
end

last_interval = h-1;
priors(1:last_interval) = interval_prior / last_interval;

% put in odds
hypotheses(:,h) = mod(vals, 2) == 1;
h = h+1;
% put in multiples of 2 through 10
for base=2:10
  hypotheses(:,h) = mod(vals,base) == 0;
  h = h + 1;
end

last_hyp = h - 1;
num_math = last_hyp - last_interval;
priors((last_interval+1):last_hyp) = math_prior / num_math;
