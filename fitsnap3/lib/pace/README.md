# analytical_ACE

### ACE descriptors and ML-PACE compatible .ace files

This library wraps functions and classes in FitSNAP that allow one to generate descriptor labels and couplings for ACE models. The descriptor labels (nu vectors), for single element systems are characterized by certain combinations of n and l quantum numbers. For an arbitrary descriptor rank, r, all descriptor labels are generated up to a user-specified n_max and l_max.

For any set of descriptor labels, the pace library will generate a coupling_coefficients.ace file that contains all the generalized Wigner-3j symbols needed to construct the ACE invariants (or ctilde functions in ML-PACE). These coupling coefficients are generated analytically for descriptor reproducability between machines. The coupling coefficient file is read in while using the LAMMPS compute style "pace" to evaluate ACE energy and force derivatives for fitting. The coupling coefficients are stored for reversible conversion between ctilde and c formats. (See Lysogorskiy et al. https://doi.org/10.1038/s41524-021-00559-9). 

The construction of ACE descriptor labels and generalized coupling coefficients are handled completely within FitSNAP. For more detailed discussion on the usage of ACE model training in FitSNAP, please see the README.md in the FitSNAP/examples/Ta_pace folder.

### Future updates

The library will interface with the ML-PACE yaml style format for multielement systems (.yace). Additional functionality will be added so that an analytical set of generalized Clebsch-Gordan coefficients may be used in place of the generalized Wigner-3j symbols to define ACE invariants.
