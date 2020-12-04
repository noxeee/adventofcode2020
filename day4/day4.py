import csv
import re

# read file

with open("input.txt", 'r') as inpt:
    # lines = inpt.read()
    passports = inpt.read().split('\n\n')
    # csvr = csv.reader(inpt, delimiter='^\s*$')
    # Read and print the entire file line by line
    # lines = [row for fow in csvr]

    # print(lines)
    print(len(passports))
    '''
     line = reader.readline()
     while line != '':  # The EOF char is an empty string
         print(line, end='')
         line = reader.readline()
         print(line)
    '''
# read as dict


valid_passports = 0


def is_valid(credentials, part2=False):

    if(part2):
        # parse credentials
        byr_idx = credentials.find("byr")
        iyr_idx = credentials.find("iyr")
        eyr_idx = credentials.find("eyr")
        hgt_idx = credentials.find("hgt")
        hcl_idx = credentials.find("hcl")
        ecl_idx = credentials.find("ecl")
        pid_idx = credentials.find("pid")

        if(
            byr_idx == -1 or
            iyr_idx == -1 or
            eyr_idx == -1 or
            hgt_idx == -1 or
            hcl_idx == -1 or
            ecl_idx == -1 or
            pid_idx == -1
        ):
            return False

        cred_list = credentials.replace('\n', ' ').split(' ')

        cred_dict = {}

        for item in cred_list:
            if(item == ''):
                continue

            key_val = item.split(':')

            cred_dict[key_val[0]] = key_val[1]

        # print(cred_list)
        print(cred_dict)

        if(int(cred_dict['byr']) < 1920 or int(cred_dict['byr']) > 2002):
            return False
        if(int(cred_dict['iyr']) < 2010 or int(cred_dict['iyr']) > 2020):
            return False
        if(int(cred_dict['eyr']) < 2020 or int(cred_dict['eyr']) > 2030):
            return False
        if(re.match("\d+(in|cm)", cred_dict['hgt']) != None):

            if cred_dict['hgt'].find('cm') != -1:
                hgt_val = int(cred_dict['hgt'].strip('cm'))

                if ((hgt_val < 150) or (hgt_val > 193)):
                    return False

            else:
                hgt_val = int(cred_dict['hgt'].strip('in'))

                if (hgt_val < 59 or hgt_val > 76):
                    return False

        else:
            return False
        
        if(re.match("#(\d|[a-f]){6}", cred_dict['hcl']) == None):
            return False

        eye_clrs=[
            "amb",
            "blu",
            "brn",
            "gry",
            "grn",
            "hzl",
            "oth"
        ]

        if (cred_dict['ecl'] not in eye_clrs):
            return False

        if(re.match("^\d{9}$", cred_dict['pid']) == None):  # 9 digit number
            return False

        return True
    else:
        necessary_fields=[

            "byr",
            "iyr",
            "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid"
        ]  # removed second part with regex: ", .*"
    # cid can be missing

    # fields = re.split('\n | \w', credentials)

        for key in necessary_fields:
            if(credentials.find(key) == -1):
                return False
    return True


def count_valid_passports(batch, part2=False):
    return len([psp for psp in batch if is_valid(psp, part2)])


print("Number of valid passports for part 1:")
print(count_valid_passports(passports))
print("Number of valid passports for part 2:")
print(count_valid_passports(passports, True))
