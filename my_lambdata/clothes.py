
    ### clothes.py

class Polo():
    def __init__(self, style, size, color):
        self.style = style
        self.size = size
        self.color = color


    def pop_collar(self, ):
        print("POPPING THIS COLLAR")


if __name__ == "__main__":

    #df = DataFrame(____)
    #print(df.head())

    polo = Polo(style="Sheek", size="L", color="Blue")
    print(type(polo))
    print(polo.size)
    print(polo.color)
    print(polo.style)
    print(polo.pop_collar())

    polo2 = Polo(style="Shimmery", size="S", color="Yellow")
    print(type(polo))
    print(polo.size)
    print(polo.color)
    print(polo.style)
    print(polo.pop_collar())