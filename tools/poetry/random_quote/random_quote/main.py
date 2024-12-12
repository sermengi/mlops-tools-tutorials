import turtle
import requests

def main():
    # Make a GET request to the dummyJSON endpoint and parse out the quote and author
    response = requests.get("https://dummyjson.com/quote/random")
    data = response.json()
    quote = data["quote"]
    author = data["author"]
    
    # Create a new turtle screen and set its background color
    screen = turtle.Screen()
    screen.bgcolor("lightyellow")
    
    # Initialize a turtle object
    t = turtle.Turtle()
    t.hideturtle()
    
    # Position the turtle and display the quote
    t.penup()
    t.goto(0, 50)
    t.write(quote, align="center", font=("Arial", 16, "italic"))
    
    # Position the turtle and display the author
    t.goto(0, -50)
    t.write(f"- {author}", align="center", font=("Arial", 14, "bold"))
    
    # Wait until the window is closed
    turtle.done()
    
if __name__=="__main__":
    main()
    
    