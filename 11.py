#Lun Jiahao 2019.4.1
#Parentheses Matcher. When compilers and interpreters report syntax errors
# in programs, one of the errors they look for is mismatched parentheses ().
# Create a function matcher that takes a string expression as a parameter and
# returns whether the opening & closing parentheses match by using a stack.
# The matcher will return true if all the nested parentheses ()  are matched,
# and false otherwise.

def matcher(str):
    stack = []
    for i in str:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

print(matcher("(45 + 36) - 5"))
print(matcher("( ( a )"))
print(matcher("map(ke(a(4)))(b((v)))"))
print(matcher("(a)b)"))
#Shopping cart. Imagine you are writing software for a shopping cart using a
# queue. Your shopping cart should implement an add function that adds an
# item and a quantity and adds that many items to the end or tail of the queue,
# and a print function that displays the items in the order they were added.


def add_shoppingCart(item, quantity, cart):
    for i in range(quantity):
        cart.append(item)
def print_showpingCartprint(cart):
    print(cart)
cart = []
add_shoppingCart("chocolate", 3, cart)
add_shoppingCart("sandwich", 1, cart)
print_showpingCartprint(cart)
add_shoppingCart("eggs", 5, cart)
print_showpingCartprint(cart)

class shoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item, number):
        for i in range(number):
            self.items.insert(0, item)

    def print(self):
        order = []
        for i in self.items:
            order.insert(0, i)
        print(order)

cart2=shoppingCart()
cart2.add("choclolate", 3)
cart2.print()
cart2.add("sandwich", 1)
cart2.print()
cart2.add("eggs", 5)
cart2.print()