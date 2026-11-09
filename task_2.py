import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


def f(x):
    return x**2


def monte_carlo_integral(
    f, a: float, b: float, num_experiments: int = 100000
    ) -> float:

    y_max = f(b)

    x_rand = np.random.uniform(a, b, num_experiments)
    y_rand = np.random.uniform(0, y_max, num_experiments)

    under_curve = y_rand <= f(x_rand)

    box_area = (b - a) * y_max
    integral_mc = box_area * (np.sum(under_curve) / num_experiments)

    return integral_mc


if __name__ == "__main__":
    a = 0
    b = 2
    N = 500_000

    mc_result = monte_carlo_integral(f, a, b, num_experiments=N)

    quad_result, quad_error = spi.quad(f, a, b)

    print(f"Результат Монте-Карло (N={N}): {mc_result:.6f}")
    print(f"Результат scipy.quad:              {quad_result:.6f}")
    print(f"Абсолютна похибка:                {abs(mc_result - quad_result):.6f}")

    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)
    fig, ax = plt.subplots()

    ax.plot(x, y, "r", linewidth=2)

    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
 
    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title(f"Графік інтегрування f(x) = x^2 від {a} до {b}")
    plt.grid()
    plt.show()