def find_active_users(log_file):

    active_users = set()

    with open(log_file, 'r') as file:
        for line in file:

            user = line.strip().split(',')
            user_id = user[1]
            action = user[2]

            # Add user to the list
            if action == 'LOGIN':
                active_users.add(user_id)
            # Remove user if exists
            elif action == 'LOGOUT':

                if user_id in active_users:
                    active_users.discard(user_id)
            else:
                raise Exception('Unknown action', action)

    return list(active_users)


if __name__ == '__main__':

    print(find_active_users('logfile.txt'))