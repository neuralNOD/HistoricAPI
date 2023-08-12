# -*- encoding: utf-8 -*-

# test model should always be isolated from main environment
# hence both `app` and `api` model is redefined in the test directory
# ADVANTAGES :
#   - considering `test-db` from `onfig.py` the database can be deleted/recreated as per will
#   - after each test, `tearDown()` should be called - thus any uniqueness is preserved everytime
#   - only the required controller can be redefined here for testing
# DISADVANTAGE :
#   - `api.add_resource()` has to be defined twice (from `manage.py` and during test-environment)
