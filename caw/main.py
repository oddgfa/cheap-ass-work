import tibber
import os
import sys


def main():
    tibber_env_var_key = 'TIBBER_ACCESS_TOKEN'
    tibber_access_token = os.environ.get(tibber_env_var_key)
    if not tibber_access_token:
        print('{} not defined as env variable'.format(tibber_env_var_key))
        sys.exit()

    tibber_connection = tibber.Tibber(access_token=tibber_access_token)
    tibber_connection.sync_update_info()
    print(tibber_connection.name)
    home = tibber_connection.get_homes()[0]
    home.sync_update_info()
    print(home.address1)

    home.sync_update_price_info()

    print(home.current_price_info)

    tibber_connection.sync_close_connection()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
