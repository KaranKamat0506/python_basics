def greet(fx):
    def myfx():
        print("Good morning")
        fx()
        print("Thanks for using this function")
    return myfx


@greet
def Hello():
    print("Hello")

Hello()
# greet(Hello)()

