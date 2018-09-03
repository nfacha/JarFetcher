import os
insert = ""
for filename in os.listdir("downloads/dist"):
    if not filename.endswith(".jar"):
        continue
    data = filename.split("-")
    type = data[0]
    version = data[1].replace(".jar", "")
    stability = "stable"
    stabilityLabel = "";
    if "snapshot" in filename:
        stability = "snapshot"
        stabilityLabel = "-snapshot"
    if type == "craftbukkit":
        insert = insert + "INSERT IGNORE INTO `jars` (`id`, `name`, `id_type`, `internal_name`, `version`, `description`, `active`, `default`) VALUES (NULL, 'CraftBukkit', 3, 'craftbukkit-%s%s.jar', '%s', '.', '0', '0');\n" % (
        version, stabilityLabel, version)
    if type == "spigot":
        insert = insert + "INSERT IGNORE INTO `jars` (`id`, `name`, `id_type`, `internal_name`, `version`, `description`, `active`, `default`) VALUES (NULL, 'Spigot', 1, 'spigot-%s%s.jar', '%s', '.', '0', '0');\n" % (
        version, stabilityLabel, version)
    if type == "vanilla":
        insert = insert + "INSERT IGNORE INTO `jars` (`id`, `name`, `id_type`, `internal_name`, `version`, `description`, `active`, `default`) VALUES (NULL, 'Vanilla', 2, 'vanilla-%s%s.jar', '%s', '.', '0', '0');\n" % (
        version, stabilityLabel, version)
    if type == "paperspigot":
        insert = insert + "INSERT IGNORE INTO `jars` (`id`, `name`, `id_type`, `internal_name`, `version`, `description`, `active`, `default`) VALUES (NULL, 'PaperSpigot', 4, 'paperspigot-%s%s.jar', '%s', '.', '0', '0');\n" % (
        version, stabilityLabel, version)

    if type == "nukkit":
        insert = insert + "INSERT IGNORE INTO `jars` (`id`, `name`, `id_type`, `internal_name`, `version`, `description`, `active`, `default`) VALUES (NULL, 'Nukkit', 5, 'nukkit-%s%s.jar', '%s', '.', '0', '0');\n" % (
        version, stabilityLabel, version)

if os.path.exists('import.sql'):
    os.remove('import.sql')
with open('import.sql', 'a') as the_file:
    the_file.write(insert)