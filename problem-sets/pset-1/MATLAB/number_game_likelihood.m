function log_likelihood = number_game_likelihood(hypothesis, data)
% hypothesis is a logical (0 or 1) vector on N elements, where
% hypothesis(i) = 1 iff i is contained in the extension of the
% concept represented by hypothesis.
%
% data is, similarly, a logical vector where data(i) = 1 iff
% i is contained in the observed dataset.
%
% note that length(hypothesis) == length(data) unless the caller
% of this procedure messed up.

% TODO: first check if data is consistent with the given hypothesis.
% if it isn't, P(D|H) = 0.

% TODO: under strong sampling WITH REPLACEMENT, every consistent hypothesis
% assigns probability 1/(#options) to each data draw.
