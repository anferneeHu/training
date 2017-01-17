# This is the entry for predict_st.


CODE=$(code)

base: GET_BASE

hist: GET_HIST

cst: GET_CST

all:
	@echo "This is the all TODO"

clean:
	@echo "clean the local cache..."
	rm -f res/*.csv
	@echo "clean done."


GET_BASE:
	@echo "get base st info..."
	python entry.py base
	@echo "base st got end."


GET_HIST:
	@echo "get hist st datas..."
	python entry.py hist $(CODE)
	@echo "got hist data end."

GET_CST:
	@echo "test get one st..."
	python entry.py cst $(CODE)
	@echo "got end."
