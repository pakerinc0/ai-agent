from app.core.version_manager import VersionManager


vm = VersionManager()


print(
    vm.save_version(
        "calculator",
        "calculator.py",
        "print('version1')"
    )
)


print(
    vm.save_version(
        "calculator",
        "calculator.py",
        "print('version2')"
    )
)


print(
    vm.list_versions(
        "calculator"
    )
)


print(
    vm.set_best(
        "calculator",
        "v2"
    )
)
