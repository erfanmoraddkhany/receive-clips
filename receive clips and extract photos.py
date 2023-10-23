python
import cv2

def extract_frames(video_path, output_path):
# باز کردن فایل ویدئو
video = cv2.VideoCapture(video_path)

# خواندن فریم ها تا زمانی که فریم دیگری موجود باشد
success, image = video.read()
count = 0
while success:
# ذخیره عکس
cv2.imwrite(f"{output_path}/frame{count}.jpg", image)

# خواندن فریم بعدی
success, image = video.read()
count += 1

# بستن ویدئو
video.release()

# مسیر و نام فایل ویدئو را تعیین کنید
video_path = "path/to/video.mp4"

# مسیر پوشه برای ذخیره عکس ها را تعیین کنید
output_path = "path/to/output/folder"

# استخراج فریم ها و ذخیره عکس ها
extract_frames(video_path, output_path)