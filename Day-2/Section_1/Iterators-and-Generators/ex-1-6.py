def echo():
    while True:
        received = yield
        print("Received:", received)

gen = echo()
next(gen)  # Prime the generator
gen.send("Hello")  # Received: Hello
gen.send("World")  # Received: World
