from steel_instance import SteelInstance
from steel_prod_solver_m2 import SteelProdSlvM2


def solve(file: str) -> None:
    data = SteelInstance(file)
    print(data.getName(), end="")
    solve_instance(data)
    print()


def solve_instance(data: SteelInstance) -> None:
    slv = SteelProdSlvM2(data)
    slv.makeTimeLimit("5s")
    slv.solve()
    print(f" & {slv.getBestSolValue()} & {slv.getCpu_in_s():.1f}", end="")


def main() -> None:
    solve("./lib/steel_production/steel10_7_3.mill")
    solve("./lib/steel_production/steelA.mill")
    solve("./lib/steel_production/steelB.mill")
    solve("./lib/steel_production/steelC.mill")
    solve("./lib/steel_production/steel111_3_88.mill")
    solve("./lib/steel_production/steel111_6_88.mill")
    solve("./lib/steel_production/steel111_11_88.mill")
    solve("./lib/steel_production/steel111_13_88.mill")
    solve("./lib/steel_production/steel111_21_88.mill")


if __name__ == "__main__":
    main()