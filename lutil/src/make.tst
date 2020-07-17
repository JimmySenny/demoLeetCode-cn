include ../etc/Makefile

BIN_NAME = lutil_tst

OBJ_LIB  = ${WORKDIR}/lib/liblutil_tst.a ${WORKDIR}/lib/liblutil.a

EXECOBJ  = ${WORKDIR}/bin/${BIN_NAME}.out

LINKRULE = ${CC} -o ${EXECOBJ} ${OBJ_LIB} -L${WORKDIR}/lib -llutil_tst -llutil

TARGETS  = ${EXECOBJ}

all:${TARGETS}

${EXECOBJ}: ${OBJ_LIB}
	${LINKRULE}

clean:
	@- rm -f ${TARGETS} ${CLEANFILES}
