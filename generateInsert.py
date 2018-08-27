import os
insert = ""
for filename in os.listdir("downloads/dist"):
    if not filename.endswith(".jar"):
        continue
    data = filename.split("-")
    type = data[0]
    version = data[1].replace(".jar", "")
    stability = "stable"
    if "snapshot" in filename:
        stability = "snapshot"
    if type == "craftbukkit":
        insert = insert + "INSERT IGNORE INTO `jars` (`id`, `name`, `id_type`, `internal_name`, `version`, `description`, `active`, `default`) VALUES (NULL, 'CraftBukkit', 3, 'craftbukkit-%s.jar', '%s', '.', '0', '0');\n" % (
        version, version)
    if type == "spigot":
        insert = insert + "INSERT IGNORE INTO `jars` (`id`, `name`, `id_type`, `internal_name`, `version`, `description`, `active`, `default`) VALUES (NULL, 'Spigot', 1, 'spigot-%s.jar', '%s', '.', '0', '0');\n" % (
        version, version)
    if type == "vanilla":
        insert = insert + "INSERT IGNORE INTO `jars` (`id`, `name`, `id_type`, `internal_name`, `version`, `description`, `active`, `default`) VALUES (NULL, 'Vanilla', 2, 'vanilla-%s.jar', '%s', '.', '0', '0');\n" % (
        version, version)
    if type == "paperspigot":
        insert = insert + "INSERT IGNORE INTO `jars` (`id`, `name`, `id_type`, `internal_name`, `version`, `description`, `active`, `default`) VALUES (NULL, 'PaperSpigot', 4, 'paperspigot-%s.jar', '%s', '.', '0', '0');\n" % (
        version, version)

    if type == "nukkit":
        insert = insert + "INSERT IGNORE INTO `jars` (`id`, `name`, `id_type`, `internal_name`, `version`, `description`, `active`, `default`) VALUES (NULL, 'Nukkit', 5, 'nukkit-%s.jar', '%s', '.', '0', '0');\n" % (
        version, version)

if os.path.exists('import.sql'):
    os.remove('import.sql')
with open('import.sql', 'a') as the_file:
    the_file.write(insert)