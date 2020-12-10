include ../etc/Makefile

BIN_NAME = ds_tst

OBJ_LIB  = ${WORKDIR}/lib/libds_tst.a ${WORKDIR}/lib/libds_stack.a ${WORKDIR}/lib/libds_queue.a ${WORKDIR}/lib/libds_dpointer.a ${WORKDIR}/lib/libds_string.a ${WORKDIR}/lib/libds_array.a ${LUTILDIR}/lib/liblutil.a

EXECOBJ  = ${WORKDIR}/bin/${BIN_NAME}.out

LINKRULE = ${CC} -o ${EXECOBJ} ${OBJ_LIB} -L${WORKDIR}/lib -lds_tst -lds_stack -lds_queue -lds_dpointer -lds_string -lds_array -L${LUTILDIR}/lib -llutil

TARGETS  = ${EXECOBJ}

all:${TARGETS}

${EXECOBJ}: ${OBJ_LIB}
	${LINKRULE}

clean:
	@- rm -f ${TARGETS} ${CLEANFILES}
