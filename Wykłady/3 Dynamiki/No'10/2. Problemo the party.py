class Employee():
    def __init__(self,fun):
        self.emp = []
        self.fun = fun
        self.f = -1
        self.g = -1

    def add_subordinate(self, subordinate):
        self.emp.append(subordinate)

def party_requrzjon(root):
    return f_function(root)


def f_function(v):

    if v.f >= 0:
        return v.f

    x = g_function(v)
    y = v.fun

    for u in v.emp:
        y += g_function(u)

    v.f = max(x,y)

    return v.f

def g_function(v):

    if v.g >= 0:
        return v.g

    v.g = 0

    for u in v.emp:
        v.g += f_function(u)

    return v.g






def print_tree(employee, level=0):
    indent = " " * (level * 4)
    num_subordinates = len(employee.emp)
    print(f"{indent}Employee with fun: {employee.fun}, Subordinates: {num_subordinates}")
    for sub in employee.emp:
        print_tree(sub, level + 1)


# Example usage:


def making_three():
    a = Employee(50)
    b = Employee(40)
    c = Employee(15)
    d = Employee(18)
    e = Employee(9)
    f = Employee(3)
    g = Employee(20)
    h = Employee(18)
    i = Employee(20)
    j = Employee(35)
    k = Employee(10)
    l = Employee(2)
    m = Employee(8)
    n = Employee(15)
    o = Employee(17)
    p = Employee(3)
    r = Employee(1)
    s = Employee(1)
    t = Employee(20)
    u = Employee(12)
    w = Employee(19)
    y = Employee(12)

    a.add_subordinate(b)
    a.add_subordinate(c)
    a.add_subordinate(d)
    b.add_subordinate(e)
    b.add_subordinate(f)
    b.add_subordinate(g)
    c.add_subordinate(h)
    d.add_subordinate(i)
    d.add_subordinate(j)
    e.add_subordinate(k)
    e.add_subordinate(l)
    f.add_subordinate(m)
    h.add_subordinate(n)
    h.add_subordinate(o)
    i.add_subordinate(p)
    j.add_subordinate(r)
    j.add_subordinate(s)
    m.add_subordinate(t)
    m.add_subordinate(u)
    p.add_subordinate(w)
    p.add_subordinate(y)

    return a

a = making_three()
# print_tree(a)

print(party_requrzjon(a))