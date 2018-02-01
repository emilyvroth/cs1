from tkinter import *
import Ball
import random

class BallDraw(object):
    def __init__ (self, parent, balls):
        ##=====DATA RELEVANT TO BALL===============
        ##  We are going to repeatedly draw a ball object on the canvas,
        ##  "moving" it across the canvas.  The ball object is specified
        ## by (a) its x and y center coordinates (a tuple), (b) its radius,
        ##  (c) the delta x and delta y to move the ball in each time
        ## increment, and (d)  its color.
        self.Balls = balls
        #Ball.Ball(80, 200, 6, -3, 10, "red")
        '''
        self.Ball.,self.Ball.y = 80,200    # initial location
        self.Ball.radius = 10
        self.Ball.dx,self.Ball.dy = 6,-3    # the movement of the ball object
        self.Ball.color = "red"
        '''

        #========DATA NEEDED FOR ANIMATION=========
        #  Here is the time in milliseconds between consecutive instances
        #  of drawing the ball.  If this time is too small the ball will
        #  zip across the canvas in a blur.
        self.wait_time = 100 

        #this will allow us to stop moving the ball when the program quits
        self.isstopped = False 

        self.maxx = 400 # canvas width, in pixels
        self.maxy = 400 # canvas height, in pixels

        #=============CREATE THE NEEDED GUI ELEMENTS===========
        ##  Create a frame, attach a canvas and 4 buttons to this frame
        ##  Buttons are used to cleanly exit the program;
        ##  to speed up or slow down the animation, and to restart 
        ##  the animation.
        ##  Canvas, like an image, is an object that we can draw objects on.
        ##  This canvas is called chart_1.  
        ##  Parent = root window, contains a frame
        ##  The frame contains the canvas and the 4 buttons.
        ##  We only care about the canvas in our animation
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        self.top_frame = Frame(self.frame)
        self.top_frame.pack(side=TOP)
        self.canvas = Canvas(self.top_frame, background="white", \
                             width=self.maxx, height=self.maxy )
        self.canvas.pack()
        self.bottom_frame = Frame(self.frame)
        self.bottom_frame.pack(side=BOTTOM)
        self.restart = Button(self.bottom_frame, text="Restart", command=self.restart)
        self.restart.pack(side=LEFT)
        self.slow = Button(self.bottom_frame, text="Slower", command=self.slower)
        self.slow.pack(side=LEFT)
        self.fast = Button(self.bottom_frame, text="Faster", command=self.faster)
        self.fast.pack(side=LEFT)
        self.quit = Button(self.bottom_frame, text="Quit", command=self.quit)
        self.quit.pack(side=RIGHT)

    def faster(self):
        if self.wait_time > 2:
            self.wait_time //= 2

    def slower(self):
        self.wait_time *= 2
            
    def restart(self):
        self.isstopped = False
        for ball in self.Balls:
            ball.x=ball.start_x
            ball.y=ball.start_y
            ball.dx=ball.start_dx
            ball.dy=ball.start_dy
        #self.Ball.x,self.Ball.y = 80,200
        self.animate()
        
    def quit(self):
        self.isstopped = True
        self.parent.destroy()
        
    def draw_balls(self):
        #  Remove all the previously-drawn balls
        self.canvas.delete("all")
        
        # Draw an oval on the canvas within the bounding box
        for Ball in self.Balls:
            bounding_box = (Ball.x-Ball.radius, \
                            Ball.y-Ball.radius,\
                            Ball.x+Ball.radius, \
                            Ball.y+Ball.radius) 
            self.canvas.create_oval(bounding_box, fill=Ball.color)
        self.canvas.update()      # Actually refresh the drawing on the canvas.

        # Pause execution.  This allows the eye to catch up
        self.canvas.after(self.wait_time)

    def animate(self):
        ##  Loop until the ball runs off the screen.
        while not self.isstopped:
            # Move the ball
            self.draw_balls()
            for Ball in self.Balls:
                Ball.x += Ball.dx
                Ball.y += Ball.dy
                Ball.check_and_reverse(self.maxx, self.maxy)


if __name__ == "__main__":
    ##  We will create a root object, which will contain all 
    ##  our user interface elements
    ##
    root = Tk()
    root.title("Tkinter: Lab 11")

    ## Create a class to handle all our animation
   

    l = []
    colorList = ['blue', 'red', 'green', 'yellow', 'magenta', 'orange']

    for i in range(10):
        x = random.randint(10,390)
        y = random.randint(10,390)
        xspeed = random.randint(-8,8)
        yspeed = random.randint(-8,8)
        rad = random.randint(5, 10)
        color = random.choice(colorList)
        rand_ball = Ball.Ball(x, y, xspeed, yspeed, rad, color)
        l.append(rand_ball)

    bd = BallDraw(root,l)
            
    ## Run the animation by continuously drawing the ball and then moving it
    bd.animate()
    
    ## This is an infinite loop that allows the window to listen to
    ## "events", which are user inputs.  The only user event here is
    ## closing the window, which ends the program. 
    root.mainloop()