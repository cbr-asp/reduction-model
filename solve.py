from os import path
from argparse import ArgumentParser
from clingo import Control, Model

def solve(asp_dir: str, input_files: str, show_supports: bool, show_precedents: bool):
    ctl1 = Control(["--enum-mode=cautious"])
    ctl1.load(f"{asp_dir}/step1.lp")

    for file in input_files:
        ctl1.load(file)

    ctl1.ground([("base", [])])

    cautious_atoms = []

    def on_model_step1(model: Model):
        nonlocal cautious_atoms
        cautious_atoms = model.symbols(shown=True)

    ctl1.solve(on_model=on_model_step1)

    show = ["constraint/2"]

    if show_supports:
        show.append("min_supports/3")
    if show_precedents:
        show.append("precedent/3")

    ctl2 = Control(["--project", "--show", ",".join(show), "--warn=no-atom-undefined"])
    ctl2.load(f"{asp_dir}/step2.lp")

    with ctl2.backend() as backend:
        for atom in cautious_atoms:
            atom_id = backend.add_atom(atom)
            backend.add_rule([atom_id])

    ctl2.ground([("base", [])])
    ctl2.solve(on_model=lambda m: print(m))

if __name__ == "__main__":
    parser = ArgumentParser(
        prog="solve.py",
        description="An implementation of the Reduction Model for incomplete and multi-precedent cases")

    parser.add_argument("-s", "--show-supports", action="store_true", help="show the minimal supporting thresholds for dimensions")
    parser.add_argument("-p", "--show-precedent", action="store_true", help="show the precedent cases in the output")
    parser.add_argument("inputfile", nargs="+", help="an input file in .lp format containing dimensions, cases, and a focus case")

    args = parser.parse_args()

    solve(f"{path.dirname(__file__)}/asp", args.inputfile, args.show_supports, args.show_precedent)
