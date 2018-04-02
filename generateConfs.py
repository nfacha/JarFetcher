import os
craftbukkit_template = ''
for filename in os.listdir("downloads/jars/craftbukkit"):
    data = filename.split("-")
    type = data[0]
    version = data[1].replace(".jar", "")
    with open('craftbukkit.template', 'r') as file:
        craftbukkit_template = file.read()
    craftbukkit_template = craftbukkit_template.replace("[VERSION]", version)
    with open('downloads/confs/craftbukkit/craftbukkit-%s.jar.conf' % version, 'a') as the_file:
        the_file.write(craftbukkit_template)
    print("Saved conf file for craftbukkit-%s.jar.conf" % version)
spigot_template = ''
for filename in os.listdir("downloads/jars/spigot"):
    data = filename.split("-")
    type = data[0]
    version = data[1].replace(".jar", "")
    with open('spigot.template', 'r') as file:
        spigot_template = file.read()
        spigot_template = spigot_template.replace("[VERSION]", version)
    with open('downloads/confs/spigot/spigot-%s.jar.conf' % version, 'a') as the_file:
        the_file.write(craftbukkit_template)
    print("Saved conf file for spigot-%s.jar.conf" % version)