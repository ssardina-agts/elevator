import argparse
import coloredlogs
import logging

LOGGING_LEVEL = 'INFO'
LOGGING_FMT = '%(asctime)s %(levelname)s %(message)s'
coloredlogs.install(level=LOGGING_LEVEL, fmt=LOGGING_FMT)


from controller.baseline_agents import Baseline, Random
from model.simulator import Simulator


def main(args):
    simulator = Simulator(args)

    # agent = Baseline()
    agent = Random(probability=0.5)
    simulator.register_agent(agent)
    simulator.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""
        An elevator simulator in Python based on https://github.com/mrbrianevans/elevator
        """
    )
    parser.add_argument(
        '--id',
        help='Id if the simulation (if any).'
    )
    parser.add_argument(
        '--num_people',
        type=int,
        default=20,
        help='Number of people, deault: %(default)s.',
    )
    parser.add_argument(
        '--num_floors',
        type=int,
        default=4,
        help='Number of floors, default: %(default)s.',
    )
    parser.add_argument(
        '--num_cars',
        type=int,
        default=3,
        help='Number of cars, default: %(default)s.',
    )
    parser.add_argument(
        '--cars_capacity',
        nargs='+',
        type=list,
        default=[5, 5, 5],
        help='Capacity of each car, default: %(default)s.',
    )
    parser.add_argument(
        '--anim_speed_factor',
        type=float,
        default=.1,
        help='The factor defines how much real time passes with each step of simulation time. Ex: if you set anim_speed_factor=2, each step will take 2 seconds, larger means slower simulation. Default: %(default)s.',
    )
    parser.add_argument(
        '--gui',
        action="store_true",
        default=True,
        help='Show the GUI display, default: %(default)s.',
    )
    # we could also use vars(parser.parse_args()) to make args a dictionary args['<option>']
    args = parser.parse_args()

    if args.num_cars != len(args.cars_capacity):
        logging.error(
            f'Error: number of cars (' + str(args.num_cars) + ') and the length of cars capacity list (' + str(
                len(args.cars_capacity)) + ') are not equal')
    else:
        logging.info(args)
        main(args)
