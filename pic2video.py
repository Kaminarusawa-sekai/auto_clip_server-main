from moviepy import ImageClip

input_path="C:\\Users\\17909\\Desktop\\炮神山.png"
output_path="C:\\Users\\17909\\Desktop\\炮神山.mp4"

image=ImageClip(input_path,duration=5)
image.write_videofile(output_path, codec="libx264", preset="ultrafast",fps=24)