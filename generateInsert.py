import os
insert = ""
for filename in os.listdir("downloads/jars/craftbukkit"):
    data = filename.split("-")
    type = data[0]
    version = data[1].replace(".jar", "")
    insert = insert + "INSERT INTO `jars` (`id`, `name`, `internal_name`, `version`, `description`, `active`, `default`) VALUES (NULL, 'CraftBukkit', 'craftbukkit-%s.jar', '%s', '.', '1', '0');\n" % (version, version)

spigot_template = ''
for filename in os.listdir("downloads/jars/spigot"):
    data = filename.split("-")
    type = data[0]
    version = data[1].replace(".jar", "")
    insert = insert + "INSERT INTO `jars` (`id`, `name`, `internal_name`, `version`, `description`, `active`, `default`) VALUES (NULL, 'Spigot', 'spigot-%s.jar', '%s', '.', '1', '0');\n" % (version, version)

with open('import.sql', 'a') as the_file:
    the_file.write(insert)