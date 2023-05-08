
all: ext
	@echo "done!"

ext: generate
	@echo "---------------- START RESULTS -----------------"
	@python3 xt_area_new.py
	@python3 xt_max_del.py
	@python3 xt_power.py
	@echo "---------------- END RESULTS -----------------"

generate: 
	vivado -mode tcl -source script.tcl
	mv vivado*.log vivado*.jou work_dir/

	

clean:
	rm -rf work_dir/
