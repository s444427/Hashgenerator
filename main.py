import hashlib


def get_md5(value: str):
    return hashlib.md5(value.encode('utf-8')).hexdigest()


def generate_correct_hash(starter: str):
    base_number = 0
    while get_md5("%s\n%s" % (starter, str(base_number).zfill(32)))[-2:] != '00':
        base_number += 1
    return str(base_number).zfill(32)


if __name__ == "__main__":
    starter = "Paweł Lewicki (444427)"
    for i in range(3):
        starter = "%s\n%s" % (starter, generate_correct_hash(starter))
        print("Iteration: %s\nStarter: \n%s\nHash: %s\n" % (i + 1, starter, get_md5(starter)))
    print("Final result: \n%s\n" % starter)