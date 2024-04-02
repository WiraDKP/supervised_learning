# Supervised Learning by J.COp
Belajar dasar-dasar machine learning dari nol. Untuk fase pertama, kita akan mempelajari teknik-teknik supervised learning menggunakan scikit-learn dan jcopml.

# Starter Guide
## Step 1: Download materi
- Klik disini untuk [Download ZIP](https://codeload.github.com/WiraDKP/supervised_learning/zip/master), atau
- Bagi yang familiar dengan git, boleh menggunakan clone
    ```
    git clone https://github.com/WiraDKP/supervised_learning.git
    ```

## Step 2: Instalasi Miniconda
### **Windows user**
- Download miniconda untuk Python 3.7
    - Klik link ini untuk download: [Miniconda Windows 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-Windows-x86_64.exe)
    - Note: skip step ini apabila kamu sudah menggunakan Anaconda sebelumnya. Walau demikian, saya akan jelaskan alasan kenapa kamu sebaiknya menggunakan miniconda nanti di course ini.

- Install miniconda
    - Ketika ada pilihan `install for`, pilih `Just Me (recommended)`
    - Untuk `Advanced Options`, silahkan centang `Register Anaconda as my default Python 3.7`
    - Tunggu hingga instalasi selesai

- Jalankan `Anaconda Prompt`

### **Mac user**
- Download miniconda untuk Python 3.7
    - Klik link ini untuk download: [Miniconda Mac OS X 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-MacOSX-x86_64.pkg)
    - 
    - Note: skip step ini apabila kamu sudah menggunakan Anaconda sebelumnya. Walau demikian, saya akan jelaskan alasan kenapa kamu sebaiknya menggunakan miniconda nanti di course ini.

- Install miniconda
    - Install tanpa mengubah opsi apapun
    - Tunggu hingga instalasi selesai

- Jalankan terminal

### **Linux user**
- Download miniconda untuk Python 3.7
    - Klik link ini untuk download: [Miniconda Linux 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-Linux-x86_64.sh)
    - Note: skip step ini apabila kamu sudah menggunakan Anaconda sebelumnya. Walau demikian, saya akan jelaskan alasan kenapa kamu sebaiknya menggunakan miniconda nanti di course ini.
    
- Install miniconda
    - jalankan terminal
    - Install miniconda menggunakan command berikut
        ```
        bash Miniconda3-py39_23.3.1-0-Linux-x86_64.sh
        ```
    - Ketik `yes` untuk agree dengan license nya, kemudian `yes` lagi untuk `prepend miniconda install location to PATH`
    - Tunggu hingga instalasi selesai
    
- hanya untuk memastikan, tutup dan buka terminal lagi

## Step 3: Instalasi Jupyter 
- Kita akan install 2 hal di base environment
    ```
    conda install -n base -c conda-forge jupyter nb_conda_kernels "notebook<6.0" 
    ```

## Step 4: Instalasi Environment
- Change directory `cd` ke folder kerja ini
    ```
    cd supervised_learning/
    ```
- Jalankan command ini untuk menginstall environment `jcopml`
    ```
    conda env create -f env_jcopml.yml
    ```

## Step 5: Memastikan environment terinstall dengan baik
- Jalankan command berikut untuk mengecek instalasi dan ikuti instruksi yang dihasilkan
    ```
    python check_installation.py
    ```
- Jika sudah aman, maka akan muncul keterangan berikut, dan kita bisa mulai belajar. Semangat!
    ```
    ✓ jupyter telah terinstall dengan baik
    ✓ nb_conda_kernels telah terinstall dengan baik
    ✓ Environment jcopml terdeteksi
    ✓ Package telah terinstall dengan baik di dalam environment jcopml
    ✓ Instalasi berjalan dengan baik. Selamat belajar!
    ```

# Note
Notebook versi 7.x breaking (hampir) semua extension yang ada, salah satunya "Snippets Menu" yang banyak digunakan di course.
Jika masih ingin menggunakan "Snippets Menu" maka mesti downgrade ke Notebook 5.x dengan command berikut
```
>> conda install -n base -c conda-forge jupyter nb_conda_kernels 
>> pip install notebook==5.7.11
```

Kalau tab nbextensions nya tidak muncul atau misalnya sudah muncul tapi isinya kosong.
Coba jalankan ini di conda prompt / terminal nya
```
>> jupyter contrib nbextension install --user
>> jupyter nbextension enable varInspector/main
```

Walau demikian, projek nbextensions sudah terlihat mati suri karena migrasi Notebook 7.x sehingga cepat lambat saya sarankan juga untuk move on (meninggalkan Jupyter Notebook dan pindah menggunakan Jupyter Lab).
Di versi jcop yang lebih baru ada sediakan snippets yang bisa digunakan di Jupyter Lab, Jupyter Notebook, dan Jupyter VS Code.
