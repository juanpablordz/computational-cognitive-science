import numpy as np
import matplotlib.pyplot as plt



def number_game_simple_init(N, interval_prior, math_prior):

	if abs((interval_prior + math_prior) - 1) > 0.05:
	  raise ValueError('Sum of interval prior and math prior should be 1!')

	# generate interval concepts of small and medium length
	hypotheses = np.zeros((0, N))
	vals = np.arange(N) + 1

	for size in np.arange(0, 20):
		for start in np.arange(N-size):
			end = start + size
			interval = np.zeros(N)
			interval[start:end+1] = 1
			hypotheses = np.vstack([hypotheses, interval])

	last_interval_concept = hypotheses.shape[0]

	#put in odds
	concept = np.equal(np.mod(vals, 2), 1).astype(int)
	hypotheses = np.vstack([hypotheses, concept])

	#put in multiples of 2 to 10
	for base in np.arange(2,11):
		concept = np.equal(np.mod(vals, base), 0).astype(int)
		hypotheses = np.vstack([hypotheses, concept])

	last_hypothesis = hypotheses.shape[0]

	#compute prior probabilities
	priors = np.empty(last_hypothesis)
	priors[:last_interval_concept] = interval_prior/last_interval_concept
	priors[last_interval_concept:] = math_prior/(last_hypothesis-last_interval_concept)

	return hypotheses, priors



def number_game_likelihood(hypothesis, data):
	"""
		hypothesis is a logical (0 or 1) vector on N elements, where
		hypothesis[i] = 1 iff i is contained in the extension of the
		concept represented by hypothesis.

		data is, similarly, a logical vector where data[i] = 1 iff
		i is contained in the observed dataset.

		note that length(hypothesis) == length(data) unless the caller
		of this procedure messed up

		TODO: first check if data is consistent with the given hypothesis.

		if it isn't, P(D|H) = 0.

		TODO: under strong sampling WITH REPLACEMENT, every consistent hypothesis
		assigns probability 1/(#options) to each data draw.
	"""

	#[...]

	return log_likelihood



def number_game_plot_predictions(hypotheses, priors, data):
	"""
		hypotheses = a matrix whose columns are particular hypotheses,
		represented as logical vectors reflecting datapoint membership

		priors = a vector of prior probabilities for each hypothesis

		data = a vector of observed numbers
	"""

	def numbers_to_logical(data):
		if np.isscalar(data): data = [data]
		logical_data = np.zeros(N)
		for datum in data:
			logical_data[datum-1] = 1
		return logical_data

	hyps, N = hypotheses.shape
	logical_data = numbers_to_logical(data)

	# compute the posterior for every hypothesis
	posteriors = np.zeros(hyps)

	for h in np.arange(hyps):
		log_joint = np.log(priors[h]) + number_game_likelihood(hypotheses[h,:], logical_data)
		joint = np.exp(log_joint)
		posteriors[h] = joint

	posteriors /= np.sum(posteriors)

	# compute the predictive contribution for each
	# hypothesis and add it in to the predictive

	predictive = np.dot(posteriors, hypotheses)

	# plot it as a bar chart, also plot human data (if available)
	# and the top 6 hypotheses in decreasing order of posterior
	# probability

	fig, ax = plt.subplots(6,1, figsize=(7, 7))
	fig.subplots_adjust(top=0.95, bottom=0.05, hspace=0.85,
		left=0.05, right=0.95)


	ax[0].bar(np.arange(N)+1.0, predictive, 0.5, color='k')
	if np.isscalar(data): data = [data]
	ax[0].set_title('Predictions given observation(s) %s'
		% ', '.join(str(d) for d in data))
	ax[0].set_xlim([-0.5, (N+1)+0.5])
	ax[0].set_ylim([-0.05, 1.05])


	datasets = ['16', '60', '[16,8,2,64]', '[60,52,57,55]', '[25,4,36,81]', '[23,16,19,20]', '[80,10,60,30]', '[98,81,86,93]']

	datasets_logical_representation = np.array([numbers_to_logical(eval(d)) for d in datasets])

	human_data = np.zeros((0, N))
	for i in np.arange(len(datasets)):
		numbers, judgments = np.genfromtxt('../data/csv/' + datasets[i] + '.csv', delimiter=',').T

		probabilities = np.zeros(N)
		for i in np.arange(numbers.size):
			probabilities[int(numbers[i])-1] = judgments[i]
		human_data = np.vstack([human_data, probabilities])

	found = False
	idx = 0
	for i, dataset  in enumerate(datasets_logical_representation):
		if np.array_equal(logical_data, dataset):
			idx = i
			found = True

	if found:
		# plot the human data
		ax[1].bar(np.arange(N)+1.0, human_data[idx], 0.5, color='k')
		ax[1].set_title('Human predictive probabilities')
		ax[1].set_xlim([-0.5, (N+1)+0.5])
		ax[1].set_ylim([-0.05, 1.05])
	else:
		ax[1].set_visible(False)

	sort_indices = np.argsort(posteriors)[::-1]

	topN = 4
	for i in np.arange(2, 6):
		hypo_index = sort_indices[(i-2)]
		ax[i].bar(np.arange(N)+1.0, hypotheses[hypo_index,:], 0.5, color='k')
		ax[i].set_xlim([-0.5, (N+1)+0.5])
		ax[i].set_ylim([-0.05, 1.05])

		# only consider hypotheses with probability greater 0
		if posteriors[hypo_index] == 0.0:
			ax[i].set_visible(False)
			topN -= 1
	ax[2].set_title('Top %u hypotheses in descending order of posterior probability' % topN)
	plt.show()

