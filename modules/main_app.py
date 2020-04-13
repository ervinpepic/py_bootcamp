# so here, from the another file we import the class or fucntions that we need...
# this file is main module, because here is when program do the stuff...

# this is one way of importing modules...
from modules.shopping.sales import calc_shipping, cacl_tax

# this is another way if importing modules, both of this importing are the same...no
import modules.shopping.sales as sale
# difference in speed or something like that...this is so caled object importing

sale.calc_shipping()  # we call funciton like this when we use object importing
sale.cacl_tax()  # we call funciton like this when we use object importing

calc_shipping()  # when we use module import, we call function like this
cacl_tax()  # when we use module import, we call function like this

