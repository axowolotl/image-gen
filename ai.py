
import requests  # Mengimpor library requests untuk mengirim permintaan HTTP ke API

def download_image(prompt):
    # Mendefinisikan fungsi download_image.
    # Fungsi ini menerima satu parameter: prompt.
    # prompt adalah deskripsi teks dari gambar yang akan dibuat.

    url = f"https://image.pollinations.ai/image/{prompt}"
    # Membuat URL permintaan.
    # Nilai variabel prompt dimasukkan ke dalam URL.
    # Ini adalah alamat yang digunakan untuk mengakses layanan pembuatan gambar.

    response = requests.get(url)
    # Mengirim permintaan GET ke server.
    # Server akan mengembalikan data gambar sebagai respons.

    with open('generated_image.jpg', 'wb') as file:
        # Membuka file generated_image.jpg dalam mode tulis biner (wb).
        # Mode wb diperlukan karena gambar adalah data biner, bukan teks biasa.

        file.write(response.content)
        # Menuliskan isi respons dari server ke dalam file.
        # response.content berisi byte gambar.

    print('Gambar diunduh!')
    # Menampilkan pesan ke konsol agar pengguna tahu program telah selesai.

# Memanggil fungsi dan memberikan prompt sebagai argumen.
# Setelah dijalankan, program akan mengirim permintaan dan menyimpan gambar ke file.