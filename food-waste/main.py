import independents
import dependents
import matplotlib.pyplot as plt

x = independents.food_spending_ratios
y = dependents.food_waste_discharge_quantities

plt.figure(layout="tight")
plt.scatter(x, y)
plt.xlim(left=7.777777)
plt.ylim(bottom=40000.0)
plt.xlabel("food spending ratio")
plt.ylabel("annual discharge qty. per unit")

plt.show()
