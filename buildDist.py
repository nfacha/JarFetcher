import os

os.system("rm -rf downloads/dist/*.jar")
os.system("rm -rf downloads/dist/*.jar.conf")
os.system("rm -rf downloads/dist/*.zip")
os.system("/usr/bin/find downloads/jar -iname '*.jar' -exec cp --target-directory downloads/dist {} \;")
os.system("/usr/bin/find downloads/conf -iname '*.jar.conf' -exec cp --target-directory downloads/dist {} \;")
os.system("cd downloads/dist && /usr/bin/zip -R -D dist.zip *")
os.system("rm -rf /var/www/html/*")
os.system("cp -R downloads/* /var/www/html")
