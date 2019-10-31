import subprocess

req = {
    "python", "tqdm", "nb_conda_kernels", "pip", "ipython", "numpy", "scipy", "pandas", 
    "scikit-learn", "matplotlib", "seaborn", "pydotplus", "ipywidgets", "nltk", 
    "xgboost", "scikit-optimize", "jcopml", "luwiji", "pillow"
}

def existing_env():
    result = subprocess.run(["conda", "env", "list"], stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8').split("\n")
    return [r.split()[0] for r in result if "envs" in r]

def existing_package(env):
    result = subprocess.run(["conda", "list", "--name", env], stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8').split("\n")
    return [r.split()[0] for r in result[4:-1]]

def main():
    if "jupyter" in existing_package("base"):
        print("✓ jupyter telah terinstall dengan baik\n")
        if "nb_conda_kernels" in existing_package("base"):
            print("✓ nb_conda_kernels telah terinstall dengan baik\n")
            if "jcopml" in existing_env():
                print("✓ Environment jcopml terdeteksi\n") 
                exist = set(existing_package("jcopml"))
                if req.issubset(exist):
                    print("✓ Package telah terinstall dengan baik di dalam environment jcopml\n")
                    print("✓ Instalasi berjalan dengan baik. Selamat belajar!")                
                else:
                    print(f"Kelihatannya package {req - exist} belum terinstall, mungkin karena masalah internet")
                    print("Cara termudah untuk menyelesaikan ini adalah install ulang environmentnya")
                    print("Note: Tidak usah khawatir karena semua yang sudah terdownload akan di skip")
                    print()
                    print("Pertama remove environment yang terlanjur dibuat")
                    print(">> conda env remove --name jcopml")
                    print("Lalu buat ulang environment nya. Pastikan sudah di folder kerja `supervised_learning`")
                    print(">> conda env create -f env_jcopml.yml")                    
            else:
                print("Environment jcopml tidak ditemukan.")            
                print("Mohon jalankan command berikut pada folder kerja `supervised_learning`")
                print(">> conda env create -f env_jcopml.yml")
        else:
            print("Apakah kamu menggunakan Anaconda? Saya merekomendasikan untuk menggunakan miniconda.")
            print("Untuk sekarang, mohon jalankan command berikut")
            print(">> conda install nb_conda_kernels")
    else:
        print("Mohon jalankan command berikut")
        print(">> conda install jupyter nb_conda_kernels")
        
if __name__ == "__main__":
    main()