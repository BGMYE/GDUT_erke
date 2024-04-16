import time
import random
import qrcode

def QR_CODE(URL, N, name):
  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4,
  )
  qr.add_data(URL)
  qr.make(fit=True)
  img = qr.make_image(fill_color="black", back_color="white")
  img.save(f"{name}{N+1}.png")

if __name__ == "__main__":
  N = 2
  URL = "http://erke.gdut.edu.cn/public/index.php/mobile/activity-detail?id=6558"
  start_index = URL.find("id=") + len("id=")
  id_str = URL[start_index:]

  start_timestamp = 1767264000  # 2026-01-01 18:40:00
  end_timestamp = 1803801599    # 2027-02-28 15:59:59
  for i in range(N):
    In_time = random.randint(start_timestamp, end_timestamp) * 1000
    Out_time = random.randint(start_timestamp, end_timestamp) * 1000
    Sign_in = f"http://erke.gdut.edu.cn/public/index.php/mobile/activity-sign-result?id={id_str}&type=in&ts={In_time}"
    Sign_out = f"http://erke.gdut.edu.cn/public/index.php/mobile/activity-sign-result?id={id_str}&type=out&ts={Out_time}"
    QR_CODE(Sign_in, i, "IN")
    QR_CODE(Sign_out, i, "OUT")
    print(Sign_in)
    print(Sign_out)
