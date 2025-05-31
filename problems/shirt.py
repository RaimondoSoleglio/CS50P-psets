import sys
from PIL import Image, ImageOps


def main():
    #  let's start with what's needed
    if not len(sys.argv) == 3:
        sys.exit("We need two args")

    # to check multiple ending we use a tuple - lowercase is there to make the check case-insensitive
    if not sys.argv[1].lower().endswith(('.jpg', '.jpeg', '.png')) \
            or not sys.argv[2].lower().endswith(('.jpg', '.jpeg', '.png')):
        sys.exit("Wrong filetype")

    # we compare the endings of the args. 1 limits the splits at the first period, [-1] gets the last element of the list
    if sys.argv[1].rsplit('.', 1)[-1] != sys.argv[2].rsplit('.', 1)[-1]:
        sys.exit("Files have different extensions")

    try:
        with Image.open(sys.argv[1]) as image:
            cropped_image = ImageOps.fit(image, (600, 600))
            with Image.open("shirt.png") as mask:
                #  the paste method modifies the image in place and doesn’t return a new image
                cropped_image.paste(mask, mask)
                cropped_image.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
