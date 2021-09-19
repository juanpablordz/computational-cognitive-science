function number_game_plot_predictions(hypotheses, priors, data)
% hypotheses = a matrix whose columns are particular hypotheses,
% represented as logical vectors reflecting datapoint membership
%
% priors = a vector of prior probabilities for each hypothesis
%
% data = a vector of observed numbers

dims = size(hypotheses);
N = dims(1);
predictive = zeros(N,1);

logical_data = zeros(1,N);
for i=1:N,
  if (find(data==i))
    logical_data(i) = 1;
  end
end
logical_data = logical(logical_data);

%disp('LOGICAL DATA:');
%disp(logical_data');

dims = size(hypotheses);
hyps = dims(2);
posteriors = zeros(1,hyps);
% compute the posterior for every hypothesis
Z = 0;
for h=1:hyps,
  cur = hypotheses(:,h);
  log_joint = log(priors(h)) + ...
      number_game_likelihood(cur, logical_data);
  joint = exp(log_joint);
  Z = Z + joint;
  posteriors(h) = joint;
end

posteriors = posteriors / Z;

% compute the predictive contribution for each
% hypothesis and add it in to the predictive
for h=1:hyps,
  predictive = predictive + hypotheses(:,h) * posteriors(h);
end

% plot it as a bar chart, also plotting the top 6 hypotheses in
% decreasing order of posterior probability

figure;

subplot(6,1,1);

str = 'Predictions given observations';
for i=1:N,
  if (logical_data(i))
    str = strcat(str, sprintf(' %d', i));
  end
end
bar(predictive);
title(str);
axis tight;
  
[sorted_post post_indices] = sort(posteriors,2,'descend');

%disp('POSTERIORS:');
%disp(posteriors');

%disp('SORTED POST:');
%disp(sorted_post');
%
%disp('POST_INDICES:');
%disp(post_indices');

offset = 0;

human_data = load('number_game_data.mat');
found = logical(0);
idx = -1;
for i=1:8,
%  if (human_data.data{i,1} == data)
   if isempty(setdiff(human_data.data{i,1},data)) ...
       && isempty(setdiff(data,human_data.data{i,1}))
    found = logical(1);
    idx = i;
    break;
  end
end

if (found)
  offset = 1;
  
  %plot the human data
  subplot(4 + 1 + offset, 1, 2);
  bar(human_data.data{i,2}, human_data.data{i,3});
  title('Human predictive probabilities');
  axis([1 N 0 1]);
end

for i=1:4,
  hyp = post_indices(i);
%  disp(sprintf('TOP HYP %d IS %d\n', i, hyp));
  subplot(4 + 1 + offset,1,i+1+offset);
  bar(hypotheses(:,hyp));
  axis tight;
  if (i == 1)
    title(['Top 6 hypotheses, in descending order of posterior ' ...
           'probability']);
  end
  
end
