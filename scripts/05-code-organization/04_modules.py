# Sample Code for accessing modules and package

# Difference Import Types
from package import module
from package import func as init_func
from package.module import func as package_func
import module
from module import func

# Consume the functions on imported modules
module.func()
init_func()
package_func()
module.func()
func()
