import sys

def main():
    location_tuples = (42.96, -71.69)
    location_list = [42.96, -71.69]

    print(f"{sys.getsizeof(location_tuples)} bytes")
    print(f"{sys.getsizeof(location_list)} bytes")


main()
