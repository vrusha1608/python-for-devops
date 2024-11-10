# update some configuration parameters of file

def update_file_conf(file_path, key, value):
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                updated_line = key+"="+value
                print(updated_line)
                file.write(updated_line)
            else:
                file.write(line)

update_file_conf("E:\devops-projects\python-for-devops\important\server-config.txt", "MAX_CONNECTIONS", "200")
