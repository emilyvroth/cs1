def frame_string(string):
	frame="*"*(len(string)+6)
	string="** "+string+" **"
	print(frame,string,frame,sep="\n")
frame_string("Spanish Inquisition")
print()
frame_string("Ni")