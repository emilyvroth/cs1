r_sun=int(input("Enter the radius of the Sun (miles) -> "))
print(r_sun)
r_moon=int(input("Enter the radius of the Moon (miles) -> "))
print(r_moon)
sun2earth=int(input("Enter the maximum distance to the Sun (miles) -> "))
print(sun2earth)
moon2earth=int(input("Enter the minimum distance to the Moon (miles) -> "))
print(moon2earth)
moon_move=float(input("Enter the rate the Moon is moving away (in/year) -> "))
print(moon_move)

moon2eath_sun_size=sun2earth*(r_moon/r_sun)
more_miles=moon2eath_sun_size-moon2earth
time=(more_miles*5280*12)/moon_move

print("The Moon will have exactly the same apparent size as the Sun when it is {:.2f} miles away.".format(moon2eath_sun_size))
print("The Moon will need to recede another {:.2f} miles".format(more_miles))
print("Which will occur in {:.0f} years at the current rate.".format(time))
print("hi mom, im on github")