# 1- Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi, а вычислить, 
# используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.

# Пример:

# - при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1

n = 1
number_pi = 0
while n < 1000000:
    element_pi = ((1/n) - (1/(n+2))) * 4
    number_pi = number_pi + element_pi
    n = n + 4
print(number_pi)


def accuracy_pi(d: str):
    str_sp = d.split('.')
    str_spfin = len(str_sp[-1])
    return str_spfin


print(round(number_pi, accuracy_pi('0.01')))