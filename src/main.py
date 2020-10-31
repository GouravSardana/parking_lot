from parking import Parking
import argparse


def main():
    parkinglot = Parking()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action="store", required=True, dest='input_file', help="input a text file")
    args = parser.parse_args()


    if args.input_file:
        with open(args.input_file) as file:
            for line in file:
                line = line.rstrip('\n')
                parkinglot.command(line)
    else:
        while True:
            line = input("$ ")
            parkinglot.command(line)



if __name__ == '__main__':
	main()