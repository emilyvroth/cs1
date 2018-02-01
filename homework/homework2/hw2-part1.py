import math

def find_sphere_volume(radius):
	vs=(4/3)*math.pi*radius**3
	return vs
def find_cube_volume(side):
	vc=side**3
	return vc

side=(input("Enter the side length of the cube (in.) => "))
print(side)
side=float(side)
radius=(input("Enter the radius of the gum ball (in.) => "))
print(radius)
radius=round(float(radius),2)

balls_in_container=(side//(2*radius))**3
total_ball_vol=find_sphere_volume(radius)*balls_in_container
density=total_ball_vol/find_cube_volume(side)
big_sphere_vol=find_sphere_volume(side/2)
balls_in_sphere=big_sphere_vol*density//find_sphere_volume(radius)

print("A box of side length {:.1f} will hold {:.0f} gum balls of radius {}.".format(side,balls_in_container,radius))
print("The gum balls will take up {:.2f} in^3".format(total_ball_vol))
print("of the total volume of {:.2f} in^3 or {:.2%}".format(find_cube_volume(side),density))
print("A sphere with a diameter of {:.1f} would have volume {:.2f} in^3".format(side,big_sphere_vol))
print("It would hold {:.0f} gum balls at the same density.".format(balls_in_sphere))
