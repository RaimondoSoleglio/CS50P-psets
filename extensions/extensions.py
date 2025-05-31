def main():
    file = input("Filename: ").strip().lower().rsplit('.', 1)
    if len(file) < 2:
        file.insert(0, '')
    output(file[1])

def output(x):
    match x:
        case "gif":
            print("image/gif")
        case "jpeg" | "jpg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")



# can i do better than this long list??
'''
def output(x):
    if x.endswith(".gif"):
        print("image/gif")
    elif x.endswith(".jpg") or x.endswith(".jpeg"):
        print("image/jpeg")
    elif x.endswith(".png"):
        print("image/png")
    elif x.endswith(".pdf"):
        print("application/pdf")
    elif x.endswith(".txt"):
        print("text/plain")
    elif x.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")
'''


main()
