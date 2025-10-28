import matplotlib.pyplot as pt

def focus_graph():
    with open("focus.txt", "r") as file:
        content = file.read().strip()   # remove extra spaces/newlines

    content = content.split(",")
    # filter out empty strings
    content = [float(i) for i in content if i.strip() != ""]

    x1 = list(range(len(content)))
    y1 = content

    print(content)
    pt.plot(x1, y1, color="red", marker="o")
    pt.title("YOUR FOCUSED TIME", fontsize=16)
    pt.xlabel("Sessions", fontsize=14)
    pt.ylabel("Focus Duration (hours)", fontsize=14)
    pt.grid(True)
    pt.show()
