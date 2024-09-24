import requests

# Fungsi untuk melacak alamat IP dengan menggunakan nomor telepon
def track_ip_by_phone(phone_number):
    # URL API pencari alamat IP
    api_url = "https://api.ip2country.info/ip"
    
    # Parameters untuk permintaan API
    params = {
        "telephone": phone_number
    }
    
    # Melakukan permintaan API
    response = requests.get(api_url, params=params)
    
    # Mengambil data hasil permintaan API
    data = response.json()
    
    # Mengambil alamat IP dan lokasi dari data hasil permintaan API
    ip_address = data.get("ip", "")
    location = data.get("country", "")
    
    return ip_address, location

# Contoh penggunaan
phone_number = "+6281228393719"  # Ganti dengan nomor telepon yang ingin dilacak
ip_address, location = track_ip_by_phone(phone_number)

print("Alamat IP:", ip_address)
print("Lokasi:", location)
