# Sample Code for accessing modules and package

# Difference Import Types
import w_module
from w_package import module
from w_module import func
from w_package.module import func as package_func


# Consume the functions on imported modules
w_module.func()
module.func()
func()
package_func()

