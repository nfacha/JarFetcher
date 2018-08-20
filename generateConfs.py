import os
folders = ['downloads/jar/stable/craftbukkit', 'downloads/jar/stable/spigot', 'downloads/jar/stable/vanilla',
           'downloads/jar/snapshot/craftbukkit', 'downloads/jar/snapshot/spigot', 'downloads/jar/snapshot/vanilla']
for path in folders:

    for filename in os.listdir(path):
        data = filename.split("-")
        type = data[0]
        version = data[1].replace(".jar", "")
        template = ""
        stability = ""
        filename = ""
        if "stable" in path:
            stability = "stable"
            filename = '%s/%s-%s.jar.conf' % (path.replace("jar", "conf"), type, version)
        else:
            stability = "snapshot"
            filename = '%s/%s-%s-snapshot.jar.conf' % (path.replace("jar", "conf"), type, version)
        if type == "craftbukkit":
            with open('templates/%s/craftbukkit.template' % stability, 'r') as file:
                template = file.read()
        if type == "spigot":
            with open('templates/%s/spigot.template' % stability, 'r') as file:
                template = file.read()
        if type == "vanilla":
            with open('templates/%s/vanilla.template' % stability, 'r') as file:
                template = file.read()
        template = template.replace("[VERSION]", version)

        with open(filename, 'a') as the_file:
            the_file.write(template)
        print("Saved conf file for %s-%s.jar.conf" % (type, version))