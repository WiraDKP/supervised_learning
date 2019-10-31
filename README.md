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
    - Klik link ini untuk download: [Miniconda Windows 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)
    - Note: skip step ini apabila kamu sudah menggunakan Anaconda sebelumnya. Walau demikian, saya akan jelaskan alasan kenapa kamu sebaiknya menggunakan miniconda nanti di course ini.

- Install miniconda
    - Ketika ada pilihan `install for`, pilih `Just Me (recommended)`
    - Untuk `Advanced Options`, silahkan centang `Register Anaconda as my default Python 3.7`
    - Tunggu hingga instalasi selesai

- Jalankan `Anaconda Prompt`

### **Mac user**
- Download miniconda untuk Python 3.7
    - Klik link ini untuk download: [Miniconda Mac OS X 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg)
    - Note: skip step ini apabila kamu sudah menggunakan Anaconda sebelumnya. Walau demikian, saya akan jelaskan alasan kenapa kamu sebaiknya menggunakan miniconda nanti di course ini.

- Install miniconda
    - Install tanpa mengubah opsi apapun
    - Tunggu hingga instalasi selesai

- Jalankan terminal

### **Linux user**
- Download miniconda untuk Python 3.7
    - Klik link ini untuk download: [Miniconda Linux 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)
    - Note: skip step ini apabila kamu sudah menggunakan Anaconda sebelumnya. Walau demikian, saya akan jelaskan alasan kenapa kamu sebaiknya menggunakan miniconda nanti di course ini.
    
- Install miniconda
    - jalankan terminal
    - Install miniconda menggunakan command berikut
        ```
        bash Miniconda3-latest-Linux-x86_64.sh
        ```
    - Ketik `yes` untuk agree dengan license nya, kemudian `yes` lagi untuk `prepend miniconda install location to PATH`
    - Tunggu hingga instalasi selesai
    
- hanya untuk memastikan, tutup dan buka terminal lagi

## Step 3: Instalasi Jupyter 
- Pastikan anda sedang berada di environment `(base)`, dan kita akan install 2 hal disana
    ```
    conda install jupyter nb_conda_kernels
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
### **Windows user**
- Jalankan command ini dan pastikan ada `jupyter` dan `nb_conda_kernels`
    ```
    conda list | findstr "jupyter nb_conda_kernels"
    ```
- Jalankan command ini dan pastikan ada `jcopml`
    ```
    conda env list | findstr jcopml
    ```
    - Kalau tidak ada, solusinya adalah install ulang environment
        ```
        conda env create -f env_jcopml.yml
        ```
- Jalankan command ini dan pastikan ada `jcopml` dan `luwiji`
    ```
    conda list --name jcopml | findstr "jcopml luwiji"
    ```
    - Kalau tidak ada, ini disebabkan internet sempat terputus di tengah jalan
    - Easy fix, remove lalu install ulang (yang sudah di download akan di skip), tapi pastikan kali ini internet berjalan dengan baik
        ```
        >> conda env remove --name jcopml
        >> conda env create -f env_jcopml.yml
        ```
    - Advance fix
        ```
        >> conda activate jcopml
        >> pip install xgboost==0.80 scikit-optimize==0.5.2 jcopml luwiji pillow==5.4.1
        >> conda deactivate
        ```
### **MAC dan Linux user**
- Jalankan command ini dan pastikan ada `jupyter` dan `nb_conda_kernels`
    ```
    conda list | grep -e jupyter -e nb_conda_kernels
    ```
- Jalankan command ini dan pastikan ada `jcopml`
    ```
    conda env list | grep jcopml
    ```
    - Kalau tidak ada, solusinya adalah install ulang environment
        ```
        conda env create -f env_jcopml.yml
        ```
- Jalankan command ini dan pastikan ada `jcopml` dan `luwiji`
    ```
    conda list --name jcopml | grep -e jcopml -e luwiji
    ```
    - Kalau tidak ada, ini disebabkan internet sempat terputus di tengah jalan
    - Easy fix, remove lalu install ulang (yang sudah di download akan di skip), tapi pastikan kali ini internet berjalan dengan baik
        ```
        >> conda env remove --name jcopml
        >> conda env create -f env_jcopml.yml
        ```
    - Advance fix
        ```
        >> conda activate jcopml
        >> pip install xgboost==0.80 scikit-optimize==0.5.2 jcopml luwiji pillow==5.4.1
        >> conda deactivate
        ```