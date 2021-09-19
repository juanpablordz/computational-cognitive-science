import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm



def opt_build_powerlaw_joint(tobs):
	"""
		returns an (anonymous) procedure of one argument - ttotal - that
		computes the joint density evaluated on that argument and tobs.

		TODO: construct and return anonymous procedure
	"""

	# [...]

	return joint



def opt_build_lifespan_joint(tobs):
	"""
		TODO: model after build_powerlaw_joint
	"""

	# [...]

	return joint



def opt_compute_posterior(joint, theta_min, theta_max, num_steps):
	"""
		Computes a table representation of the posterior distribution
		with at most num_steps joint density evaluations, covering the
		range from theta_min to theta_max.

		People interested in fancier integrators should feel free to
		modify the signature for this procedure, as well as its callers,
		as appropriate.

		TODO: compute Z along with an unnormalized table

		TODO: normalize joint

	"""

	# [...]

	return thetavals, postvals
