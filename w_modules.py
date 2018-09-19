# Sample Code for accessing modules and package

# Difference Import Types
from w_package import module
from w_package import func as init_func
from w_package.module import func as package_func
import w_module
from w_module import func

# Consume the functions on imported modules
module.func()
init_func()
package_func()
w_module.func()
func()


