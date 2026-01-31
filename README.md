# An Implementation of the Reduction Model for Dimensions and Incomplete Facts

This repository contains an implementation of the Reduction Model for dimensions and incomplete facts. The implementation utilises answer set programming (ASP) and uses as
its backend the state-of-the-art solver [clingo](https://potassco.org/clingo/).
This repository is an addition to the paper written on the same matter.

## Implementation Details

- `asp/` contains the two ASP computing steps.
    1. `step1.lp` contains the code for generating a single interpretation.
    2. `step2.lp` contains the code for inferring constraint from the case base and the known supporting thresholds.
- `solve.py` glues together the two computing steps. First, the intersection of all answer sets of `step1.lp` together with the input is computed using the clingo CLI flag `--enum-mode=cautious` to infer the supporting thresholds. The output of the intersection is then passed to `step2.lp` where constraint is inferred.
- `examples/` contains examples that can be passed to the program as input.

## Installation

This project requires [Python 3.13](https://www.python.org/downloads/) or newer to be installed.
To install the dependencies, including the Python module for clingo, run:

```bash
> pip install -r requirements.txt
```

## Execution

To execute the program, pass .lp input files via the command line.
The program will then output whether constraint applies:

```
> python solve.py example/example1.lp
constraint(cf, defendant)
```

### CLI options

Further options, such as `-s` and `-p`, can be specified to add further information to the output of the program.

```
> python solve.py --help
usage: solve.py [-h] [-s] [-p] inputfile [inputfile ...]

An implementation of the Reduction Model for dimensions and incomplete facts

positional arguments:
  inputfile             an input file in .lp format containing dimensions, cases, and a focus case

options:
  -h, --help            show this help message and exit
  -s, --show-supports   show the minimal supporting thresholds for dimensions
  -p, --show-precedent  show the precedent cases in the output
```
