dic_users = dict()  # словарь username:uid
dic_shells = dict()  # словарь  shell:count
dic_groups_uid = dict()  # словарь  groupname: [uid]
#  Читаем файл etc/passwd и записываем в словарь dic_users и dic_shells
passwd = open("etc/passwd", "r")
for p_str in passwd:
    dic_users[p_str.split(":")[0]] = p_str.split(":")[2]
    shell = p_str.split(":")[-1][:-1]
    if shell not in dic_shells.keys():
        dic_shells[shell] = 1
    else:
        dic_shells[shell] += 1
passwd.close()
# Читаем файл etc/group
# Находим имя группы и пользователей, которые в нее входят
# Для каждого имени группы берем имя пользователя и из словаря dic_users берем uid и записываем в словарь dic_groups_uid
group = open("etc/group", "r")
for g_str in group:
    group_usernames = g_str.split(":")[3][:-1].split(",")
    if group_usernames != [""]:  # Проверка наличия пользователей у группы
        group_name = g_str.split(":")[0]
        for group_username in group_usernames:
            if group_username in dic_users.keys():
                if group_name in dic_groups_uid.keys():
                    dic_groups_uid[group_name].append(dic_users[group_username])
                else:
                    dic_groups_uid[group_name] = [dic_users[group_username]]
group.close()
#  Записываем в файл output.txt данные из словаря dic_shells и dic_groups_uid
output = open("output.txt", "w")
for sh, count in dic_shells.items():
    output.write(f"{sh} - {count};\n")
for g_name, u in dic_groups_uid.items():
    uid = ''.join((f"{x}," for x in u))
    output.write(f"{g_name}:{uid}\n")
