import argparse
import logging

import coloredlogs

from controller.baseline_agents import Baseline, Efficient
from model.simulator import Simulator

def main(args):
    simulator = Simulator(people_number=args.num_people, floors_number=args.num_floors, info_cars={"car_number": 1, "capacity": [3]})
    agent = Baseline()
    # agent = Efficient()

    simulator.register_agent(agent)
    simulator.run(animation_speed=args.anim_speed)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""
        An elevator simulator in Python based on https://github.com/mrbrianevans/elevator
        """
    )
    # parser.add_argument(
    #     dest='COBURG_SHEET',
    #     type=str,
    #     help='The Excel sheet Coburg sends with games.'
    # )
    parser.add_argument(
        '--id',
        help='Id if the simulation (if any).'
    )
    parser.add_argument(
        '--num-people',
        type=int,
        default=10,
        help='Do not set the RSVP option %(default)s.',
    )
    parser.add_argument(
        '--num-floors',
        type=int,
        default=4,
        help='Number of floor in building %(default)s.',
    )
    parser.add_argument(
        '--anim-speed',
        type=float,
        default=0.5,
        help='Delay step in the simulation, larger means slower simulation %(default)s.',
    )
    parser.add_argument(
        '--gui',
        action="store_true",
        help='Show the GUI display.',
    )
    # we could also use vars(parser.parse_args()) to make args a dictionary args['<option>']
    args = parser.parse_args()
    print(args)

    main(args)
