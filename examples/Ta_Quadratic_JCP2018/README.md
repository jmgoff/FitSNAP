## FitSnap3 Tantalum quadratic example

This example will generate a potential for tantalum as published in 
Wood, M. A., & Thompson, A. P. (2018) J. Chem. Phys. 24 (2018) 241721.  This version 
of the tantalum potential uses the quadratic version of SNAP.

#### Running this example:

To run this example, use the following command in this directory:

mpirun -n 4 python3 -m fitsnap3 Ta-example.in

#### Files in this Directory

Ta-example.in 

Input file containing parameters to run FitSNAP and generate
the tantalum quadratic potential

JSON/

Directory that contains all the training configurations which are organized
into different groups.

#### Files generated by example:

Ta_pot.snapcoeff

SNAP potential coefficient file that contains all the beta coefficients for 
this potential.  This is one of two files needed to use this potential in LAMMPS

Ta_pot.snapparam

SNAP potential parameters file that contains the hyperparameters and options used during 
the fit for this potential.  This is one of two files needed to use this potential in LAMMPS

Ta_metrics.csv

Contains a variety of error metrics for all the training groups for this fit.

Note that the 20May21_Standard/ directory contains sample output for this example for comparison

#### Important input parameters for this example

rcutfac = 5.594 : Radial cutoff (hyperparameters) chosen for this potential (different from linear example)
wj1 = 1.0 : Elemental weight on tantalum for density expansion
radelem1 = 0.5 : Tantalum per-element cutoff 
type1 = Ta : Chemical symbol for element which should match training files in JSON
bzeroflag = 1 : Forces Bspec to 0 when atoms are non-interacting (different from linear example)
quadraticflag = 1 : Quadratic SNAP is turned on, using quadratic SNAP (different from linear example)

See docs/TEMPLATE.in for further information on input parameters

#### Tantalum data from:

The JSON configurations and hyperparameters used for this example are published in:

Wood, M. A., & Thompson, A. P. (2018). Extending the accuracy of
the SNAP interatomic potential form. The Journal of chemical
physics, 148(24), 241721. 


**Note to Developers: Make sure this example still reproduces the same results when modifying code**



