from cx_Freeze import setup, Executable

# Setup fonksiyonu, cx_Freeze kütüphanesinin kullanımını ayarlar ve programın özelliklerini belirler.

setup(
    name='WpMs', # Programın adı
    version='0.1', # Programın sürüm numarası
    description='WpMs', # Programın açıklaması
    
    options={
        'build_exe': { # build_exe seçeneği, derlenmiş bir yürütülebilir (.exe) dosya oluştururken kullanılacak yapılandırmaları içerir
            'packages': ['pyautogui'], # Derlenmiş exe dosyasına dahil edilecek Python paketleri
            'include_msvcr': True, # Microsoft Visual C++ Kütüphanelerini dahil etme seçeneği
            'include_files': ['C:\\Users\\muham\\Desktop\\main.py'] # Derlenmiş exe dosyasına dahil edilecek diğer dosyalar
        },
        'bdist_msi': { # bdist_msi seçeneği, Windows MSI (Microsoft Installer) paketi oluşturmak için kullanılır
            'upgrade_code': '{6666CCCC-CCCC-CCCC-CCCC-CCCCCCCCCCCC}', # Yükseltme kodu, eski sürümlerin güncellenmesini sağlar
            'add_to_path': True # Programın PATH değişkenine eklenip eklenmeyeceğini belirler
        }
    },
    
    executables=[Executable('C:\\Users\\muham\\Desktop\\main.py', base='Win32GUI')] # Derlenmiş exe dosyasının ayarlarını içeren Executable nesnesi
)
