import pyautogui as pg
import webbrowser as wb
import time

def send_whatsapp_message_now(phone_number, message):
    """
    Mengirim pesan WhatsApp segera setelah membuka WhatsApp Web.
    
    Args:
        phone_number (str): Nomor telepon WhatsApp dengan kode negara, contoh: "+628123456789".
        message (str): Pesan yang ingin dikirim.
    """
    # Format URL WhatsApp Web untuk membuka chat langsung
    whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_number}&text={message}"
    
    # Membuka WhatsApp Web di browser default
    wb.open(whatsapp_url)
    
    # Tunggu beberapa detik untuk memastikan halaman terbuka sepenuhnya
    time.sleep(10)  # Kamu bisa mengurangi atau menambah waktu sesuai kecepatan internet
    
    # Simulasikan tekan tombol Enter untuk mengirim pesan
    pg.press("enter")

# Contoh penggunaan
phone_number = "+6289509352085"  # Ganti dengan nomor tujuan, pastikan menggunakan format internasional
message = "hallo"  # Pesan yang ingin kamu kirim

send_whatsapp_message_now(phone_number, message)