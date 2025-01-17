from importlib.metadata import distributions


def generate_requirements():
    installed_packages = distributions()
    installed_packages_list = sorted([f"{dist.metadata['Name']}=={dist.version}" for dist in installed_packages])
    with open('requirements.txt', 'w') as f:
        f.write('\n'.join(installed_packages_list))


if __name__ == "__main__":
    generate_requirements()
