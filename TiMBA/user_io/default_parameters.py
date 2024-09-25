default_year = 2020
default_max_period = 10
default_calc_product_price = "shadow_PP"  # possibilities: "shadow_PP", "calculated_PP" (Only shadow_PP were validated extensively)
default_calc_world_price = "shadow_WP"  # possbilities: "shadow_WP", "constant_WP", "average_WP, exogen_WP" (Only shadow_WP were validated extensively)

default_MB = "C_specific_MB"  # possibilities:"RC_specific_MB"(= region and commodity specific material balance),
#                                              "RCG_specific_MB"(= region and commodity group specific material balance)
#                                              "C_specific_MB"(= commodity specific material balance) (Only C_specific_MB were validated extensively)

default_transportation_impexp_factor = 1

serialization_flag = False  # if true read data from stored pkl files
constants = [False, False, False]  # [constant prices, constant slopes, constant intercep] (Only default options were validated extensively)
dynamization_activated = True
capped_prices = False # (Only default option was validated extensively)
cleaned_opt_quantity = False  # cleaned opt quantity have not been validated extensively
global_material_balance = False  # Results with global material balance activated have not been validated yet
verbose_optimization_logger = True
verbose_calculation_logger = False
read_additional_information_file = True
test_timba_results = True  # activate unittest to compare TiMBA results with validated results

user_input = {"year": default_year, "max_period": default_max_period, "product_price": default_calc_product_price,
              "world_price": default_calc_world_price, "transportation_factor": default_transportation_impexp_factor,
              "material_balance": default_MB, "serialization": serialization_flag, "constants": constants,
              "dynamization_activated": dynamization_activated, "capped_prices": capped_prices,
              "cleaned_opt_quantity": cleaned_opt_quantity, "global_material_balance": global_material_balance,
              "verbose_optimization_logger": verbose_optimization_logger,
              "verbose_calculation_logger": verbose_calculation_logger, "addInfo": read_additional_information_file,
              "test_timba_results": test_timba_results}
