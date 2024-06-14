import argparse
import coloredlogs
import logging

LOGGING_LEVEL = "INFO"
LOGGING_FMT = "%(asctime)s %(levelname)s %(message)s"
coloredlogs.install(level=LOGGING_LEVEL, fmt=LOGGING_FMT)


from controller.baseline_agents import Baseline, Random
from model.simulator import Simulator


def main(args):
    simulator = Simulator(
        no_people=args.people,
        no_floors=args.floors,
        no_cars=args.cars,
        capacity=args.capacity,
        speed=args.speed,
        gui=args.gui,
        id=0,
    )

    # agent = Baseline()
    agent = Random(probability=0.5)
    simulator.register_agent(agent)
    simulator.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""
        An multi-elevator simulator in Python
        """
    )
    parser.add_argument("--id", help="Id if the simulation (if any).")
    parser.add_argument(
        "--people",
        "-p",
        type=int,
        default=20,
        help="Total number of people to be served (Default: %(default)s)",
    )
    parser.add_argument(
        "--floors",
        "-f",
        type=int,
        default=4,
        help="Number of floors (Default: %(default)s)",
    )
    parser.add_argument(
        "--cars",
        "-c",
        type=int,
        default=3,
        help="Number of cars (Default: %(default)s)",
    )
    parser.add_argument(
        "--capacity",
        "-cc",
        nargs="+",
        # type=list,
        default=[5, 5, 5],
        help="Capacity of each car (Default: %(default)s)",
    )
    parser.add_argument(
        "--speed",
        "-s",
        type=float,
        default=0.1,
        help="The factor defines how much real time passes with each step of simulation time. Ex: if you set speed=2, each step will take 2 seconds, larger means slower simulation. Default: %(default)s.",
    )
    parser.add_argument(
        "--gui",
        "-g",
        action="store_true",
        default=False,
        help="Show the GUI display (Default: %(default)s)",
    )
    # we could also use vars(parser.parse_args()) to make args a dictionary args['<option>']
    args = parser.parse_args()

    if args.cars != len(args.capacity):
        logging.warning(
            f"Car capacity list length ({len(args.capacity)}) does not match number of cars ({args.cars}). Assuming uniform capacity for all cars to: {args.capacity[0]}"
        )
        args.capacity = [args.capacity[0]] * args.cars

    logging.info(args)
    main(args)
