import os
import sys
import shutil
path=os.getcwd()+"/MainFolder"
def createDir():
    if os.path.exists(path):
        print("Директорія існує")
    else:
        os.mkdir("MainFolder")
        dd=os.getcwd()
        os.chdir(dd+'/MainFolder')
        print('Поточна директорія :', os.getcwd())
        for i in range(1,5):
            name="Folder"+str(i)
            os.mkdir(name)
            dd1 = os.getcwd()
            os.chdir(dd1 + '/'+name)
            os.mkdir("SubFolder"+str(i))
            open("File_0"+str(i)+".txt","w")
            os.chdir(dd1)
def menu():

    n=sys.argv
 #   n = input("Пошук файла або директорії- Search\nВидалення файлу - DelFile\n Видалення каталогу - Del"
  #            "\nПерейменування визначеного файлу або папки - Ren\n Для переходу в папку використовуйте - cd \nВийти з консолі - ^")
    return n
def create1(par):
    path1 = os.getcwd()+"/"+par
    if os.path.exists(path1):
        print("Директорія існує")
    else:
        os.mkdir(par)
    print(os.getcwd())
    sys.exit(0)
def cd(par):
    path3 = os.getcwd()
    print(path3)
    print(os.listdir(path3))
    cd = par
    os.chdir(path3 + '/' + cd)
    path4 = os.getcwd()
    print(path4)
def search(find):

    if find == "^":
        print("jhgj")
    else:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(find):
                    print("МИ ЗНАЙШЛИ ФАЙЛ\n")
                    f = True
                    path_file = os.path.join(root, file)
                    print(path_file)
            for dir in dirs:
                if dir.endswith(find):
                    print("МИ ЗНАЙШЛИ Директорію\n")
                    f = True
                    path_file = os.path.join(root, dir)
                    print(path_file)
    if f == False:
        print("Тут немає такого файлу")
def ren(ren,new_r):
    if ren.find(".") == -1:
        path1 = os.getcwd() + "/MainFolder/" + ren
        path2 = os.getcwd() + "/MainFolder/" + new_r
    else:
        path1 = os.getcwd() + "/MainFolder/" + ren
        path2 = os.getcwd() + "/MainFolder/" + new_r
    if os.path.exists(path1):
        os.rename(path1, path2)
    else:
        print("В цій директорії такого файлу немає")
        print(path1)
def del1(del1):

    path1 = os.getcwd() + "/MainFolder/" + del1
    if os.path.exists(path1):
        if not os.listdir(path1):
            os.rmdir(path1)
        else:
            y = input("Папка не пуста. Чи видаляти її? Yes, No")
            if y == 'Yes':
                shutil.rmtree(path1)
                print("Папку видалено")

    print("Ви в каталозі" + path + "\nВміст каталогу")
    print(os.listdir(path))
def del2(del1):

    path1 = os.getcwd() + "/MainFolder/" + del1
    if os.path.exists(path1):
        os.remove(path1)
    else:
        print("В цій директорії такого файлу немає")
        print(os.listdir(path))
createDir()

n1 = menu()
n=n1[1]
if n=='--create':
    create1(n1[2])

elif n=="--searche":
     search(n1[2])
elif n=="--del":
       del1(n1[2])

elif n=="--delFile":
    del2(n1[2])
elif n=="--ren":
    ren(n1[2],n1[3])

elif n=="cd":
        cd(n1[2])
elif n=="--help":
    print("Меню\n Пошук файла або директорії- --search\nВидалення файлу - --delFile\n Видалення каталогу - --del\n Переіменування - --ren")
else:
    print("Не існує команди")