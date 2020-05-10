include ../../etc/Makefile

MODULE_NAME = alg_tst
MODULE_OBJ  = alg_tst.o \
			        tst_array.o

MODULE_LIB  = ${WORKDIR}/lib/lib${MODULE_NAME}.a

TARGETS     = ${MODULE_LIB}

all:${TARGETS}

${MODULE_LIB}: ${MODULE_OBJ}
	${AR} ${AROPT} $@ ${MODULE_OBJ}
	${RANLIB} $@
# $@ 表示规则中的目标文件集。在模式规则中，如果有多个目标，那么，"$@"就是匹配于目标中模式定义的集合。

clean:
	@- rm -f ${TARGETS} ${CLEANFILES}
