# EXES AND SCRIPTS
BINDIR=../../bin/
PW_EXE=${BINDIR}/pw.x
PP_EXE=${BINDIR}/pp.x
CUP_EXE=${BINDIR}epcdft_coupling.x
NP:=$(shell grep -c ^processor /proc/cpuinfo)
PW_CMD=export OMP_NUM_THREADS=1; export MKL_NUM_THREADS=1; mpirun -np $(NP) $(PW_EXE)
PP_CMD=export OMP_NUM_THREADS=1; export MKL_NUM_THREADS=1; mpirun -np $(NP) $(PP_EXE)

all: scf.out pp.out
clean: 
	rm -rf out *.out coupling.in *t_sdd.* *.cube txt *.sdd

# the meat
scf.out: scf.in
	$(PW_CMD) -in $^ > $@

pp.out: pp.in
	$(PP_CMD) -in $^ > $@

