# Using pathlib
Path("output.txt").write_text("hello")

# Using open()
with open("output.txt", "w") as f:
    f.write("hello")
