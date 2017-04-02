from sympy import *
from sympy.matrices import *


def diagonalElementsInLatex(level):
    def sharelatex(y):
        y = y.replace('\\left(', '(')
        y = y.replace('\\right)', ')')
        return y

    m = print_density_matrix(level)
    for i in xrange(4):
        print sharelatex(latex(m[i, i]))
        print
        print


def get_resource_parameters(level=None):
    if level is not None:
        return symbols('p%s l%s L%s P%s' % tuple([level + 1] * 4), real=True)
    return symbols('p l L P', real=True)

def get_basis_parameters(level=None):
    if level is not None:
        return symbols('q%s Q%s' % tuple([level + 1] * 2), real=True)
    return symbols('q Q', real=True)

def get_initial_secret_parameters():
    return symbols('a b', real=True)

def subsitute2(expr):
    p, l, L, P = get_resource_parameters()
    q, Q = get_basis_parameters()
    change = [l, a, p, q, b]
    for sym in change:
        expr = expr.subs(sym*conjugate(sym), Abs(sym)**2)
    return expr

def subsitute(coeff_comm):
    p, l, L, P = get_resource_parameters()
    q, Q = get_basis_parameters()
    coeff_comm = coeff_comm.subs(L, 1/(1+Abs(l)**2)**0.5).subs(P, 1/(1+Abs(p)**2)**0.5).subs(Q, 1/(1+Abs(q)**2)**0.5)
    return coeff_comm

def simplify_density_matrix(density_matrix):
    for row in xrange(4):
        for col in xrange(4):
            density_matrix[row, col] = subsitute2(combsimp(density_matrix[row, col]))
    return density_matrix