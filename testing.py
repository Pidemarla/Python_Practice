import boto3
import time

def main():
    # iam_client = boto3.client('iam')

    # Path to the text file containing policy ARNs
    file_path = 'policies.txt'

    # Initialize an empty list to store names
    names_list = []

    # Open the file and read lines
    with open(file_path, 'r') as file:
        for line in file:
            # Strip any extra spaces and add to the list if the line is not empty
            name = line.strip()
            if name:
                names_list.append(name)

    for i in names_list:
        print(i)

if __name__ == '__main__':
    main()
