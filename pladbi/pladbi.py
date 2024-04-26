import os, zipfile, sys
import yaml

def main(function: None, path: None, path_to_end: None):
        if function == "install":
            with zipfile.ZipFile(path, 'r') as tmp:
                    
                    tmp.extract("about.yaml")

                    with open("about.yaml", "r", encoding="utf-8") as lol:
                        lol0 = yaml.load(lol, Loader=yaml.FullLoader)
                    os.mkdir(path_to_end + "/" + lol0.get("appname"))
                    tmp.extractall(path_to_end + "/" + lol0.get("appname"))
                    print('"' + lol0.get("appname") + '" has been successfully installed')
                    lol.close()
                    tmp.close()
                    os.remove("about.yaml")

        if function == "pack":
                    
                    os.chdir(path_to_end)
                    with open(path + "/about.yaml", "r", encoding="utf-8") as lol:
                        lol0 = yaml.load(lol, Loader=yaml.FullLoader)
                    appname = lol0.get("appname")

                    directory_path = path
                    zipf_name = (appname + ".pladbp")
                    zipf = zipfile.ZipFile(zipf_name, 'w', zipfile.ZIP_DEFLATED)
                    for root, dirs, files in os.walk(directory_path):
                        for file in files:
                            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(directory_path)))

                    zipf.close()

                    print(f"Program {appname} has been successfully packaged to path {path_to_end}")



if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])