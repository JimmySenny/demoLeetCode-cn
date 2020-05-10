include ../etc/Makefile

BIN_NAME = alg_tst

OBJ_LIB  = ${WORKDIR}/lib/libalg_tst.a ${WORKDIR}/lib/libalg_array.a ${WORKDIR}/lib/libalg_comm.a

EXECOBJ  = ${WORKDIR}/bin/${BIN_NAME}.out

LINKRULE = ${CC} -o ${EXECOBJ} ${OBJ_LIB} -L${WORKDIR}/lib -lalg_tst -lalg_array -lalg_comm

TARGETS  = ${EXECOBJ}

all:${TARGETS}

${EXECOBJ}: ${OBJ_LIB}
	${LINKRULE}

clean:
	@- rm -f ${TARGETS} ${CLEANFILES}
