# LaurensiusDaniRendragraha_19624272_URO_openCVobjectDetection
# Video Penjelasan Program OpenCV Object Detection (Laurensius Dani Rendragraha/19624272)
https://drive.google.com/file/d/1gcslyOlgqCjc6hkMIR0sW_tgoAbINv3d/view?usp=sharing 

# Spesifikasi Program

## Program: `colorPicker.py`
- Program ini digunakan untuk membantu pengguna menemukan nilai **Hue**, **Saturation**, dan **Value (HSV)** yang tepat untuk mendeteksi warna tertentu pada sebuah video.
- Video yang diproses diubah menjadi representasi **HSV color space**.
- Pengguna dapat menggunakan **TrackBar** untuk menyesuaikan nilai **HUE Min**, **SAT Min**, **VALUE Min**, **HUE Max**, **SAT Max**, dan **VALUE Max** secara real-time.
- Dengan menyesuaikan nilai-nilai tersebut, pengguna dapat melihat bagaimana perubahan rentang HSV memengaruhi deteksi warna objek di video.
- Nilai **lower_bound** dan **upper_bound** yang didapatkan melalui **TrackBar** akan digunakan pada program utama (`main.py`) untuk mendeteksi objek.

### Cara Kerja Program:
1. Membuka video dari file yang sudah ditentukan.
2. Menampilkan beberapa jendela:
   - **Original Frame**: Frame asli dari video.
   - **HSV Color Space**: Frame yang telah dikonversi ke HSV.
   - **Mask**: Mask dari frame yang dihasilkan berdasarkan rentang HSV.
   - **Result**: Frame yang hanya menunjukkan area warna yang terdeteksi berdasarkan mask.
   - **Horizontal Stacking**: Gabungan frame (Original, Mask, Result) untuk memudahkan pengamatan.
3. Dengan memanfaatkan **TrackBar**, pengguna dapat mengatur nilai HSV secara interaktif untuk menentukan rentang yang sesuai untuk mendeteksi warna objek.

## Program: `main.py`
- Program utama ini bertujuan untuk mendeteksi **lingkaran merah** pada sebuah video berdasarkan nilai **lower_bound** dan **upper_bound** yang telah ditentukan dari program `colorPicker.py`.
- Program ini memanfaatkan nilai HSV untuk membuat sebuah **mask**, mendeteksi kontur objek, dan menggambar **bounding rectangle** di sekitar objek yang terdeteksi.

### Langkah-Langkah Program:
1. **Membaca Video**: Program membaca video frame per frame.
2. **Resizing Frame**: Frame video diubah ukurannya menggunakan fungsi `rescaleFrame()` untuk mempercepat pemrosesan.
3. **Konversi ke HSV**:
   - Setiap frame dikonversi menjadi representasi HSV menggunakan `cv2.cvtColor()`.
4. **Pembuatan Mask**:
   - Mask dihasilkan menggunakan `cv2.inRange()`, di mana area dalam rentang `lower_bound` dan `upper_bound` akan menjadi putih (255), dan area lainnya menjadi hitam (0).
5. **Deteksi Kontur**:
   - Menggunakan `cv2.findContours()`, kontur dari objek dalam mask dideteksi.
   - Program memfilter kontur kecil (area < 500) untuk menghindari noise.
6. **Menggambar Bounding Rectangle**:
   - Untuk setiap kontur yang valid, program menggambar **bounding rectangle** pada frame asli menggunakan `cv2.rectangle()`.
7. **Menampilkan Hasil**:
   - Hasil berupa frame asli dengan bounding rectangle di sekitar objek yang terdeteksi.

## Cara Penggunaan

### 1. Menjalankan `colorPicker.py`
- Jalankan `colorPicker.py` untuk mencari nilai **lower_bound** dan **upper_bound**.
- Gunakan **TrackBar** untuk menyesuaikan nilai HSV hingga hanya warna objek target yang terdeteksi.
- Catat nilai **HUE Min**, **SAT Min**, **VALUE Min**, **HUE Max**, **SAT Max**, dan **VALUE Max** dari TrackBar.

### 2. Menjalankan `main.py`
- Edit variabel `lower_bound` dan `upper_bound` di `main.py` sesuai dengan nilai yang telah diperoleh dari `colorPicker.py`.
- Jalankan `main.py` untuk mendeteksi objek pada video.
- Hasilnya, lingkaran merah pada video akan terdeteksi dan dikelilingi oleh **bounding rectangle** berwarna hijau.

## Penjelasan Variabel Utama

### Program `colorPicker.py`
- **TrackBar**: Memungkinkan pengguna menyesuaikan nilai HSV secara interaktif.
- **Mask**: Biner gambar (hitam-putih) yang memisahkan area warna target dari background.
- **Horizontal Stacking**: Membantu pengguna membandingkan frame asli, mask, dan hasil deteksi secara visual.

### Program `main.py`
- **lower_bound & upper_bound**:
  - Mendefinisikan rentang HSV untuk mendeteksi warna target.
- **Mask**:
  - Memfilter area di frame berdasarkan nilai HSV.
  - Hanya objek dengan warna dalam rentang `lower_bound` dan `upper_bound` yang akan terlihat.
- **Contours**:
  - Mengambil batas luar objek yang terdeteksi di mask.
- **Bounding Rectangle**:
  - Menyorot objek yang terdeteksi dengan menggambar kotak di sekitar objek pada frame asli.

## Fitur Utama
1. **Interaktif HSV Adjustment**:
   - Menggunakan program `colorPicker.py`, pengguna dapat menyesuaikan rentang HSV secara real-time untuk mendeteksi objek dengan akurasi tinggi.
2. **Object Detection**:
   - Program `main.py` mendeteksi dan menyorot objek target (lingkaran merah) pada video.
3. **Noise Filtering**:
   - Program mengabaikan area kecil untuk menghindari deteksi objek yang tidak relevan.
