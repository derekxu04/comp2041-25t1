#! /usr/bin/env python3

import sys

def main():
    n_lines = 10
    if len(sys.argv) > 1:
        n_lines = int(sys.argv[1][1:])

        sys.argv.pop(1)

    if len(sys.argv) > 1:
        # Files have been specified
        for file in sys.argv[1:]:
            print(f"==> {file} <==")

            try:
                with open(file, "r") as stream:
                    i = 1
                    for line in stream:
                        if i > n_lines:
                            break

                        print(line, end='')

                        i += 1
            except IOError as e:
                print("Error: ", e)
            # stream = open(file, "r")

            # i = 1
            # for line in stream:
            #     if i > n_lines:
            #         break

            #     print(line, end='')

            #     i += 1
            
            # stream.close()
    else:
        # Read from stdin

        i = 1
        for line in sys.stdin:
            if i > n_lines:
                break

            print(line, end='')

            i += 1

if __name__ == "__main__":
    main()