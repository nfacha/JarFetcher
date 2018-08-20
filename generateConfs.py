import os
folders = ['downloads/jar/stable/craftbukkit', 'downloads/jar/stable/spigot', 'downloads/jar/stable/vanilla']
for path in folders:

    for filename in os.listdir(path):
        data = filename.split("-")
        type = data[0]
        version = data[1].replace(".jar", "")
        template = ""
        if type == "craftbukkit":
            with open('templates/craftbukkit.template', 'r') as file:
                template = file.read()
        if type == "spigot":
            with open('templates/spigot.template', 'r') as file:
                template = file.read()
        if type == "vanilla":
            with open('templates/vanilla.template', 'r') as file:
                template = file.read()
        template = template.replace("[VERSION]", version)
        with open('%s/%s-%s.jar.conf' % (path.replace("jar", "conf"), type, version), 'a') as the_file:
            the_file.write(template)
        print("Saved conf file for %s-%s.jar.conf" % (type, version))