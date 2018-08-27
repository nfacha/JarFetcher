import os

folders = ['downloads/jar/stable/craftbukkit', 'downloads/jar/stable/spigot', 'downloads/jar/stable/vanilla',
           'downloads/jar/stable/paperspigot', 'downloads/jar/stable/nukkit',
           'downloads/jar/snapshots/craftbukkit', 'downloads/jar/snapshots/spigot', 'downloads/jar/snapshots/vanilla']
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
            stability = "snapshots"
            filename = '%s/%s-%s-snapshot.jar.conf' % (path.replace("jar", "conf"), type, version)
        if type == "craftbukkit":
            with open('templates/%s/craftbukkit.template' % stability, 'r') as file:
                template = file.read()
        if type == "spigot":
            with open('templates/%s/spigot.template' % stability, 'r') as file:
                template = file.read()
        if type == "paperspigot":
            with open('templates/%s/paperspigot.template' % stability, 'r') as file:
                template = file.read()
        if type == "vanilla":
            with open('templates/%s/vanilla.template' % stability, 'r') as file:
                template = file.read()
        template = template.replace("[VERSION]", version)

        if type == "nukkit":
            with open('templates/%s/nukkit.template' % stability, 'r') as file:
                template = file.read()
        template = template.replace("[VERSION]", version)

        if os.path.exists(filename):
            os.remove(filename)
        with open(filename, 'a') as the_file:
            the_file.write(template)
        print("Saved conf file for %s-%s.jar.conf" % (type, version))
