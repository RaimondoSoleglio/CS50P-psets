import sys
import csv


def main():
    # check for the right number of arguments
    if not len(sys.argv) == 3:
        sys.exit("Not the right number of args")

    students = []

    try:
        with open(sys.argv[1], "r") as f:
            # build the reader as collection of Dict whose keys are given by first row
            reader = csv.DictReader(f)
            for row in reader:
                # splitting the name into name and surname
                new_surname, new_name = row["name"].split(", ")
                student = [new_name, new_surname, row["house"]]
                students.append(student)
    except IOError:
        sys.exit("Something went wrong")

    with open(sys.argv[2], "w") as f:
        writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
        #  the header must be outside of the loop
        writer.writeheader()
        for student in students:
            # create a dictionary, whose keys are fieldnames and values the 3 parts of the lists in students list
            writer.writerow({"first": student[0], "last": student[1], "house": student[2]})


if __name__ == "__main__":
    main()
