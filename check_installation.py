import subprocess

req = {
    "python", "tqdm", "nb_conda_kernels", "pip", "ipython", "numpy", "scipy", "pandas", 
    "scikit-learn", "matplotlib", "seaborn", "ipywidgets", "xgboost", "scikit-optimize", 
    "jcopml", "luwiji"
}
env_name = "jcopml"
working_folder = "supervised_learning"
env_file = "env_jcopml.yml"


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
            if env_name in existing_env():
                print(f"✓ Environment {env_name} terdeteksi\n")
                exist = set(existing_package(env_name))
                if req.issubset(exist):
                    print(f"✓ Package telah terinstall dengan baik di dalam environment {env_name}\n")
                    print("✓ Instalasi berjalan dengan baik. Selamat belajar!")                
                else:
                    print(f"Kelihatannya package {req - exist} belum terinstall, mungkin karena masalah internet")
                    print("Cara termudah untuk menyelesaikan ini adalah install ulang environmentnya")
                    print("Note: Tidak usah khawatir karena semua yang sudah terdownload akan di skip")
                    print()
                    print("Pertama remove environment yang terlanjur dibuat")
                    print(f">> conda env remove --name {env_name}")
                    print(f"Lalu buat ulang environment nya. Pastikan sudah di folder kerja `{working_folder}`")
                    print(f">> conda env create -f {env_file}")
            else:
                print(f"Environment {env_name} tidak ditemukan.")
                print(f"Mohon jalankan command berikut pada folder kerja `{working_folder}`")
                print(f">> conda env create -f {env_file}")
        else:
            print("Apakah kamu menggunakan Anaconda? Saya merekomendasikan untuk menggunakan miniconda.")
            print("Untuk sekarang, mohon jalankan command berikut")
            print(">> conda install nb_conda_kernels")
    else:
        print("Mohon jalankan command berikut")
        print(">> conda install jupyter nb_conda_kernels")
        
if __name__ == "__main__":
    main()
