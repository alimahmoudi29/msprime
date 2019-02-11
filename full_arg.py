# how to use the last version of a github module
# fist fork
# then git clone
# then git submodule init
# git submodule update
# make

from algorithms import *

ts_arg= msprime.simulate(sample_size=4, Ne=5000, length=1e4,mutation_rate=1e-8,
                              recombination_rate= 1e-8,random_seed=2, record_full_arg=True)
ts_noarg= msprime.simulate(sample_size=4, Ne=5000, length=1e4,mutation_rate=1e-8,
                              recombination_rate= 1e-8,random_seed=2, record_full_arg=False)
print(ts_arg.dump_tables())
print("-"*50)
print(ts_noarg.dump_tables())
def draw_trees(ts):
    trees = [tree.draw(format="unicode").splitlines() for tree in ts.trees()]
    max_height = max(len(tree) for tree in trees)
    for j in range(max_height):
        line = ""
        for tree in trees:
            k = j - max_height + len(tree)
            if k < 0:
                line += " " * len(tree[0])
            else:
                line += tree[k]
            line += " | "
        print(line)
# ts_arg = msprime.load("arg.trees")
# ts_noarg = msprime.load("noarg.trees")
ts_arg = ts_arg.simplify()
ts_noarg = ts_noarg.simplify()
# draw_trees(ts_noarg)
draw_trees(ts_arg)
draw_trees(ts_noarg)

def full_arg_example():
    ts = msprime.simulate(
        sample_size=6, recombination_rate=0.4, record_full_arg=True, random_seed=42)
    print(ts.tables.nodes)
    print(ts.tables.edges)
    print()
    for tree in ts.trees():
        print("interval:", tree.interval)
        print(tree.draw(format="unicode"))

full_arg_example()
