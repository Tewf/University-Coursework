from car_seq_instance import CarSeqInstance
from car_seq_solver import CarSeqSolver

def solve_instance(file_path: str, element_model: bool) -> None:
    data = CarSeqInstance(file_path)
    solver = CarSeqSolver(data, element_model=element_model)
    sol = solver.solve(time_limit_s=30)
    status = solver.isSat

    if sol is not None:
        check = data.checker(sol)
        if check != "Ok":
            raise RuntimeError(f"Checker failed: {check}")
    print(f"{data.getName()} | {solver.get_name()} | "
          f"{'SAT' if status else 'UNSAT'} | "
          f"fails={solver.nbFail} | time={solver.cpu_in_s:.4f}s")


if __name__ == "__main__":
    files = [
        "./lib/car_sequencing/ford10_3_4.car",
        #"./lib/car_sequencing/ford10_6_5.car",
        #"./lib/car_sequencing/ford17_7_5.car",
        #"./lib/car_sequencing/ford25_5_5.car",
        #"./lib/car_sequencing/ford25_10_5.car",
        #"./lib/car_sequencing/ford33_7_5.car",
        #"./lib/car_sequencing/ford100_19_5.car",
    ]

    for f in files:
        # M1 : reified IfThen
        solve_instance(f, element_model=False)
        # M2 : Element
        #solve_instance(f, element_model=True)