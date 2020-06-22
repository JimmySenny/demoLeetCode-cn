include ../etc/Makefile

BIN_NAME = ds_tst

OBJ_LIB  = ${WORKDIR}/lib/libds_tst.a ${WORKDIR}/lib/libds_queue.a ${WORKDIR}/lib/libds_string.a ${WORKDIR}/lib/libds_array.a ${WORKDIR}/lib/libds_util.a ${WORKDIR}/lib/libds_comm.a

EXECOBJ  = ${WORKDIR}/bin/${BIN_NAME}.out

LINKRULE = ${CC} -o ${EXECOBJ} ${OBJ_LIB} -L${WORKDIR}/lib -lds_tst -lds_queue -lds_string -lds_array -lds_comm

TARGETS  = ${EXECOBJ}

all:${TARGETS}

${EXECOBJ}: ${OBJ_LIB}
	${LINKRULE}

clean:
	@- rm -f ${TARGETS} ${CLEANFILES}
