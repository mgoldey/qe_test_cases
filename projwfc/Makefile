# EXES AND SCRIPTS
BINDIR=../../bin/
PW_EXE=${BINDIR}/pw.x
PP_EXE=${BINDIR}/projwfc.x
NP:=$(shell grep -c ^processor /proc/cpuinfo)
PW_CMD=export OMP_NUM_THREADS=1; export MKL_NUM_THREADS=1; mpirun -np $(NP) $(PW_EXE)
PP_CMD=export OMP_NUM_THREADS=1; export MKL_NUM_THREADS=1; mpirun -np $(NP) $(PP_EXE)

all: scf.out pdos.out
clean: 
	rm -rf out *.out coupling.in *t_sdd.* *.cube txt *.sdd

# the meat
scf.out: scf.in
	$(PW_CMD) -in $^ > $@

pdos.out: pdos.in
	$(PP_CMD) -in $^ > $@

