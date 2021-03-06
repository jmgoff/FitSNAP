from .solver import Solver
from ..parallel_tools import pt
from ..io.input import config
from sklearn.linear_model import ARDRegression
import numpy as np


class ARD(Solver):

    def __init__(self, name):
        super().__init__(name)

    @pt.sub_rank_zero
    def perform_fit(self):
        if pt.shared_arrays['configs_per_group'].testing_elements != 0:
            testing = -1*pt.shared_arrays['configs_per_group'].testing_elements
        else:
            testing = len(pt.shared_arrays['w'].array)
        w = pt.shared_arrays['w'].array[:testing]
        aw, bw = w[:, np.newaxis] * pt.shared_arrays['a'].array[:testing], w * pt.shared_arrays['b'].array[:testing]
        if config.sections['EXTRAS'].apply_transpose:
            bw = aw.T@bw
            aw = aw.T@aw
        alval_small = config.sections['SOLVER'].alphasmall
        alval_big = config.sections['SOLVER'].alphabig
        lmbval_small = config.sections['SOLVER'].lambdasmall
        lmbval_big = config.sections['SOLVER'].lambdabig
        thresh = config.sections['SOLVER'].threshold_lambda
        reg = ARDRegression(n_iter=300, tol=0.001, threshold_lambda=thresh, alpha_1=alval_big, alpha_2=alval_big, lambda_1=lmbval_small, lambda_2=lmbval_small,fit_intercept=False)
        reg.fit(aw,bw)
        self.fit = reg.coef_
        residues = reg.predict(aw) - bw

    def _dump_a(self):
        np.savez_compressed('a.npz', a=pt.shared_arrays['a'].array)

    def _dump_x(self):
        np.savez_compressed('x.npz', x=self.fit)

    def _dump_b(self):
        b = pt.shared_arrays['a'].array @ self.fit
        np.savez_compressed('b.npz', b=b)

